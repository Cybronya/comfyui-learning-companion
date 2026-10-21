---
key: 图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json
name: Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json
hash: 2c808ee620ee4b78
coverage: 0.894737
learned_at: 2026-10-19 22:29:58
nodes: [CLIPTextEncode, ModelSamplingAuraFlow, UNETLoader, CLIPTextEncode, KSampler, VAEDecode, VAEDecode, VAEDecode, KSampler, VAEDecode, CLIPTextEncode, MarkdownNote, VAELoader, UNETLoader, UNETLoader, PrimitiveNode, UNETLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, EmptyLatentImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPLoader, CLIPTextEncode, KSampler, VAEDecode, KSampler, KSampler, UNETLoader, AddLabel, SaveImage, AddLabel, SaveImage, ImageConcatMulti, Reroute, Reroute, AddLabel, AddLabel, SaveImage, AddLabel, SaveImage, SaveImage, SaveImage, PrimitiveInt, PrimitiveInt, EmptySD3LatentImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 119119590087014, "steps": 15, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Base Turbo  Art distilled  super图像对比_2018274455566426114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveNode`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `AddLabel`
- `SaveImage`
- `AddLabel`
- `SaveImage`
- `ImageConcatMulti`
- `Reroute`
- `Reroute`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `AddLabel`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `EmptySD3LatentImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `119119590087014`
- `steps` = `15`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（51/57）

**有卡**：`CLIPTextEncode`、`ModelSamplingAuraFlow`、`UNETLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`LayerUtility: PurgeVRAM`、`EmptyLatentImage`、`CLIPLoader`、`AddLabel`、`SaveImage`、`ImageConcatMulti`、`EmptySD3LatentImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CR Prompt Text

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
