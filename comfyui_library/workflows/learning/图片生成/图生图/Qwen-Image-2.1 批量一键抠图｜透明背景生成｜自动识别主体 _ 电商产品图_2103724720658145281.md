---
key: 图片生成/图生图/Qwen-Image-2.1 批量一键抠图｜透明背景生成｜自动识别主体 _ 电商产品图_2103724720658145281.json
name: Qwen-Image-2.1 批量一键抠图｜透明背景生成｜自动识别主体 _ 电商产品图_2103724720658145281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 批量一键抠图｜透明背景生成｜自动识别主体 _ 电商产品图_2103724720658145281.json
hash: d9517a7ad9f2defc
coverage: 0.764706
learned_at: 2026-10-21 00:43:13
nodes: [UNETLoader, CLIPLoader, VAELoader, KSampler, PreviewImage, VAEDecode, HAIGC_SaveImagesToZip, ImageScaleToTotalPixels, easy imageSize, RHUploadZip_V2, MarkdownNote, Note, RHHiddenNodes, TextEncodeQwenImage21, RHHiddenNodes, QwenImage21Cache, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 243465076856238, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1 批量一键抠图｜透明背景生成｜自动识别主体 _ 电商产品图_2103724720658145281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 批量一键抠图｜透明背景生成｜自动识别主体 _ 电商产品图_2103724720658145281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `HAIGC_SaveImagesToZip`
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `RHUploadZip_V2`
- `MarkdownNote`
- `Note`
- `RHHiddenNodes`
- `TextEncodeQwenImage21`
- `RHHiddenNodes`
- `QwenImage21Cache`
- `MarkdownNote`

## 关键参数

- `seed` = `243465076856238`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`HAIGC_SaveImagesToZip`、`ImageScaleToTotalPixels`、`easy imageSize`、`RHUploadZip_V2`、`RHHiddenNodes`、`TextEncodeQwenImage21`、`QwenImage21Cache`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、QwenImage21Cache、UNETLoader、easy imageSize
