---
key: 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809.json
name: ⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809.json
hash: f302853285299b16
coverage: 0.805556
learned_at: 2026-10-23 11:47:49
nodes: [VAEEncode, ReferenceLatent, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, CFGGuider, VAELoader, CLIPLoader, KSamplerAdvanced, VAEEncode, RunningHub Deepcleaner, ModelSamplingAuraFlow, CLIPTextEncode, VAEDecode, LoraLoaderModelOnly, CLIPTextEncode, VAELoader, CLIPLoader, GetImageSize+, easy showAnything, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, GetImageSize+, TTP_Image_Tile_Batch, PreviewImage, ImageResize+, ImageCASharpening+, TTP_Image_Assy, SaveImage, ImageScaleBy, SeedVR2LoadVAEModel, easy showAnything, PrimitiveFloat, SaveImage, DWPreprocessor, UNETLoader, ReferenceLatent, GetImageSize, Any Switch (rgthree), VAEDecode, CLIPTextEncode, CLIPTextEncode, Image Comparer (rgthree), easy cleanGpuUsed, llama_cpp_model_loader, llama_cpp_parameters, ImageScaleToTotalPixels, GetNode, GetNode, TTP_Tile_image_size, Note, ImageResize+, ImageScaleBy, easy cleanGpuUsed, LoadImage, PreviewAny, CR Text, SetNode, SaveImage, llama_cpp_instruct_adv, LayerUtility: ImageScaleByAspectRatio V2, DepthAnythingV2Preprocessor, CannyEdgePreprocessor, PreviewImage, Fast Groups Muter (rgthree), RandomNoise, Image Comparer (rgthree), SamplerCustomAdvanced, LoadImage, UNETLoader, easy cleanGpuUsed, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "beta57", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/⭐️⭐️⭐️⭐️⭐️Klein CN+提示词洗图+Z image修复+TTP&seed VR2放大_2017033094146039809.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `VAEEncode` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `VAELoader`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `VAEEncode` ★核心
- `RunningHub Deepcleaner`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `GetImageSize+`
- `easy showAnything`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `GetImageSize+`
- `TTP_Image_Tile_Batch`
- `PreviewImage`
- `ImageResize+`
- `ImageCASharpening+`
- `TTP_Image_Assy`
- `SaveImage`
- `ImageScaleBy`
- `SeedVR2LoadVAEModel`
- `easy showAnything`
- `PrimitiveFloat`
- `SaveImage`
- `DWPreprocessor`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `GetImageSize`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `TTP_Tile_image_size`
- `Note`
- `ImageResize+`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `LoadImage`
- `PreviewAny`
- `CR Text`
- `SetNode`
- `SaveImage`
- `llama_cpp_instruct_adv`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DepthAnythingV2Preprocessor`
- `CannyEdgePreprocessor`
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `RandomNoise`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta57`

## 知识

覆盖率 **81%**（58/72）

**有卡**：`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`VAELoader`、`CLIPLoader`、`KSamplerAdvanced`、`RunningHub Deepcleaner`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`VAEDecode`、`LoraLoaderModelOnly`、`GetImageSize+`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`TTP_Image_Tile_Batch`、`ImageResize+`、`ImageCASharpening+`、`TTP_Image_Assy`、`SaveImage`、`ImageScaleBy`、`SeedVR2LoadVAEModel`、`DWPreprocessor`、`UNETLoader`、`GetImageSize`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`LoadImage`、`CR Text`、`llama_cpp_instruct_adv`、`LayerUtility: ImageScaleByAspectRatio V2`、`DepthAnythingV2Preprocessor`、`CannyEdgePreprocessor`、`RandomNoise`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
