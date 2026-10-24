---
key: 图片生成/图生图/Aiwood-千问imageEdit拼好图+InstantID角色保持_1957718066450853889.json
name: Aiwood-千问imageEdit拼好图+InstantID角色保持_1957718066450853889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Aiwood-千问imageEdit拼好图+InstantID角色保持_1957718066450853889.json
hash: 249f554cbaec6563
coverage: 0.84
learned_at: 2026-10-23 10:51:01
nodes: [Note, ModelSamplingAuraFlow, CLIPTextEncode, Note, EmptySD3LatentImage, CLIPTextEncode, InpaintModelConditioning, InstantIDFaceAnalysis, InpaintStitchImproved, GrowMaskWithBlur, MaskPreview+, FaceAnalysisModels, VAEDecode, PreviewImage, ImageResize+, FaceSegmentation, VAEDecode, easy imageRemBg, Get Image Size, PreviewImage, CLIPTextEncode, DifferentialDiffusion, KSampler, easy imageRemBg, LoadImage, MaskPreview+, InpaintCropImproved, TextEncodeQwenImageEdit, KSampler, InstantIDModelLoader, ControlNetLoader, ApplyInstantID, PreviewImage, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, CheckpointLoaderSimple, InpaintResize, LoadImage, ImageScaleToMegapixels, LoadImage, ImageConcatMulti, BetterFilmGrain, SaveImage, PreviewImage, PreviewImage, ImageConcanate, PreviewImage, easy imageRemBg]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "boltningRealistic_v10.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 900714287981434, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Aiwood-千问imageEdit拼好图+InstantID角色保持_1957718066450853889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Aiwood-千问imageEdit拼好图+InstantID角色保持_1957718066450853889.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `Note`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `Note`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InpaintStitchImproved`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `FaceAnalysisModels`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageResize+`
- `FaceSegmentation`
- `VAEDecode` ★核心
- `easy imageRemBg`
- `Get Image Size`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `DifferentialDiffusion`
- `KSampler` ★核心
- `easy imageRemBg`
- `LoadImage`
- `MaskPreview+`
- `InpaintCropImproved`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心
- `InstantIDModelLoader`
- `ControlNetLoader`
- `ApplyInstantID`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `InpaintResize`
- `LoadImage`
- `ImageScaleToMegapixels`
- `LoadImage`
- `ImageConcatMulti`
- `BetterFilmGrain`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `ImageConcanate`
- `PreviewImage`
- `easy imageRemBg`

## 关键参数

- `seed` = `900714287981434`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `boltningRealistic_v10.safetensors`

## 知识

覆盖率 **84%**（42/50）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`EmptySD3LatentImage`、`InpaintModelConditioning`、`InstantIDFaceAnalysis`、`InpaintStitchImproved`、`GrowMaskWithBlur`、`MaskPreview+`、`FaceAnalysisModels`、`VAEDecode`、`ImageResize+`、`FaceSegmentation`、`easy imageRemBg`、`Get Image Size`、`DifferentialDiffusion`、`KSampler`、`LoadImage`、`InpaintCropImproved`、`TextEncodeQwenImageEdit`、`InstantIDModelLoader`、`ControlNetLoader`、`ApplyInstantID`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`InpaintResize`、`ImageScaleToMegapixels`、`ImageConcatMulti`、`BetterFilmGrain`、`SaveImage`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
