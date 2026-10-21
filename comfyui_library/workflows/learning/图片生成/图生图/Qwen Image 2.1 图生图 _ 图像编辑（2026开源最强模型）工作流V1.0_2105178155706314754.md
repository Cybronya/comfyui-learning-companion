---
key: 图片生成/图生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2105178155706314754.json
name: Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2105178155706314754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2105178155706314754.json
hash: 25cc717c2e751066
coverage: 0.526882
learned_at: 2026-10-21 00:42:13
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PathchSageAttentionKJ, MarkdownNote, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, MarkdownNote, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenImage21Cache, LoraLoaderModelOnly, PixaromaGroupSwitch, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Groups Muter (rgthree), PixaromaGroupSwitch, UNETLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, EmptyLatentImage, QwenPERewriteT8, CLIPLoader, VAEDecode, Any Switch (rgthree), SaveImage, PixaromaLabel, PixaromaLabel, Fast Bypasser (rgthree), ShowText|pysssss, TextEncodeQwenImage21, SaveImageAdvanced, PixaromaGroupSwitch, LoadImage, LoadImage, CR Prompt Text, ResolutionSelector]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 690787852573901, "steps": 40, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2105178155706314754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2105178155706314754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `PixaromaGroupSwitch`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Groups Muter (rgthree)`
- `PixaromaGroupSwitch`
- `UNETLoader` ★核心
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `QwenPERewriteT8`
- `CLIPLoader`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `SaveImage`
- `PixaromaLabel`
- `PixaromaLabel`
- `Fast Bypasser (rgthree)`
- `ShowText|pysssss`
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `PixaromaGroupSwitch`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `ResolutionSelector`

## 关键参数

- `seed` = `690787852573901`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（49/93）

**有卡**：`PathchSageAttentionKJ`、`LoadImage`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`PixaromaGroupSwitch`、`Mute / Bypass Repeater (rgthree)`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`QwenPERewriteT8`、`CLIPLoader`、`SaveImage`、`PixaromaLabel`、`Fast Bypasser (rgthree)`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`CR Prompt Text`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
