---
key: 图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2021371911606898689.json
name: Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2021371911606898689
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2021371911606898689.json
hash: 5748b2598e88863c
coverage: 0.723684
learned_at: 2026-10-23 11:29:05
nodes: [SeedVR2LoadVAEModel, ImageScaleBy, CLIPLoader, easy showAnything, easy showAnything, GetImageSize+, TTP_Tile_image_size, Note, easy showAnything, easy showAnything, LayerUtility: ImageReelComposit, ImageResize+, ImageScaleBy, ImpactSwitch, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, SaveImage, easy cleanGpuUsed, ImageResize+, easy cleanGpuUsed, TTP_Image_Tile_Batch, easy cleanGpuUsed, LayerUtility: ImageReel, easy cleanGpuUsed, TTP_Image_Assy, easy cleanGpuUsed, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy cleanGpuUsed, SaveImage, SeedVR2LoadDiTModel, GetImageSize+, ImageScaleBy, Reroute, Reroute, Note, PrimitiveNode, Reroute, Reroute, ImpactInt, Reroute, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingAuraFlow, Reroute, ConditioningZeroOut, VAEEncode, PreviewImage, ModelSamplingAuraFlow, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KOOK_SaveJPGImage, KOOK_ImageCompression, Image Comparer (rgthree), VAEDecode, VAEDecode, KSampler, ShowText|pysssss, Fast Groups Muter (rgthree), KSampler, UNETLoader, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, CLIPTextEncode, llama_cpp_model_loader, llama_cpp_parameters, LoadImage, easy showAnything, llama_cpp_instruct_adv, RH_LLMAPI_Pro_Node]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.35, "sampler_name": "er_sde", "scheduler": "sgm_uniform", "seed": 585156486818865, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2021371911606898689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-IMAGE BASE+TRUBOL 超精致自动反推洗图+SeedVR2放大-人像效果顶级-高清-8K_2021371911606898689.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `CLIPLoader`
- `easy showAnything`
- `easy showAnything`
- `GetImageSize+`
- `TTP_Tile_image_size`
- `Note`
- `easy showAnything`
- `easy showAnything`
- `LayerUtility: ImageReelComposit`
- `ImageResize+`
- `ImageScaleBy`
- `ImpactSwitch`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `SaveImage`
- `easy cleanGpuUsed`
- `ImageResize+`
- `easy cleanGpuUsed`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `LayerUtility: ImageReel`
- `easy cleanGpuUsed`
- `TTP_Image_Assy`
- `easy cleanGpuUsed`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy cleanGpuUsed`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `GetImageSize+`
- `ImageScaleBy`
- `Reroute`
- `Reroute`
- `Note`
- `PrimitiveNode`
- `Reroute`
- `Reroute`
- `ImpactInt`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingAuraFlow`
- `Reroute`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KOOK_SaveJPGImage`
- `KOOK_ImageCompression`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ShowText|pysssss`
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `LoadImage`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `RH_LLMAPI_Pro_Node`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `585156486818865`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.35`

## 知识

覆盖率 **72%**（55/76）

**有卡**：`SeedVR2LoadVAEModel`、`ImageScaleBy`、`CLIPLoader`、`GetImageSize+`、`TTP_Tile_image_size`、`LayerUtility: ImageReelComposit`、`ImageResize+`、`LayerUtility: ImageReel`、`SaveImage`、`easy cleanGpuUsed`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`ImpactInt`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`VAEEncode`、`KOOK_SaveJPGImage`、`KOOK_ImageCompression`、`VAEDecode`、`KSampler`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`LoadImage`、`llama_cpp_instruct_adv`、`RH_LLMAPI_Pro_Node`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
