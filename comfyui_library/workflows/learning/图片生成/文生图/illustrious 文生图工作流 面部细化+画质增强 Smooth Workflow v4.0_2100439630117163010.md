---
key: 图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json
name: illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/illustrious 文生图工作流 面部细化+画质增强 Smooth Workflow v4.0_2100439630117163010.json
hash: 0ae5cca1dc38d4d2
coverage: 0.5
learned_at: 2026-10-07 03:05:05
nodes: [SetNode, SetNode, SetNode, KSampler, GetNode, VAEDecode, VAELoader, GetNode, CheckpointLoaderSimple, EmptyLatentImage, GetNode, GetNode, easy hiresFix, SaveImage, SAMLoader, GetNode, UltralyticsDetectorProvider, FaceDetailer, SaveImage, CLIPTextEncode, CLIPTextEncode, MarkdownNote, GetNode, Lora Loader Stack (rgthree)]
patterns: [text_to_image]
missing: [Lora Loader Stack (rgthree), easy hiresFix]
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "silvermoonmix_v60VPred.safetensors", "denoise": 1, "height": 2080, "sampler_name": "euler", "scheduler": "simple", "seed": 1020876831251013, "steps": 20, "width": 1088}
discoveries: [次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `easy hiresFix` 仅有 Upscale 的通用知识，没有该节点自己的说明]
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

覆盖率 **50%**（12/24）

**有卡**：`KSampler`、`VAEDecode`、`VAELoader`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`SaveImage`、`SAMLoader`、`UltralyticsDetectorProvider`、`FaceDetailer`、`CLIPTextEncode`

**缺卡**（2）：`Lora Loader Stack (rgthree)`、`easy hiresFix`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、FaceDetailer

## 学习发现

- 次要节点 `Lora Loader Stack (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `easy hiresFix` 仅有 Upscale 的通用知识，没有该节点自己的说明
