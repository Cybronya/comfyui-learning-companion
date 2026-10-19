---
key: 图片生成/文生图/Z-Image-ControlNet二阶Refiner+Pose_Depth_Line_1996508277796126722.json
name: Z-Image-ControlNet二阶Refiner+Pose_Depth_Line_1996508277796126722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-ControlNet二阶Refiner+Pose_Depth_Line_1996508277796126722.json
hash: 5a227a27b03e3dcf
coverage: 0.818792
learned_at: 2026-10-19 21:32:50
nodes: [CLIPLoader, EmptySD3LatentImage, Note, MarkdownNote, GetImageSize, ImageLoader, MultiplePathsInput, easy cleanGpuUsed, CLIPTextEncode, Seed (rgthree), PreviewImage, KSampler, VAEDecode, ImageScaleBy, VAEEncode, LatentUpscaleBy, VAELoader, PreviewImage, VAEDecode, VAEDecode, UNETLoader, KSampler, KSampler, QwenImageDiffsynthControlnet, ConditioningZeroOut, JWStringConcat, easy showAnything, String Literal, AIO_Preprocessor, ImageScaleToMaxDimension, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingAuraFlow, CLIPLoader, ModelPatchLoader, EmptySD3LatentImage, Note, SaveImage, MarkdownNote, GetImageSize, PreviewImage, easy cleanGpuUsed, CLIPTextEncode, Seed (rgthree), PreviewImage, KSampler, VAEDecode, ImageScaleBy, VAEEncode, LatentUpscaleBy, VAELoader, PreviewImage, VAEDecode, VAEDecode, UNETLoader, QwenImageDiffsynthControlnet, ConditioningZeroOut, JWStringConcat, ImageScaleToMaxDimension, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingAuraFlow, AIO_Preprocessor, CLIPLoader, ModelPatchLoader, EmptySD3LatentImage, Note, SaveImage, MarkdownNote, GetImageSize, PreviewImage, MultiplePathsInput, easy cleanGpuUsed, CLIPTextEncode, Seed (rgthree), PreviewImage, KSampler, VAEDecode, ImageScaleBy, VAEEncode, LatentUpscaleBy, VAELoader, PreviewImage, VAEDecode, VAEDecode, UNETLoader, KSampler, KSampler, QwenImageDiffsynthControlnet, ConditioningZeroOut, JWStringConcat, easy showAnything, String Literal, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingAuraFlow, CLIPLoader, ModelPatchLoader, EmptySD3LatentImage, Note, SaveImage, MarkdownNote, GetImageSize, PreviewImage, CLIPTextEncode, Seed (rgthree), PreviewImage, KSampler, VAEDecode, ImageScaleBy, VAEEncode, LatentUpscaleBy, VAELoader, PreviewImage, VAEDecode, VAEDecode, UNETLoader, KSampler, KSampler, ConditioningZeroOut, ImageScaleToMaxDimension, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingAuraFlow, ImageLoader, AIO_Preprocessor, String Literal, Image Comparer (rgthree), KSampler, KSampler, Image Comparer (rgthree), MultiplePathsInput, Qwen3_VQA, easy showAnything, Qwen3_VQA, String Literal, Qwen3_VQA, ModelPatchLoader, Image Comparer (rgthree), ImageLoader, Image Comparer (rgthree), QwenImageDiffsynthControlnet, DownloadAndLoadDepthAnythingV3Model, ImageLoader, ImageScaleToMaxDimension, DepthAnything_V3, AIO_Preprocessor, PreviewImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.7500000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 1096871997057434, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-ControlNet二阶Refiner+Pose_Depth_Line_1996508277796126722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-ControlNet二阶Refiner+Pose_Depth_Line_1996508277796126722.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（149 个）：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `Note`
- `MarkdownNote`
- `GetImageSize`
- `ImageLoader`
- `MultiplePathsInput`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `LatentUpscaleBy`
- `VAELoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `QwenImageDiffsynthControlnet`
- `ConditioningZeroOut`
- `JWStringConcat`
- `easy showAnything`
- `String Literal`
- `AIO_Preprocessor`
- `ImageScaleToMaxDimension`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `ModelPatchLoader`
- `EmptySD3LatentImage`
- `Note`
- `SaveImage`
- `MarkdownNote`
- `GetImageSize`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `LatentUpscaleBy`
- `VAELoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `QwenImageDiffsynthControlnet`
- `ConditioningZeroOut`
- `JWStringConcat`
- `ImageScaleToMaxDimension`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `AIO_Preprocessor`
- `CLIPLoader`
- `ModelPatchLoader`
- `EmptySD3LatentImage`
- `Note`
- `SaveImage`
- `MarkdownNote`
- `GetImageSize`
- `PreviewImage`
- `MultiplePathsInput`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `LatentUpscaleBy`
- `VAELoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `QwenImageDiffsynthControlnet`
- `ConditioningZeroOut`
- `JWStringConcat`
- `easy showAnything`
- `String Literal`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `ModelPatchLoader`
- `EmptySD3LatentImage`
- `Note`
- `SaveImage`
- `MarkdownNote`
- `GetImageSize`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `LatentUpscaleBy`
- `VAELoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `ImageScaleToMaxDimension`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ModelSamplingAuraFlow`
- `ImageLoader`
- `AIO_Preprocessor`
- `String Literal`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `MultiplePathsInput`
- `Qwen3_VQA`
- `easy showAnything`
- `Qwen3_VQA`
- `String Literal`
- `Qwen3_VQA`
- `ModelPatchLoader`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `Image Comparer (rgthree)`
- `QwenImageDiffsynthControlnet`
- `DownloadAndLoadDepthAnythingV3Model`
- `ImageLoader`
- `ImageScaleToMaxDimension`
- `DepthAnything_V3`
- `AIO_Preprocessor`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `1096871997057434`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7500000000000001`

## 知识

覆盖率 **82%**（122/149）

**有卡**：`CLIPLoader`、`EmptySD3LatentImage`、`GetImageSize`、`ImageLoader`、`MultiplePathsInput`、`easy cleanGpuUsed`、`CLIPTextEncode`、`Seed (rgthree)`、`KSampler`、`VAEDecode`、`ImageScaleBy`、`VAEEncode`、`LatentUpscaleBy`、`VAELoader`、`UNETLoader`、`QwenImageDiffsynthControlnet`、`ConditioningZeroOut`、`JWStringConcat`、`String Literal`、`AIO_Preprocessor`、`ImageScaleToMaxDimension`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`ModelPatchLoader`、`SaveImage`、`Qwen3_VQA`、`DownloadAndLoadDepthAnythingV3Model`、`DepthAnything_V3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 12 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
