---
key: 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2004148282525949953.json
name: Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2004148282525949953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2004148282525949953.json
hash: b42707461c958d98
coverage: 0.809524
learned_at: 2026-10-23 11:16:15
nodes: [TextEncodeQwenImageEditPlusCustom_lrzjason, InpaintCrop, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, ImageAndMaskPreview, KSampler, Image Comparer (rgthree), QwenEditOutputExtractor, LoadImage, PrimitiveStringMultiline, MarkdownNote, Fast Groups Bypasser (rgthree), QwenEditConfigPreparer, VAEDecode, WujiCleaner, CropWithPadInfo, InpaintStitch, WujiUpscaler, SaveImage, CheckpointLoaderSimple]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "WuJi_Qwen2511-AIO-SFW聚合版_2603.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 756367675947770, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2004148282525949953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Eidt-2511+SeedVR2.5零偏移遮罩精细化改图局部重绘图像编辑_2004148282525949953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `InpaintCrop`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageAndMaskPreview`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `QwenEditOutputExtractor`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `QwenEditConfigPreparer`
- `VAEDecode` ★核心
- `WujiCleaner`
- `CropWithPadInfo`
- `InpaintStitch`
- `WujiUpscaler`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `756367675947770`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `WuJi_Qwen2511-AIO-SFW聚合版_2603.safetensors`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`TextEncodeQwenImageEditPlusCustom_lrzjason`、`InpaintCrop`、`ConditioningZeroOut`、`FluxKontextMultiReferenceLatentMethod`、`ImageAndMaskPreview`、`KSampler`、`QwenEditOutputExtractor`、`LoadImage`、`QwenEditConfigPreparer`、`VAEDecode`、`WujiCleaner`、`CropWithPadInfo`、`InpaintStitch`、`WujiUpscaler`、`SaveImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、SaveImage、LoadImage、FluxKontextMultiReferenceLatentMethod、TextEncodeQwenImageEditPlusCustom_lrzjason

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
