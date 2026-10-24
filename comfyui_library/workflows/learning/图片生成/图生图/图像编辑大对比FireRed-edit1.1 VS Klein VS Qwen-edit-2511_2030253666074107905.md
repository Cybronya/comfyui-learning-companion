---
key: 图片生成/图生图/图像编辑大对比FireRed-edit1.1 VS Klein VS Qwen-edit-2511_2030253666074107905.json
name: 图像编辑大对比FireRed-edit1.1 VS Klein VS Qwen-edit-2511_2030253666074107905
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像编辑大对比FireRed-edit1.1 VS Klein VS Qwen-edit-2511_2030253666074107905.json
hash: c672afc7afb1beec
coverage: 0.909091
learned_at: 2026-10-23 12:39:06
nodes: [ConditioningZeroOut, UNETLoader, CLIPLoader, KSampler, VAELoader, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, PainterFluxImageEdit, UNETLoader, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, ConditioningZeroOut, CLIPLoader, CFGNorm, VAELoader, TextEncodeQwenImageEditPlus, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, KSampler, VAEDecode, easy cleanGpuUsed, AddLabel, VAEDecode, easy cleanGpuUsed, AddLabel, AddLabel, easy cleanGpuUsed, PreviewImage, VAEDecode, PreviewImage, AddLabel, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Text, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, LoadImage, ImageConcatMulti, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 863340159222065, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图像编辑大对比FireRed-edit1.1 VS Klein VS Qwen-edit-2511_2030253666074107905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像编辑大对比FireRed-edit1.1 VS Klein VS Qwen-edit-2511_2030253666074107905.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PainterFluxImageEdit`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `CLIPLoader`
- `CFGNorm`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `AddLabel`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `AddLabel`
- `AddLabel`
- `easy cleanGpuUsed`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `AddLabel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `ImageConcatMulti`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `863340159222065`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（40/44）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`CLIPLoader`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`PainterFluxImageEdit`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`VAEDecode`、`easy cleanGpuUsed`、`AddLabel`、`Text`、`LoadImage`、`ImageConcatMulti`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
