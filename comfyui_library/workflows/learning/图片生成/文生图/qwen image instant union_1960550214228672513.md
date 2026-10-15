---
key: 图片生成/文生图/qwen image instant union_1960550214228672513.json
name: qwen image instant union_1960550214228672513
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image instant union_1960550214228672513.json
hash: 12be34af3b99254d
coverage: 0.72
learned_at: 2026-10-10 20:59:23
nodes: [MarkdownNote, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, VAEDecode, Note, Note, MarkdownNote, MarkdownNote, MarkdownNote, Canny, ControlNetApplyAdvanced, VAEEncode, CLIPTextEncode, PreviewImage, LoraLoaderModelOnly, KSampler, SaveImage, ImageScaleToTotalPixels, LoadImage, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, ControlNetLoader, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 591603842309734, "steps": 20}
---

# 图片生成/文生图/qwen image instant union_1960550214228672513.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image instant union_1960550214228672513.json`

## 结构

**节点**（25 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `ModelSamplingAuraFlow`
- `VAEDecode`
- `Note`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Canny`
- `ControlNetApplyAdvanced`
- `VAEEncode`
- `CLIPTextEncode`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `KSampler`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `ControlNetLoader`
- `CLIPTextEncode`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `2.5`
- `controlnet_strength` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `591603842309734`
- `steps` = `20`

## 知识

覆盖率 **72%**（18/25）

**有卡**：`MarkdownNote`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`Note`、`Canny`、`ControlNetApplyAdvanced`、`VAEEncode`、`CLIPTextEncode`、`PreviewImage`、`LoraLoaderModelOnly`、`KSampler`
