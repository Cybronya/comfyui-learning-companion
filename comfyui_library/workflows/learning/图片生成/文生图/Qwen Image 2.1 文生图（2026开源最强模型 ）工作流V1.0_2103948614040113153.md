---
key: 图片生成/文生图/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json
name: Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json
hash: a16bf040d37c507f
coverage: 0.692308
learned_at: 2026-10-10 21:27:41
nodes: [LoadImage, LoadImage, MarkdownNote, LoraLoaderModelOnly, PixaromaGroupSwitch, TextEncodeQwenImage21, KSampler, PixaromaResolution, EmptyLatentImage, KSampler, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Any Switch (rgthree), PixaromaLabel, PixaromaLabel, VAEDecode, VAEDecode, LoraLoaderModelOnly, CR Text Concatenate, CR Text Concatenate, CR Prompt Text, CR Prompt Text, PixaromaGroupSwitch, Any Switch (rgthree), SaveImage, LoadImage, PreviewAny, QwenPERewriteT8, SaveImageAdvanced, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, QwenImage21Cache, PathchSageAttentionKJ, ModelAttentionBackend, QwenPERewriteT8, CR Prompt Text]
patterns: []
missing: [CR Text Concatenate, CR Text Concatenate, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 222703940394256, "steps": 8, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图（2026开源最强模型 ）工作流V1.0_2103948614040113153.json`

## 结构

**节点**（39 个）：
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `LoraLoaderModelOnly`
- `PixaromaGroupSwitch`
- `TextEncodeQwenImage21`
- `KSampler`
- `PixaromaResolution`
- `EmptyLatentImage`
- `KSampler`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `PixaromaLabel`
- `PixaromaLabel`
- `VAEDecode`
- `VAEDecode`
- `LoraLoaderModelOnly`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Prompt Text`
- `CR Prompt Text`
- `PixaromaGroupSwitch`
- `Any Switch (rgthree)`
- `SaveImage`
- `LoadImage`
- `PreviewAny`
- `QwenPERewriteT8`
- `SaveImageAdvanced`
- `CLIPLoader`
- `UNETLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `PathchSageAttentionKJ`
- `ModelAttentionBackend`
- `QwenPERewriteT8`
- `CR Prompt Text`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `222703940394256`
- `steps` = `8`
- `width` = `1024`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`LoadImage`、`MarkdownNote`、`LoraLoaderModelOnly`、`PixaromaGroupSwitch`、`TextEncodeQwenImage21`、`KSampler`、`PixaromaResolution`、`EmptyLatentImage`、`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`Any Switch (rgthree)`、`PixaromaLabel`、`VAEDecode`、`CR Text Concatenate`、`CR Prompt Text`、`SaveImage`

**缺卡**（8）：`CR Text Concatenate`、`CR Text Concatenate`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
