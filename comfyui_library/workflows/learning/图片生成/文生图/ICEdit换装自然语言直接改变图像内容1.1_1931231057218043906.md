---
key: 图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json
name: ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json
hash: 1ef19c537e2cb55f
coverage: 0.894737
learned_at: 2026-10-15 22:26:33
nodes: [Evaluate Strings, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, InpaintModelConditioning, Text Multiline, Seed Everywhere, EmptyImage, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, DifferentialDiffusion, FaceAnalysisModels, FaceBoundingBox, ImageResize+, easy makeImageForICLora, PreviewImage, MaskPreview+, VAEDecode, easy imageInsetCrop, PreviewImage, SaveImage, Image Comparer (rgthree), BaiduTranslateNode, UpscaleModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PreviewImage, ApplyPulidFlux, UltimateSDUpscale, LoadImage, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, UNETLoader, PulidFluxModelLoader, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 975732478488269, "steps": 35}
---

# 图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `Evaluate Strings`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `Text Multiline`
- `Seed Everywhere`
- `EmptyImage`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DifferentialDiffusion`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `ImageResize+`
- `easy makeImageForICLora`
- `PreviewImage`
- `MaskPreview+`
- `VAEDecode` ★核心
- `easy imageInsetCrop`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `BaiduTranslateNode`
- `UpscaleModelLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PreviewImage`
- `ApplyPulidFlux`
- `UltimateSDUpscale`
- `LoadImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `PulidFluxModelLoader`
- `KSampler` ★核心

## 关键参数

- `seed` = `975732478488269`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`Evaluate Strings`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`InpaintModelConditioning`、`Text Multiline`、`Seed Everywhere`、`EmptyImage`、`ImageToMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`DifferentialDiffusion`、`FaceAnalysisModels`、`FaceBoundingBox`、`ImageResize+`、`easy makeImageForICLora`、`MaskPreview+`、`VAEDecode`、`easy imageInsetCrop`、`SaveImage`、`BaiduTranslateNode`、`UpscaleModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`ApplyPulidFlux`、`UltimateSDUpscale`、`LoadImage`、`VAELoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`UNETLoader`、`PulidFluxModelLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
