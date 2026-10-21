---
key: 图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json
name: Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json
hash: 265b39132a6bfb72
coverage: 0.891304
learned_at: 2026-10-21 02:55:36
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, llama_cpp_model_loader, CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, KSampler, KSampler, VAEDecode, VAEDecode, CLIPLoader, VAELoader, KSampler, UNETLoader, VAEDecode, AddLabel, EmptyLatentImage, CLIPTextEncode, EmptyLatentImage, CR Prompt Text, PreviewImage, PreviewImage, SaveImage, PreviewImage, CLIPTextEncode, ShowText|pysssss, llama_cpp_instruct_adv, ImageConcatMulti, ConditioningZeroOut, EmptyLatentImage, AddLabel, AddLabel, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 648252134594636, "steps": 8, "width": 896}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Anime VS Z-image  VS  ERNIE-image-动漫风格对比_2049475191444606977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `llama_cpp_model_loader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CR Prompt Text`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `ImageConcatMulti`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `AddLabel`
- `AddLabel`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `648252134594636`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `896`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（41/46）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`llama_cpp_model_loader`、`KSampler`、`VAEDecode`、`AddLabel`、`EmptyLatentImage`、`CR Prompt Text`、`SaveImage`、`llama_cpp_instruct_adv`、`ImageConcatMulti`、`ConditioningZeroOut`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
