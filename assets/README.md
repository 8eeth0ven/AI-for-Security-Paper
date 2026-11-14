# 图片说明 / Asset notes

[返回首页](../README.md) · [English home](../README.en.md)

| 文件 / File | 用途 / Use | 生成方式 / Source |
|---|---|---|
| [cover.png](cover.png) | 共享横向封面 / Shared landscape cover | Built-in image generation，2026-11-14；编辑插画，非产品截图。Editorial illustration, not a screenshot. |
| [reading-path-zh.svg](reading-path-zh.svg) | 中文阅读路径 / Chinese reading path | `scripts/build_assets.py` |
| [reading-path-en.svg](reading-path-en.svg) | 英文阅读路径 / English reading path | `scripts/build_assets.py` |

全套采用白底、黑白灰、细线与横向构图，宽大于高。封面不放动态统计，避免论文增补后图片数字过期。流程图有 SVG title/desc 与 README 替代文字。

All assets use a light monochrome palette and landscape composition. The cover contains no corpus counts that could become stale. SVG guides provide title/description text and README alt text.

```sh
python scripts/build_assets.py
python scripts/build_assets.py --check
```

## 封面最终提示词 / Final cover prompt

Mode: built-in `image_gen` (no fallback CLI). Use case: ads-marketing.

```text
Asset type: GitHub README cover for AI-for-Security-Paper, landscape 1800 x 900 or similar wide ratio.
Primary request: Create a polished editorial cover for an open research paper review collection about AI-assisted security code auditing.
Style/medium: minimal monochrome editorial design with subtle tactile paper illustration, clean white background, charcoal black type, light grey dividers, generous whitespace. Codex light aesthetic.
Composition: landscape, left half has clear title typography, right half a refined isometric arrangement of white research paper sheets with code lines, a small graph of connected analysis nodes, and a magnifying lens inspecting code. Restrained, calm and scholarly.
Text (verbatim): main title "AI for Security"; subtitle "Papers · Evidence · Engineering"; tiny top label "RESEARCH COLLECTION".
Constraints: all text perfectly legible and correctly spelled, height less than width, no emojis, no logos, no colored accents, no neon, no fake screenshots, no performance claims or numerical statistics, no watermark.
```
