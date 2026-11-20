---
key: 平台全量/Qwen-Image-Edit 懒人版一键去水印换背景 V1.0_1964345381922422785.json
name: Qwen-Image-Edit 懒人版一键去水印换背景 V1.0_1964345381922422785
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-Edit 懒人版一键去水印换背景 V1.0_1964345381922422785.json
hash: 9d42c5e4563dec5d
coverage: 0.933333
learned_at: 2026-11-14 00:51:40
nodes: [TextEncodeQwenImageEdit, CFGNorm, ModelSamplingAuraFlow, VAEDecode, VAELoader, ImageScaleToTotalPixels, LoraLoaderModelOnly, VAEEncode, SaveImage, MarkdownNote, CLIPLoader, UNETLoader, LoadImage, TextEncodeQwenImageEdit, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 241249976423507, "steps": 40}
---

# 平台全量/Qwen-Image-Edit 懒人版一键去水印换背景 V1.0_1964345381922422785.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-Edit 懒人版一键去水印换背景 V1.0_1964345381922422785.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `TextEncodeQwenImageEdit`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `241249976423507`
- `steps` = `40`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`TextEncodeQwenImageEdit`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAEDecode`、`VAELoader`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`VAEEncode`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm
