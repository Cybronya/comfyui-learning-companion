---
key: 千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642.json
name: 千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642.json
hash: 9aac79bb4dc5d0a7
coverage: 0.740741
learned_at: 2026-10-10 20:59:38
nodes: [ModelSamplingAuraFlow, SaveImage, VAEDecode, ImageStitch, SaveImage, CFGNorm, UNETLoader, CLIPLoader, VAELoader, PrimitiveString, Text Concatenate, CR SDXL Aspect Ratio, ImageScaleDownToSize, GetImageSizeAndCount, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, LoadImage, KSampler, PreviewImage, LoraLoaderModelOnly, Text Multiline, MarkdownNote, VAEEncode, MarkdownNote, LoraLoaderModelOnly, AIO_Preprocessor]
patterns: [image_to_image]
missing: [Text Concatenate, Text Multiline, CR SDXL Aspect Ratio]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 967749126102292, "steps": 20}
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 千问多合一CN控制器_Union-Diffsynth_QWen-Image_1958844000902000642.json

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

覆盖率 **74%**（20/27）

**有卡**：`ModelSamplingAuraFlow`、`SaveImage`、`VAEDecode`、`ImageStitch`、`CFGNorm`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleDownToSize`、`GetImageSizeAndCount`、`ReferenceLatent`、`CLIPTextEncode`、`LoadImage`、`KSampler`、`LoraLoaderModelOnly`、`VAEEncode`、`AIO_Preprocessor`

**缺卡**（3）：`Text Concatenate`、`Text Multiline`、`CR SDXL Aspect Ratio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
