---
key: 图片生成/文生图/Z家族模型大对比：Z-Image-Base Vs Turbo Vs Art_2017783121365700609.json
name: Z家族模型大对比：Z-Image-Base Vs Turbo Vs Art_2017783121365700609
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z家族模型大对比：Z-Image-Base Vs Turbo Vs Art_2017783121365700609.json
hash: ede0a77b9079a54d
coverage: 0.894737
learned_at: 2026-10-19 22:15:38
nodes: [CLIPTextEncode, MuyeSizeSelector, PrimitiveNode, KSampler, KSampler, ImageConcatMulti, VAELoader, MarkdownNote, CLIPTextEncode, CLIPTextEncode, KSampler, CLIPLoader, ModelSamplingAuraFlow, UNETLoader, UNETLoader, EmptyLatentImage, MarkdownNote, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, UNETLoader, AddLabel, AddLabel, CR Prompt Text, CLIPTextEncode, Reroute, CLIPTextEncode, CLIPTextEncode, SaveImage, easy promptLine, easy promptLine, AddLabel, VAEDecode, SaveImage, SaveImage, SaveImage, VAEDecode, VAEDecode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 236892566088897, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z家族模型大对比：Z-Image-Base Vs Turbo Vs Art_2017783121365700609.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z家族模型大对比：Z-Image-Base Vs Turbo Vs Art_2017783121365700609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPTextEncode` ★核心
- `MuyeSizeSelector`
- `PrimitiveNode`
- `KSampler` ★核心
- `KSampler` ★核心
- `ImageConcatMulti`
- `VAELoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `AddLabel`
- `AddLabel`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy promptLine`
- `easy promptLine`
- `AddLabel`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `236892566088897`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（34/38）

**有卡**：`CLIPTextEncode`、`MuyeSizeSelector`、`KSampler`、`ImageConcatMulti`、`VAELoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`EmptyLatentImage`、`LayerUtility: PurgeVRAM`、`AddLabel`、`CR Prompt Text`、`SaveImage`、`easy promptLine`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
