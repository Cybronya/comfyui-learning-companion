---
key: 图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 4模型贞贞对比_2013662502973874178.json
name: Flux2 Klein Vs Z-image Vs Qwen Image 2512 4模型贞贞对比_2013662502973874178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 4模型贞贞对比_2013662502973874178.json
hash: 20d3bb9c23e987c9
coverage: 1
learned_at: 2026-10-19 22:15:02
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, UNETLoader, CLIPTextEncode, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingAuraFlow, UnetLoaderGGUF, SaveImage, ModelPatchTorchSettings, LayerUtility: PurgeVRAM, EmptySD3LatentImage, CR Prompt Text, easy promptLine, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, UNETLoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, LoraLoaderModelOnly, VAEDecode, VAEDecode, EmptyLatentImage, SaveImage, EmptyFlux2LatentImage, JWInteger, JWInteger, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, ModelPatchTorchSettings, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, AddLabel, AddLabel, ImageConcatMulti, PDIMAGE_LongerSize, AddLabel, AddLabel, SaveImage, LoraLoaderModelOnly, KSampler, KSampler, KSampler, KSampler]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1600, "sampler_name": "euler", "scheduler": "simple", "seed": 396473063056891, "steps": 10, "width": 904}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 4模型贞贞对比_2013662502973874178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 4模型贞贞对比_2013662502973874178.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `UnetLoaderGGUF` ★核心
- `SaveImage`
- `ModelPatchTorchSettings`
- `LayerUtility: PurgeVRAM`
- `EmptySD3LatentImage`
- `CR Prompt Text`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `EmptyFlux2LatentImage`
- `JWInteger`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `904`
- `height` = `1600`
- `batch_size` = `1`
- `seed` = `396473063056891`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（58/58）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`SaveImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`UnetLoaderGGUF`、`ModelPatchTorchSettings`、`LayerUtility: PurgeVRAM`、`EmptySD3LatentImage`、`CR Prompt Text`、`easy promptLine`、`PathchSageAttentionKJ`、`VAEDecode`、`EmptyLatentImage`、`EmptyFlux2LatentImage`、`JWInteger`、`AddLabel`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
