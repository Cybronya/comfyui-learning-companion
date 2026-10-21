---
key: 图片生成/图生图/qwen2.1替换主体_2103386241126457346.json
name: qwen2.1替换主体_2103386241126457346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1替换主体_2103386241126457346.json
hash: 55aab2904a01e8d6
coverage: 0.823529
learned_at: 2026-10-21 00:46:12
nodes: [Anything Everywhere3, VAEDecode, PixaromaInpaintCrop, PreviewImage, PreviewImage, LoadImage, Text, LoadImage, SaveImage, ImageToMask, LoadImage, UNETLoader, CLIPLoader, VAELoader, KSampler, PixaromaUncrop, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 211867111689391, "steps": 25}
---

# 图片生成/图生图/qwen2.1替换主体_2103386241126457346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1替换主体_2103386241126457346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `Anything Everywhere3`
- `VAEDecode` ★核心
- `PixaromaInpaintCrop`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `Text`
- `LoadImage`
- `SaveImage`
- `ImageToMask`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `PixaromaUncrop`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `211867111689391`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`VAEDecode`、`PixaromaInpaintCrop`、`LoadImage`、`Text`、`SaveImage`、`ImageToMask`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`PixaromaUncrop`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage
