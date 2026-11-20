---
key: 平台全量/FireRedEdit1.1 vs QwenEdit2511_2029776462538084353.json
name: FireRedEdit1.1 vs QwenEdit2511_2029776462538084353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FireRedEdit1.1 vs QwenEdit2511_2029776462538084353.json
hash: ed0b365442a531dc
coverage: 0.581081
learned_at: 2026-11-14 00:26:45
nodes: [CFGNorm, LayerUtility: PurgeVRAM V2, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, ModelSamplingAuraFlow, GetNode, GetNode, SetNode, PrimitiveInt, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, TextEncodeQwenImageEditPlus, ConditioningZeroOut, SaveImage, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, GetImageSize, VAELoader, CLIPLoader, SetNode, LoadImage, UNETLoader, CFGNorm, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImageEditPlus, ConditioningZeroOut, SaveImage, KSampler, UNETLoader, SetNode, GetNode, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, Text Multiline, GetNode, VAEDecode, ImageStitch, GetNode, GetNode, VAEDecode, ImageStitch, ImageStitch, ImageStitch, ImageStitch, 孤海-图像添加水印, 孤海-图像添加水印, 孤海-图像添加水印, ImageStitch, ImageStitch, PreviewImage, SaveImage, SaveImage, ImageStitch, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 476602248560184, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FireRedEdit1.1 vs QwenEdit2511_2029776462538084353.json

> 来源文件 `comfyui_library/workflows/平台全量/FireRedEdit1.1 vs QwenEdit2511_2029776462538084353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `CFGNorm`
- `LayerUtility: PurgeVRAM V2`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ModelSamplingAuraFlow`
- `GetNode`
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
- `GetNode`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `SaveImage`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `GetImageSize`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `CFGNorm`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `GetNode`
- `VAEDecode` ★核心
- `ImageStitch`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `ImageStitch`
- `ImageStitch`
- `ImageStitch`
- `ImageStitch`
- `孤海-图像添加水印`
- `孤海-图像添加水印`
- `孤海-图像添加水印`
- `ImageStitch`
- `ImageStitch`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `MarkdownNote`

## 关键参数

- `seed` = `476602248560184`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（43/74）

**有卡**：`CFGNorm`、`LayerUtility: PurgeVRAM V2`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`SaveImage`、`EmptySD3LatentImage`、`KSampler`、`GetImageSize`、`VAELoader`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`Text Multiline`、`VAEDecode`、`ImageStitch`、`孤海-图像添加水印`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
