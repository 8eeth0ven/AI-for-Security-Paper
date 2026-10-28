# AI Security Code Audit Papers — Bilingual Repository

This repository contains a curated, evidence-based survey and ranking of recent research papers on **AI security code audit agents** — LLM/agentic systems for vulnerability detection, localization, repair, fuzzing, and secure code generation.

Two language copies of each document are provided:

| Folder | Language |
|---|---|
| [`zh/`](../zh/) | Chinese (中文) |
| [`en/`](../en/) | English |

## Documents

| File | Description |
|---|---|
| [`value-ranking-leaderboard.md`](value-ranking-leaderboard.md) | Leaderboard of **658** papers ranked by automated evidence score, graded **A / B / C / D**. Each row scores five dimensions: Innovation, Rigor, Authenticity (grounding), Reproducibility, and Engineering. |
| [`comprehensive-ranking-and-detailed-reviews.md`](comprehensive-ranking-and-detailed-reviews.md) | Deep, comprehensive ranking plus per-paper in-depth reviews. Covers **328** in-window papers (main window: 2025-08-04 → 2026-08-04, conclusion date 2026-08-20; supplemental window: 2026-08-05 → 2026-10-28, +182 papers, marked 🆕) plus 1 historical reference. Contains four ranking lists — Experimental Credibility, Agent-Method Inspiration, Engineering Implementation Reuse, and Conclusion Reliability — a scoring methodology, detailed reviews of key papers, and a supplemental-window highlights section. |
| [`per-paper-value-master-table.md`](per-paper-value-master-table.md) | Master table of per-paper content value, grouped by topic. Each row carries an overall rank, date, tier, grade/score, confidence, and a per-paper judgment (bonus / deduction reasoning). |

All three documents cover the same population of **658 papers**.

## Topic Categories

| Category | Papers |
|---|---|
| Vulnerability Detection, Localization & Verification (漏洞检测、定位与验证) | 162 |
| Secure Code Review & Static Analysis (安全代码评审与静态分析) | 53 |
| Smart Contract Auditing (智能合约审计) | 63 |
| Vulnerability Repair & Security Patches (漏洞修复与安全补丁) | 34 |
| AI-Generated Code Security (AI 生成代码安全) | 57 |
| Fuzzing, Dynamic Analysis & Exploit Verification (模糊测试、动态分析与利用验证) | 47 |
| Binary, Firmware & Reverse Engineering (二进制、固件与逆向分析) | 28 |
| Software Supply Chain, Malicious Code & Packages (软件供应链、恶意代码与软件包) | 16 |
| Benchmarks, Datasets & Evaluation Methods (基准、数据集与评测方法) | 16 |
| **Total** | **658** |

## How to Use

- Start with `value-ranking-leaderboard.md` for a quick overview of the graded landscape.
- Read `comprehensive-ranking-and-detailed-reviews.md` for the reasoning behind the rankings and detailed critiques of the strongest papers.
- Use `per-paper-value-master-table.md` to browse papers by topic and see per-paper judgments.

> Reading order intended: **Chinese** readers start from [`zh/README.md`](../zh/README.md); **English** readers start here.
