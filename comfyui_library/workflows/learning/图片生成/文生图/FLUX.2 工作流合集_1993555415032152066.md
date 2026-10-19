---
key: 图片生成/文生图/FLUX.2 工作流合集_1993555415032152066.json
name: FLUX.2 工作流合集_1993555415032152066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 工作流合集_1993555415032152066.json
hash: 5812b1f8432b99e0
coverage: 0.829787
learned_at: 2026-10-19 21:32:28
nodes: [CLIPLoader, VAELoader, UNETLoader, Anything Everywhere3, RandomNoise, BasicGuider, KSamplerSelect, LoadImage, VAEEncode, SamplerCustomAdvanced, SaveImage, Int, Any Switch (rgthree), OnnxDetectionModelLoader, LoadImage, PoseAndFaceDetection, LayerUtility: ImageMaskScaleAsV2, DrawViTPose, ReferenceLatent, ReferenceLatent, VAEEncode, PreviewImage, Any Switch (rgthree), Flux2Scheduler, EmptyFlux2LatentImage, LoadImage, CLIPTextEncode, FluxGuidance, MarkdownNote, VAEEncode, VAEEncode, ReferenceLatent, VAEDecode, ImageScaleToTotalPixels, MarkdownNote, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, RBGImageStitchPlus, ImageScaleToTotalPixels, SaveImage, RBGImageStitchPlus, LoadImage, Fast Groups Bypasser (rgthree), easy imageSize, Int, CR Text, Note]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 工作流合集_1993555415032152066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 工作流合集_1993555415032152066.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Anything Everywhere3`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `Int`
- `Any Switch (rgthree)`
- `OnnxDetectionModelLoader`
- `LoadImage`
- `PoseAndFaceDetection`
- `LayerUtility: ImageMaskScaleAsV2`
- `DrawViTPose`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `PreviewImage`
- `Any Switch (rgthree)`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `MarkdownNote`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RBGImageStitchPlus`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `RBGImageStitchPlus`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `Int`
- `CR Text`
- `Note`

## 知识

覆盖率 **83%**（39/47）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`LoadImage`、`VAEEncode`、`SamplerCustomAdvanced`、`SaveImage`、`Int`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`LayerUtility: ImageMaskScaleAsV2`、`DrawViTPose`、`ReferenceLatent`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`FluxGuidance`、`VAEDecode`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`RBGImageStitchPlus`、`easy imageSize`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
