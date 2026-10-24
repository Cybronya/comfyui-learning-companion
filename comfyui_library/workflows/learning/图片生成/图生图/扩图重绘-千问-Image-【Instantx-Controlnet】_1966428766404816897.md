---
key: 图片生成/图生图/扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897.json
name: 扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897.json
hash: 2a58986dfb0f3149
coverage: 0.857143
learned_at: 2026-10-23 12:54:06
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, SaveImage, UNETLoader, ControlNetLoader, VAEDecode, SaveImage, VAEEncode, ModelSamplingAuraFlow, Note, ImageAndMaskPreview, MarkdownNote, ImageStitch, ControlNetInpaintingAliMamaApply, LoadImage, ImagePadForOutpaint, PreviewImage, CLIPTextEncode, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 681387158891744, "steps": 20}
---

# 图片生成/图生图/扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/扩图重绘-千问-Image-【Instantx-Controlnet】_1966428766404816897.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
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
- `ImageAndMaskPreview`
- `MarkdownNote`
- `ImageStitch`
- `ControlNetInpaintingAliMamaApply`
- `LoadImage`
- `ImagePadForOutpaint`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `681387158891744`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`UNETLoader`、`ControlNetLoader`、`VAEDecode`、`VAEEncode`、`ModelSamplingAuraFlow`、`ImageAndMaskPreview`、`ImageStitch`、`ControlNetInpaintingAliMamaApply`、`LoadImage`、`ImagePadForOutpaint`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
