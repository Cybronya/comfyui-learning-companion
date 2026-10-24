---
key: 图片生成/图生图/Qwen-ImageEdit多图编辑+InstantID角色保持v1_1957745161907568642.json
name: Qwen-ImageEdit多图编辑+InstantID角色保持v1_1957745161907568642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-ImageEdit多图编辑+InstantID角色保持v1_1957745161907568642.json
hash: dcc6e19529b0d11a
coverage: 0.843137
learned_at: 2026-10-23 11:17:21
nodes: [Note, ModelSamplingAuraFlow, CLIPTextEncode, Note, EmptySD3LatentImage, CLIPTextEncode, InpaintModelConditioning, InstantIDFaceAnalysis, InpaintStitchImproved, GrowMaskWithBlur, MaskPreview+, FaceAnalysisModels, VAEDecode, PreviewImage, ImageResize+, FaceSegmentation, VAEDecode, easy imageRemBg, Get Image Size, PreviewImage, DifferentialDiffusion, KSampler, easy imageRemBg, LoadImage, MaskPreview+, InpaintCropImproved, KSampler, InstantIDModelLoader, ControlNetLoader, ApplyInstantID, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, CheckpointLoaderSimple, InpaintResize, ImageConcatMulti, BetterFilmGrain, ImageConcanate, PreviewImage, easy imageRemBg, PreviewImage, SaveImage, PreviewImage, PreviewImage, CLIPTextEncode, LoadImage, LoadImage, ImageScaleToMegapixels, TextEncodeQwenImageEdit, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "boltningRealistic_v10.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 586042185275710, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-ImageEdit多图编辑+InstantID角色保持v1_1957745161907568642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-ImageEdit多图编辑+InstantID角色保持v1_1957745161907568642.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
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
- `DifferentialDiffusion`
- `KSampler` ★核心
- `easy imageRemBg`
- `LoadImage`
- `MaskPreview+`
- `InpaintCropImproved`
- `KSampler` ★核心
- `InstantIDModelLoader`
- `ControlNetLoader`
- `ApplyInstantID`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `InpaintResize`
- `ImageConcatMulti`
- `BetterFilmGrain`
- `ImageConcanate`
- `PreviewImage`
- `easy imageRemBg`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `ImageScaleToMegapixels`
- `TextEncodeQwenImageEdit`
- `CR Text`

## 关键参数

- `seed` = `586042185275710`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `boltningRealistic_v10.safetensors`

## 知识

覆盖率 **84%**（43/51）

**有卡**：`ModelSamplingAuraFlow`、`CLIPTextEncode`、`EmptySD3LatentImage`、`InpaintModelConditioning`、`InstantIDFaceAnalysis`、`InpaintStitchImproved`、`GrowMaskWithBlur`、`MaskPreview+`、`FaceAnalysisModels`、`VAEDecode`、`ImageResize+`、`FaceSegmentation`、`easy imageRemBg`、`Get Image Size`、`DifferentialDiffusion`、`KSampler`、`LoadImage`、`InpaintCropImproved`、`InstantIDModelLoader`、`ControlNetLoader`、`ApplyInstantID`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`InpaintResize`、`ImageConcatMulti`、`BetterFilmGrain`、`ImageConcanate`、`SaveImage`、`ImageScaleToMegapixels`、`TextEncodeQwenImageEdit`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
