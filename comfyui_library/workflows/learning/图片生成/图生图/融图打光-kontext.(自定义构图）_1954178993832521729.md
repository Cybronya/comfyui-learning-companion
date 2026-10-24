---
key: 图片生成/图生图/融图打光-kontext.(自定义构图）_1954178993832521729.json
name: 融图打光-kontext.(自定义构图）_1954178993832521729
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/融图打光-kontext.(自定义构图）_1954178993832521729.json
hash: e9fd74e3872647c3
coverage: 0.745455
learned_at: 2026-10-23 13:25:14
nodes: [ConditioningZeroOut, FluxGuidance, Seed (rgthree), easy imageSize, VAEEncode, easy cleanGpuUsed, TeaCache, UNETLoader, CLIPTextEncode, KSampler, PreviewImage, Image Comparer (rgthree), VAEEncode, ConditioningZeroOut, LoraLoaderModelOnly, TeaCache, UNETLoader, SaveImage, ReferenceLatent, FluxGuidance, LayerMask: MaskGrow, PreviewImage, Reroute, VAELoader, CLIPTextEncode, DualCLIPLoader, LayerMask: SegmentAnythingUltra V2, PreviewImage, LayerMask: MaskPreview, DetailTransfer, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, easy imageSizeBySide, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PreviewImage, Image Comparer (rgthree), VAEDecode, LayerMask: MaskGrow, easy imageColorMatch, ImageScale, DetailTransfer, Image Comparer (rgthree), LoadImage, ConditioningZeroOut, FluxGuidance, Reroute, Anything Everywhere, Seed (rgthree), VAEEncode, Image Comparer (rgthree), PreviewImage, PreviewImage, easy imageSizeBySide, easy cleanGpuUsed, TeaCache, UNETLoader, CLIPTextEncode, KSampler, VAEDecode, Image Comparer (rgthree), PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), DualCLIPLoader, VAELoader, VAEEncode, ConditioningZeroOut, CLIPTextEncode, LoraLoaderModelOnly, TeaCache, UNETLoader, PreviewImage, PreviewImage, PreviewImage, LayerMask: MaskGrow, ImageScale, Image Comparer (rgthree), Anything Everywhere, SaveImage, KSampler, VAEDecode, ReferenceLatent, FluxGuidance, PreviewImage, LoadImage, LayerMask: MaskGrow, PreviewImage, DetailTransfer, LoadImage, LayerUtility: CropByMask V2, easy imageSize, FastCanvasTool, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskPreview, easy imageColorMatch, DetailTransfer, PreviewImage, BiRefNetRMBG, Note, RMBG, RMBG, LayerUtility: CropByMask V2, RMBG, PreviewImage, RMBG, LoadImage, FastCanvas, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 338894734139254, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/融图打光-kontext.(自定义构图）_1954178993832521729.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/融图打光-kontext.(自定义构图）_1954178993832521729.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（110 个）：
- `ConditioningZeroOut`
- `FluxGuidance`
- `Seed (rgthree)`
- `easy imageSize`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `TeaCache`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `UNETLoader` ★核心
- `SaveImage`
- `ReferenceLatent`
- `FluxGuidance`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `Reroute`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `LayerMask: SegmentAnythingUltra V2`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `DetailTransfer`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSizeBySide`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LayerMask: MaskGrow`
- `easy imageColorMatch`
- `ImageScale`
- `DetailTransfer`
- `Image Comparer (rgthree)`
- `LoadImage`
- `ConditioningZeroOut`
- `FluxGuidance`
- `Reroute`
- `Anything Everywhere`
- `Seed (rgthree)`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `easy imageSizeBySide`
- `easy cleanGpuUsed`
- `TeaCache`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `DualCLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `UNETLoader` ★核心
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: MaskGrow`
- `ImageScale`
- `Image Comparer (rgthree)`
- `Anything Everywhere`
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `PreviewImage`
- `LoadImage`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `DetailTransfer`
- `LoadImage`
- `LayerUtility: CropByMask V2`
- `easy imageSize`
- `FastCanvasTool`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskPreview`
- `easy imageColorMatch`
- `DetailTransfer`
- `PreviewImage`
- `BiRefNetRMBG`
- `Note`
- `RMBG`
- `RMBG`
- `LayerUtility: CropByMask V2`
- `RMBG`
- `PreviewImage`
- `RMBG`
- `LoadImage`
- `FastCanvas`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `338894734139254`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（82/110）

**有卡**：`ConditioningZeroOut`、`FluxGuidance`、`Seed (rgthree)`、`easy imageSize`、`VAEEncode`、`easy cleanGpuUsed`、`TeaCache`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`SaveImage`、`ReferenceLatent`、`LayerMask: MaskGrow`、`VAELoader`、`DualCLIPLoader`、`LayerMask: SegmentAnythingUltra V2`、`LayerMask: MaskPreview`、`DetailTransfer`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSizeBySide`、`VAEDecode`、`easy imageColorMatch`、`ImageScale`、`LoadImage`、`LayerUtility: CropByMask V2`、`FastCanvasTool`、`BiRefNetRMBG`、`RMBG`、`FastCanvas`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
