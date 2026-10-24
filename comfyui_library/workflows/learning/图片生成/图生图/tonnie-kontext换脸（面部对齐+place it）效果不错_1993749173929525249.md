---
key: 图片生成/图生图/tonnie-kontext换脸（面部对齐+place it）效果不错_1993749173929525249.json
name: tonnie-kontext换脸（面部对齐+place it）效果不错_1993749173929525249
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/tonnie-kontext换脸（面部对齐+place it）效果不错_1993749173929525249.json
hash: 2fb6c74e20d946d9
coverage: 0.724138
learned_at: 2026-10-23 11:45:41
nodes: [UNETLoader, LoraLoaderModelOnly, TeaCache, DualCLIPLoader, VAELoader, VAEEncode, ReferenceLatent, FluxGuidance, ConditioningZeroOut, KSampler, VAEDecode, PreviewImage, AutoCropFaces, PreviewImage, PreviewImage, PreviewImage, Note, AutoCropFaces, Note, FaceAlign, FaceAnalysisModels, Image Paste Crop, FluxKontextImageScale, LoadImage, LoadImage, CLIPTextEncode, Note, SaveImage, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 217958017712736, "steps": 20}
---

# 图片生成/图生图/tonnie-kontext换脸（面部对齐+place it）效果不错_1993749173929525249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/tonnie-kontext换脸（面部对齐+place it）效果不错_1993749173929525249.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `DualCLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `AutoCropFaces`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `AutoCropFaces`
- `Note`
- `FaceAlign`
- `FaceAnalysisModels`
- `Image Paste Crop`
- `FluxKontextImageScale`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Note`
- `SaveImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `217958017712736`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（21/29）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`TeaCache`、`DualCLIPLoader`、`VAELoader`、`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`AutoCropFaces`、`FaceAlign`、`FaceAnalysisModels`、`Image Paste Crop`、`FluxKontextImageScale`、`LoadImage`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
