# 方法、数据与公开材料边界

[English](methodology.en.md) · [返回首页](../README.md)

## 三种内容分别看

1. **全库目录**：双语排行榜和总表各 676 条，按 arXiv ID 去重；每篇有一个主主题、多个标签。日期沿用总表的首次提交日期，不代表最新修订日。
2. **自动证据评分**：沿用既有五维评分与理由。本轮只验证加总、阈值、排名和双语对应，不重新运行原评分器；原始评分程序、采集日志及完整检索式未随仓库公开，因此不能宣称从原始论文端到端复现了评分。
3. **重点深度评述**：保留结论日期 2026-08-20 的原始排名（328 篇窗口内论文 + 1 篇历史对照），以及至 2026-10-28 的亮点速览。当前文件含首批 6 篇详细评述；引用的第二至第五十二批中引用的 50 份附件未包含在公开仓库中。原引用已改为明确的未公开材料标记，并保存在[引用清单](unpublished-references.json)。不补造全文，不把目录覆盖说成全文审稿覆盖。

文献窗口止于 **2026-11-09**。文档维护日期 **2026-11-14** 不表示完成了之后五天的论文检索，也不代表全领域穷尽收录。

## 评分解释

| 自动评分维度 | 上限 |
|---|---:|
| 创新 | 20 |
| 严谨 | 30 |
| 真实证据（grounding） | 20 |
| 复现 | 15 |
| 工程 | 15 |

A ≥ 75、B 60–74、C 45–59、D < 45。总表中的 `core` / `adjacent` 是既有收录范围标记；`高/中/低` 为既有判断置信度，两者都不是另一个排名。深度评述的 10 分制与上述 100 分制用途不同，不能线性换算。

自动提取容易漏掉章节、表格和公开声明。“未识别”不等于事实不存在。例如 [OpenAnt 原站](https://arxiv.org/abs/2606.19149) 明确给出开源链接，[VCAO 原站](https://arxiv.org/abs/2604.08291) 声明发布工件。因此原有判断中的提取失败措辞只可视为复核线索。论文报告的性能、CVE 数量或修复率均为作者或既有评述的陈述，本仓库未独立重做全部实验。

## 2026-11-14 核查范围

- 对全库检查双语 ID、标题、首次日期、排名、分数与五维分数；676 个 ID 唯一，九主题合计 676，分级为 A 7 / B 226 / C 352 / D 91。
- 抽核 9 篇论文原站的标题和首次日期：[项目级检测实证](https://arxiv.org/abs/2601.19239)、[CVE-Factory](https://arxiv.org/abs/2602.03012)、[Antaeus](https://arxiv.org/abs/2607.01138)、[OpenAnt](https://arxiv.org/abs/2606.19149)、[ABSENTIA](https://arxiv.org/abs/2610.00977)、[VCAO](https://arxiv.org/abs/2604.08291)、[漏洞定位基准](https://arxiv.org/abs/2609.15939)、[Sifting the Noise](https://arxiv.org/abs/2601.22952)。另核正 [Agent Audit 标题](https://arxiv.org/abs/2603.22853)中的旧拼写错误。这是元数据抽检，不是全库外链可达性测试或论文结论验证。
- 未批量修改旧分数、标签及逐篇结论；未新增论文。原站可能有新版本，采用方案时应再次核对。

## 机器可读目录

[papers.json](../data/papers.json) 与 [papers.csv](../data/papers.csv) 由 `scripts/build_catalog.py` 确定性生成；中文与英文排行榜/总表仍是事实来源。JSON 顶层含 `schema_version`、`corpus_cutoff`、`documentation_updated`、`source_files`、`score_origin`、`statistics`、`papers`。

每篇记录含 `id/title/url/rank/date/tier/score/dimensions/scope`；`topic/tags/confidence/judgment` 用 `zh/en` 保存双语文本。CSV 将双语字段展开，以 ` · ` 分隔多个标签。CSV 是 UTF-8，Excel 可通过“数据 → 从文本/CSV”指定 UTF-8 导入。

检查只保证数据内部一致性和本地链接有效，不保证研究结论正确、翻译等价、工件仍可运行或外部站点永远可访问。标签索引为既有编辑材料，维护时须单独复核。

## 调研与复用

论文库导航、分类、历史档案与贡献流程已有成熟实践，参考 [Awesome-LLMs-for-Vulnerability-Detection](https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection)、[Awesome-LLM4SVD](https://github.com/hs-esslingen-it-security/Awesome-LLM4SVD) 与 [Awesome-LLM_For-SE-Sec-Papers](https://github.com/EvanXiaa/Awesome-LLM_For-SE-Sec-Papers)。本轮为维护与呈现优化，不作原创方法声明。
