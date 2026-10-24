---
key: 图片生成/图生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  + 控制网 文生图换脸重绘工作流_2052396960895782913.json
name: RES4LYF + Z-Image Turbo Inpaint & Face Swap  + 控制网 文生图换脸重绘工作流_2052396960895782913
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  + 控制网 文生图换脸重绘工作流_2052396960895782913.json
hash: 9696d63936758129
coverage: 0.6875
learned_at: 2026-10-23 11:22:57
nodes: [easy cleanGpuUsed, easy clearCacheAll, SAM3_Detect, CLIPTextEncode, FaceEmbedDistance, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, PreviewImage, ConditioningZeroOut, ImageStitch, PreviewImage, TextGenerate, PreviewAny, SetLatentNoiseMask, GrowMaskWithBlur, Image Comparer (rgthree), PreviewImage, PreviewImage, PrimitiveInt, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ZImageFunControlnet, ModelSamplingAuraFlow, LoraLoaderModelOnly, Note, EmptySD3LatentImage, ModelPatchLoader, CheckpointLoaderSimple, CLIPTextEncode, CLIPLoader, LoadImage, VAEDecode, CLIPLoader, SaveImage, LoadImage, Note, VAEEncode, MaskPreview, ClownsharKSampler_Beta, KSampler, VAEDecode, VAELoader, SaveImage, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1-multiplex-fp16.safetensors", "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 0, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  + 控制网 文生图换脸重绘工作流_2052396960895782913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/RES4LYF + Z-Image Turbo Inpaint & Face Swap  + 控制网 文生图换脸重绘工作流_2052396960895782913.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SAM3_Detect`
- `CLIPTextEncode` ★核心
- `FaceEmbedDistance`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `ImageStitch`
- `PreviewImage`
- `TextGenerate`
- `PreviewAny`
- `SetLatentNoiseMask`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `PrimitiveInt`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ZImageFunControlnet`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `EmptySD3LatentImage`
- `ModelPatchLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoadImage`
- `VAEDecode` ★核心
- `CLIPLoader`
- `SaveImage`
- `LoadImage`
- `Note`
- `VAEEncode` ★核心
- `MaskPreview`
- `ClownsharKSampler_Beta` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `SaveImage`
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`
- `seed` = `0`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（33/48）

**有卡**：`easy cleanGpuUsed`、`easy clearCacheAll`、`SAM3_Detect`、`CLIPTextEncode`、`FaceEmbedDistance`、`FaceAnalysisModels`、`ConditioningZeroOut`、`ImageStitch`、`TextGenerate`、`SetLatentNoiseMask`、`GrowMaskWithBlur`、`ZImageFunControlnet`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`ModelPatchLoader`、`CheckpointLoaderSimple`、`CLIPLoader`、`LoadImage`、`VAEDecode`、`SaveImage`、`VAEEncode`、`MaskPreview`、`ClownsharKSampler_Beta`、`KSampler`、`VAELoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
