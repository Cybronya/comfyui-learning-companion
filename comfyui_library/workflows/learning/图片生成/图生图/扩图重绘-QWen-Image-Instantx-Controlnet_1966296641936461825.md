---
key: 图片生成/图生图/扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825.json
name: 扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825.json
hash: ae21daf77600aa17
coverage: 0.818182
learned_at: 2026-10-23 12:54:06
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, SaveImage, UNETLoader, MarkdownNote, ControlNetLoader, VAEDecode, SaveImage, VAEEncode, ModelSamplingAuraFlow, Note, CLIPTextEncode, ImageAndMaskPreview, MarkdownNote, ImageStitch, ControlNetInpaintingAliMamaApply, LoadImage, CLIPTextEncode, ImagePadForOutpaint, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 933177540700879, "steps": 20}
---

# 图片生成/图生图/扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/扩图重绘-QWen-Image-Instantx-Controlnet_1966296641936461825.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
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
- `ImageAndMaskPreview`
- `MarkdownNote`
- `ImageStitch`
- `ControlNetInpaintingAliMamaApply`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImagePadForOutpaint`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `933177540700879`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`UNETLoader`、`ControlNetLoader`、`VAEDecode`、`VAEEncode`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`ImageAndMaskPreview`、`ImageStitch`、`ControlNetInpaintingAliMamaApply`、`LoadImage`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
