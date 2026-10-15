---
key: 图片生成/文生图/HyperLora（CN姿势控制+InstantID+面部细化）_1918163723956195329.json
name: HyperLora（CN姿势控制+InstantID+面部细化）_1918163723956195329
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HyperLora（CN姿势控制+InstantID+面部细化）_1918163723956195329.json
hash: 96be30e7c15c1ef3
coverage: 0.681319
learned_at: 2026-10-15 22:26:33
nodes: [ImpactMakeImageBatch, HyperLoRAIDCond, HyperLoRAGenerateIDLoRA, SetNode, HyperLoRAFaceAttr, HyperLoRALoader, GetNode, HyperLoRAApplyLoRA, SetNode, LayerMask: PersonMaskUltra V2, InstantIDModelLoader, CLIPTextEncode, PreviewImage, GoogleTranslateTextNode, HyperLoRAConfig, Anything Everywhere3, BNK_CLIPTextEncodeAdvanced, GetNode, CheckpointLoaderSimple, ApplyFBCacheOnModel, Note, GetNode, DifferentialDiffusion, VAEEncode, SetLatentNoiseMask, VAEDecode, Note, Note, SaveImage, PreviewImage, ShowText|pysssss, ShowText|pysssss, InstantIDFaceAnalysis, ApplyInstantID, FaceAnalysisModels, GetNode, CLIPTextEncode, ImageResize+, ImageResize+, FaceBoundingBox, PreviewImage, KSampler, LayerColor: ColorAdapter, Bounded Image Blend with Mask, Bounded Image Crop with Mask, LayerMask: MaskGrow, PreviewImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: PersonMaskUltra V2, Florence2ModelLoader, ControlNetLoader, Florence2Run, easy textSwitch, CR Text, SetNode, GetNode, PixelPerfectResolution, OpenposePreprocessor, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, InstantIDModelLoader, InstantIDFaceAnalysis, ApplyInstantID, ControlNetLoader, Reroute, BNK_CLIPTextEncodeAdvanced, LoadImage, KSampler, PreviewImage, GetNode, ImageConcanate, EmptyLatentImage, easy seed, PreviewImage, CR Text, Note, FaceDetailer, CR Text Concatenate, ControlNetApplyAdvanced, PreviewBridge, Reroute, ControlNetLoader, VAEDecode, SetNode, GetNode, SaveImage, SetNode, GetNode, UltralyticsDetectorProvider, LayerUtility: PurgeVRAM V2]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 2, "checkpoint": "juggernautXL_v9-Lightning_4S_V9 + RDPhoto 2.safetensors", "controlnet_strength": 0.7000000000000002, "denoise": 1, "height": 1024, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 516343490393189, "steps": 6, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/HyperLora（CN姿势控制+InstantID+面部细化）_1918163723956195329.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/HyperLora（CN姿势控制+InstantID+面部细化）_1918163723956195329.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `ImpactMakeImageBatch`
- `HyperLoRAIDCond`
- `HyperLoRAGenerateIDLoRA`
- `SetNode`
- `HyperLoRAFaceAttr`
- `HyperLoRALoader` ★核心
- `GetNode`
- `HyperLoRAApplyLoRA`
- `SetNode`
- `LayerMask: PersonMaskUltra V2`
- `InstantIDModelLoader`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `GoogleTranslateTextNode`
- `HyperLoRAConfig`
- `Anything Everywhere3`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `ApplyFBCacheOnModel`
- `Note`
- `GetNode`
- `DifferentialDiffusion`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `VAEDecode` ★核心
- `Note`
- `Note`
- `SaveImage`
- `PreviewImage`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `InstantIDFaceAnalysis`
- `ApplyInstantID`
- `FaceAnalysisModels`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `ImageResize+`
- `FaceBoundingBox`
- `PreviewImage`
- `KSampler` ★核心
- `LayerColor: ColorAdapter`
- `Bounded Image Blend with Mask`
- `Bounded Image Crop with Mask`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: PersonMaskUltra V2`
- `Florence2ModelLoader`
- `ControlNetLoader`
- `Florence2Run`
- `easy textSwitch`
- `CR Text`
- `SetNode`
- `GetNode`
- `PixelPerfectResolution`
- `OpenposePreprocessor`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `ApplyInstantID`
- `ControlNetLoader`
- `Reroute`
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `LoadImage`
- `KSampler` ★核心
- `PreviewImage`
- `GetNode`
- `ImageConcanate`
- `EmptyLatentImage` ★核心
- `easy seed`
- `PreviewImage`
- `CR Text`
- `Note`
- `FaceDetailer`
- `CR Text Concatenate`
- `ControlNetApplyAdvanced` ★核心
- `PreviewBridge`
- `Reroute`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SaveImage`
- `SetNode`
- `GetNode`
- `UltralyticsDetectorProvider`
- `LayerUtility: PurgeVRAM V2`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `checkpoint` = `juggernautXL_v9-Lightning_4S_V9 + RDPhoto 2.safetensors`
- `seed` = `516343490393189`
- `steps` = `6`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `controlnet_strength` = `0.7000000000000002`

## 知识

覆盖率 **68%**（62/91）

**有卡**：`ImpactMakeImageBatch`、`HyperLoRAIDCond`、`HyperLoRAGenerateIDLoRA`、`HyperLoRAFaceAttr`、`HyperLoRALoader`、`HyperLoRAApplyLoRA`、`LayerMask: PersonMaskUltra V2`、`InstantIDModelLoader`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`HyperLoRAConfig`、`BNK_CLIPTextEncodeAdvanced`、`CheckpointLoaderSimple`、`ApplyFBCacheOnModel`、`DifferentialDiffusion`、`VAEEncode`、`SetLatentNoiseMask`、`VAEDecode`、`SaveImage`、`InstantIDFaceAnalysis`、`ApplyInstantID`、`FaceAnalysisModels`、`ImageResize+`、`FaceBoundingBox`、`KSampler`、`LayerColor: ColorAdapter`、`Bounded Image Blend with Mask`、`Bounded Image Crop with Mask`、`LayerMask: MaskGrow`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Florence2ModelLoader`、`ControlNetLoader`、`Florence2Run`、`easy textSwitch`、`CR Text`、`PixelPerfectResolution`、`OpenposePreprocessor`、`ImageConcanate`、`EmptyLatentImage`、`easy seed`、`FaceDetailer`、`CR Text Concatenate`、`ControlNetApplyAdvanced`、`PreviewBridge`、`UltralyticsDetectorProvider`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、ControlNetApplyAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
