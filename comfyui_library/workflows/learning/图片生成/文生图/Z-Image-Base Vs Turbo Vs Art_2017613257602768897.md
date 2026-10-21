---
key: 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json
name: Z-Image-Base Vs Turbo Vs Art_2017613257602768897
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json
hash: 9329196e7cf448b3
coverage: 0.857143
learned_at: 2026-10-19 22:15:23
nodes: [MarkdownNote, CLIPTextEncode, ModelSamplingAuraFlow, LayerUtility: PurgeVRAM, UNETLoader, MarkdownNote, CLIPTextEncode, KSampler, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, VAEDecode, EmptySD3LatentImage, VAEDecode, AddLabel, UNETLoader, KSampler, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, VAEDecode, ImageConcatMulti, VAELoader, CLIPLoader, UNETLoader, CR Prompt Text, LayerUtility: PurgeVRAM, AddLabel, AddLabel, LayerUtility: PurgeVRAM, PrimitiveInt, PrimitiveInt, SaveImage, PrimitiveNode, KSampler]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 236892566088897, "steps": 50, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Base Vs Turbo Vs Art_2017613257602768897.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `AddLabel`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveImage`
- `PrimitiveNode`
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `236892566088897`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`CLIPTextEncode`、`ModelSamplingAuraFlow`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`EmptySD3LatentImage`、`AddLabel`、`ImageConcatMulti`、`VAELoader`、`CLIPLoader`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
