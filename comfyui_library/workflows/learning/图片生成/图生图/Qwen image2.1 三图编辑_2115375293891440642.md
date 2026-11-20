---
key: 图片生成/图生图/Qwen image2.1 三图编辑_2115375293891440642.json
name: Qwen image2.1 三图编辑_2115375293891440642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1 三图编辑_2115375293891440642.json
hash: cc68a26d7c2d6b70
coverage: 0.952381
learned_at: 2026-10-30 17:50:55
nodes: [VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, SaveImage, PrimitiveStringMultiline, StringConcatenate, CLIPLoader, TextEncodeQwenImage21, LoadImage, LoadImage, UNETLoader, KSampler, LoraLoaderModelOnly, JjkShowText, ResolutionSelector, QwenImage21_EditPromptRewrite, LoadImage, ResizeLongestToNode, RHLLMChatNode, JjkShowText]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 308889807272718, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1 三图编辑_2115375293891440642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1 三图编辑_2115375293891440642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `JjkShowText`
- `ResolutionSelector`
- `QwenImage21_EditPromptRewrite`
- `LoadImage`
- `ResizeLongestToNode`
- `RHLLMChatNode`
- `JjkShowText`

## 关键参数

- `width` = `1024`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `308889807272718`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`SaveImage`、`StringConcatenate`、`TextEncodeQwenImage21`、`LoadImage`、`UNETLoader`、`KSampler`、`LoraLoaderModelOnly`、`JjkShowText`、`ResolutionSelector`、`QwenImage21_EditPromptRewrite`、`ResizeLongestToNode`、`RHLLMChatNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
