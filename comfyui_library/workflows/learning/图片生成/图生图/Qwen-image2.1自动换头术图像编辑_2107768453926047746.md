---
key: 图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json
name: Qwen-image2.1自动换头术图像编辑_2107768453926047746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json
hash: 1b76d447db64c255
coverage: 1
learned_at: 2026-10-21 00:43:30
nodes: [ImageCompare, LoadImage, LoadImage, TextEncodeQwenImage21, VAEDecode, KSampler, WujiCleaner, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, QwenImage21SageAttentionT8, LoraLoaderModelOnly, WujiUpscaler2, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107768453926047746.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ImageCompare`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `WujiCleaner`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `LoraLoaderModelOnly` ★核心
- `WujiUpscaler2`
- `SaveImage`

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ImageCompare`、`LoadImage`、`TextEncodeQwenImage21`、`VAEDecode`、`KSampler`、`WujiCleaner`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`QwenImage21SageAttentionT8`、`WujiUpscaler2`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
