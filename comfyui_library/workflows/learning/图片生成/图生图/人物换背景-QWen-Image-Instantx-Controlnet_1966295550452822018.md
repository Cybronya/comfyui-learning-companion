---
key: 图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json
name: 人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json
hash: 506f13e03f6cbcea
coverage: 0.833333
learned_at: 2026-10-23 12:10:28
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, SaveImage, UNETLoader, MarkdownNote, ControlNetLoader, VAEDecode, SaveImage, VAEEncode, ModelSamplingAuraFlow, Note, CLIPTextEncode, MarkdownNote, ImageStitch, PreviewImage, MaskPreview, easy imageRemBg, InvertMask, ControlNetInpaintingAliMamaApply, CLIPTextEncode, LoadImage, ImageAndMaskPreview]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 634067893014611, "steps": 20}
---

# 图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物换背景-QWen-Image-Instantx-Controlnet_1966295550452822018.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `MarkdownNote`
- `ControlNetLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `ImageStitch`
- `PreviewImage`
- `MaskPreview`
- `easy imageRemBg`
- `InvertMask`
- `ControlNetInpaintingAliMamaApply`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageAndMaskPreview`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `634067893014611`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`UNETLoader`、`ControlNetLoader`、`VAEDecode`、`VAEEncode`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`ImageStitch`、`MaskPreview`、`easy imageRemBg`、`InvertMask`、`ControlNetInpaintingAliMamaApply`、`LoadImage`、`ImageAndMaskPreview`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
