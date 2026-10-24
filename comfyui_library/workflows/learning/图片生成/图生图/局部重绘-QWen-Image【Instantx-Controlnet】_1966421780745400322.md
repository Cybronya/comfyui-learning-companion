---
key: 图片生成/图生图/局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322.json
name: 局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322.json
hash: 354d0ec882a7eb89
coverage: 0.809524
learned_at: 2026-10-23 12:49:56
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, SaveImage, UNETLoader, MarkdownNote, VAEDecode, SaveImage, VAEEncode, ModelSamplingAuraFlow, Note, ImageAndMaskPreview, ControlNetInpaintingAliMamaApply, PreviewImage, MarkdownNote, ImageStitch, ControlNetLoader, CLIPTextEncode, CLIPTextEncode, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 358665711989895, "steps": 20}
---

# 图片生成/图生图/局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘-QWen-Image【Instantx-Controlnet】_1966421780745400322.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `ImageAndMaskPreview`
- `ControlNetInpaintingAliMamaApply`
- `PreviewImage`
- `MarkdownNote`
- `ImageStitch`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `358665711989895`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`UNETLoader`、`VAEDecode`、`VAEEncode`、`ModelSamplingAuraFlow`、`ImageAndMaskPreview`、`ControlNetInpaintingAliMamaApply`、`ImageStitch`、`ControlNetLoader`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
