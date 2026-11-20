---
key: 平台全量/超级换装（FireRed-Image-edit1.1 双图编辑）_2036633845113556994.json
name: 超级换装（FireRed-Image-edit1.1 双图编辑）_2036633845113556994
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/超级换装（FireRed-Image-edit1.1 双图编辑）_2036633845113556994.json
hash: 5d4368fc7c5abc40
coverage: 1
learned_at: 2026-11-14 02:46:39
nodes: [LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, ModelSamplingAuraFlow, CFGNorm, easy cleanGpuUsed, SaveImage, LoadImage, LoadImage, FluxKontextImageScale, TextEncodeQwenImageEditPlus, FluxKontextImageScale, EmptyLatentImage, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ImageUpscaleWithModel, VAEDecode, TextEncodeQwenImageEditPlus, KSampler, UltimateSDUpscaleCustomSample, ConditioningZeroOut, CLIPTextEncode, SaveImage, KSamplerSelect, UpscaleModelLoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 830541752564978, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/超级换装（FireRed-Image-edit1.1 双图编辑）_2036633845113556994.json

> 来源文件 `comfyui_library/workflows/平台全量/超级换装（FireRed-Image-edit1.1 双图编辑）_2036633845113556994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `easy cleanGpuUsed`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ImageUpscaleWithModel`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `UltimateSDUpscaleCustomSample`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSamplerSelect` ★核心
- `UpscaleModelLoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `830541752564978`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`easy cleanGpuUsed`、`SaveImage`、`LoadImage`、`FluxKontextImageScale`、`TextEncodeQwenImageEditPlus`、`EmptyLatentImage`、`ImageUpscaleWithModel`、`VAEDecode`、`KSampler`、`UltimateSDUpscaleCustomSample`、`ConditioningZeroOut`、`CLIPTextEncode`、`KSamplerSelect`、`UpscaleModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
