---
key: 图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json
name: ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json
hash: 1ef19c537e2cb55f
coverage: 0.684211
learned_at: 2026-10-07 22:34:40
nodes: [Evaluate Strings, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, InpaintModelConditioning, Text Multiline, Seed Everywhere, EmptyImage, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, DifferentialDiffusion, FaceAnalysisModels, FaceBoundingBox, ImageResize+, easy makeImageForICLora, PreviewImage, MaskPreview+, VAEDecode, easy imageInsetCrop, PreviewImage, SaveImage, Image Comparer (rgthree), BaiduTranslateNode, UpscaleModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PreviewImage, ApplyPulidFlux, UltimateSDUpscale, LoadImage, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, UNETLoader, PulidFluxModelLoader, KSampler]
patterns: []
missing: [Evaluate Strings, LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, easy imageInsetCrop, ImageResize+, MaskPreview+, Seed Everywhere, easy makeImageForICLora]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 975732478488269, "steps": 35}
discoveries: [次要节点 `Evaluate Strings` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageInsetCrop` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy makeImageForICLora` 仅有 LoRA 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/ICEdit换装自然语言直接改变图像内容1.1_1931231057218043906.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1931231057218043906.json`

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

覆盖率 **68%**（26/38）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`InpaintModelConditioning`、`EmptyImage`、`ImageToMask`、`DifferentialDiffusion`、`FaceAnalysisModels`、`FaceBoundingBox`、`VAEDecode`、`SaveImage`、`BaiduTranslateNode`、`UpscaleModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`ApplyPulidFlux`、`UltimateSDUpscale`、`LoadImage`、`VAELoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`UNETLoader`、`PulidFluxModelLoader`、`KSampler`

**缺卡**（8）：`Evaluate Strings`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Multiline`、`easy imageInsetCrop`、`ImageResize+`、`MaskPreview+`、`Seed Everywhere`、`easy makeImageForICLora`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 学习发现

- 次要节点 `Evaluate Strings` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageInsetCrop` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy makeImageForICLora` 仅有 LoRA 的通用知识，没有该节点自己的说明
