---
key: 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2028996886971027458.json
name: illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2028996886971027458
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2028996886971027458.json
hash: 9d08cc44ac1ee6d1
coverage: 0.625
learned_at: 2026-10-20 23:21:57
nodes: [SetNode, SetNode, SetNode, KSampler, GetNode, VAEDecode, VAELoader, GetNode, GetNode, CheckpointLoaderSimple, Label (rgthree), EmptyLatentImage, Lora Loader Stack (rgthree), GetNode, GetNode, easy hiresFix, SaveImage, CLIPTextEncode, CLIPTextEncode, SAMLoader, GetNode, UltralyticsDetectorProvider, FaceDetailer, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "silvermoonmix_v60VPred.safetensors", "denoise": 1, "height": 2080, "sampler_name": "euler", "scheduler": "simple", "seed": 487025545233639, "steps": 20, "width": 1088}
---

# 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2028996886971027458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2028996886971027458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `KSampler` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `VAELoader`
- `GetNode`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `Label (rgthree)`
- `EmptyLatentImage` ★核心
- `Lora Loader Stack (rgthree)`
- `GetNode`
- `GetNode`
- `easy hiresFix`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SAMLoader`
- `GetNode`
- `UltralyticsDetectorProvider`
- `FaceDetailer`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `487025545233639`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `silvermoonmix_v60VPred.safetensors`
- `width` = `1088`
- `height` = `2080`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（15/24）

**有卡**：`KSampler`、`VAEDecode`、`VAELoader`、`CheckpointLoaderSimple`、`Label (rgthree)`、`EmptyLatentImage`、`Lora Loader Stack (rgthree)`、`easy hiresFix`、`SaveImage`、`CLIPTextEncode`、`SAMLoader`、`UltralyticsDetectorProvider`、`FaceDetailer`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、Lora Loader Stack (rgthree)、easy hiresFix
