---
key: 图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json
name: 精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json
hash: 7d5fb941ad53c414
coverage: 0.826087
learned_at: 2026-10-23 13:21:04
nodes: [PulidInsightFaceLoader, easy imageSize, JWMaskResize, LayerMask: MaskGrow, LayerMask: MaskEdgeUltraDetail V2, ReActorFaceSwap, InstantIDFaceAnalysis, PulidModelLoader, Note, ImageToMask, CheckpointLoaderSimple, Image Comparer (rgthree), CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), ApplyInstantIDAdvanced, Note, PreviewImage, VAEEncode, CLIPTextEncode, easy seed, PulidEvaClipLoader, RH_Captioner, VAEDecode, VAEEncode, SetLatentNoiseMask, PreviewImage, LayerMask: MaskPreview, PreviewImage, Mask Fill Holes, RemapMaskRange, MaskToImage, PreviewImage, MaskToImage, Bounded Image Crop with Mask, Bounded Image Crop with Mask, JWImageResizeByLongerSide, PreviewImage, ImageToMask, easy int, ImageRandomTransform+, LayerMask: PersonMaskUltra V2, JWImageResizeByLongerSide, Bounded Image Crop with Mask, PreviewImage, Reroute, ApplyPulid, DifferentialDiffusion, KSampler, KSampler, VAEDecode, SetLatentNoiseMask, ColorMatch, JWImageResizeByLongerSide, SaveImage, ImpactMakeImageBatch, LayerMask: PersonMaskUltra V2, ControlNetLoader, InstantIDModelLoader, Bounded Image Blend, ImageConcanate, LayerUtility: PurgeVRAM, LoadImage, LoadImage, Image Comparer (rgthree), PMRF, SeedVR2, ImageConcanate, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.4000000000000001, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "denoise": 0.44, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 1010933797884400, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/精准完美换脸三合一 _ ReActor+InstantID+Pulid 终极融合方案_1956683504673284097.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `PulidInsightFaceLoader`
- `easy imageSize`
- `JWMaskResize`
- `LayerMask: MaskGrow`
- `LayerMask: MaskEdgeUltraDetail V2`
- `ReActorFaceSwap`
- `InstantIDFaceAnalysis`
- `PulidModelLoader`
- `Note`
- `ImageToMask`
- `CheckpointLoaderSimple` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Image Comparer (rgthree)`
- `ApplyInstantIDAdvanced`
- `Note`
- `PreviewImage`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy seed`
- `PulidEvaClipLoader`
- `RH_Captioner`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `Mask Fill Holes`
- `RemapMaskRange`
- `MaskToImage`
- `PreviewImage`
- `MaskToImage`
- `Bounded Image Crop with Mask`
- `Bounded Image Crop with Mask`
- `JWImageResizeByLongerSide`
- `PreviewImage`
- `ImageToMask`
- `easy int`
- `ImageRandomTransform+`
- `LayerMask: PersonMaskUltra V2`
- `JWImageResizeByLongerSide`
- `Bounded Image Crop with Mask`
- `PreviewImage`
- `Reroute`
- `ApplyPulid`
- `DifferentialDiffusion`
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetLatentNoiseMask`
- `ColorMatch`
- `JWImageResizeByLongerSide`
- `SaveImage`
- `ImpactMakeImageBatch`
- `LayerMask: PersonMaskUltra V2`
- `ControlNetLoader`
- `InstantIDModelLoader`
- `Bounded Image Blend`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PMRF`
- `SeedVR2`
- `ImageConcanate`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `dreamshaperXL_v21TurboDPMSDE.safetensors`
- `seed` = `1010933797884400`
- `steps` = `8`
- `cfg` = `1.4000000000000001`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.44`

## 知识

覆盖率 **83%**（57/69）

**有卡**：`PulidInsightFaceLoader`、`easy imageSize`、`JWMaskResize`、`LayerMask: MaskGrow`、`LayerMask: MaskEdgeUltraDetail V2`、`ReActorFaceSwap`、`InstantIDFaceAnalysis`、`PulidModelLoader`、`ImageToMask`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ApplyInstantIDAdvanced`、`VAEEncode`、`easy seed`、`PulidEvaClipLoader`、`RH_Captioner`、`VAEDecode`、`SetLatentNoiseMask`、`LayerMask: MaskPreview`、`Mask Fill Holes`、`RemapMaskRange`、`MaskToImage`、`Bounded Image Crop with Mask`、`JWImageResizeByLongerSide`、`easy int`、`ImageRandomTransform+`、`LayerMask: PersonMaskUltra V2`、`ApplyPulid`、`DifferentialDiffusion`、`KSampler`、`ColorMatch`、`SaveImage`、`ImpactMakeImageBatch`、`ControlNetLoader`、`InstantIDModelLoader`、`Bounded Image Blend`、`ImageConcanate`、`LayerUtility: PurgeVRAM`、`LoadImage`、`PMRF`、`SeedVR2`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、SeedVR2、easy seed

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
