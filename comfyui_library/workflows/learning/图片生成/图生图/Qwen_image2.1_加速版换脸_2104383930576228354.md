---
key: 图片生成/图生图/Qwen_image2.1_加速版换脸_2104383930576228354.json
name: Qwen_image2.1_加速版换脸_2104383930576228354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image2.1_加速版换脸_2104383930576228354.json
hash: f9c141e0efac7664
coverage: 0.823529
learned_at: 2026-10-21 00:44:01
nodes: [CLIPLoader, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, SaveImage, VAELoader, TextEncodeQwenImage21, PreviewImage, DrawMaskOnImage, MaskFillHoles, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, LoadImage, EmptyImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 554602198321176, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_image2.1_加速版换脸_2104383930576228354.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image2.1_加速版换脸_2104383930576228354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VAELoader`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `DrawMaskOnImage`
- `MaskFillHoles`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `554602198321176`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`CLIPLoader`、`VAEDecode`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`VAELoader`、`TextEncodeQwenImage21`、`DrawMaskOnImage`、`MaskFillHoles`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
