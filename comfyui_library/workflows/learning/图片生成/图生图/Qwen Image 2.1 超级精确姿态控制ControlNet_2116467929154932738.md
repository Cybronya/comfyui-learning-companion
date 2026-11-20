---
key: 图片生成/图生图/Qwen Image 2.1 超级精确姿态控制ControlNet_2116467929154932738.json
name: Qwen Image 2.1 超级精确姿态控制ControlNet_2116467929154932738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 超级精确姿态控制ControlNet_2116467929154932738.json
hash: 7e0bab30900addb5
coverage: 0.814815
learned_at: 2026-11-02 19:12:43
nodes: [MarkdownNote, LoadImage, MarkdownNote, SDPoseOODLoader, SDPoseOODProcessor, ResolutionSelector, PreviewImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, ZImageFunControlnet, ModelPatchLoader, BatchImagesNode, CLIPLoader, TextGenerate, MuyeTextEditOutput, PreviewAny, MuyeTextEditOutput, StringConcatenate, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 708428766240709, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 超级精确姿态控制ControlNet_2116467929154932738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 超级精确姿态控制ControlNet_2116467929154932738.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `ResolutionSelector`
- `PreviewImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ZImageFunControlnet`
- `ModelPatchLoader`
- `BatchImagesNode`
- `CLIPLoader`
- `TextGenerate`
- `MuyeTextEditOutput`
- `PreviewAny`
- `MuyeTextEditOutput`
- `StringConcatenate`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `708428766240709`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`LoadImage`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ZImageFunControlnet`、`ModelPatchLoader`、`BatchImagesNode`、`TextGenerate`、`MuyeTextEditOutput`、`StringConcatenate`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
