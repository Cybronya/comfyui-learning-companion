---
key: 图片生成/图生图/QwenRapid-AIO-融图-去塑料感-v2.0_2046133973675417602.json
name: QwenRapid-AIO-融图-去塑料感-v2.0_2046133973675417602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenRapid-AIO-融图-去塑料感-v2.0_2046133973675417602.json
hash: 482b7a46770685f7
coverage: 1
learned_at: 2026-10-23 11:20:52
nodes: [GetImageSize, ImageScaleToTotalPixels, GetImageSize, ImpactMinMax, ImpactMinMax, QwenEditConfigPreparer, ImpactMinMax, ImageScaleToTotalPixels, QwenEditConfigPreparer, ImageScaleToTotalPixels, GetImageSize, ConditioningZeroOut, QwenEditConfigPreparer, VAEDecode, KSampler, CFGNorm, SaveImage, CheckpointLoaderSimple, TextEncodeQwenImageEditPlusCustom_lrzjason, EmptyLatentImage, LoadImage, LoadImage, LoadImage, Text Multiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors", "denoise": 1, "height": 1792, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 1015687752179283, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenRapid-AIO-融图-去塑料感-v2.0_2046133973675417602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenRapid-AIO-融图-去塑料感-v2.0_2046133973675417602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `ImpactMinMax`
- `ImpactMinMax`
- `QwenEditConfigPreparer`
- `ImpactMinMax`
- `ImageScaleToTotalPixels`
- `QwenEditConfigPreparer`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `ConditioningZeroOut`
- `QwenEditConfigPreparer`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CFGNorm`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text Multiline`

## 关键参数

- `seed` = `1015687752179283`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `QwenRapidAIO 23-22-21_QwenRapidAIO 23.safetensors`
- `width` = `1024`
- `height` = `1792`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`GetImageSize`、`ImageScaleToTotalPixels`、`ImpactMinMax`、`QwenEditConfigPreparer`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`CFGNorm`、`SaveImage`、`CheckpointLoaderSimple`、`TextEncodeQwenImageEditPlusCustom_lrzjason`、`EmptyLatentImage`、`LoadImage`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、ConditioningZeroOut、EmptyLatentImage、LoadImage、CFGNorm、TextEncodeQwenImageEditPlusCustom_lrzjason

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
