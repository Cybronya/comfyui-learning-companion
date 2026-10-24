---
key: 图片生成/图生图/我和疯狂动物城合照-I took a photo with Zootopia_1995758961028632578.json
name: 我和疯狂动物城合照-I took a photo with Zootopia_1995758961028632578
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/我和疯狂动物城合照-I took a photo with Zootopia_1995758961028632578.json
hash: b17cb5c506ae6782
coverage: 0.933333
learned_at: 2026-10-23 12:52:35
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, easy imageConcat, TextEncodeQwenImageEditPlus, easy cleanGpuUsed, LoadImage, SeedVR2, SaveImage, Image Comparer (rgthree), SaveImage, SaveImage, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, Reroute, VAEDecode, KSampler, PIP_图像联结, LoadImage, Text, LoadImage, EmptyLatentImage, LoraLoaderModelOnly, CFGNorm, LoraLoaderModelOnly, ReActorFaceSwap]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1600, "sampler_name": "euler", "scheduler": "simple", "seed": 581140097840344, "steps": 6, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/我和疯狂动物城合照-I took a photo with Zootopia_1995758961028632578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/我和疯狂动物城合照-I took a photo with Zootopia_1995758961028632578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `easy imageConcat`
- `TextEncodeQwenImageEditPlus`
- `easy cleanGpuUsed`
- `LoadImage`
- `SeedVR2`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `PIP_图像联结`
- `LoadImage`
- `Text`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `ReActorFaceSwap`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `581140097840344`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1600`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（28/30）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`easy imageConcat`、`TextEncodeQwenImageEditPlus`、`easy cleanGpuUsed`、`LoadImage`、`SeedVR2`、`SaveImage`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`VAEDecode`、`KSampler`、`PIP_图像联结`、`Text`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CFGNorm`、`ReActorFaceSwap`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
