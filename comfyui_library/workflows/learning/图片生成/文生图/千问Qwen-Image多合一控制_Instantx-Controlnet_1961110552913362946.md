---
key: 图片生成/文生图/千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946.json
name: 千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946.json
hash: 5831a617ef8beb9d
coverage: 0.826087
learned_at: 2026-10-10 20:59:38
nodes: [CLIPLoader, VAELoader, ModelSamplingAuraFlow, LoraLoaderModelOnly, KSampler, ImageStitch, ImageStitch, PreviewImage, MarkdownNote, VAEEncode, Note, MarkdownNote, VAEDecode, SaveImage, SaveImage, CLIPTextEncode, CLIPTextEncode, LoadImage, UNETLoader, AIO_Preprocessor, ImageScaleDownToSize, ControlNetApplyAdvanced, ControlNetLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 626698065671678, "steps": 20}
---

# 图片生成/文生图/千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问Qwen-Image多合一控制_Instantx-Controlnet_1961110552913362946.json`

## 结构

**节点**（23 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly`
- `KSampler`
- `ImageStitch`
- `ImageStitch`
- `PreviewImage`
- `MarkdownNote`
- `VAEEncode`
- `Note`
- `MarkdownNote`
- `VAEDecode`
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LoadImage`
- `UNETLoader`
- `AIO_Preprocessor`
- `ImageScaleDownToSize`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `2.5`
- `controlnet_strength` = `1.0000000000000002`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `626698065671678`
- `steps` = `20`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`KSampler`、`ImageStitch`、`PreviewImage`、`MarkdownNote`、`VAEEncode`、`Note`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`LoadImage`、`UNETLoader`
