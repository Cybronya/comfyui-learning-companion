---
key: 图片生成/图生图/4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102556522755743746.json
name: 4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102556522755743746.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102556522755743746.json
hash: 1744e3b6a536a200
coverage: 0.745098
learned_at: 2026-10-09 22:19:29
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SDPoseOODProcessor, PreviewImage, KSampler, SDPoseOODLoader, YOLOModelLoader, GroundingDinoModelLoader_SDPose, Note, CheckpointLoaderSimple, Note, TextEncodeQwenImageEditPlus, GetNode, VAEEncode, SetNode, TextEncodeQwenImageEditPlus, ConditioningZeroOut, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, PreviewImage, UNETLoader, MemoryCleaner, MemoryCleaner, MemoryCleaner, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Note, ImageScaleToTotalPixels, PreviewImage, VAEDecode, SaveImage, SaveImage, LoadImage, ModelSamplingAuraFlow, CFGNorm, EmptySD3LatentImage, VAELoader, INTConstant, KSampler, TextEncodeQwenImageEditPlus, CR Text, LoadImage, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), SeedVR2VideoUpscaler, VAEDecode, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v20.0.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 845884622820324, "steps": 6}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/4K 4K Outfit Transfer + Pose Transfer 换装迁移 +姿态迁移+人_2102556522755743746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102556522755743746.json`

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
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2VideoUpscaler`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `845884622820324`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v20.0.safetensors`

## 知识

覆盖率 **75%**（38/51）

**有卡**：`LoraLoaderModelOnly`、`SDPoseOODProcessor`、`KSampler`、`SDPoseOODLoader`、`YOLOModelLoader`、`GroundingDinoModelLoader_SDPose`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`MemoryCleaner`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleToTotalPixels`、`VAEDecode`、`SaveImage`、`LoadImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`EmptySD3LatentImage`、`VAELoader`、`INTConstant`、`SeedVR2VideoUpscaler`

**缺卡**（2）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
