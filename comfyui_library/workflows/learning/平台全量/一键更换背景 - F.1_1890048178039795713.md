---
key: 平台全量/一键更换背景 - F.1_1890048178039795713.json
name: 一键更换背景 - F.1_1890048178039795713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键更换背景 - F.1_1890048178039795713.json
hash: c45e04f8eb07f5b2
coverage: 0.923077
learned_at: 2026-11-14 01:28:57
nodes: [ShowText|pysssss, InpaintModelConditioning, MaskPreview+, PreviewImage, StyleModelApply, DifferentialDiffusion, LoadImage, LoadImage, MaskToSEGS, preview_mask, GrowMaskWithBlur, GrowMaskWithBlur, CLIPTextEncodeFlux, Text Concatenate (JPS), CLIPTextEncode, ConditioningZeroOut, CLIPTextEncodeFlux, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, Joy_caption_two, SaveImage, Image Comparer (rgthree), DetailerForEach, SaveImage, CR Text, VAELoader, Joy_caption_two_load, UNETLoader, DualCLIPLoader, LoraLoader, CLIPVisionLoader, CLIPVisionEncode, StyleModelLoader, UNETLoader, LoraLoaderModelOnly, ConstrainImage|pysssss, LayerMask: SegmentAnythingUltra V2, KSampler]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "In-Context-LoRA_电影分镜头生成.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 827816625666086, "steps": 30, "strength_clip": 1, "strength_model": 0.6}
---

# 平台全量/一键更换背景 - F.1_1890048178039795713.json

> 来源文件 `comfyui_library/workflows/平台全量/一键更换背景 - F.1_1890048178039795713.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `ShowText|pysssss`
- `InpaintModelConditioning`
- `MaskPreview+`
- `PreviewImage`
- `StyleModelApply`
- `DifferentialDiffusion`
- `LoadImage`
- `LoadImage`
- `MaskToSEGS`
- `preview_mask`
- `GrowMaskWithBlur`
- `GrowMaskWithBlur`
- `CLIPTextEncodeFlux` ★核心
- `Text Concatenate (JPS)`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncodeFlux` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Joy_caption_two`
- `SaveImage`
- `Image Comparer (rgthree)`
- `DetailerForEach`
- `SaveImage`
- `CR Text`
- `VAELoader`
- `Joy_caption_two_load`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConstrainImage|pysssss`
- `LayerMask: SegmentAnythingUltra V2`
- `KSampler` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `In-Context-LoRA_电影分镜头生成.safetensors`
- `strength_model` = `0.6`
- `strength_clip` = `1`
- `seed` = `827816625666086`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`InpaintModelConditioning`、`MaskPreview+`、`StyleModelApply`、`DifferentialDiffusion`、`LoadImage`、`MaskToSEGS`、`preview_mask`、`GrowMaskWithBlur`、`CLIPTextEncodeFlux`、`Text Concatenate (JPS)`、`CLIPTextEncode`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`VAEDecode`、`Joy_caption_two`、`SaveImage`、`DetailerForEach`、`CR Text`、`VAELoader`、`Joy_caption_two_load`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`StyleModelLoader`、`LoraLoaderModelOnly`、`ConstrainImage|pysssss`、`LayerMask: SegmentAnythingUltra V2`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
