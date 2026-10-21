---
key: 图片生成/文生图/Krea2 Text-to-Image (场景增强v0.1)_2075783987632627713.json
name: Krea2 Text-to-Image (场景增强v0.1)_2075783987632627713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 Text-to-Image (场景增强v0.1)_2075783987632627713.json
hash: 3894af48e967a7da
coverage: 0.944444
learned_at: 2026-10-20 00:19:14
nodes: [UNETLoader, VAELoader, ConditioningZeroOut, ImageResizeAdvanced, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageScaleBy, TTP_Image_Tile_Batch, ImageResizeAdvanced, 1hew_IntImageSize, ImageScaleBy, SeedVR2VideoUpscaler, GetImageSize, TTP_Image_Assy, KSampler, LayerUtility: PurgeVRAM V2, CLIPTextEncode, CLIPLoader, SaveImage, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, ModelSamplingAuraFlow, ConditioningZeroOut, ModelSamplingAuraFlow, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, PreviewAny, VAEDecode, EmptyLatentImage, Int, QZ_ResolutionPreset, TTP_Tile_image_size, VAEEncode, CFGNorm, UNETLoader, VAEDecode, CLIPLoader, VAELoader, CFGNorm, ConditioningZeroOut, VAEEncode, KSampler, VAEDecode, LayerUtility: PurgeVRAM V2, SaveImage, Fast Groups Bypasser (rgthree), CLIPTextEncode, RHLLMChatNode, PrimitiveStringMultiline, SeedNode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.25000000000000006, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 3714553705346, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2 Text-to-Image (场景增强v0.1)_2075783987632627713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 Text-to-Image (场景增强v0.1)_2075783987632627713.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `ImageResizeAdvanced`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageScaleBy`
- `TTP_Image_Tile_Batch`
- `ImageResizeAdvanced`
- `1hew_IntImageSize`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `GetImageSize`
- `TTP_Image_Assy`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SaveImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Int`
- `QZ_ResolutionPreset`
- `TTP_Tile_image_size`
- `VAEEncode` ★核心
- `CFGNorm`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `RHLLMChatNode`
- `PrimitiveStringMultiline`
- `SeedNode`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `3714553705346`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（51/54）

**有卡**：`UNETLoader`、`VAELoader`、`ConditioningZeroOut`、`ImageResizeAdvanced`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageScaleBy`、`TTP_Image_Tile_Batch`、`1hew_IntImageSize`、`SeedVR2VideoUpscaler`、`GetImageSize`、`TTP_Image_Assy`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`CLIPLoader`、`SaveImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`KSamplerAdvanced`、`VAEDecode`、`EmptyLatentImage`、`Int`、`QZ_ResolutionPreset`、`TTP_Tile_image_size`、`VAEEncode`、`CFGNorm`、`RHLLMChatNode`、`SeedNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
