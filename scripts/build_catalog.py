"""Export the bilingual Markdown corpus; no network, third-party packages or rescoring."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "zh": ("zh/含金量排行榜.md", "zh/逐篇论文含金量总表.md"),
    "en": ("en/value-ranking-leaderboard.md", "en/per-paper-value-master-table.md"),
}
DIMENSIONS = {"innovation": 20, "rigor": 30, "grounding": 20,
              "reproducibility": 15, "engineering": 15}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def table_rows(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\| \d+ \|", line):
            yield [v.strip().replace(r"\|", "|") for v in re.split(r"(?<!\\)\|", line.strip("|"))]


def identity(cell):
    match = re.search(r"\[([^\]]+)\]\((https://arxiv.org/abs/(\d{4}\.\d{4,5}))\)", cell)
    require(match is not None, f"Invalid paper cell: {cell}")
    return match.group(3), match.group(1), match.group(2)


def load_language(lang):
    board, master = (ROOT / p for p in SOURCES[lang])
    papers = {}
    for c in table_rows(board):
        require(len(c) == 9, f"{board}: expected 9 columns")
        pid, title, url = identity(c[1])
        require(pid not in papers, f"Duplicate ID in {board}: {pid}")
        tier, score = c[3].split(" / ")
        scores = dict(zip(DIMENSIONS, map(int, c[4:])))
        score = int(score)
        require(sum(scores.values()) == score, f"Score sum differs: {pid}")
        require(all(0 <= scores[k] <= cap for k, cap in DIMENSIONS.items()), f"Score out of range: {pid}")
        expected = "A" if score >= 75 else "B" if score >= 60 else "C" if score >= 45 else "D"
        require(tier == expected, f"Incorrect grade: {pid}")
        papers[pid] = {"id": pid, "title": title, "url": url, "rank": int(c[0]),
                       "topic": c[2], "tier": tier, "score": score, "dimensions": scores}
    seen = set()
    for c in table_rows(master):
        require(len(c) == 8, f"{master}: expected 8 columns")
        pid, title, _ = identity(c[1])
        require(pid in papers and pid not in seen, f"Unexpected/duplicate master ID: {pid}")
        seen.add(pid)
        p = papers[pid]
        require(p["rank"] == int(c[0]) and p["title"] == title, f"Master identity differs: {pid}")
        require(c[4] == f'{p["tier"]} / {p["score"]}', f"Master score differs: {pid}")
        require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", c[2]) is not None, f"Invalid date: {pid}")
        date.fromisoformat(c[2])
        p.update(date=c[2], scope=c[3], confidence=c[5], tags=c[6].split(" · "), judgment=c[7])
    require(seen == papers.keys(), f"Master/leaderboard IDs differ: {lang}")
    ordered = sorted(papers.values(), key=lambda p: p["rank"])
    require([p["rank"] for p in ordered] == list(range(1, len(ordered) + 1)), "Non-contiguous ranks")
    require([p["score"] for p in ordered] == sorted((p["score"] for p in ordered), reverse=True), "Unsorted scores")
    return papers


def check_links():
    """Check local Markdown/HTML image paths and GitHub-style heading anchors."""
    def anchors(path):
        counts, result = Counter(), set()
        for line in path.read_text(encoding="utf-8").splitlines():
            if not re.match(r"^#{1,6} ", line):
                continue
            heading = re.sub(r"^#+ ", "", line).lower().strip()
            heading = re.sub(r"[^\w\-\s\u0080-\uffff]", "", heading).replace(" ", "-")
            n = counts[heading]
            counts[heading] += 1
            result.add(heading + (f"-{n}" if n else ""))
        return result

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        urls = re.findall(r"\]\(([^)]+)\)", text) + re.findall(r'<img[^>]+src="([^"]+)"', text)
        for url in urls:
            if re.match(r"(?:https?://|mailto:)", url):
                continue
            local, _, fragment = unquote(url).partition("#")
            target = path.parent / local if local else path
            require(target.exists(), f"Broken local link: {path.relative_to(ROOT)} -> {url}")
            if fragment and target.suffix == ".md":
                require(fragment in anchors(target), f"Broken anchor: {path.relative_to(ROOT)} -> {url}")


def build():
    zh, en = load_language("zh"), load_language("en")
    require(zh.keys() == en.keys(), "Bilingual paper IDs differ")
    topic_map, reverse_map = {}, {}
    papers = []
    for pid, z in zh.items():
        e = en[pid]
        require(topic_map.setdefault(z["topic"], e["topic"]) == e["topic"], f"Bilingual topic differs: {pid}")
        require(reverse_map.setdefault(e["topic"], z["topic"]) == z["topic"], f"Bilingual topic differs: {pid}")
        for key in ("title", "rank", "tier", "score", "dimensions", "date", "scope"):
            require(z[key] == e[key], f"Bilingual {key} differs: {pid}")
        paper = {key: z[key] for key in ("id", "title", "url", "rank", "tier", "score", "dimensions", "date", "scope")}
        for key in ("topic", "tags", "confidence", "judgment"):
            paper[key] = {"zh": z[key], "en": e[key]}
        papers.append(paper)
    papers.sort(key=lambda p: p["rank"])
    stats = {"total": len(papers), "tiers": {k: sum(p["tier"] == k for p in papers) for k in "ABCD"},
             "topics": [{"zh": topic, "en": en[next(pid for pid in zh if zh[pid]["topic"] == topic)]["topic"], "count": count}
                        for topic, count in Counter(p["topic"] for p in zh.values()).most_common()]}
    catalog = {"schema_version": 1, "corpus_cutoff": "2026-11-09", "documentation_updated": "2026-11-14",
               "source_files": SOURCES, "score_origin": "existing automated evidence scores; not independently reproduced",
               "statistics": stats, "papers": papers}
    outputs = {"data/papers.json": json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"}
    buf = io.StringIO(newline="")
    fields = ["id", "title", "url", "rank", "date", "tier", "score", *DIMENSIONS, "scope",
              "topic_zh", "topic_en", "tags_zh", "tags_en", "confidence_zh", "confidence_en", "judgment_zh", "judgment_en"]
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for p in papers:
        row = {k: p[k] for k in ("id", "title", "url", "rank", "date", "tier", "score", "scope")}
        row.update(p["dimensions"])
        for key in ("topic", "tags", "confidence", "judgment"):
            for lang in ("zh", "en"):
                row[f"{key}_{lang}"] = " · ".join(p[key][lang]) if key == "tags" else p[key][lang]
        writer.writerow(row)
    outputs["data/papers.csv"] = buf.getvalue()
    for name, lang in (("README.md", "zh"), ("README.en.md", "en"), ("zh/README.md", "zh"), ("en/README.md", "en")):
        path = ROOT / name
        current = path.read_text(encoding="utf-8")
        header = "| 主题 | 篇数 |\n|---|---:|" if lang == "zh" else "| Topic | Papers |\n|---|---:|"
        table = header + "\n" + "\n".join(f'| {t[lang]} | {t["count"]} |' for t in stats["topics"])
        table += f'\n| **{"合计" if lang == "zh" else "Total"}** | **{len(papers)}** |'
        updated, n = re.subn(r"<!-- topics:start -->.*?<!-- topics:end -->", f"<!-- topics:start -->\n{table}\n<!-- topics:end -->", current, flags=re.S)
        require(n == 1, f"Expected exactly one topics block: {name}")
        outputs[name] = updated
    return outputs, stats


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate sources, links and generated file freshness without writing")
    args = parser.parse_args()
    outputs, stats = build()
    stale = []
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    require(not stale, f"Run python scripts/build_catalog.py to update: {', '.join(stale)}")
    check_links()
    print(f'OK: {stats["total"]} unique bilingual papers; scores, ranks, local links and exports checked.')


if __name__ == "__main__":
    main()
