---
key: 图片生成/文生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  文生图换脸重绘工作流_2052380950432108546.json
name: RES4LYF + Z-Image Turbo Inpaint & Face Swap  文生图换脸重绘工作流_2052380950432108546
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  文生图换脸重绘工作流_2052380950432108546.json
hash: 567e8405c4a93aca
coverage: 0.6875
learned_at: 2026-10-19 22:45:40
nodes: [SAM3_Detect, CLIPTextEncode, FaceEmbedDistance, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, PreviewImage, ConditioningZeroOut, ImageStitch, VAEEncode, MaskPreview, GrowMaskWithBlur, ModelSamplingAuraFlow, ZImageFunControlnet, PreviewImage, KSampler, PreviewImage, LoadImage, PrimitiveInt, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, EmptySD3LatentImage, TextGenerate, CLIPLoader, PreviewImage, Image Comparer (rgthree), Note, VAEDecode, easy cleanGpuUsed, easy clearCacheAll, PreviewAny, SaveImage, SaveImage, ModelPatchLoader, Note, CheckpointLoaderSimple, SetLatentNoiseMask, ClownsharKSampler_Beta, VAEDecode, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 8, "checkpoint": "sam3.1-multiplex-fp16.safetensors", "denoise": 1, "sampler_name": -1, "scheduler": 1, "seed": 0.5, "steps": "bong_tangent"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  文生图换脸重绘工作流_2052380950432108546.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  文生图换脸重绘工作流_2052380950432108546.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `SAM3_Detect`
- `CLIPTextEncode` ★核心
- `FaceEmbedDistance`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `ImageStitch`
- `VAEEncode` ★核心
- `MaskPreview`
- `GrowMaskWithBlur`
- `ModelSamplingAuraFlow`
- `ZImageFunControlnet`
- `PreviewImage`
- `KSampler` ★核心
- `PreviewImage`
- `LoadImage`
- `PrimitiveInt`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `TextGenerate`
- `CLIPLoader`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Note`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `PreviewAny`
- `SaveImage`
- `SaveImage`
- `ModelPatchLoader`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `SetLatentNoiseMask`
- `ClownsharKSampler_Beta` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `0.5`
- `steps` = `bong_tangent`
- `cfg` = `8`
- `sampler_name` = `-1`
- `scheduler` = `1`
- `denoise` = `1`
- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **69%**（33/48）

**有卡**：`SAM3_Detect`、`CLIPTextEncode`、`FaceEmbedDistance`、`FaceAnalysisModels`、`ConditioningZeroOut`、`ImageStitch`、`VAEEncode`、`MaskPreview`、`GrowMaskWithBlur`、`ModelSamplingAuraFlow`、`ZImageFunControlnet`、`KSampler`、`LoadImage`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`TextGenerate`、`VAEDecode`、`easy cleanGpuUsed`、`easy clearCacheAll`、`SaveImage`、`ModelPatchLoader`、`CheckpointLoaderSimple`、`SetLatentNoiseMask`、`ClownsharKSampler_Beta`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
