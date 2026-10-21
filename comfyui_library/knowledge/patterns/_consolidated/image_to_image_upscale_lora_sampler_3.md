---
name: image_to_image_upscale_lora_sampler_3
type: Image To Image
frequency: 4
level: moderate
coverage: 0.62425
common_nodes: [CLIPLoader, CLIPTextEncode, ColorCorrect, EditTextEncode_EditUtils, Flux2KleinConfigPreparer_EditUtils, Flux2KleinModelConfig_EditUtils, Get Image Size, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy boolean, easy cleanGpuUsed, easy ifElse, easy imageColorMatch, easy imageScaleToNormPixels, easy int, easy showAnything, 图像缩放V2_孤海, 孤海-浮点滑条, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR Text Concatenate, LayerUtility: PurgeVRAM V2, easy boolean, easy cleanGpuUsed, easy imageColorMatch, easy imageScaleToNormPixels, easy int, 取色器_孤海, 图像缩放V2_孤海, 孤海-浮点滑条, 数学运算_孤海, Get Image Size, GetImageSize+, ImageResize+]
members: [图片生成/图生图/2037730083359694850.json, 图片生成/图生图/2058911393428107266.json, 图片生成/文生图/( Flux-2-klein-9B)身材调整_2077560918359236610.json, 数字人/数字人/Flux2-Klein+zimage人像精修+高清放大_2046588836989378561.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2037730083359694850.json、图片生成/图生图/2058911393428107266.json、图片生成/文生图/( Flux-2-klein-9B)身材调整_2077560918359236610.json、数字人/数字人/Flux2-Klein+zimage人像精修+高清放大_2046588836989378561.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorCorrect`
- `EditTextEncode_EditUtils`
- `Flux2KleinConfigPreparer_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Get Image Size`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageColorMatch`
- `easy imageScaleToNormPixels`
- `easy int`
- `easy showAnything`
- `图像缩放V2_孤海`
- `孤海-浮点滑条`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `StringConstant` —— 3/4 个有
- `取色器_孤海` —— 3/4 个有
- `GetImageSize` —— 2/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CFGGuider` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `DuckQREncodeNode` —— 1/4 个有
- `EmptyFlux2LatentImage` —— 1/4 个有
- `Flux2Scheduler` —— 1/4 个有
- `KSamplerSelect` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `PainterFluxImageEdit` —— 1/4 个有
- `RandomNoise` —— 1/4 个有
- `SamplerCustomAdvanced` —— 1/4 个有
- `llama_cpp_instruct_adv` —— 1/4 个有
- `llama_cpp_model_loader` —— 1/4 个有
- `llama_cpp_parameters` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、LayerUtility: PurgeVRAM V2、easy boolean、easy cleanGpuUsed
