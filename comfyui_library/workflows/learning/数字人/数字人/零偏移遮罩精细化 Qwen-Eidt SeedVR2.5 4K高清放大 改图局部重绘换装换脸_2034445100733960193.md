---
key: 数字人/数字人/零偏移遮罩精细化 Qwen-Eidt SeedVR2.5 4K高清放大 改图局部重绘换装换脸_2034445100733960193.json
name: 零偏移遮罩精细化 Qwen-Eidt SeedVR2.5 4K高清放大 改图局部重绘换装换脸_2034445100733960193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/零偏移遮罩精细化 Qwen-Eidt SeedVR2.5 4K高清放大 改图局部重绘换装换脸_2034445100733960193.json
hash: 5534049586b8bc57
coverage: 0.894737
learned_at: 2026-10-26 02:05:54
nodes: [TextEncodeQwenImageEditPlusCustom_lrzjason, ConditioningZeroOut, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, ImageAndMaskPreview, KSampler, QwenEditOutputExtractor, QwenEditConfigPreparer, VAEDecode, CropWithPadInfo, InpaintStitch, CheckpointLoaderSimple, PrimitiveStringMultiline, WujiCleaner, SaveImage, InpaintCrop, LoadImage, WujiUpscaler, Image Comparer (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "WuJi_Qwen2511-AIO-SFW聚合版_2603.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 756367675947770, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/零偏移遮罩精细化 Qwen-Eidt SeedVR2.5 4K高清放大 改图局部重绘换装换脸_2034445100733960193.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/零偏移遮罩精细化 Qwen-Eidt SeedVR2.5 4K高清放大 改图局部重绘换装换脸_2034445100733960193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `ConditioningZeroOut`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageAndMaskPreview`
- `KSampler` ★核心
- `QwenEditOutputExtractor`
- `QwenEditConfigPreparer`
- `VAEDecode` ★核心
- `CropWithPadInfo`
- `InpaintStitch`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveStringMultiline`
- `WujiCleaner`
- `SaveImage`
- `InpaintCrop`
- `LoadImage`
- `WujiUpscaler`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `756367675947770`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `WuJi_Qwen2511-AIO-SFW聚合版_2603.safetensors`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`TextEncodeQwenImageEditPlusCustom_lrzjason`、`ConditioningZeroOut`、`FluxKontextMultiReferenceLatentMethod`、`ImageAndMaskPreview`、`KSampler`、`QwenEditOutputExtractor`、`QwenEditConfigPreparer`、`VAEDecode`、`CropWithPadInfo`、`InpaintStitch`、`CheckpointLoaderSimple`、`WujiCleaner`、`SaveImage`、`InpaintCrop`、`LoadImage`、`WujiUpscaler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、SaveImage、LoadImage、FluxKontextMultiReferenceLatentMethod、TextEncodeQwenImageEditPlusCustom_lrzjason

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
