---
name: text_to_image_upscale_lora_sampler_19
type: Text To Image
frequency: 5
level: weak
coverage: 0.4626
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageScale, ImageSharpen, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPassThrough, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, PrimitiveString, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, StringConcatenate, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageSize, easy imageSizeBySide, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: [CR Simple Text Watermark, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, PlaySound|pysssss, easy cleanGpuUsed, easy int, easy imageSize, easy imageSizeBySide]
members: [图片生成/图生图/2102191115112898562.json, 图片生成/文生图/❻「写真V1」Z双采+AIO分镜+K-HD TTP-HD「9.19」_2033062724925661185.json, 图片生成/文生图/❻「写真V1」Z双采+K分镜+K高清 TTP-HD「9.19」_2033062739102404610.json, 图片生成/文生图/写真V1双采方案｜Z双采样+AIO分镜+K-HD高清 TTP-HD_2101486731685089282.json, 图片生成/文生图/写真V1组合流｜Z双采样+K分镜+K高清TTP-HD人像_2101505448003334146.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102191115112898562.json、图片生成/文生图/❻「写真V1」Z双采+AIO分镜+K-HD TTP-HD「9.19」_2033062724925661185.json、图片生成/文生图/❻「写真V1」Z双采+K分镜+K高清 TTP-HD「9.19」_2033062739102404610.json、图片生成/文生图/写真V1双采方案｜Z双采样+AIO分镜+K-HD高清 TTP-HD_2101486731685089282.json、图片生成/文生图/写真V1组合流｜Z双采样+K分镜+K高清TTP-HD人像_2101505448003334146.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageScale`
- `ImageSharpen`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPassThrough`
- `ModelSamplingAuraFlow`
- `PlaySound|pysssss`
- `PreviewImage`
- `PrimitiveString`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
- `StringConcatenate`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy int`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 4/5 个有
- `Flux2Scheduler` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `KSamplerSelect` —— 4/5 个有
- `Mute / Bypass Relay (rgthree)` —— 4/5 个有
- `Mute / Bypass Repeater (rgthree)` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `RHUploadZip` —— 4/5 个有
- `RandomNoise` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `SamplerCustomAdvanced` —— 4/5 个有
- `Seed (rgthree)` —— 4/5 个有
- `Split String` —— 4/5 个有
- `VAEEncode` —— 4/5 个有
- `easy float` —— 4/5 个有
- `CheckpointLoaderSimple` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `solarL_SaveImagesToZip` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `CR Simple Text Watermark` —— 1/5 个有
- `CameraWatermarkNode` —— 1/5 个有
- `KOOK_ImageCompression` —— 1/5 个有
- `KOOK_SaveJPGImage` —— 1/5 个有
- `LazyCache` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 15 | 5 | 20% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 512 | 5 | 16% |
| 高度 | 80 | 80 - 512 | 5 | 16% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 75/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 15，5 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 高度 中位数 80，观测区间 80 - 512，5 个样本，取值分散，一致性仅 16%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（75/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Simple Text Watermark、ImageCASharpening+、LayerUtility: ImageScaleByAspectRatio V2、PlaySound|pysssss、easy cleanGpuUsed
