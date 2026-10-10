---
key: Qwen文生图控制(姿势、线稿、深度)InstantX-Union-ControlNet工作流_1966590309864026114.json
name: Qwen文生图控制(姿势、线稿、深度)InstantX-Union-ControlNet工作流_1966590309864026114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen文生图控制(姿势、线稿、深度)InstantX-Union-ControlNet工作流_1966590309864026114.json
hash: b2036a7bbe918348
coverage: 0.72
learned_at: 2026-10-10 20:59:09
nodes: [CLIPTextEncode, ModelSamplingAuraFlow, Note, MarkdownNote, VAELoader, Note, EmptySD3LatentImage, CLIPLoader, MarkdownNote, SetUnionControlNetType, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, CLIPTextEncode, SaveImage, ImageConcanate, VAEDecode, LoadImage, ControlNetApplySD3, UNETLoader, ControlNetLoader, LoraLoaderModelOnly, KSampler, PreviewImage, AIO_Preprocessor]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "controlnet_strength": 0.75, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 297711440235749, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen文生图控制(姿势、线稿、深度)InstantX-Union-ControlNet工作流_1966590309864026114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen文生图控制(姿势、线稿、深度)InstantX-Union-ControlNet工作流_1966590309864026114.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `MarkdownNote`
- `VAELoader`
- `Note`
- `EmptySD3LatentImage`
- `CLIPLoader`
- `MarkdownNote`
- `SetUnionControlNetType`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `LoadImage`
- `ControlNetApplySD3` ★核心
- `UNETLoader` ★核心
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `AIO_Preprocessor`

## 关键参数

- `controlnet_strength` = `0.75`
- `seed` = `297711440235749`
- `steps` = `8`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（18/25）

**有卡**：`CLIPTextEncode`、`ModelSamplingAuraFlow`、`VAELoader`、`EmptySD3LatentImage`、`CLIPLoader`、`SetUnionControlNetType`、`LoraLoaderModelOnly`、`SaveImage`、`ImageConcanate`、`VAEDecode`、`LoadImage`、`ControlNetApplySD3`、`UNETLoader`、`ControlNetLoader`、`KSampler`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
