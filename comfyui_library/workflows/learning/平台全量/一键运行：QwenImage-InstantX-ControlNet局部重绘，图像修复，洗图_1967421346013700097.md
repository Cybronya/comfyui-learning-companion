---
key: 平台全量/一键运行：QwenImage-InstantX-ControlNet局部重绘，图像修复，洗图_1967421346013700097.json
name: 一键运行：QwenImage-InstantX-ControlNet局部重绘，图像修复，洗图_1967421346013700097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：QwenImage-InstantX-ControlNet局部重绘，图像修复，洗图_1967421346013700097.json
hash: 263c82c7b5176abe
coverage: 0.761905
learned_at: 2026-11-14 01:30:15
nodes: [PreviewImage, ModelSamplingAuraFlow, GetImageSize, UNETLoader, LayerFilter: HDREffects, ControlNetInpaintingAliMamaApply, Prompts Everywhere, Note, CLIPTextEncode, ImageConcanate, SaveImage, CLIPLoader, CLIPTextEncode, VAELoader, KSampler (Efficient), LoadImage, Anything Everywhere, EmptyLatentImage, Anything Everywhere, ControlNetLoader, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 435384263674997, "steps": 10, "width": 512}
---

# 平台全量/一键运行：QwenImage-InstantX-ControlNet局部重绘，图像修复，洗图_1967421346013700097.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：QwenImage-InstantX-ControlNet局部重绘，图像修复，洗图_1967421346013700097.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Process → Output → Other

**节点**（21 个）：
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `GetImageSize`
- `UNETLoader` ★核心
- `LayerFilter: HDREffects`
- `ControlNetInpaintingAliMamaApply`
- `Prompts Everywhere`
- `Note`
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `SaveImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler (Efficient)` ★核心
- `LoadImage`
- `Anything Everywhere`
- `EmptyLatentImage` ★核心
- `Anything Everywhere`
- `ControlNetLoader`
- `MarkdownNote`

## 关键参数

- `seed` = `435384263674997`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`ModelSamplingAuraFlow`、`GetImageSize`、`UNETLoader`、`LayerFilter: HDREffects`、`ControlNetInpaintingAliMamaApply`、`Prompts Everywhere`、`CLIPTextEncode`、`ImageConcanate`、`SaveImage`、`CLIPLoader`、`VAELoader`、`KSampler (Efficient)`、`LoadImage`、`EmptyLatentImage`、`ControlNetLoader`

**用到的条目**：VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、UNETLoader、ControlNetInpaintingAliMamaApply、ControlNetLoader
