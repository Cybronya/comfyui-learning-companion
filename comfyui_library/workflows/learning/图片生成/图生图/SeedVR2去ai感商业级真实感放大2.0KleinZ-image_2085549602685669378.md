---
key: 图片生成/图生图/SeedVR2去ai感商业级真实感放大2.0KleinZ-image_2085549602685669378.json
name: SeedVR2去ai感商业级真实感放大2.0KleinZ-image_2085549602685669378
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SeedVR2去ai感商业级真实感放大2.0KleinZ-image_2085549602685669378.json
hash: 531a84270a267160
coverage: 0.803738
learned_at: 2026-10-21 00:44:27
nodes: [SeedVR2LoadVAEModel, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, VAELoader, FluxForwardODESampler, BasicScheduler, FluxDeGuidance, DisableNoise, VAEEncode, FluxDeGuidance, InFluxModelSamplingPred, BasicGuider, SamplerCustomAdvanced, DisableNoise, OutFluxModelSamplingPred, BasicScheduler, FluxReverseODESampler, BasicGuider, SamplerCustomAdvanced, FlipSigmas, ImageResize+, Get resolution [Crystools], TTP_Tile_image_size, TTP_Image_Tile_Batch, SimpleMath+, Get resolution [Crystools], PreviewImage, PreviewImage, PreviewImage, SaveImage, PreviewImage, PreviewImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, PreviewImage, VAEDecode, ImageScaleBy, PreviewImage, LoadImage, PreviewImage, LayerUtility: PurgeVRAM V2, SaveImage, Note, Float, Note, Float, Latent Noise Injection, Latent Noise Injection, PrimitiveFloat, Note, TTP_Image_Assy, CLIPTextEncode, ConditioningZeroOut, KSamplerSelect, UpscaleModelLoader, UltimateSDUpscaleCustomSample, ImageUpscaleWithModel, Upscale Model Loader, ImageResize+, ImageScaleBy, ImageResize+, AdvancedLyingSigmaSampler, CLIPLoader, easy imageColorMatch, easy imageColorMatch, Note, JWFloat, Note, JWFloat, Note, Int, Int, Note, Note, Note, Note, UNETLoader, LayerUtility: PurgeVRAM V2, VAEEncode, RHHiddenNodes, MemoryCleaner, easy imageColorMatch, DisTorchPurgeVRAMV2, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, CR Text, easy showAnything, GroupExecutor, LayerColor: Color of Shadow & Highlight, LayerColor: Color of Shadow & Highlight, easy int, JWFloat, JWFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, VAEDecode, VAEDecode, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, LayerColor: RGB, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.4000000000000001, "sampler_name": "er_sde", "scheduler": "sgm_uniform", "seed": 683441965899982, "steps": 3}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/SeedVR2去ai感商业级真实感放大2.0KleinZ-image_2085549602685669378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SeedVR2去ai感商业级真实感放大2.0KleinZ-image_2085549602685669378.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `SeedVR2LoadVAEModel`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `VAELoader`
- `FluxForwardODESampler` ★核心
- `BasicScheduler`
- `FluxDeGuidance`
- `DisableNoise`
- `VAEEncode` ★核心
- `FluxDeGuidance`
- `InFluxModelSamplingPred`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `OutFluxModelSamplingPred`
- `BasicScheduler`
- `FluxReverseODESampler` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `FlipSigmas`
- `ImageResize+`
- `Get resolution [Crystools]`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `SimpleMath+`
- `Get resolution [Crystools]`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `PreviewImage`
- `LoadImage`
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `Note`
- `Float`
- `Note`
- `Float`
- `Latent Noise Injection`
- `Latent Noise Injection`
- `PrimitiveFloat`
- `Note`
- `TTP_Image_Assy`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `UpscaleModelLoader`
- `UltimateSDUpscaleCustomSample`
- `ImageUpscaleWithModel`
- `Upscale Model Loader`
- `ImageResize+`
- `ImageScaleBy`
- `ImageResize+`
- `AdvancedLyingSigmaSampler` ★核心
- `CLIPLoader`
- `easy imageColorMatch`
- `easy imageColorMatch`
- `Note`
- `JWFloat`
- `Note`
- `JWFloat`
- `Note`
- `Int`
- `Int`
- `Note`
- `Note`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode` ★核心
- `RHHiddenNodes`
- `MemoryCleaner`
- `easy imageColorMatch`
- `DisTorchPurgeVRAMV2`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `CR Text`
- `easy showAnything`
- `GroupExecutor`
- `LayerColor: Color of Shadow & Highlight`
- `LayerColor: Color of Shadow & Highlight`
- `easy int`
- `JWFloat`
- `JWFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `LayerColor: RGB`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `683441965899982`
- `steps` = `3`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **80%**（86/107）

**有卡**：`SeedVR2LoadVAEModel`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`VAELoader`、`FluxForwardODESampler`、`BasicScheduler`、`FluxDeGuidance`、`DisableNoise`、`VAEEncode`、`InFluxModelSamplingPred`、`BasicGuider`、`SamplerCustomAdvanced`、`OutFluxModelSamplingPred`、`FluxReverseODESampler`、`FlipSigmas`、`ImageResize+`、`Get resolution [Crystools]`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`SimpleMath+`、`SaveImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`ImageScaleBy`、`LoadImage`、`LayerUtility: PurgeVRAM V2`、`Float`、`Latent Noise Injection`、`TTP_Image_Assy`、`ConditioningZeroOut`、`KSamplerSelect`、`UpscaleModelLoader`、`UltimateSDUpscaleCustomSample`、`ImageUpscaleWithModel`、`Upscale Model Loader`、`AdvancedLyingSigmaSampler`、`CLIPLoader`、`easy imageColorMatch`、`JWFloat`、`Int`、`UNETLoader`、`RHHiddenNodes`、`MemoryCleaner`、`DisTorchPurgeVRAMV2`、`easy cleanGpuUsed`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`CR Text`、`GroupExecutor`、`LayerColor: Color of Shadow & Highlight`、`easy int`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LayerColor: RGB`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
