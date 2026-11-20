---
key: 平台全量/FireRed-Image-Edit-1.0_8步加速工作流_2028330972269256706.json
name: FireRed-Image-Edit-1.0_8步加速工作流_2028330972269256706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FireRed-Image-Edit-1.0_8步加速工作流_2028330972269256706.json
hash: fd9beeae18ff73df
coverage: 0.5
learned_at: 2026-11-14 00:26:43
nodes: [CFGNorm, LayerUtility: PurgeVRAM V2, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, ModelSamplingAuraFlow, GetNode, SetNode, GetNode, SetNode, PrimitiveInt, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageStitch, GetNode, GetNode, SetNode, SaveImage, TextEncodeQwenImageEditPlus, ConditioningZeroOut, SaveImage, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, UNETLoader, GetImageSize, CLIPLoader, ImageStitch, SetNode, LoadImage, MarkdownNote, Fast Groups Bypasser (rgthree), LoadImage, VAELoader, Text Multiline, LoadImage, VAEDecode, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 476602248560184, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FireRed-Image-Edit-1.0_8步加速工作流_2028330972269256706.json

> 来源文件 `comfyui_library/workflows/平台全量/FireRed-Image-Edit-1.0_8步加速工作流_2028330972269256706.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `CFGNorm`
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `ModelSamplingAuraFlow`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageStitch`
- `GetNode`
- `GetNode`
- `SetNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `SaveImage`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `GetImageSize`
- `CLIPLoader`
- `ImageStitch`
- `SetNode`
- `LoadImage`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAELoader`
- `Text Multiline`
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`

## 关键参数

- `seed` = `476602248560184`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **50%**（23/46）

**有卡**：`CFGNorm`、`LayerUtility: PurgeVRAM V2`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`ImageStitch`、`SaveImage`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSampler`、`UNETLoader`、`GetImageSize`、`CLIPLoader`、`LoadImage`、`VAELoader`、`Text Multiline`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
