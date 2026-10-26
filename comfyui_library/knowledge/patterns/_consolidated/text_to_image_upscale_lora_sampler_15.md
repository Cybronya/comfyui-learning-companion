---
name: text_to_image_upscale_lora_sampler_15
type: Text To Image
frequency: 10
level: weak
coverage: 0.4771
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, ColorMatch, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageScale, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPassThrough, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageSize, easy imageSizeBySide, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein AIO分镜 Zimage 修复 TTP-HD_2067521433626046466.json, 图片生成/图生图/Klein AIO分镜Z修复TTP-HD写真V2图生图处理工作流_2101730737555853314.json, 图片生成/图生图/Klein+AIO分镜+Zimage+修复+TTP-HD 人像批量不同姿势+角度 写真摄影 真实拍摄_2079748698262818817.json, 图片生成/图生图/Z双采+TTP-HD写真V2文生图图生图处理工作流_2102191115112898562.json, 图片生成/图生图/❼「写真V2」Klein AIO分镜 Z修复 TTP-HD_2038281393624588290.json, 图片生成/图生图/写真V2版｜Klein AIO分镜加Z修复 TTP-HD高清人像写真_2101484903287320577.json, 图片生成/文生图/❻「写真V1」Z双采+AIO分镜+K-HD TTP-HD「9.19」_2033062724925661185.json, 图片生成/文生图/❻「写真V1」Z双采+K分镜+K高清 TTP-HD「9.19」_2033062739102404610.json, 图片生成/文生图/写真V1双采方案｜Z双采样+AIO分镜+K-HD高清 TTP-HD_2101486731685089282.json, 图片生成/文生图/写真V1组合流｜Z双采样+K分镜+K高清TTP-HD人像_2101505448003334146.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Klein AIO分镜 Zimage 修复 TTP-HD_2067521433626046466.json、图片生成/图生图/Klein AIO分镜Z修复TTP-HD写真V2图生图处理工作流_2101730737555853314.json、图片生成/图生图/Klein+AIO分镜+Zimage+修复+TTP-HD 人像批量不同姿势+角度 写真摄影 真实拍摄_2079748698262818817.json、图片生成/图生图/Z双采+TTP-HD写真V2文生图图生图处理工作流_2102191115112898562.json、图片生成/图生图/❼「写真V2」Klein AIO分镜 Z修复 TTP-HD_2038281393624588290.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 10 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageScale`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPassThrough`
- `ModelSamplingAuraFlow`
- `PlaySound|pysssss`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `SomethingToString`
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
- `EmptyFlux2LatentImage` —— 9/10 个有
- `ImageScaleToTotalPixels` —— 9/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 9/10 个有
- `RHUploadZip` —— 9/10 个有
- `ReferenceLatent` —— 9/10 个有
- `VAEEncode` —— 9/10 个有
- `CheckpointLoaderSimple` —— 8/10 个有
- `CameraWatermarkNode` —— 6/10 个有
- `KOOK_ImageCompression` —— 6/10 个有
- `KOOK_SaveJPGImage` —— 6/10 个有
- `SaveImage` —— 6/10 个有
- `ConditioningZeroOut` —— 5/10 个有
- `EmptySD3LatentImage` —— 5/10 个有
- `ImageRGBA2RGB` —— 5/10 个有
- `ImageSharpen` —— 5/10 个有
- `ImageUpscaleWithModel` —— 5/10 个有
- `JjkText` —— 5/10 个有
- `KSamplerAdvanced` —— 5/10 个有
- `LayerUtility: ImageBlendAdvance V3` —— 5/10 个有
- `LayerUtility: SimpleTextImage` —— 5/10 个有
- `ModelPatchTorchSettings` —— 5/10 个有
- `PathchSageAttentionKJ` —— 5/10 个有
- `PrimitiveString` —— 5/10 个有
- `ProcessString` —— 5/10 个有
- `StringConcatenate` —— 5/10 个有
- `TextEncodeQwenImageEditPlus` —— 5/10 个有
- `UpscaleModelLoader` —— 5/10 个有
- `easy promptLine` —— 5/10 个有
- `solarL_SaveImagesToZip` —— 5/10 个有
- `孤海注释` —— 5/10 个有
- `CFGGuider` —— 4/10 个有
- `Flux2Scheduler` —— 4/10 个有
- `GetImageSizeAndCount` —— 4/10 个有
- `KSamplerSelect` —— 4/10 个有
- `Mute / Bypass Relay (rgthree)` —— 4/10 个有
- `PrimitiveFloat` —— 4/10 个有
- `RandomNoise` —— 4/10 个有
- `SamplerCustomAdvanced` —— 4/10 个有
- `Seed (rgthree)` —— 4/10 个有
- `Split String` —— 4/10 个有
- `easy float` —— 4/10 个有
- `PrimitiveInt` —— 3/10 个有
- `CR Simple Text Watermark` —— 1/10 个有
- `LazyCache` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 15 | 10 | 4% |
| 采样算法 | er_sde | - | 10 | 50% |
| 调度器 | beta | - | 10 | 80% |
| 重绘幅度 | 1 | 0.15 - 1 | 9 | 44% |
| 宽度 | 296 | 80 - 1088 | 10 | 7% |
| 高度 | 296 | 80 - 1920 | 10 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 87/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 15，10 个样本，取值分散，一致性仅 4%
- 采样算法 最常用 er_sde，10 个样本，一致性 50%
- 调度器 最常用 beta，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，9 个样本，取值分散，一致性仅 44%
- 宽度 中位数 296，观测区间 80 - 1088，10 个样本，取值分散，一致性仅 7%
- 高度 中位数 296，观测区间 80 - 1920，10 个样本，取值分散，一致性仅 0%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 高发问题（87/10 个样本）：Steps较低可能导致细节不足
