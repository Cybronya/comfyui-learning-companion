---
key: 图片生成/图生图/qwen2.1去除油腻_2103758229087014913.json
name: qwen2.1去除油腻_2103758229087014913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1去除油腻_2103758229087014913.json
hash: 54db0d46025ac92a
coverage: 0.842105
learned_at: 2026-10-21 00:46:10
nodes: [Anything Everywhere3, VAEDecode, PixaromaInpaintCrop, PreviewImage, VAELoader, KSampler, TextEncodeQwenImage21, UNETLoader, CLIPLoader, LoraLoaderModelOnly, ImageToMask, PreviewImage, SaveImage, Text, PixaromaUncrop, LoadImage, LoadImage, Image Remove Alpha JK, ImageColorMatch+]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 474223575360350, "steps": 25}
---

# 图片生成/图生图/qwen2.1去除油腻_2103758229087014913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1去除油腻_2103758229087014913.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `PixaromaInpaintCrop`
- `PreviewImage`
- `VAELoader`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageToMask`
- `PreviewImage`
- `SaveImage`
- `Text`
- `PixaromaUncrop`
- `LoadImage`
- `LoadImage`
- `Image Remove Alpha JK`
- `ImageColorMatch+`

## 关键参数

- `seed` = `474223575360350`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`VAEDecode`、`PixaromaInpaintCrop`、`VAELoader`、`KSampler`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`ImageToMask`、`SaveImage`、`Text`、`PixaromaUncrop`、`LoadImage`、`Image Remove Alpha JK`、`ImageColorMatch+`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
