---
key: 数字人/数字人/增强真实感增强质感去ai感2.0_2013168387253342210.json
name: 增强真实感增强质感去ai感2.0_2013168387253342210
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/增强真实感增强质感去ai感2.0_2013168387253342210.json
hash: 03112e2a8453b080
coverage: 0.85
learned_at: 2026-10-26 02:01:20
nodes: [PreviewImage, ImageCASharpening+, ImpactMinMax, ImageResize+, ImpactMinMax, ImpactMinMax, SimpleMath+, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy imageSize, ImageResize+, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, PreviewImage, SeedVR2, ImageCASharpening+, CLIPLoader, easy imageSize, CLIPTextEncode, CLIPTextEncode, UNETLoader, VAELoader, PreviewImage, ImageResize+, DF_Integer, KSampler, ImageScaleBy, TTP_Tile_image_size, ImageResize+, Get resolution [Crystools], TTP_Image_Tile_Batch, ImageScaleBy, Get resolution [Crystools], VAEDecode, VAEDecode, KSampler, VAEEncode, Latent Noise Injection, UltimateSDUpscaleNoUpscale, VAEEncode, Latent Noise Injection, Upscale Model Loader, easy int, PreviewImage, LayerUtility: PurgeVRAM V2, PreviewImage, SeedVR2, ImageResize+, TTP_Image_Assy, LayerUtility: PurgeVRAM V2, PreviewImage, ImageUpscaleWithModel, ImageFromBatch, Int, Int, Int, Int, PreviewImage, PreviewImage, ImpactMakeAnyList, SeedVR2, SaveImage, Int, Int, Int, JWFloat, JWFloat, Int, JWFloat, JWFloat, Fast Groups Bypasser (rgthree), AILab_QwenVL, LayerUtility: PurgeVRAM V2, PreviewImage, Image Comparer (rgthree), Note, ImageResize+, LoadImage, Label (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.15000000000000002, "sampler_name": "er_sde", "scheduler": "sgm_uniform", "seed": 455276412503056, "steps": 2}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/增强真实感增强质感去ai感2.0_2013168387253342210.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/增强真实感增强质感去ai感2.0_2013168387253342210.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `PreviewImage`
- `ImageCASharpening+`
- `ImpactMinMax`
- `ImageResize+`
- `ImpactMinMax`
- `ImpactMinMax`
- `SimpleMath+`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy imageSize`
- `ImageResize+`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `SeedVR2`
- `ImageCASharpening+`
- `CLIPLoader`
- `easy imageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `PreviewImage`
- `ImageResize+`
- `DF_Integer`
- `KSampler` ★核心
- `ImageScaleBy`
- `TTP_Tile_image_size`
- `ImageResize+`
- `Get resolution [Crystools]`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `Get resolution [Crystools]`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `Latent Noise Injection`
- `UltimateSDUpscaleNoUpscale`
- `VAEEncode` ★核心
- `Latent Noise Injection`
- `Upscale Model Loader`
- `easy int`
- `PreviewImage`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `SeedVR2`
- `ImageResize+`
- `TTP_Image_Assy`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `ImageUpscaleWithModel`
- `ImageFromBatch`
- `Int`
- `Int`
- `Int`
- `Int`
- `PreviewImage`
- `PreviewImage`
- `ImpactMakeAnyList`
- `SeedVR2`
- `SaveImage`
- `Int`
- `Int`
- `Int`
- `JWFloat`
- `JWFloat`
- `Int`
- `JWFloat`
- `JWFloat`
- `Fast Groups Bypasser (rgthree)`
- `AILab_QwenVL`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Note`
- `ImageResize+`
- `LoadImage`
- `Label (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `455276412503056`
- `steps` = `2`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.15000000000000002`

## 知识

覆盖率 **85%**（68/80）

**有卡**：`ImageCASharpening+`、`ImpactMinMax`、`ImageResize+`、`SimpleMath+`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`easy imageSize`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`SeedVR2`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`VAELoader`、`DF_Integer`、`KSampler`、`ImageScaleBy`、`TTP_Tile_image_size`、`Get resolution [Crystools]`、`VAEDecode`、`VAEEncode`、`Latent Noise Injection`、`UltimateSDUpscaleNoUpscale`、`Upscale Model Loader`、`easy int`、`ImageUpscaleWithModel`、`ImageFromBatch`、`Int`、`ImpactMakeAnyList`、`SaveImage`、`JWFloat`、`AILab_QwenVL`、`LoadImage`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SeedVR2

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
