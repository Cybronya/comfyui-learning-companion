---
key: 平台全量/换装+动作迁移 qwen 人物一致 平替Seedream 4.5  全能图片V1 Pro2.0_2003352801348550657.json
name: 换装+动作迁移 qwen 人物一致 平替Seedream 4.5  全能图片V1 Pro2.0_2003352801348550657
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/换装+动作迁移 qwen 人物一致 平替Seedream 4.5  全能图片V1 Pro2.0_2003352801348550657.json
hash: bb8a4a0802f8bb4b
coverage: 0.861111
learned_at: 2026-11-14 02:09:08
nodes: [GroundingDinoModelLoader_SDPose, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, Image Comparer (rgthree), TextEncodeQwenImageEditPlus, VAEDecode, PreviewImage, YOLOModelLoader, SDPoseOODProcessor, PreviewImage, TextEncodeQwenImageEditPlus, VAEEncode, VAEDecode, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, EmptySD3LatentImage, CFGNorm, ConditioningZeroOut, KSampler, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingAuraFlow, KSampler, SDPoseOODLoader, SaveImage, GetNode, LoadImage, LoadImage, UNETLoader, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-SFW-v11.safetensors", "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 558278695620541, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/换装+动作迁移 qwen 人物一致 平替Seedream 4.5  全能图片V1 Pro2.0_2003352801348550657.json

> 来源文件 `comfyui_library/workflows/平台全量/换装+动作迁移 qwen 人物一致 平替Seedream 4.5  全能图片V1 Pro2.0_2003352801348550657.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `GroundingDinoModelLoader_SDPose`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `PreviewImage`
- `YOLOModelLoader`
- `SDPoseOODProcessor`
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `CFGNorm`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `SDPoseOODLoader`
- `SaveImage`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-SFW-v11.safetensors`
- `seed` = `558278695620541`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`GroundingDinoModelLoader_SDPose`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`YOLOModelLoader`、`SDPoseOODProcessor`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`EmptySD3LatentImage`、`CFGNorm`、`ConditioningZeroOut`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`SDPoseOODLoader`、`SaveImage`、`LoadImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
