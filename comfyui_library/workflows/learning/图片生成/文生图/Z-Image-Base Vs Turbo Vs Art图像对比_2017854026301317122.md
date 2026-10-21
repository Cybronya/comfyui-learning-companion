---
key: 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json
name: Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json
hash: cd2c1f9748c3945d
coverage: 0.891892
learned_at: 2026-10-19 22:15:24
nodes: [CLIPTextEncode, ModelSamplingAuraFlow, CLIPTextEncode, KSampler, CLIPTextEncode, MarkdownNote, CLIPTextEncode, KSampler, CLIPLoader, VAELoader, KSampler, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, PrimitiveNode, SaveImage, CR Prompt Text, PrimitiveInt, EmptyLatentImage, EmptyLatentImage, UNETLoader, UNETLoader, UNETLoader, PrimitiveInt, EmptySD3LatentImage, CLIPTextEncode, VAEDecode, VAEDecode, AddLabel, AddLabel, SaveImage, LayerUtility: PurgeVRAM, AddLabel, ImageConcatMulti, SaveImage, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 236892566088885, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Base Vs Turbo Vs Art图像对比_2017854026301317122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `SaveImage`
- `CR Prompt Text`
- `PrimitiveInt`
- `EmptyLatentImage` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `236892566088885`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`CLIPTextEncode`、`ModelSamplingAuraFlow`、`KSampler`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`SaveImage`、`CR Prompt Text`、`EmptyLatentImage`、`UNETLoader`、`EmptySD3LatentImage`、`AddLabel`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
