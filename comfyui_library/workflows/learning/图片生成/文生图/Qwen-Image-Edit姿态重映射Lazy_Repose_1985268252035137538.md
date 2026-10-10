---
key: Qwen-Image-Edit姿态重映射Lazy_Repose_1985268252035137538.json
name: Qwen-Image-Edit姿态重映射Lazy_Repose_1985268252035137538
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit姿态重映射Lazy_Repose_1985268252035137538.json
hash: 644f4127bb420aa4
coverage: 0.730769
learned_at: 2026-10-10 20:59:01
nodes: [CFGNorm, EmptySD3LatentImage, MarkdownNote, MarkdownNote, ModelSamplingAuraFlow, KSampler, VAEDecode, TextEncodeQwenImageEditPlus, PreviewImage, AIO_Preprocessor, GetImageSize, ImageConcanate, ImageResizeKJv2, ImageConcanate, SaveImage, SaveImage, MarkdownNote, MarkdownNote, MarkdownNote, ImageScaleToTotalPixels, MarkdownNote, CheckpointLoaderSimple, LoadImage, TextEncodeQwenImageEditPlus, LoadImage, VAEEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v7.1.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 943812448198413, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen-Image-Edit姿态重映射Lazy_Repose_1985268252035137538.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit姿态重映射Lazy_Repose_1985268252035137538.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CFGNorm`
- `EmptySD3LatentImage`
- `MarkdownNote`
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `AIO_Preprocessor`
- `GetImageSize`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `VAEEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `943812448198413`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v7.1.safetensors`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`CFGNorm`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`KSampler`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`AIO_Preprocessor`、`GetImageSize`、`ImageConcanate`、`ImageResizeKJv2`、`SaveImage`、`ImageScaleToTotalPixels`、`CheckpointLoaderSimple`、`LoadImage`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、CFGNorm、TextEncodeQwenImageEditPlus、VAEEncode、EmptySD3LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
