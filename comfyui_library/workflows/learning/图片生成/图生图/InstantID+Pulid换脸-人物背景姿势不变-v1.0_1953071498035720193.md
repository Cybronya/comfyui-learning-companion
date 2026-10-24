---
key: 图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json
name: InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json
hash: 478ec40bf273beb3
coverage: 0.830986
learned_at: 2026-10-23 11:03:44
nodes: [PulidInsightFaceLoader, easy imageSize, JWMaskResize, LayerMask: MaskGrow, LayerMask: MaskEdgeUltraDetail V2, ReActorFaceSwap, InstantIDFaceAnalysis, PulidModelLoader, ImageConcanate, Note, ImageToMask, CheckpointLoaderSimple, Image Comparer (rgthree), CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), ApplyInstantIDAdvanced, Note, PreviewImage, VAEEncode, CLIPTextEncode, easy seed, LoadImage, PulidEvaClipLoader, RH_Captioner, VAEDecode, VAEEncode, SetLatentNoiseMask, PreviewImage, LayerMask: MaskPreview, LoadImage, PreviewImage, Mask Fill Holes, RemapMaskRange, MaskToImage, PreviewImage, MaskToImage, Bounded Image Crop with Mask, Bounded Image Crop with Mask, JWImageResizeByLongerSide, PreviewImage, ImageToMask, easy int, ImageRandomTransform+, LayerMask: PersonMaskUltra V2, JWImageResizeByLongerSide, Bounded Image Crop with Mask, PreviewImage, Reroute, ApplyPulid, DifferentialDiffusion, KSampler, KSampler, VAEDecode, SetLatentNoiseMask, ColorMatch, JWImageResizeByLongerSide, Image Comparer (rgthree), SaveImage, SaveImage, ImpactMakeImageBatch, LoadImage, SaveImage, LayerMask: PersonMaskUltra V2, ControlNetLoader, InstantIDModelLoader, Bounded Image Blend, ImageConcanate, LayerUtility: PurgeVRAM, SeedVR2, PMRF]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.4000000000000001, "checkpoint": "dreamshaperXL_v21TurboDPMSDE.safetensors", "denoise": 0.44, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 1010933797884400, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/InstantID+Pulid换脸-人物背景姿势不变-v1.0_1953071498035720193.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `PulidInsightFaceLoader`
- `easy imageSize`
- `JWMaskResize`
- `LayerMask: MaskGrow`
- `LayerMask: MaskEdgeUltraDetail V2`
- `ReActorFaceSwap`
- `InstantIDFaceAnalysis`
- `PulidModelLoader`
- `ImageConcanate`
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
- `LoadImage`
- `PulidEvaClipLoader`
- `RH_Captioner`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LoadImage`
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
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `ImpactMakeImageBatch`
- `LoadImage`
- `SaveImage`
- `LayerMask: PersonMaskUltra V2`
- `ControlNetLoader`
- `InstantIDModelLoader`
- `Bounded Image Blend`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM`
- `SeedVR2`
- `PMRF`

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

覆盖率 **83%**（59/71）

**有卡**：`PulidInsightFaceLoader`、`easy imageSize`、`JWMaskResize`、`LayerMask: MaskGrow`、`LayerMask: MaskEdgeUltraDetail V2`、`ReActorFaceSwap`、`InstantIDFaceAnalysis`、`PulidModelLoader`、`ImageConcanate`、`ImageToMask`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ApplyInstantIDAdvanced`、`VAEEncode`、`easy seed`、`LoadImage`、`PulidEvaClipLoader`、`RH_Captioner`、`VAEDecode`、`SetLatentNoiseMask`、`LayerMask: MaskPreview`、`Mask Fill Holes`、`RemapMaskRange`、`MaskToImage`、`Bounded Image Crop with Mask`、`JWImageResizeByLongerSide`、`easy int`、`ImageRandomTransform+`、`LayerMask: PersonMaskUltra V2`、`ApplyPulid`、`DifferentialDiffusion`、`KSampler`、`ColorMatch`、`SaveImage`、`ImpactMakeImageBatch`、`ControlNetLoader`、`InstantIDModelLoader`、`Bounded Image Blend`、`LayerUtility: PurgeVRAM`、`SeedVR2`、`PMRF`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、SeedVR2、easy seed

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
