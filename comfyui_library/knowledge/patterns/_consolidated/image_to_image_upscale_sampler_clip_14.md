---
name: image_to_image_upscale_sampler_clip_14
type: Image To Image
frequency: 8
level: strong
coverage: 0.847
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物8K高清放大增强版-无痕去水印logo_1979887403118792705.json, 图片生成/图生图/万物溶图打光_Kontext_1993326331377156097.json, 图片生成/图生图/图片快速去水印、高清放大工作流_2086265837211701250.json, 图片生成/图生图/图片快速去水印、高清放大工作流_2086272119310209025.json, 图片生成/图生图/大饼-Kontext 双肩包精修V1_2032361944446935042.json, 图片生成/图生图/服装提取器-言灵ru_1993295371319312385.json, 图片生成/图生图/模特图转实拍图3d图，修图磨面料高清2k_2016007638638661634.json, 图片生成/文生图/【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/万物8K高清放大增强版-无痕去水印logo_1979887403118792705.json、图片生成/图生图/万物溶图打光_Kontext_1993326331377156097.json、图片生成/图生图/图片快速去水印、高清放大工作流_2086265837211701250.json、图片生成/图生图/图片快速去水印、高清放大工作流_2086272119310209025.json、图片生成/图生图/大饼-Kontext 双肩包精修V1_2032361944446935042.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 7/8 个有
- `ImageUpscaleWithModel` —— 7/8 个有
- `LoraLoader` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `CR Latent Batch Size` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `CR Latent Input Switch` —— 2/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ImpactImageBatchToImageList` —— 1/8 个有
- `LayerMask: BiRefNetUltraV2` —— 1/8 个有
- `LayerMask: LoadBiRefNetModel` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `UltimateSDUpscale` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 8 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，8 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
