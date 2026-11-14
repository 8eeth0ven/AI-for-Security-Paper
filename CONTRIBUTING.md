# 贡献与维护 / Contributing

## 新增或纠正论文 / Papers and corrections

请提供论文原站、arXiv ID、准确标题、首次提交日期、修改依据及可用的作者代码/数据链接。元数据在原站确认；预印本与会议录用分开描述。重复修订不作为新论文计数。

Provide primary URLs, arXiv ID, exact title, first submission date, correction evidence and available author code/data links. Verify metadata at the source; distinguish preprints from accepted publications. A revision is not a new paper.

1. 同时更新双语排行榜、总表与标签索引，保持 ID、排名、日期、分数、主主题对应。Update both languages together.
2. 未重新核验的分数与结论保留；更改须记录证据、版本、理由和日期。Do not silently rescore existing entries.
3. 深度审稿仅在实际公开完整材料后链接，不能编造缺失附件。Link detailed reviews only after publishing the actual material.
4. CHANGELOG 区分文献增补、评分修订和文档维护。Record these changes separately.

## 生成与验证 / Build and validate

```sh
python scripts/build_catalog.py
python scripts/build_catalog.py --check
python scripts/build_assets.py --check
python -m unittest discover -s tests
```

Python 3.10+，仅标准库。生成器从既有 Markdown 读取，不联网、不自动打分；双语排行榜与总表仍是源文件。JSON/CSV 与四份 README 主题表为生成产物，修改源表后重建并一起提交。`corpus_cutoff` 仅在真实增补后更新；`documentation_updated` 为目录或文档维护日期。

Python 3.10+, standard library only. The generator reads Markdown without network access or rescoring. Bilingual leaderboards and master tables remain the sources. Regenerate and commit JSON/CSV and all four README topic tables after source changes. Keep actual corpus additions and documentation maintenance dates separate.

检查涵盖双语 ID/标题/日期/排名/分数、唯一性、五维上限与加总、分级阈值、连续且按分数降序的排名、本地链接与 Markdown 标题锚点、生成文件新鲜度。它不验证外站内容、实验结论或翻译语义；标签索引仍需编辑核对。CI 在 PR 与 main 推送时执行相同检查。

Checks cover bilingual metadata/scores, ID uniqueness, dimension bounds/sums, grade thresholds, contiguous score-ordered ranks, local links/Markdown anchors and export freshness. They do not validate remote sources, experimental claims or translation semantics; tag indexes still require editorial review. CI runs the same checks on pull requests and pushes to main.

## 图片 / Images

配图采用明亮黑白灰、横向构图（宽 > 高），不把示意图当截图；双语流程图信息对齐。见[图片说明](assets/README.md)。

Use light monochrome landscape images (width > height), label illustrations honestly and align bilingual diagrams. See [asset notes](assets/README.md).

## 许可 / Licensing

本仓库当前未设置整体开源许可证；公开可读不等于授予任意复制分发许可。第三方论文、代码、数据、图片分别遵循原许可。

No repository-wide open-source license is currently declared. Public readability does not grant unrestricted redistribution rights. Respect the original licenses of third-party materials.
