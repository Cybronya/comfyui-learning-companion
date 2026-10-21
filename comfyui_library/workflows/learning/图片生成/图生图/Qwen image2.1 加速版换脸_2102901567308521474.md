---
key: 图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json
name: Qwen image2.1 加速版换脸_2102901567308521474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json
hash: a3e88ab9304a68cd
coverage: 0.866667
learned_at: 2026-10-21 00:43:01
nodes: [CLIPLoader, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, SaveImage, VAELoader, TextEncodeQwenImage21, PreviewImage, DrawMaskOnImage, MaskFillHoles, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 724362340742628, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1 加速版换脸_2102901567308521474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
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

## 关键参数

- `seed` = `724362340742628`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAEDecode`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`VAELoader`、`TextEncodeQwenImage21`、`DrawMaskOnImage`、`MaskFillHoles`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
