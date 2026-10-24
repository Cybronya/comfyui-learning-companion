---
key: 图片生成/图生图/千问OOTD百搭秀·奇迹暖暖1.0_1967826759494283265.json
name: 千问OOTD百搭秀·奇迹暖暖1.0_1967826759494283265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问OOTD百搭秀·奇迹暖暖1.0_1967826759494283265.json
hash: e513d6f90e2d6079
coverage: 0.9
learned_at: 2026-10-23 12:29:51
nodes: [Image Blank, LayerMask: SegmentAnythingUltra V2, GetImageSize, LayerUtility: ImageBlendAdvance V3, ModelSamplingAuraFlow, ImageScaleToTotalPixels, CLIPLoader, VAELoader, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, CFGNorm, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ImageConcanate, PreviewImage, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, JjkText, KSampler, ImpactSwitch, ImpactSwitch, UNETLoader, LoraLoaderModelOnly, VAEDecode, Int, ImpactInt, EmptyLatentImage, PreviewImage, LoadImage, SaveImage, SaveImage, ImageConcanate, LoadImage, CR Text Concatenate, TextInput_, ImageConcanate, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1064474567287393, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/千问OOTD百搭秀·奇迹暖暖1.0_1967826759494283265.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问OOTD百搭秀·奇迹暖暖1.0_1967826759494283265.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `Image Blank`
- `LayerMask: SegmentAnythingUltra V2`
- `GetImageSize`
- `LayerUtility: ImageBlendAdvance V3`
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `CFGNorm`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ImageConcanate`
- `PreviewImage`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `JjkText`
- `KSampler` ★核心
- `ImpactSwitch`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `Int`
- `ImpactInt`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `CR Text Concatenate`
- `TextInput_`
- `ImageConcanate`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `1064474567287393`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（45/50）

**有卡**：`Image Blank`、`LayerMask: SegmentAnythingUltra V2`、`GetImageSize`、`LayerUtility: ImageBlendAdvance V3`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEdit`、`CFGNorm`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ImageConcanate`、`ImpactInt`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`Int`、`EmptyLatentImage`、`SaveImage`、`CR Text Concatenate`、`TextInput_`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
