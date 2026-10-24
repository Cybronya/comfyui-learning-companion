---
name: text_to_image_upscale_lora_sampler_83
type: Text To Image
frequency: 3
level: weak
coverage: 0.650333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FastFilmGrain, FlowMatchEulerDiscreteScheduler (Custom), GetImageSize+, GetNode, HFEPostProcessor (lrzjason), Image Compare (mtb), ImageCASharpening+, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, JjkText, KSampler, KSamplerSelect, LayerColor: BrightnessContrastV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PhotoShakeNode, PreviewAny, RandomNoise, RunningHub Deepcleaner, SamplerCustomAdvanced, SaveImageAndMetadata_, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text Concatenate, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-Image图推大合集｜多模式图生图重绘工作流_2095210656319496194.json, 图片生成/图生图/Z-Image图推大合集｜李泽钧图生图一站式生成_2095489377202954242.json, 图片生成/图生图/李泽钧-Z-Image图推大合集_2075062052477038594.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_83

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Z-Image图推大合集｜多模式图生图重绘工作流_2095210656319496194.json、图片生成/图生图/Z-Image图推大合集｜李泽钧图生图一站式生成_2095489377202954242.json、图片生成/图生图/李泽钧-Z-Image图推大合集_2075062052477038594.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FastFilmGrain`
- `FlowMatchEulerDiscreteScheduler (Custom)`
- `GetImageSize+`
- `GetNode`
- `HFEPostProcessor (lrzjason)`
- `Image Compare (mtb)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: BrightnessContrastV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PhotoShakeNode`
- `PreviewAny`
- `RandomNoise`
- `RunningHub Deepcleaner`
- `SamplerCustomAdvanced`
- `SaveImageAndMetadata_`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 3 | 51% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 1432 | 3 | 0% |
| 高度 | 80 | 80 - 1536 | 3 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，3 个样本
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1432，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，3 个样本，取值分散，一致性仅 0%
- 高发问题（14/3 个样本）：Steps较低可能导致细节不足
