---
key: 图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json
name: Qwen-image2.1自动换头术图像编辑_2107805917923336194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json
hash: a5a6b82716b2c907
coverage: 1
learned_at: 2026-10-21 00:43:31
nodes: [ImageCompare, LoadImage, LoadImage, QwenImage21Cache, LoraLoaderModelOnly, TextEncodeQwenImage21, VAEDecode, WujiUpscaler2, KSampler, WujiCleaner, SaveImage, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1自动换头术图像编辑_2107805917923336194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ImageCompare`
- `LoadImage`
- `LoadImage`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `WujiUpscaler2`
- `KSampler` ★核心
- `WujiCleaner`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ImageCompare`、`LoadImage`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`VAEDecode`、`WujiUpscaler2`、`KSampler`、`WujiCleaner`、`SaveImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
