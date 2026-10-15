---
key: 图片生成/文生图/千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642.json
name: 千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642.json
hash: 9aac79bb4dc5d0a7
coverage: 0.851852
learned_at: 2026-10-15 22:28:17
nodes: [ModelSamplingAuraFlow, SaveImage, VAEDecode, ImageStitch, SaveImage, CFGNorm, UNETLoader, CLIPLoader, VAELoader, PrimitiveString, Text Concatenate, CR SDXL Aspect Ratio, ImageScaleDownToSize, GetImageSizeAndCount, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, LoadImage, KSampler, PreviewImage, LoraLoaderModelOnly, Text Multiline, MarkdownNote, VAEEncode, MarkdownNote, LoraLoaderModelOnly, AIO_Preprocessor]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 967749126102292, "steps": 20}
---

# 图片生成/文生图/千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageStitch`
- `SaveImage`
- `CFGNorm`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveString`
- `Text Concatenate`
- `CR SDXL Aspect Ratio`
- `ImageScaleDownToSize`
- `GetImageSizeAndCount`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `Text Multiline`
- `MarkdownNote`
- `VAEEncode` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `AIO_Preprocessor`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `967749126102292`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`ModelSamplingAuraFlow`、`SaveImage`、`VAEDecode`、`ImageStitch`、`CFGNorm`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Text Concatenate`、`CR SDXL Aspect Ratio`、`ImageScaleDownToSize`、`GetImageSizeAndCount`、`ReferenceLatent`、`CLIPTextEncode`、`LoadImage`、`KSampler`、`LoraLoaderModelOnly`、`Text Multiline`、`VAEEncode`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
