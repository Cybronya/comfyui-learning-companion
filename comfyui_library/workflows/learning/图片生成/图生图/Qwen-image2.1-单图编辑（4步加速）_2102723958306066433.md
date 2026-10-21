---
key: 图片生成/图生图/Qwen-image2.1-单图编辑（4步加速）_2102723958306066433.json
name: Qwen-image2.1-单图编辑（4步加速）_2102723958306066433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-单图编辑（4步加速）_2102723958306066433.json
hash: 0a28f1992f8701d4
coverage: 0.9
learned_at: 2026-10-21 00:43:26
nodes: [CLIPLoader, SaveImage, VAEDecode, LoadImage, VAELoader, UNETLoader, KSampler, PreviewImage, TextEncodeQwenImage21, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 647182085624182, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1-单图编辑（4步加速）_2102723958306066433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-单图编辑（4步加速）_2102723958306066433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPLoader`
- `SaveImage`
- `VAEDecode` ★核心
- `LoadImage`
- `VAELoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `647182085624182`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPLoader`、`SaveImage`、`VAEDecode`、`LoadImage`、`VAELoader`、`UNETLoader`、`KSampler`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
