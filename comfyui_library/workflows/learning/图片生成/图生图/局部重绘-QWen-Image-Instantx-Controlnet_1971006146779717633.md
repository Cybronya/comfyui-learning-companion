---
key: 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633.json
name: 局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633.json
hash: e82484bbe898c533
coverage: 0.85
learned_at: 2026-10-23 12:49:54
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, SaveImage, UNETLoader, ControlNetLoader, VAEDecode, SaveImage, VAEEncode, ModelSamplingAuraFlow, Note, CLIPTextEncode, LoadImage, ImageAndMaskPreview, PreviewImage, MarkdownNote, ImageStitch, CLIPTextEncode, ControlNetInpaintingAliMamaApply]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 340644179560832, "steps": 20}
---

# 图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘-QWen-Image-Instantx-Controlnet_1971006146779717633.json`

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
- `LoadImage`
- `ImageAndMaskPreview`
- `PreviewImage`
- `MarkdownNote`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `ControlNetInpaintingAliMamaApply`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `340644179560832`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`UNETLoader`、`ControlNetLoader`、`VAEDecode`、`VAEEncode`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LoadImage`、`ImageAndMaskPreview`、`ImageStitch`、`ControlNetInpaintingAliMamaApply`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
