---
name: unknown_workflow_upscale_sampler_clip_50
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.792
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ColorCorrectOfUtils, ConditioningZeroOut, DF_Int_to_Float, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, GetImageSize+, ImageResize+, ImageScaleBy, ImageScaleToTotalPixels, Int, KSamplerSelect, LoadImage, PreviewImage, RH_Nano_Banana2_Image2Image, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text, TextConcatenate_UTK, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/酒店房间修图_2030823786915827713.json, 图片生成/图生图/酒店房间修图多模型版_2030834069440827394.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/酒店房间修图_2030823786915827713.json、图片生成/图生图/酒店房间修图多模型版_2030834069440827394.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorCorrectOfUtils`
- `ConditioningZeroOut`
- `DF_Int_to_Float`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `Int`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana2_Image2Image`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text`
- `TextConcatenate_UTK`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `RH_GPT_Image15` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
