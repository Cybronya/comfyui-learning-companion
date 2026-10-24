---
key: 图片生成/图生图/林茜数字人_Qwen 2.1换脸工作流_2112738971427106817.json
name: 林茜数字人_Qwen 2.1换脸工作流_2112738971427106817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/林茜数字人_Qwen 2.1换脸工作流_2112738971427106817.json
hash: aed9934ddeb803c1
coverage: 0.916667
learned_at: 2026-10-23 13:09:47
nodes: [UNETLoader, VAELoader, LoadImage, ImageScaleToTotalPixels, QwenImage21Cache, TextEncodeQwenImage21, KSampler, VAEDecode, Image Comparer (rgthree), LoraLoaderModelOnly, CLIPLoader, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 969709401962603, "steps": 40}
---

# 图片生成/图生图/林茜数字人_Qwen 2.1换脸工作流_2112738971427106817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/林茜数字人_Qwen 2.1换脸工作流_2112738971427106817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `SaveImage`

## 关键参数

- `seed` = `969709401962603`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`UNETLoader`、`VAELoader`、`LoadImage`、`ImageScaleToTotalPixels`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`LoraLoaderModelOnly`、`CLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
