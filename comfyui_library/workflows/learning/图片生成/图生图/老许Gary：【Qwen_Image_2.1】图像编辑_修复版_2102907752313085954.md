---
key: 图片生成/图生图/老许Gary：【Qwen_Image_2.1】图像编辑_修复版_2102907752313085954.json
name: 老许Gary：【Qwen_Image_2.1】图像编辑_修复版_2102907752313085954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老许Gary：【Qwen_Image_2.1】图像编辑_修复版_2102907752313085954.json
hash: 87a19fcb24f27e43
coverage: 0.95
learned_at: 2026-10-21 00:55:51
nodes: [TextConcatenator, CLIPLoader, CR Prompt Text, TextEncodeQwenImage21, KSampler, VAEDecode, BatchImagesNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, TextGenerate, UNETLoader, CLIPLoader, VAELoader, MarkdownNote, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1116671134715947, "steps": 40}
---

# 图片生成/图生图/老许Gary：【Qwen_Image_2.1】图像编辑_修复版_2102907752313085954.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老许Gary：【Qwen_Image_2.1】图像编辑_修复版_2102907752313085954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
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
- `MarkdownNote`
- `SaveImage`

## 关键参数

- `seed` = `1116671134715947`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`TextConcatenator`、`CLIPLoader`、`CR Prompt Text`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`BatchImagesNode`、`LoadImage`、`TextGenerate`、`UNETLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、CR Prompt Text
