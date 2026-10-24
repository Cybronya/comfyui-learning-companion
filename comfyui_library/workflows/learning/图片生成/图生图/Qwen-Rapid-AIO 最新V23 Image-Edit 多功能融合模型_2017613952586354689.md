---
key: 图片生成/图生图/Qwen-Rapid-AIO 最新V23 Image-Edit 多功能融合模型_2017613952586354689.json
name: Qwen-Rapid-AIO 最新V23 Image-Edit 多功能融合模型_2017613952586354689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Rapid-AIO 最新V23 Image-Edit 多功能融合模型_2017613952586354689.json
hash: 06c1588c73f4193c
coverage: 0.846154
learned_at: 2026-10-23 11:17:31
nodes: [Note, GetImageSize, ImageScaleToTotalPixels, GetImageSize, LoadImage, ImpactMinMax, ImpactMinMax, QwenEditConfigPreparer, ImpactMinMax, RH_LLMAPI_NODE, CFGNorm, TextEncodeQwenImageEditPlusCustom_lrzjason, QwenEditOutputExtractor, ConditioningZeroOut, KSampler, EmptyLatentImage, FluxResolutionNode, ImpactInt, VAEDecode, ImpactSwitch, EmptyLatentImage, ImageConcanate, SaveImage, Note, easy showAnything, SaveImage, PreviewImage, ImageScaleToTotalPixels, GetImageSize, QwenEditConfigPreparer, QwenEditConfigPreparer, AIO_Preprocessor, Fast Groups Bypasser (rgthree), ImageConcatMulti, ImageScaleToTotalPixels, CheckpointLoaderSimple, LoadImage, LoadImage, Text Multiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Rapid-AIO-NSFW-v23.0.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1092258416389363, "steps": 4, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Rapid-AIO 最新V23 Image-Edit 多功能融合模型_2017613952586354689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Rapid-AIO 最新V23 Image-Edit 多功能融合模型_2017613952586354689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `Note`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `LoadImage`
- `ImpactMinMax`
- `ImpactMinMax`
- `QwenEditConfigPreparer`
- `ImpactMinMax`
- `RH_LLMAPI_NODE`
- `CFGNorm`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `QwenEditOutputExtractor`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `FluxResolutionNode`
- `ImpactInt`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `EmptyLatentImage` ★核心
- `ImageConcanate`
- `SaveImage`
- `Note`
- `easy showAnything`
- `SaveImage`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `QwenEditConfigPreparer`
- `QwenEditConfigPreparer`
- `AIO_Preprocessor`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `LoadImage`
- `Text Multiline`

## 关键参数

- `seed` = `1092258416389363`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v23.0.safetensors`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`GetImageSize`、`ImageScaleToTotalPixels`、`LoadImage`、`ImpactMinMax`、`QwenEditConfigPreparer`、`RH_LLMAPI_NODE`、`CFGNorm`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`QwenEditOutputExtractor`、`ConditioningZeroOut`、`KSampler`、`EmptyLatentImage`、`FluxResolutionNode`、`ImpactInt`、`VAEDecode`、`ImageConcanate`、`SaveImage`、`AIO_Preprocessor`、`ImageConcatMulti`、`CheckpointLoaderSimple`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、EmptyLatentImage、SaveImage、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
