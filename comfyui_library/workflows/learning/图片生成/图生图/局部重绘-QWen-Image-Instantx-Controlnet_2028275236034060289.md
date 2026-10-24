---
key: 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289.json
name: 局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289.json
hash: 92a84d701fc82d9b
coverage: 0.85
learned_at: 2026-10-23 12:49:54
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, SaveImage, UNETLoader, ControlNetLoader, VAEDecode, SaveImage, VAEEncode, ModelSamplingAuraFlow, Note, CLIPTextEncode, ImageAndMaskPreview, PreviewImage, MarkdownNote, ImageStitch, ControlNetInpaintingAliMamaApply, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 813627022032334, "steps": 20}
---

# 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_2028275236034060289.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `CLIPTextEncode` ★核心
- `ImageAndMaskPreview`
- `PreviewImage`
- `MarkdownNote`
- `ImageStitch`
- `ControlNetInpaintingAliMamaApply`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `813627022032334`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`UNETLoader`、`ControlNetLoader`、`VAEDecode`、`VAEEncode`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`ImageAndMaskPreview`、`ImageStitch`、`ControlNetInpaintingAliMamaApply`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
