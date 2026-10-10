---
key: 图片生成/图生图/Z-image+Klein+SeedVR2去ai感商业级图片真实感放大2.0_2055160504007569410.json
name: Z-image+Klein+SeedVR2去ai感商业级图片真实感放大2.0_2055160504007569410
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image+Klein+SeedVR2去ai感商业级图片真实感放大2.0_2055160504007569410.json
hash: 1fcced1b84bdf947
coverage: 0.693069
learned_at: 2026-10-10 20:48:11
nodes: [SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, VAELoader, FluxForwardODESampler, BasicScheduler, FluxDeGuidance, DisableNoise, VAEEncode, FluxDeGuidance, InFluxModelSamplingPred, BasicGuider, SamplerCustomAdvanced, DisableNoise, OutFluxModelSamplingPred, BasicScheduler, FluxReverseODESampler, BasicGuider, SamplerCustomAdvanced, FlipSigmas, ImageResize+, LoadImage, VAEEncode, ImageScaleBy, ImageResize+, Get resolution [Crystools], TTP_Tile_image_size, TTP_Image_Tile_Batch, SimpleMath+, ImageScaleBy, Get resolution [Crystools], CLIPLoader, VAELoader, PreviewImage, PreviewImage, PreviewImage, SaveImage, Image Comparer (rgthree), PreviewImage, PreviewImage, CLIPTextEncode, Latent Noise Injection, Note, Latent Noise Injection, Float, Note, Note, Note, Note, VAEDecode, VAEDecode, CLIPTextEncode, UNETLoader, ModelSamplingAuraFlow, Note, JWFloat, easy int, JWFloat, JWFloat, JWFloat, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, Float, easy cleanGpuUsed, KSampler, KSampler, PreviewImage, easy imageColorMatch, ImageResize+, LayerUtility: PurgeVRAM V2, AILab_QwenVL, CR Text, ShowText|pysssss, TTP_Image_Assy, ImageUpscaleWithModel, LayerUtility: PurgeVRAM V2, KSamplerSelect, UpscaleModelLoader, Upscale Model Loader, ConditioningZeroOut, AdvancedLyingSigmaSampler, UltimateSDUpscaleCustomSample, VAELoader, CLIPLoader, easy cleanGpuUsed, CLIPTextEncode, KSampler, VAEEncode, ReferenceLatent, VAEDecode, ConditioningZeroOut, VAEDecode, easy imageColorMatch, UNETLoader_Any, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: [CR Text, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy imageColorMatch, easy imageColorMatch, easy int, Get resolution [Crystools], Get resolution [Crystools], ImageResize+, ImageResize+, ImageResize+, Latent Noise Injection, Latent Noise Injection, Upscale Model Loader]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 167474355682548, "steps": 4}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Latent Noise Injection` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `Latent Noise Injection` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `Upscale Model Loader` 仅有 Upscale 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image+Klein+SeedVR2去ai感商业级图片真实感放大2.0_2055160504007569410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image+Klein+SeedVR2去ai感商业级图片真实感放大2.0_2055160504007569410.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（101 个）：
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
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
- `LoadImage`
- `VAEEncode` ★核心
- `ImageScaleBy`
- `ImageResize+`
- `Get resolution [Crystools]`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `SimpleMath+`
- `ImageScaleBy`
- `Get resolution [Crystools]`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `Latent Noise Injection`
- `Note`
- `Latent Noise Injection`
- `Float`
- `Note`
- `Note`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `JWFloat`
- `easy int`
- `JWFloat`
- `JWFloat`
- `JWFloat`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Float`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `easy imageColorMatch`
- `ImageResize+`
- `LayerUtility: PurgeVRAM V2`
- `AILab_QwenVL`
- `CR Text`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerSelect` ★核心
- `UpscaleModelLoader`
- `Upscale Model Loader`
- `ConditioningZeroOut`
- `AdvancedLyingSigmaSampler` ★核心
- `UltimateSDUpscaleCustomSample`
- `VAELoader`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `easy imageColorMatch`
- `UNETLoader_Any` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `167474355682548`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（70/101）

**有卡**：`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`VAELoader`、`FluxForwardODESampler`、`BasicScheduler`、`FluxDeGuidance`、`DisableNoise`、`VAEEncode`、`InFluxModelSamplingPred`、`BasicGuider`、`SamplerCustomAdvanced`、`OutFluxModelSamplingPred`、`FluxReverseODESampler`、`FlipSigmas`、`LoadImage`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`CLIPLoader`、`SaveImage`、`CLIPTextEncode`、`Float`、`VAEDecode`、`UNETLoader`、`ModelSamplingAuraFlow`、`JWFloat`、`LoraLoaderModelOnly`、`KSampler`、`AILab_QwenVL`、`TTP_Image_Assy`、`ImageUpscaleWithModel`、`KSamplerSelect`、`UpscaleModelLoader`、`ConditioningZeroOut`、`AdvancedLyingSigmaSampler`、`UltimateSDUpscaleCustomSample`、`ReferenceLatent`、`UNETLoader_Any`

**缺卡**（17）：`CR Text`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageColorMatch`、`easy imageColorMatch`、`easy int`、`Get resolution [Crystools]`、`Get resolution [Crystools]`、`ImageResize+`、`ImageResize+`、`ImageResize+`、`Latent Noise Injection`、`Latent Noise Injection`、`Upscale Model Loader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Get resolution [Crystools]` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Latent Noise Injection` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `Latent Noise Injection` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `Upscale Model Loader` 仅有 Upscale 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
