---
key: 图片生成/文生图/boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946.json
name: boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946.json
hash: ef0ef46151546152
coverage: 0.897436
learned_at: 2026-10-19 23:22:12
nodes: [UNETLoader, CLIPTextEncode, CLIPTextEncode, SaveImage, KSampler, CLIPLoader, VAELoader, EmptyLatentImage, PreviewImage, VAELoader, CLIPLoader, UNETLoader, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, KSampler, SaveImage, PreviewImage, CLIPLoader, VAELoader, VAEDecode, UNETLoader, KSampler, PreviewImage, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, ModelSamplingAuraFlow, VAEDecode, VAEDecode, AddLabel, AddLabel, AddLabel, ImageConcatMulti, CR Prompt Text, Int, Int, PreviewImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 94970783357899, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/boogu-trubo VS boogu-base VS Z-image-trubo—图像对比_2068142561574866946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `CR Prompt Text`
- `Int`
- `Int`
- `PreviewImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `94970783357899`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`SaveImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`AddLabel`、`ImageConcatMulti`、`CR Prompt Text`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
