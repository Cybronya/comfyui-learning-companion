---
key: 图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json
name: Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json
hash: f4e9a7128bb616fc
coverage: 0.928571
learned_at: 2026-10-21 00:42:12
nodes: [CLIPLoader, VAELoader, UNETLoader, SeedNode, TextEncodeQwenImage21, LoraLoaderModelOnly, QwenImage21Cache, KSampler, VAEDecode, SplitImageWithAlpha, LoadImage, SaveImage, CR Text, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25}
---

# 图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图片清晰度增强与细节修复 V1_2108522729849843713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SeedNode`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SplitImageWithAlpha`
- `LoadImage`
- `SaveImage`
- `CR Text`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `0`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`SeedNode`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SplitImageWithAlpha`、`LoadImage`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
