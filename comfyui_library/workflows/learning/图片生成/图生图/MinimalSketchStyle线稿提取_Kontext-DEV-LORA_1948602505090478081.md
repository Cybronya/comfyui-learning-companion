---
key: 图片生成/图生图/MinimalSketchStyle线稿提取_Kontext-DEV-LORA_1948602505090478081.json
name: MinimalSketchStyle线稿提取_Kontext-DEV-LORA_1948602505090478081
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/MinimalSketchStyle线稿提取_Kontext-DEV-LORA_1948602505090478081.json
hash: 536c4d19af7d5b8b
coverage: 0.875
learned_at: 2026-10-23 11:09:31
nodes: [LoadImage, KSampler, VAELoader, DualCLIPLoader, FluxGuidance, ConditioningZeroOut, PreviewImage, UNETLoader, ReferenceLatent, Image Padding, ShowText|pysssss, CLIPTextEncode, TeaCache, VAEEncode, ImageStitch, VAEDecode, SaveImage, FluxKontextImageScale, LoraLoaderModelOnly, LoadImage, MarkdownNote, Text Multiline, SaveImage, CR Simple Image Compare]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 643560998990012, "steps": 20}
---

# 图片生成/图生图/MinimalSketchStyle线稿提取_Kontext-DEV-LORA_1948602505090478081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/MinimalSketchStyle线稿提取_Kontext-DEV-LORA_1948602505090478081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LoadImage`
- `KSampler` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ConditioningZeroOut`
- `PreviewImage`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `Image Padding`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `TeaCache`
- `VAEEncode` ★核心
- `ImageStitch`
- `VAEDecode` ★核心
- `SaveImage`
- `FluxKontextImageScale`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `MarkdownNote`
- `Text Multiline`
- `SaveImage`
- `CR Simple Image Compare`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `643560998990012`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`LoadImage`、`KSampler`、`VAELoader`、`DualCLIPLoader`、`FluxGuidance`、`ConditioningZeroOut`、`UNETLoader`、`ReferenceLatent`、`Image Padding`、`CLIPTextEncode`、`TeaCache`、`VAEEncode`、`ImageStitch`、`VAEDecode`、`SaveImage`、`FluxKontextImageScale`、`LoraLoaderModelOnly`、`Text Multiline`、`CR Simple Image Compare`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
