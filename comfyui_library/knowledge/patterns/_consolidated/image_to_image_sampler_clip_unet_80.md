---
name: image_to_image_sampler_clip_unet_80
type: Image To Image
frequency: 6
level: strong
coverage: 0.849167
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext Plus修改效果功能强化版_1969762671421779969.json, 图片生成/图生图/kontext 全能溶图打光-针对电商产品_1950880176618020866.json, 图片生成/图生图/kontext-溶图+打光_1951587985403924482.json, 图片生成/图生图/【非API】 Kontext Dev 模型｜多图融合_1938484652631851009.json, 图片生成/图生图/动漫线稿上色｜多彩活力插画_1942398408399204354.json, 图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_80

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/kontext Plus修改效果功能强化版_1969762671421779969.json、图片生成/图生图/kontext 全能溶图打光-针对电商产品_1950880176618020866.json、图片生成/图生图/kontext-溶图+打光_1951587985403924482.json、图片生成/图生图/【非API】 Kontext Dev 模型｜多图融合_1938484652631851009.json、图片生成/图生图/动漫线稿上色｜多彩活力插画_1942398408399204354.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `ImageStitch` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `LayerMask: BiRefNetUltraV2` —— 2/6 个有
- `LayerMask: LoadBiRefNetModel` —— 2/6 个有
- `ChinesePrompt_Mix` —— 1/6 个有
- `ConcatText_Zho` —— 1/6 个有
- `GoogleTranslateTextNode` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `LayerUtility: GetImageSize` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `Seed (rgthree)` —— 1/6 个有
- `Text` —— 1/6 个有
- `easy promptList` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
