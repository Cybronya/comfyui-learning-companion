---
key: 图片生成/图生图/krea2_image_to_image_+flux2_klein三采极_James008##_2100515839752626177.json
name: krea2_image_to_image_+flux2_klein三采极_James008##_2100515839752626177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/krea2_image_to_image_+flux2_klein三采极_James008##_2100515839752626177.json
hash: 8a614422cbcb1e60
coverage: 0.865854
learned_at: 2026-10-21 00:45:48
nodes: [VAEEncode, ReferenceLatent, ReferenceLatent, ImageResize+, TTP_Image_Tile_Batch, SeedVR2LoadVAEModel, TTP_Tile_image_size, ImageScaleBy, easy imageSize, easy imageSize, CFGGuider, Flux2Scheduler, KSamplerSelect, GetImageSize, ColorMatch, ImageResize+, EmptyFlux2LatentImage, CLIPLoader, VAELoader, ImageScaleToTotalPixels, VAEDecode, TTP_Image_Assy, SaveImage, SeedVR2LoadDiTModel, ImageScaleBy, PreviewImage, Image Comparer (rgthree), GetNode, SetNode, Image Comparer (rgthree), ConditioningZeroOut, VAELoader, VAEEncodeTiled, CLIPLoader, ImageUpscaleWithModel, ImageUpscaleWithModel, ImageScaleToTotalPixels, LoraLoaderModelOnly, CLIPTextEncode, UNETLoader, UpscaleModelLoader, UpscaleModelLoader, LoraLoaderModelOnly, VAEDecodeTiled, easy cleanGpuUsed, KSamplerAdvanced, Image Comparer (rgthree), SaveImage, CLIPTextEncode, ConditioningZeroOut, SamplerCustomAdvanced, easy imageColorMatch, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, SeedVR2VideoUpscaler, VAEEncode, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, BasicScheduler, RandomNoise, AILab_QwenVL, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, CLIPLoader, VAELoader, PrimitiveNode, CLIPTextEncode, Image Comparer (rgthree), LoadImage, PrimitiveInt, Fast Groups Bypasser (rgthree), LoraLoader, VAEDecode, Label (rgthree), SaveImage, LoraLoader, LoraLoaderModelOnly, EmptyImage, PreviewImage]
patterns: [lora]
missing: []
parameters: {"cfg": 10, "denoise": "kl_optimal", "lora_name": "stud100_krea2_c1-st5000.safetensors", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed", "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/krea2_image_to_image_+flux2_klein三采极_James008##_2100515839752626177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/krea2_image_to_image_+flux2_klein三采极_James008##_2100515839752626177.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageResize+`
- `TTP_Image_Tile_Batch`
- `SeedVR2LoadVAEModel`
- `TTP_Tile_image_size`
- `ImageScaleBy`
- `easy imageSize`
- `easy imageSize`
- `CFGGuider`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `GetImageSize`
- `ColorMatch`
- `ImageResize+`
- `EmptyFlux2LatentImage`
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `SetNode`
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `VAELoader`
- `VAEEncodeTiled` ★核心
- `CLIPLoader`
- `ImageUpscaleWithModel`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `easy imageColorMatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `SeedVR2VideoUpscaler`
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `RandomNoise`
- `AILab_QwenVL`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `PrimitiveInt`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `Label (rgthree)`
- `SaveImage`
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `kl_optimal`
- `lora_name` = `stud100_krea2_c1-st5000.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **87%**（71/82）

**有卡**：`VAEEncode`、`ReferenceLatent`、`ImageResize+`、`TTP_Image_Tile_Batch`、`SeedVR2LoadVAEModel`、`TTP_Tile_image_size`、`ImageScaleBy`、`easy imageSize`、`CFGGuider`、`Flux2Scheduler`、`KSamplerSelect`、`GetImageSize`、`ColorMatch`、`EmptyFlux2LatentImage`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`TTP_Image_Assy`、`SaveImage`、`SeedVR2LoadDiTModel`、`ConditioningZeroOut`、`VAEEncodeTiled`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`UNETLoader`、`UpscaleModelLoader`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`SamplerCustomAdvanced`、`easy imageColorMatch`、`RandomNoise`、`SeedVR2VideoUpscaler`、`BasicGuider`、`BasicScheduler`、`AILab_QwenVL`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LoraLoader`、`Label (rgthree)`、`EmptyImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
