---
key: 图片生成/图生图/老许Gary_【Qwen_Image_2.1】图像编辑_修复版_2104380995423268865.json
name: 老许Gary_【Qwen_Image_2.1】图像编辑_修复版_2104380995423268865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老许Gary_【Qwen_Image_2.1】图像编辑_修复版_2104380995423268865.json
hash: f64563c1485c88e3
coverage: 0.952381
learned_at: 2026-10-21 00:55:50
nodes: [TextConcatenator, CLIPLoader, CR Prompt Text, TextEncodeQwenImage21, KSampler, VAEDecode, BatchImagesNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, TextGenerate, UNETLoader, CLIPLoader, VAELoader, SaveImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 364486383371045, "steps": 40}
---

# 图片生成/图生图/老许Gary_【Qwen_Image_2.1】图像编辑_修复版_2104380995423268865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老许Gary_【Qwen_Image_2.1】图像编辑_修复版_2104380995423268865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `TextConcatenator`
- `CLIPLoader`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `TextGenerate`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `364486383371045`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`TextConcatenator`、`CLIPLoader`、`CR Prompt Text`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`BatchImagesNode`、`LoadImage`、`TextGenerate`、`UNETLoader`、`VAELoader`、`SaveImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、CR Prompt Text
