---
key: 图片生成/图生图/调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657.json
name: 调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657.json
hash: f1c5d8d3e10411b4
coverage: 0.85
learned_at: 2026-10-23 13:28:03
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, UNETLoader, ControlNetLoader, VAEEncode, ModelSamplingAuraFlow, Note, CLIPTextEncode, ImageAndMaskPreview, ControlNetInpaintingAliMamaApply, LoadImage, ImageStitch, PreviewImage, MarkdownNote, SaveImage, SaveImage, VAEDecode, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 608177463283663, "steps": 20}
---

# 图片生成/图生图/调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/调色局部重绘-QWen-Image-Instantx-Controlnet_2026552365544902657.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ControlNetLoader`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `CLIPTextEncode` ★核心
- `ImageAndMaskPreview`
- `ControlNetInpaintingAliMamaApply`
- `LoadImage`
- `ImageStitch`
- `PreviewImage`
- `MarkdownNote`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `608177463283663`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`UNETLoader`、`ControlNetLoader`、`VAEEncode`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`ImageAndMaskPreview`、`ControlNetInpaintingAliMamaApply`、`LoadImage`、`ImageStitch`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
