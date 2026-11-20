---
key: 平台全量/AA--图片编辑-Qwen-image-Edit-2511-controlnet-姿势合成_2006728292652556289.json
name: AA--图片编辑-Qwen-image-Edit-2511-controlnet-姿势合成_2006728292652556289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AA--图片编辑-Qwen-image-Edit-2511-controlnet-姿势合成_2006728292652556289.json
hash: 73b08b14599a1c2d
coverage: 0.787879
learned_at: 2026-11-14 00:14:38
nodes: [CLIPLoader, ControlNetLoader, VAELoader, UNETLoader, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, Note, INTConstant, Note, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, VAEDecode, Note, Note, Note, PreviewImage, easy cleanGpuUsed, GetImageSizeAndCount, EmptyLatentImage, SaveImage, SeedVR2VideoUpscaler, SetUnionControlNetType, LoadImage, LoadImage, Text Multiline, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, DWPreprocessor, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, ControlNetApplySD3, KSampler, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "beta57", "seed": 561439948531573, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/AA--图片编辑-Qwen-image-Edit-2511-controlnet-姿势合成_2006728292652556289.json

> 来源文件 `comfyui_library/workflows/平台全量/AA--图片编辑-Qwen-image-Edit-2511-controlnet-姿势合成_2006728292652556289.json`

## 结构

**生成流程**：Model → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPLoader`
- `ControlNetLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `Note`
- `INTConstant`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `Note`
- `Note`
- `Note`
- `PreviewImage`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SetUnionControlNetType`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DWPreprocessor`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `controlnet_strength` = `1.0000000000000002`
- `seed` = `561439948531573`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`CLIPLoader`、`ControlNetLoader`、`VAELoader`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`INTConstant`、`LoraLoaderModelOnly`、`VAEDecode`、`easy cleanGpuUsed`、`GetImageSizeAndCount`、`EmptyLatentImage`、`SaveImage`、`SeedVR2VideoUpscaler`、`SetUnionControlNetType`、`LoadImage`、`Text Multiline`、`LayerUtility: ImageScaleByAspectRatio V2`、`DWPreprocessor`、`TextEncodeQwenImageEditPlus`、`ControlNetApplySD3`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
