---
key: 图片生成/图生图/F.2klein9b换装服装替换动作参考_2059115957766938625.json
name: F.2klein9b换装服装替换动作参考_2059115957766938625
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein9b换装服装替换动作参考_2059115957766938625.json
hash: fc349ac2d1f83f53
coverage: 0.888889
learned_at: 2026-10-23 10:52:52
nodes: [GroundingDinoModelLoader_SDPose, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, ConditioningZeroOut, KSamplerSelect, SamplerCustomAdvanced, RandomNoise, VAELoader, ConditioningZeroOut, CLIPLoader, DF_Integer, SimpleMath+, TTP_Image_Tile_Batch, ImageResize+, Get Image Size, ImpactMinMax, SetNode, DF_Integer, ImageCASharpening+, PreviewImage, Flux2Scheduler, ImageConcanate, UNETLoader, LoraLoaderModelOnly, VAEDecode, easy cleanGpuUsed, ImageResize+, PreviewImage, SeedVR2, EmptySD3LatentImage, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, TTP_Image_Assy, ImageCASharpening+, ColorCorrect, VAEDecode, ImageConcanate, ImageConcanate, CFGNorm, ModelSamplingAuraFlow, PreviewImage, SDPoseOODProcessor, SDPoseOODLoader, YOLOModelLoader, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, SaveImage, SaveImage, KSampler, PreviewImage, PreviewImage, LoadImage, ImageScaleToTotalPixels, VAEEncode, VAEEncode, CLIPTextEncode, ReferenceLatent, JWFloat, ImageScaleToTotalPixels, CFGGuider, ReferenceLatent, ReferenceLatent, ReferenceLatent, CR Text, LoadImage, Image Comparer (rgthree), PreviewImage, UNETLoader, CLIPLoader, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 8, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2klein9b换装服装替换动作参考_2059115957766938625.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein9b换装服装替换动作参考_2059115957766938625.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `GroundingDinoModelLoader_SDPose`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAELoader`
- `ConditioningZeroOut`
- `CLIPLoader`
- `DF_Integer`
- `SimpleMath+`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `Get Image Size`
- `ImpactMinMax`
- `SetNode`
- `DF_Integer`
- `ImageCASharpening+`
- `PreviewImage`
- `Flux2Scheduler`
- `ImageConcanate`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ImageResize+`
- `PreviewImage`
- `SeedVR2`
- `EmptySD3LatentImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `ColorCorrect`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SDPoseOODProcessor`
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `JWFloat`
- `ImageScaleToTotalPixels`
- `CFGGuider`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `CR Text`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `8`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（64/72）

**有卡**：`GroundingDinoModelLoader_SDPose`、`LoraLoaderModelOnly`、`VAELoader`、`ConditioningZeroOut`、`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`CLIPLoader`、`DF_Integer`、`SimpleMath+`、`TTP_Image_Tile_Batch`、`ImageResize+`、`Get Image Size`、`ImpactMinMax`、`ImageCASharpening+`、`Flux2Scheduler`、`ImageConcanate`、`UNETLoader`、`VAEDecode`、`easy cleanGpuUsed`、`SeedVR2`、`EmptySD3LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Assy`、`ColorCorrect`、`CFGNorm`、`ModelSamplingAuraFlow`、`SDPoseOODProcessor`、`SDPoseOODLoader`、`YOLOModelLoader`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`KSampler`、`LoadImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`JWFloat`、`CFGGuider`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
