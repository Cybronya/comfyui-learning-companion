---
key: 图片生成/图生图/千问穿搭秀·OOTD2.0(脸型匹配+姿势匹配)_1969672912473104386.json
name: 千问穿搭秀·OOTD2.0(脸型匹配+姿势匹配)_1969672912473104386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问穿搭秀·OOTD2.0(脸型匹配+姿势匹配)_1969672912473104386.json
hash: 57c4c97f75338222
coverage: 0.919355
learned_at: 2026-10-23 12:31:42
nodes: [Image Blank, LayerMask: SegmentAnythingUltra V2, ModelSamplingAuraFlow, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, ImpactInt, JjkText, ImpactSwitch, ImpactSwitch, VAEDecode, Int, ImpactInt, LoadImage, SaveImage, LoadImage, CR Text Concatenate, LayerUtility: ImageBlendAdvance V3, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, LoadImage, ImageConcanate, CFGNorm, CLIPLoader, VAELoader, KSampler, EmptyLatentImage, LayerUtility: PurgeVRAM V2, ControlNetApplyAdvanced, LayerUtility: PurgeVRAM V2, GetImageSize, SaveImage, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, DWPreprocessor, ControlNetApplyAdvanced, AIO_Preprocessor, LoadImage, ImageConcanate, PreviewImage, easy imageConcat, ImageConcanate, PreviewImage, LoraLoaderModelOnly, UNETLoader, TextInput_, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1.3000000000000003, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 491383854177280, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/千问穿搭秀·OOTD2.0(脸型匹配+姿势匹配)_1969672912473104386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问穿搭秀·OOTD2.0(脸型匹配+姿势匹配)_1969672912473104386.json`

## 结构

**生成流程**：Model → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `Image Blank`
- `LayerMask: SegmentAnythingUltra V2`
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `ImpactSwitch`
- `ImpactSwitch`
- `VAEDecode` ★核心
- `Int`
- `ImpactInt`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `CR Text Concatenate`
- `LayerUtility: ImageBlendAdvance V3`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `LoadImage`
- `ImageConcanate`
- `CFGNorm`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ControlNetApplyAdvanced` ★核心
- `LayerUtility: PurgeVRAM V2`
- `GetImageSize`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `DWPreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `AIO_Preprocessor`
- `LoadImage`
- `ImageConcanate`
- `PreviewImage`
- `easy imageConcat`
- `ImageConcanate`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `TextInput_`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `491383854177280`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `controlnet_strength` = `1.3000000000000003`

## 知识

覆盖率 **92%**（57/62）

**有卡**：`Image Blank`、`LayerMask: SegmentAnythingUltra V2`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`VAEDecode`、`Int`、`LoadImage`、`SaveImage`、`CR Text Concatenate`、`LayerUtility: ImageBlendAdvance V3`、`TextEncodeQwenImageEdit`、`ImageConcanate`、`CFGNorm`、`CLIPLoader`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`LayerUtility: PurgeVRAM V2`、`ControlNetApplyAdvanced`、`GetImageSize`、`DWPreprocessor`、`AIO_Preprocessor`、`easy imageConcat`、`LoraLoaderModelOnly`、`UNETLoader`、`TextInput_`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
