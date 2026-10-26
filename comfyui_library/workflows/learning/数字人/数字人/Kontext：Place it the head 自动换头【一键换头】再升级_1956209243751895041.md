---
key: 数字人/数字人/Kontext：Place it the head 自动换头【一键换头】再升级_1956209243751895041.json
name: Kontext：Place it the head 自动换头【一键换头】再升级_1956209243751895041
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Kontext：Place it the head 自动换头【一键换头】再升级_1956209243751895041.json
hash: 477553ae0a5b6fe5
coverage: 0.764706
learned_at: 2026-10-26 01:55:39
nodes: [DualCLIPLoader, VAELoader, FaceAlign, AutoCropFaces, VAEEncode, KSampler, ConditioningZeroOut, ReferenceLatent, RepeatLatentBatch, FluxGuidance, ImageStitch, ImageStitch, easy showAnything, PreviewImage, AutoCropFaces, PreviewImage, VAEDecode, UNETLoader, Image Paste Face, PreviewImage, Reroute, LoraLoaderModelOnly, SaveImage, PreviewImage, ImageFlip+, SaveImage, Note, CLIPTextEncode, PreviewImage, ImageFlip+, LoadImage, LoadImage, FaceAnalysisModels, FluxKontextImageScale]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 705949358099720, "steps": 20}
---

# 数字人/数字人/Kontext：Place it the head 自动换头【一键换头】再升级_1956209243751895041.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Kontext：Place it the head 自动换头【一键换头】再升级_1956209243751895041.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `DualCLIPLoader`
- `VAELoader`
- `FaceAlign`
- `AutoCropFaces`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `FluxGuidance`
- `ImageStitch`
- `ImageStitch`
- `easy showAnything`
- `PreviewImage`
- `AutoCropFaces`
- `PreviewImage`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Image Paste Face`
- `PreviewImage`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PreviewImage`
- `ImageFlip+`
- `SaveImage`
- `Note`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImageFlip+`
- `LoadImage`
- `LoadImage`
- `FaceAnalysisModels`
- `FluxKontextImageScale`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `705949358099720`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`DualCLIPLoader`、`VAELoader`、`FaceAlign`、`AutoCropFaces`、`VAEEncode`、`KSampler`、`ConditioningZeroOut`、`ReferenceLatent`、`RepeatLatentBatch`、`FluxGuidance`、`ImageStitch`、`VAEDecode`、`UNETLoader`、`Image Paste Face`、`LoraLoaderModelOnly`、`SaveImage`、`ImageFlip+`、`CLIPTextEncode`、`LoadImage`、`FaceAnalysisModels`、`FluxKontextImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
