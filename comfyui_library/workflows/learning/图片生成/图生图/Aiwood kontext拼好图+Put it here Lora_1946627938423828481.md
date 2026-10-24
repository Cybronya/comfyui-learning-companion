---
key: 图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json
name: Aiwood kontext拼好图+Put it here Lora_1946627938423828481
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json
hash: 0229ede99c88383b
coverage: 0.871795
learned_at: 2026-10-23 10:51:00
nodes: [ConditioningZeroOut, ReferenceLatent, FluxGuidance, ImageScaleToMegapixels, ImageScaleToMegapixels, FastCanvasTool, CLIPTextEncode, ImageConcatMulti, FluxKontextImageScale, ImageScaleToMegapixels, ReferenceLatent, VAEEncode, FluxGuidance, ConditioningZeroOut, VAEDecode, PreviewImage, ImageConcanate, KSampler, easy imageRemBg, DeepTranslatorTextNode, PreviewImage, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, VAELoader, LoadImage, VAEDecode, ImageConcanate, DeepTranslatorTextNode, FastCanvas, PreviewImage, PreviewImage, PreviewImage, SaveImage, SaveImage, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 20}
---

# 图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Aiwood kontext拼好图+Put it here Lora_1946627938423828481.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxGuidance`
- `ImageScaleToMegapixels`
- `ImageScaleToMegapixels`
- `FastCanvasTool`
- `CLIPTextEncode` ★核心
- `ImageConcatMulti`
- `FluxKontextImageScale`
- `ImageScaleToMegapixels`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageConcanate`
- `KSampler` ★核心
- `easy imageRemBg`
- `DeepTranslatorTextNode`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `DeepTranslatorTextNode`
- `FastCanvas`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `999`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`ConditioningZeroOut`、`ReferenceLatent`、`FluxGuidance`、`ImageScaleToMegapixels`、`FastCanvasTool`、`CLIPTextEncode`、`ImageConcatMulti`、`FluxKontextImageScale`、`VAEEncode`、`VAEDecode`、`ImageConcanate`、`KSampler`、`easy imageRemBg`、`DeepTranslatorTextNode`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`FastCanvas`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
