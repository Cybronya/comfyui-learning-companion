---
key: 图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json
name: Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json
hash: 1159901512ae113a
coverage: 0.75
learned_at: 2026-10-10 20:58:52
nodes: [ResolutionSelector, LoadImage, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, GetNode, TextEncodeQwenImage21, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), ResizeImageMaskNode, VAEEncodeTiled, VAELoader, SeedVR2Preprocess, SeedVR2Conditioning, KSampler, VAEDecodeTiled, SeedVR2PostProcessing, PreviewImage, UNETLoader, CLIPLoader, VAELoader, UNETLoader, Fast Groups Bypasser (rgthree), LoadImage, VAEDecode, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图片编辑工作流，文生图图生图处理方案_2103967167434813441.json`

## 结构

**节点**（64 个）：
- `ResolutionSelector`
- `LoadImage`
- `EmptyLatentImage`
- `KSampler`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `ResizeImageMaskNode`
- `VAEEncodeTiled`
- `VAELoader`
- `SeedVR2Preprocess`
- `SeedVR2Conditioning`
- `KSampler`
- `VAEDecodeTiled`
- `SeedVR2PostProcessing`
- `PreviewImage`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAEDecode`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **75%**（48/64）

**有卡**：`ResolutionSelector`、`LoadImage`、`EmptyLatentImage`、`KSampler`、`ComfySwitchNode`、`QwenImage21Cache`、`SetNode`、`GetNode`、`TextEncodeQwenImage21`、`Fast Groups Bypasser (rgthree)`、`ResizeImageMaskNode`、`VAEEncodeTiled`、`VAELoader`、`SeedVR2Preprocess`、`SeedVR2Conditioning`、`VAEDecodeTiled`、`SeedVR2PostProcessing`、`PreviewImage`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`孤海注释`、`LoraLoaderModelOnly`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
