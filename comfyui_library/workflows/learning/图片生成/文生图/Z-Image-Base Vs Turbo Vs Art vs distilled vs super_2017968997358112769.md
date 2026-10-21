---
key: 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json
name: Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json
hash: bbd4566dda8132b0
coverage: 0.867925
learned_at: 2026-10-19 22:15:23
nodes: [MarkdownNote, CLIPTextEncode, ModelSamplingAuraFlow, LayerUtility: PurgeVRAM, UNETLoader, MarkdownNote, CLIPTextEncode, KSampler, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, VAEDecode, EmptySD3LatentImage, VAEDecode, AddLabel, UNETLoader, KSampler, CLIPTextEncode, EmptyLatentImage, VAEDecode, VAELoader, CLIPLoader, LayerUtility: PurgeVRAM, AddLabel, AddLabel, PrimitiveInt, PrimitiveInt, PrimitiveNode, KSampler, CLIPTextEncode, UNETLoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, EmptyLatentImage, VAEDecode, CLIPTextEncode, KSampler, UNETLoader, AddLabel, LayerUtility: PurgeVRAM, CLIPTextEncode, EmptyLatentImage, VAEDecode, CLIPTextEncode, UNETLoader, KSampler, AddLabel, CR Prompt Text, ImageConcatMulti, Reroute, Reroute, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 236892566088897, "steps": 15, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Base Vs Turbo Vs Art vs distilled vs super_2017968997358112769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
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
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `AddLabel`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `AddLabel`
- `CR Prompt Text`
- `ImageConcatMulti`
- `Reroute`
- `Reroute`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `236892566088897`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（46/53）

**有卡**：`CLIPTextEncode`、`ModelSamplingAuraFlow`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`EmptySD3LatentImage`、`AddLabel`、`VAELoader`、`CLIPLoader`、`CR Prompt Text`、`ImageConcatMulti`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
