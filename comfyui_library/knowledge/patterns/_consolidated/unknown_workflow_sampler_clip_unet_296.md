---
name: unknown_workflow_sampler_clip_unet_296
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.829
common_nodes: [CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageScaleToTotalPixels, JWFloat, KSamplerAdvanced, LatentSwitch, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, YC Color Match]
problems: []
missing: []
members: [图片生成/图生图/极速图像拆分，九宫格 四宫格 自动高清_2037817863880314881.json, 图片生成/图生图/模糊变清晰，修复细节 ，  极速 Klein 9B_2036341734451453954.json, 图片生成/图生图/自动九宫格拆分，四宫格拆分，自动变清晰，极速。_2037807292028035073.json, 图片生成/图生图/高清放大，一键模糊变清晰，  Klein 9B  极速_2036332368893579265.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_296

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/极速图像拆分，九宫格 四宫格 自动高清_2037817863880314881.json、图片生成/图生图/模糊变清晰，修复细节 ，  极速 Klein 9B_2036341734451453954.json、图片生成/图生图/自动九宫格拆分，四宫格拆分，自动变清晰，极速。_2037807292028035073.json、图片生成/图生图/高清放大，一键模糊变清晰，  Klein 9B  极速_2036332368893579265.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `JWFloat`
- `KSamplerAdvanced`
- `LatentSwitch`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YC Color Match`

**可变部分**（部分 workflow 才有）：
- `GuHaiAutoImageSplit` —— 2/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `ImageResizeKJv2` —— 2/4 个有
- `Int` —— 2/4 个有
- `TTResolutionSelector` —— 2/4 个有
- `TwoWaySwitch` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `math_calculate` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
