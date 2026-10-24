---
key: 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2030166401742282754.json
name: 小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2030166401742282754
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2030166401742282754.json
hash: c9aa09d55638e2d0
coverage: 0.821429
learned_at: 2026-10-23 12:49:12
nodes: [VAEEncode, VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, Any Switch (rgthree), TextEncodeQwenImageEditPlus, Fast Groups Muter (rgthree), PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, FluxKontextImageScale, FluxKontextImageScale, KSampler, Any Switch (rgthree), VAEDecode, easy cleanGpuUsed, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy int, Image Comparer (rgthree), SaveImage, LoadImage, LoadImage, CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 607587165253807, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2030166401742282754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑（文字排版参考）_2030166401742282754.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `VAEEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `607587165253807`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`VAEEncode`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`FluxKontextImageScale`、`KSampler`、`VAEDecode`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UNETLoader`、`easy int`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
