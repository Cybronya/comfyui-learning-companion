---
key: 平台全量/Face and Background Swaps_1867495175500218369.json
name: Face and Background Swaps_1867495175500218369
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Face and Background Swaps_1867495175500218369.json
hash: ce4a7fdf341a93b5
coverage: 0.6875
learned_at: 2026-11-14 00:26:28
nodes: [Anything Everywhere3, ConditioningZeroOut, ConditioningZeroOut, Image Comparer (rgthree), StyleModelApply, CannyEdgePreprocessor, GetNode, VAEEncode, SetNode, easy imageSize, JWIntegerMin, SetNode, easy imageRemBg, GetNode, CLIPVisionEncode, LoadImage, easy imageSize, VAEDecode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, Anything Everywhere, easy imageSize, ImageCompositeMasked, SetNode, PreviewImage, GrowMask, PreviewImage, LamaRemover, FluxGuidance, KSampler, Anything Everywhere3, FluxGuidance, InstructPixToPixConditioning, Fast Groups Bypasser (rgthree), GetNode, easy imageRemBg, PreviewImage, PreviewImage, Label (rgthree), UNETLoader, DualCLIPLoader, VAELoader, StyleModelLoader, CLIPVisionLoader, UnetLoaderGGUF, VAEDecode, SaveImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 44946413095850, "steps": 28}
---

# 平台全量/Face and Background Swaps_1867495175500218369.json

> 来源文件 `comfyui_library/workflows/平台全量/Face and Background Swaps_1867495175500218369.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `Anything Everywhere3`
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `StyleModelApply`
- `CannyEdgePreprocessor`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `easy imageSize`
- `JWIntegerMin`
- `SetNode`
- `easy imageRemBg`
- `GetNode`
- `CLIPVisionEncode`
- `LoadImage`
- `easy imageSize`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Anything Everywhere`
- `easy imageSize`
- `ImageCompositeMasked`
- `SetNode`
- `PreviewImage`
- `GrowMask`
- `PreviewImage`
- `LamaRemover`
- `FluxGuidance`
- `KSampler` ★核心
- `Anything Everywhere3`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `easy imageRemBg`
- `PreviewImage`
- `PreviewImage`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `UnetLoaderGGUF` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `44946413095850`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **69%**（33/48）

**有卡**：`ConditioningZeroOut`、`StyleModelApply`、`CannyEdgePreprocessor`、`VAEEncode`、`easy imageSize`、`JWIntegerMin`、`easy imageRemBg`、`CLIPVisionEncode`、`LoadImage`、`VAEDecode`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCompositeMasked`、`GrowMask`、`LamaRemover`、`FluxGuidance`、`InstructPixToPixConditioning`、`Label (rgthree)`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`StyleModelLoader`、`CLIPVisionLoader`、`UnetLoaderGGUF`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、CannyEdgePreprocessor
