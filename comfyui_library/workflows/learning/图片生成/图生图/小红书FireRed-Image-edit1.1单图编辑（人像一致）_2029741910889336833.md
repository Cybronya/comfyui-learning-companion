---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致）_2029741910889336833.json
name: 小红书FireRed-Image-edit1.1单图编辑（人像一致）_2029741910889336833
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致）_2029741910889336833.json
hash: 6865feac22008a35
coverage: 0.863636
learned_at: 2026-10-23 12:49:15
nodes: [LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), FluxKontextImageScale, Any Switch (rgthree), KSampler, VAEDecode, SaveImage, CLIPLoader, VAELoader, ModelSamplingAuraFlow, CFGNorm, SaveImage, easy cleanGpuUsed, LoraLoaderModelOnly, UNETLoader, easy int, LoadImage, CR Prompt Text, VAEEncode, PreviewImage, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 921416452521256, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致）_2029741910889336833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑（人像一致）_2029741910889336833.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `FluxKontextImageScale`
- `Any Switch (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SaveImage`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy int`
- `LoadImage`
- `CR Prompt Text`
- `VAEEncode` ★核心
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `921416452521256`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`FluxKontextImageScale`、`KSampler`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UNETLoader`、`easy int`、`LoadImage`、`CR Prompt Text`、`VAEEncode`、`TextEncodeQwenImageEditPlus`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
