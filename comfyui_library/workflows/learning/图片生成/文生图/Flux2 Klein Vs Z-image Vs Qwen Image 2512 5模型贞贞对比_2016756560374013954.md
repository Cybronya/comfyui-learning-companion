---
key: 图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 5模型贞贞对比_2016756560374013954.json
name: Flux2 Klein Vs Z-image Vs Qwen Image 2512 5模型贞贞对比_2016756560374013954
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 5模型贞贞对比_2016756560374013954.json
hash: a42d96350d4b3aa4
coverage: 0.957746
learned_at: 2026-10-19 22:15:02
nodes: [ConditioningZeroOut, UNETLoader, CLIPTextEncode, LoraLoaderModelOnly, CLIPTextEncode, CLIPLoader, CLIPTextEncode, VAELoader, ModelSamplingAuraFlow, UnetLoaderGGUF, EmptySD3LatentImage, easy promptLine, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, LoraLoaderModelOnly, VAEDecode, EmptyLatentImage, EmptyFlux2LatentImage, CLIPLoader, VAELoader, ModelPatchTorchSettings, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, VAEDecode, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, KSampler, KSampler, KSampler, CLIPTextEncode, LayerUtility: PurgeVRAM, KSampler, MarkdownNote, CLIPTextEncode, CLIPLoader, EmptySD3LatentImage, JWInteger, JWInteger, VAEDecode, SaveImage, SaveImage, SaveImage, Reroute, ModelSamplingAuraFlow, UNETLoader, VAELoader, LoraLoaderModelOnly, SaveImage, CLIPTextEncode, LayerUtility: PurgeVRAM, MarkdownNote, CLIPTextEncode, VAEDecode, SaveImage, ModelSamplingAuraFlow, LoraLoaderModelOnly, ImageConcatMulti, PDIMAGE_LongerSize, AddLabel, AddLabel, AddLabel, AddLabel, KSampler, CR Prompt Text, SaveImage, AddLabel]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1600, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 399865039407114, "steps": 50, "width": 904}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 5模型贞贞对比_2016756560374013954.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2 Klein Vs Z-image Vs Qwen Image 2512 5模型贞贞对比_2016756560374013954.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `UnetLoaderGGUF` ★核心
- `EmptySD3LatentImage`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `EmptyFlux2LatentImage`
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `EmptySD3LatentImage`
- `JWInteger`
- `JWInteger`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Reroute`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `ImageConcatMulti`
- `PDIMAGE_LongerSize`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `KSampler` ★核心
- `CR Prompt Text`
- `SaveImage`
- `AddLabel`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `904`
- `height` = `1600`
- `batch_size` = `1`
- `seed` = `399865039407114`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（68/71）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`UnetLoaderGGUF`、`EmptySD3LatentImage`、`easy promptLine`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`EmptyLatentImage`、`EmptyFlux2LatentImage`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`KSampler`、`JWInteger`、`SaveImage`、`ImageConcatMulti`、`PDIMAGE_LongerSize`、`AddLabel`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
