---
key: 图片生成/图生图/Qwen-image2.1-换脸_2102751184430919681.json
name: Qwen-image2.1-换脸_2102751184430919681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-换脸_2102751184430919681.json
hash: 0054b1325d6400bb
coverage: 0.866667
learned_at: 2026-10-21 00:43:27
nodes: [CLIPLoader, VAEDecode, KSampler, UNETLoader, LoraLoaderModelOnly, SaveImage, VAELoader, TextEncodeQwenImage21, PreviewImage, DrawMaskOnImage, MaskFillHoles, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 334616504876072, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1-换脸_2102751184430919681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-换脸_2102751184430919681.json`

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
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`

## 关键参数

- `seed` = `334616504876072`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`CLIPLoader`、`VAEDecode`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`VAELoader`、`TextEncodeQwenImage21`、`DrawMaskOnImage`、`MaskFillHoles`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
