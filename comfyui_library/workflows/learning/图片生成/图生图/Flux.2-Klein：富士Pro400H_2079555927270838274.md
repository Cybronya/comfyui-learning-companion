---
key: 图片生成/图生图/Flux.2-Klein：富士Pro400H_2079555927270838274.json
name: Flux.2-Klein：富士Pro400H_2079555927270838274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Klein：富士Pro400H_2079555927270838274.json
hash: 013a59c17ac8784e
coverage: 0.811321
learned_at: 2026-10-23 10:58:51
nodes: [KSamplerSelect, RandomNoise, VAELoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, Flux2Scheduler, SetUnionControlNetType, ControlNetLoader, ConditioningZeroOut, CFGGuider, GetImageSize, ReferenceLatent, easy showAnything, easy showAnything, easy showAnything, easy showAnything, TTP_Image_Tile_Batch, TTP_Tile_image_size, Note, GetImageSize+, GetImageSize+, easy cleanGpuUsed, ImageScaleBy, TTP_Image_Assy, SeedVR2LoadVAEModel, Image Comparer (rgthree), PreviewImage, VAEDecode, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, ImageCASharpening+, ImageResize+, ImageResize+, ImageScaleBy, UNETLoader, FluxUnionControlNetApply, LoraLoaderModelOnly, SaveImage, Any To String (mtb), PrimitiveStringMultiline, RHLLMChatNode, CLIPLoader, PrimitiveFloat, ConditioningCombine, ImageScaleToTotalPixels, AIO_Preprocessor, VAEEncode, CLIPTextEncode, Note, CLIPTextEncode, CLIPTextEncode, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"controlnet_strength": "canny"}
---

# 图片生成/图生图/Flux.2-Klein：富士Pro400H_2079555927270838274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Klein：富士Pro400H_2079555927270838274.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `ConditioningZeroOut`
- `CFGGuider`
- `GetImageSize`
- `ReferenceLatent`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Note`
- `GetImageSize+`
- `GetImageSize+`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `TTP_Image_Assy`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageResize+`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `FluxUnionControlNetApply` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Any To String (mtb)`
- `PrimitiveStringMultiline`
- `RHLLMChatNode`
- `CLIPLoader`
- `PrimitiveFloat`
- `ConditioningCombine`
- `ImageScaleToTotalPixels`
- `AIO_Preprocessor`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveImage`

## 关键参数

- `controlnet_strength` = `canny`

## 知识

覆盖率 **81%**（43/53）

**有卡**：`KSamplerSelect`、`RandomNoise`、`VAELoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`SetUnionControlNetType`、`ControlNetLoader`、`ConditioningZeroOut`、`CFGGuider`、`GetImageSize`、`ReferenceLatent`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`GetImageSize+`、`easy cleanGpuUsed`、`ImageScaleBy`、`TTP_Image_Assy`、`SeedVR2LoadVAEModel`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`ImageCASharpening+`、`ImageResize+`、`UNETLoader`、`FluxUnionControlNetApply`、`LoraLoaderModelOnly`、`SaveImage`、`Any To String (mtb)`、`RHLLMChatNode`、`CLIPLoader`、`ConditioningCombine`、`ImageScaleToTotalPixels`、`AIO_Preprocessor`、`VAEEncode`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
