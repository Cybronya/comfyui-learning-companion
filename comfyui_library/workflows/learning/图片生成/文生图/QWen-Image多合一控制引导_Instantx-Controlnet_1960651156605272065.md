---
key: 图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json
name: QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json
hash: c76012484880912e
coverage: 0.8
learned_at: 2026-10-10 20:58:50
nodes: [CLIPLoader, VAELoader, ModelSamplingAuraFlow, Note, Canny, LoraLoaderModelOnly, KSampler, MarkdownNote, VAEDecode, SaveImage, ImageStitch, ImageStitch, SaveImage, PreviewImage, UNETLoader, ImageScaleDownToSize, ControlNetLoader, MarkdownNote, MarkdownNote, AIO_Preprocessor, CLIPTextEncode, CLIPTextEncode, ControlNetApplyAdvanced, LoadImage, VAEEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 347949227543602, "steps": 20}
---

# 图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWen-Image多合一控制引导_Instantx-Controlnet_1960651156605272065.json`

## 结构

**节点**（25 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `Note`
- `Canny`
- `LoraLoaderModelOnly`
- `KSampler`
- `MarkdownNote`
- `VAEDecode`
- `SaveImage`
- `ImageStitch`
- `ImageStitch`
- `SaveImage`
- `PreviewImage`
- `UNETLoader`
- `ImageScaleDownToSize`
- `ControlNetLoader`
- `MarkdownNote`
- `MarkdownNote`
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `ControlNetApplyAdvanced`
- `LoadImage`
- `VAEEncode`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `2.5`
- `controlnet_strength` = `1.0000000000000002`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `347949227543602`
- `steps` = `20`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`Note`、`Canny`、`LoraLoaderModelOnly`、`KSampler`、`MarkdownNote`、`VAEDecode`、`SaveImage`、`ImageStitch`、`PreviewImage`、`UNETLoader`、`ImageScaleDownToSize`、`ControlNetLoader`、`AIO_Preprocessor`
