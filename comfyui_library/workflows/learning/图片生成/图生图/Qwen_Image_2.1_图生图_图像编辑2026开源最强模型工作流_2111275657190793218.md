---
key: 图片生成/图生图/Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流_2111275657190793218.json
name: Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流_2111275657190793218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流_2111275657190793218.json
hash: d84c0c793ae62872
coverage: 0.536842
learned_at: 2026-10-23 11:21:13
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PathchSageAttentionKJ, MarkdownNote, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, QwenImage21Cache, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Groups Muter (rgthree), PixaromaGroupSwitch, UNETLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, EmptyLatentImage, VAEDecode, Any Switch (rgthree), SaveImage, ResolutionSelector, TextEncodeQwenImage21, CR Text Concatenate, GetNode, CR Prompt Text, QwenPERewriteT8, ShowText|pysssss, CR Prompt Text, PixaromaGroupSwitch, PixaromaGroupSwitch, SaveImageAdvanced, Any Switch (rgthree), CR Text Concatenate, CR Prompt Text, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Bypasser (rgthree), CLIPLoader, CR Prompt Text, PixaromaLabel, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 971922728037536, "steps": 40, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流_2111275657190793218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_图生图_图像编辑2026开源最强模型工作流_2111275657190793218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
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
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `CR Text Concatenate`
- `GetNode`
- `CR Prompt Text`
- `QwenPERewriteT8`
- `ShowText|pysssss`
- `CR Prompt Text`
- `PixaromaGroupSwitch`
- `PixaromaGroupSwitch`
- `SaveImageAdvanced`
- `Any Switch (rgthree)`
- `CR Text Concatenate`
- `CR Prompt Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `CR Prompt Text`
- `PixaromaLabel`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `971922728037536`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（51/95）

**有卡**：`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`Mute / Bypass Repeater (rgthree)`、`PixaromaGroupSwitch`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`EmptyLatentImage`、`SaveImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`CR Text Concatenate`、`CR Prompt Text`、`QwenPERewriteT8`、`SaveImageAdvanced`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`PixaromaLabel`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
