---
name: image_to_image_controlnet_upscale_lora_4
type: Image To Image
frequency: 7
level: strong
coverage: 0.842429
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Latent Batch Size, CR Text, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoaderAdvanced, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MathExpression|pysssss, RH_Translator, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy int]
problems: []
missing: []
members: [图片生成/图生图/Flux完美高清放大V2_1948192858460291074.json, 图片生成/图生图/Kontext高清放大（适用场景图）_1967070382207459329.json, 图片生成/图生图/kontext+Flux高清放大_2015697220879781889.json, 图片生成/图生图/kontext+Flux高清放大增强版_2058861706306211842.json, 图片生成/图生图/人像高清放大 _ 万物调节_高清修复_人像修复_1979167859815387137.json, 图片生成/图生图/高清放大_增强版_kontext+Flux_2096497022147842050.json, 图片生成/图生图/高清放大_增强版_kontext+Flux_2096798026231803905.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux完美高清放大V2_1948192858460291074.json、图片生成/图生图/Kontext高清放大（适用场景图）_1967070382207459329.json、图片生成/图生图/kontext+Flux高清放大_2015697220879781889.json、图片生成/图生图/kontext+Flux高清放大增强版_2058861706306211842.json、图片生成/图生图/人像高清放大 _ 万物调节_高清修复_人像修复_1979167859815387137.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Latent Batch Size`
- `CR Text`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoaderAdvanced`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MathExpression|pysssss`
- `RH_Translator`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 6/7 个有
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `Primitive float [Crystools]` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `easy imageSize` —— 6/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.3 | 0.3 - 0.4 | 7 | 89% |
| LoRA 文本强度 | 0.3 | 0.3 - 0.4 | 7 | 89% |
| ControlNet 权重 | 1 | 1 - 1 | 7 | 100% |
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 86% |
| 重绘幅度 | 0.55 | 0.55 - 1 | 7 | 74% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.3，观测区间 0.3 - 0.4，7 个样本，取值集中（一致性 89%）
- LoRA 文本强度 中位数 0.3，观测区间 0.3 - 0.4，7 个样本，取值集中（一致性 89%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 86%
- 重绘幅度 中位数 0.55，观测区间 0.55 - 1，7 个样本
