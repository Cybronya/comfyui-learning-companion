---
name: unknown_workflow_upscale_lora_sampler_33
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.464833
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CameraWatermarkNode, ConditioningZeroOut, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageScale, KOOK_ImageCompression, KOOK_SaveJPGImage, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPassThrough, ModelSamplingAuraFlow, PlaySound|pysssss, PreviewImage, PrimitiveString, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SomethingToString, StringConcatenate, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextInput_, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageSize, easy imageSizeBySide, easy int, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Z-image+双采+反推+TTP-HD_2067530663779192834.json, 图片生成/图生图/高清放大 — Zimage双采+SeedVR2高清+TTP分块_2040612027781091330.json, 图片生成/图生图/高清放大 — Zimage双采+SeedVR2高清+TTP分块_2070775940573130753.json, 图片生成/图生图/鳌拜拜人设V2_2061710823273353218.json, 图片生成/图生图/鳌拜拜人设V2自选lora_2061718505837383681.json, 图片生成/文生图/❼「写真V2」Z双采+TTP-HD「9.20」_2039328218167123970.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Z-image+双采+反推+TTP-HD_2067530663779192834.json、图片生成/图生图/高清放大 — Zimage双采+SeedVR2高清+TTP分块_2040612027781091330.json、图片生成/图生图/高清放大 — Zimage双采+SeedVR2高清+TTP分块_2070775940573130753.json、图片生成/图生图/鳌拜拜人设V2_2061710823273353218.json、图片生成/图生图/鳌拜拜人设V2自选lora_2061718505837383681.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CameraWatermarkNode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageScale`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
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
- `LoadImagesFromDir //Inspire` —— 5/6 个有
- `CR Simple Text Watermark` —— 4/6 个有
- `CheckpointLoaderSimple` —— 4/6 个有
- `ColorMatch` —— 4/6 个有
- `ImageSharpen` —— 4/6 个有
- `LazyCache` —— 4/6 个有
- `ImageRGBA2RGB` —— 2/6 个有
- `LayerUtility: ImageBlendAdvance V3` —— 2/6 个有
- `RHUploadZip` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 6 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 15 | 6 | 89% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | dpmpp_sde | - | 6 | 67% |
| 重绘幅度 | simple | - | 6 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 15，6 个样本，取值集中（一致性 89%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，6 个样本，一致性 67%
- 重绘幅度 最常用 simple，6 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 15，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
