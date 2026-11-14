"""Generate accessible, bilingual landscape SVG reading guides."""
import argparse
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY = {
    "zh": ("从论文到工程判断", "先定位研究，再核查证据，最后决定如何采用。", [
        ("总览论文", "排行榜 / 自动评分", "找到值得先读的研究"),
        ("按主题筛选", "方法 · 任务 · 对象 · 证据", "总表与四轴标签交叉阅读"),
        ("核查原始证据", "最新论文 / 代码 / 数据", "确认负例、执行验证与成本"),
        ("形成工程判断", "重点评述 / 自行复现", "在自己的场景验证取舍")], "自动评分辅助阅读，采用结论仍需原始证据与独立验证。"),
    "en": ("From papers to engineering decisions", "Find the research. Inspect the evidence. Decide what to adopt.", [
        ("Scan the research", "Leaderboard / scores", "Choose what to read first"),
        ("Select a topic", "Method / task / target / evidence", "Use the table and tag index"),
        ("Check the evidence", "Latest paper / code / data", "Inspect controls, tests and cost"),
        ("Make a decision", "Reviews / reproduction", "Validate in your own setting")], "Automated scores guide reading; adoption requires source evidence and independent validation."),
}


def render(lang):
    title, subtitle, cards, footer = COPY[lang]
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440" role="img" aria-labelledby="title desc" xml:lang="{lang}">',
           f'<title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle + " " + footer)}</desc>',
           '<rect width="1200" height="440" rx="20" fill="#fff"/>',
           '<rect x="1" y="1" width="1198" height="438" rx="19" fill="none" stroke="#e8e8e8"/>',
           '<g font-family="Arial, Microsoft YaHei, Noto Sans CJK SC, sans-serif">',
           f'<text x="42" y="64" fill="#171717" font-size="32" font-weight="700">{escape(title)}</text>',
           f'<text x="42" y="100" fill="#666" font-size="18">{escape(subtitle)}</text>']
    for index, (heading, line1, line2) in enumerate(cards):
        x = 42 + index * 282
        svg += [f'<rect x="{x}" y="140" width="270" height="202" rx="12" fill="#fafafa" stroke="#e8e8e8"/>',
                f'<text x="{x+22}" y="180" fill="#777" font-size="15" font-weight="700">0{index+1}</text>',
                f'<text x="{x+22}" y="222" fill="#171717" font-size="22" font-weight="700">{escape(heading)}</text>',
                f'<text x="{x+22}" y="264" fill="#555" font-size="15">{escape(line1)}</text>',
                f'<text x="{x+22}" y="297" fill="#555" font-size="15">{escape(line2)}</text>']
    svg += [f'<text x="42" y="396" fill="#666" font-size="17">{escape(footer)}</text>', '</g></svg>']
    return "\n".join(svg) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for lang in COPY:
        path = ROOT / f"assets/reading-path-{lang}.svg"
        content = render(lang)
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                raise SystemExit(f"Stale SVG: {path.name}; run python scripts/build_assets.py")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    print("OK: bilingual landscape SVG guides.")
