---
key: 图片生成/图生图/豹豹喵呜制作：qwen2.1稳定动作迁移工作流（PE版）_2110617835973201922.json
name: 豹豹喵呜制作：qwen2.1稳定动作迁移工作流（PE版）_2110617835973201922
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/豹豹喵呜制作：qwen2.1稳定动作迁移工作流（PE版）_2110617835973201922.json
hash: 5614e0dd715bcaa6
coverage: 0.823529
learned_at: 2026-10-23 13:28:16
nodes: [CLIPLoader, VAELoader, PathchSageAttentionKJ, QwenImage21Cache, SDPoseKeypointExtractor, SDPoseDrawKeypoints, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, LayerUtility: NumberCalculator, easy showAnything, Text Multiline, TextGenerateLTX2Prompt, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, ComfyMathExpression, PrimitiveFloat, JoinStrings, easy positive, PrimitiveString, SaveImage, UNETLoader, CheckpointLoaderSimple, CLIPLoader, LoadImage, Image Comparer (rgthree), PreviewImage, BatchImagesNode, TextEncodeQwenImageEditPlus, VAEEncode, ConditioningZeroOut, VAEDecode, LoadImage, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sdpose_wholebody_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "linear_quadratic", "seed": 753121711067180, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/豹豹喵呜制作：qwen2.1稳定动作迁移工作流（PE版）_2110617835973201922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/豹豹喵呜制作：qwen2.1稳定动作迁移工作流（PE版）_2110617835973201922.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `SDPoseKeypointExtractor`
- `SDPoseDrawKeypoints`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `LayerUtility: NumberCalculator`
- `easy showAnything`
- `Text Multiline`
- `TextGenerateLTX2Prompt`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `JoinStrings`
- `easy positive`
- `PrimitiveString`
- `SaveImage`
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `BatchImagesNode`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`
- `seed` = `753121711067180`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`SDPoseKeypointExtractor`、`SDPoseDrawKeypoints`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LayerUtility: NumberCalculator`、`Text Multiline`、`TextGenerateLTX2Prompt`、`ComfyMathExpression`、`JoinStrings`、`easy positive`、`SaveImage`、`UNETLoader`、`CheckpointLoaderSimple`、`BatchImagesNode`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
