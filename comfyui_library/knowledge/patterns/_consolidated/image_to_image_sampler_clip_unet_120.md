---
name: image_to_image_sampler_clip_unet_120
type: Image To Image
frequency: 4
level: strong
coverage: 0.83725
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext Plus修改效果功能强化版_1969762671421779969.json, 图片生成/图生图/kontext 全能溶图打光-针对电商产品_1950880176618020866.json, 图片生成/图生图/kontext-溶图+打光_1951587985403924482.json, 图片生成/图生图/▶Kontext扩图流_1956304739745103874.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_120

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/kontext Plus修改效果功能强化版_1969762671421779969.json、图片生成/图生图/kontext 全能溶图打光-针对电商产品_1950880176618020866.json、图片生成/图生图/kontext-溶图+打光_1951587985403924482.json、图片生成/图生图/▶Kontext扩图流_1956304739745103874.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
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
- `LoraLoaderModelOnly` —— 3/4 个有
- `ChinesePrompt_Mix` —— 1/4 个有
- `ConcatText_Zho` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GoogleTranslateTextNode` —— 1/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `LayerMask: BiRefNetUltraV2` —— 1/4 个有
- `LayerMask: LoadBiRefNetModel` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
