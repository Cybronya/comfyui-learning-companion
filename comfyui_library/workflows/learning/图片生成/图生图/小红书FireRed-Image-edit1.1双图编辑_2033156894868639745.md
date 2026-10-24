---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json
name: 小红书FireRed-Image-edit1.1双图编辑_2033156894868639745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json
hash: 77e7a3b0b95215ec
coverage: 0.95
learned_at: 2026-10-23 12:49:17
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, VAEDecode, easy cleanGpuUsed, UNETLoader, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, KSampler, VAELoader, CR Prompt Text, Image Comparer (rgthree), SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 285010555931613, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `285010555931613`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`CLIPLoader`、`KSampler`、`VAELoader`、`CR Prompt Text`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
