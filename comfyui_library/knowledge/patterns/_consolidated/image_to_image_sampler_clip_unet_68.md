---
name: image_to_image_sampler_clip_unet_68
type: Image To Image
frequency: 7
level: strong
coverage: 0.859857
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物溶图打光_Kontext_1993326331377156097.json, 图片生成/图生图/产品精修-金属类_1951522356852371458.json, 图片生成/图生图/图片快速去水印、高清放大工作流_2086265837211701250.json, 图片生成/图生图/图片快速去水印、高清放大工作流_2086272119310209025.json, 图片生成/图生图/大饼-Kontext 双肩包精修V1_2032361944446935042.json, 图片生成/图生图/服装提取器-言灵ru_1993295371319312385.json, 图片生成/图生图/模特图转实拍图3d图，修图磨面料高清2k_2016007638638661634.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/万物溶图打光_Kontext_1993326331377156097.json、图片生成/图生图/产品精修-金属类_1951522356852371458.json、图片生成/图生图/图片快速去水印、高清放大工作流_2086265837211701250.json、图片生成/图生图/图片快速去水印、高清放大工作流_2086272119310209025.json、图片生成/图生图/大饼-Kontext 双肩包精修V1_2032361944446935042.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `FluxKontextImageScale` —— 6/7 个有
- `ImageUpscaleWithModel` —— 6/7 个有
- `UpscaleModelLoader` —— 6/7 个有
- `CR Latent Batch Size` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `CR Latent Input Switch` —— 2/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ConstrainImage|pysssss` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `LayerMask: BiRefNetUltraV2` —— 1/7 个有
- `LayerMask: LoadBiRefNetModel` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | 20 | 20 - 25 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 25，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
