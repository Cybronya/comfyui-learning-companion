---
key: 图片生成/图生图/多图编辑Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2107725897594925057.json
name: 多图编辑Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2107725897594925057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2107725897594925057.json
hash: b25926a0456697cc
coverage: 0.541667
learned_at: 2026-10-21 00:51:55
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PathchSageAttentionKJ, MarkdownNote, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, QwenImage21Cache, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Groups Muter (rgthree), UNETLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, EmptyLatentImage, VAEDecode, Any Switch (rgthree), SaveImage, GetNode, QwenPERewriteT8, ShowText|pysssss, SaveImageAdvanced, Any Switch (rgthree), CR Text Concatenate, CR Prompt Text, LoraLoaderModelOnly, CLIPLoader, PixaromaGroupSwitch, CR Text Concatenate, CR Prompt Text, CR Prompt Text, PixaromaGroupSwitch, Fast Bypasser (rgthree), PixaromaGroupSwitch, LoraLoaderModelOnly, TextEncodeQwenImage21, ResolutionSelector, CR Prompt Text, PixaromaLabel, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 307873573335419, "steps": 40, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多图编辑Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2107725897594925057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2107725897594925057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
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
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Groups Muter (rgthree)`
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
- `LoadImage`
- `LoadImage`
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
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `SaveImage`
- `GetNode`
- `QwenPERewriteT8`
- `ShowText|pysssss`
- `SaveImageAdvanced`
- `Any Switch (rgthree)`
- `CR Text Concatenate`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `PixaromaGroupSwitch`
- `CR Text Concatenate`
- `CR Prompt Text`
- `CR Prompt Text`
- `PixaromaGroupSwitch`
- `Fast Bypasser (rgthree)`
- `PixaromaGroupSwitch`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `CR Prompt Text`
- `PixaromaLabel`
- `LoadImage`

## 关键参数

- `seed` = `307873573335419`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（52/96）

**有卡**：`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`Mute / Bypass Repeater (rgthree)`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`EmptyLatentImage`、`SaveImage`、`QwenPERewriteT8`、`SaveImageAdvanced`、`CR Text Concatenate`、`CR Prompt Text`、`CLIPLoader`、`PixaromaGroupSwitch`、`Fast Bypasser (rgthree)`、`TextEncodeQwenImage21`、`ResolutionSelector`、`PixaromaLabel`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
