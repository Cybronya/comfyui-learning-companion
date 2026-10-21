---
key: 图片生成/图生图/Posture Control4K Outfit Transfer Pose   换装迁移 姿态迁移_2107627479518240770.json
name: Posture Control4K Outfit Transfer Pose   换装迁移 姿态迁移_2107627479518240770
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Posture Control4K Outfit Transfer Pose   换装迁移 姿态迁移_2107627479518240770.json
hash: 9e00296b4ef36569
coverage: 0.784314
learned_at: 2026-10-21 00:41:52
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SDPoseOODProcessor, PreviewImage, KSampler, SDPoseOODLoader, YOLOModelLoader, GroundingDinoModelLoader_SDPose, Note, CheckpointLoaderSimple, Note, TextEncodeQwenImageEditPlus, GetNode, VAEEncode, SetNode, TextEncodeQwenImageEditPlus, ConditioningZeroOut, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, PreviewImage, UNETLoader, MemoryCleaner, MemoryCleaner, MemoryCleaner, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Note, ImageScaleToTotalPixels, PreviewImage, VAEDecode, SaveImage, SaveImage, LoadImage, ModelSamplingAuraFlow, CFGNorm, EmptySD3LatentImage, VAELoader, INTConstant, KSampler, TextEncodeQwenImageEditPlus, CR Text, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), SeedVR2VideoUpscaler, VAEDecode, Image Comparer (rgthree), LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v20.0.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 925258820462391, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Posture Control4K Outfit Transfer Pose   换装迁移 姿态迁移_2107627479518240770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Posture Control4K Outfit Transfer Pose   换装迁移 姿态迁移_2107627479518240770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SDPoseOODProcessor`
- `PreviewImage`
- `KSampler` ★核心
- `SDPoseOODLoader`
- `YOLOModelLoader`
- `GroundingDinoModelLoader_SDPose`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `UNETLoader` ★核心
- `MemoryCleaner`
- `MemoryCleaner`
- `MemoryCleaner`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Note`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `EmptySD3LatentImage`
- `VAELoader`
- `INTConstant`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `CR Text`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2VideoUpscaler`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `925258820462391`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v20.0.safetensors`

## 知识

覆盖率 **78%**（40/51）

**有卡**：`LoraLoaderModelOnly`、`SDPoseOODProcessor`、`KSampler`、`SDPoseOODLoader`、`YOLOModelLoader`、`GroundingDinoModelLoader_SDPose`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ConditioningZeroOut`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`MemoryCleaner`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`LoadImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`EmptySD3LatentImage`、`VAELoader`、`INTConstant`、`CR Text`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
