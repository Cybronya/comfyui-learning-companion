---
key: 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json
name: illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json
hash: 0ae5cca1dc38d4d2
coverage: 0.583333
learned_at: 2026-10-15 22:27:48
nodes: [SetNode, SetNode, SetNode, KSampler, GetNode, VAEDecode, VAELoader, GetNode, CheckpointLoaderSimple, EmptyLatentImage, GetNode, GetNode, easy hiresFix, SaveImage, SAMLoader, GetNode, UltralyticsDetectorProvider, FaceDetailer, SaveImage, CLIPTextEncode, CLIPTextEncode, MarkdownNote, GetNode, Lora Loader Stack (rgthree)]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "silvermoonmix_v60VPred.safetensors", "denoise": 1, "height": 2080, "sampler_name": "euler", "scheduler": "simple", "seed": 1020876831251013, "steps": 20, "width": 1088}
---

# 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json`

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
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `GetNode`
- `GetNode`
- `easy hiresFix`
- `SaveImage`
- `SAMLoader`
- `GetNode`
- `UltralyticsDetectorProvider`
- `FaceDetailer`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `GetNode`
- `Lora Loader Stack (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `1020876831251013`
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

覆盖率 **58%**（14/24）

**有卡**：`KSampler`、`VAEDecode`、`VAELoader`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`easy hiresFix`、`SaveImage`、`SAMLoader`、`UltralyticsDetectorProvider`、`FaceDetailer`、`CLIPTextEncode`、`Lora Loader Stack (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、Lora Loader Stack (rgthree)、easy hiresFix
