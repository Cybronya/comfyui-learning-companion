---
key: 图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json
name: Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json
hash: 480d5c1373b5a94b
coverage: 0.272727
learned_at: 2026-10-06 21:36:16
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PathchSageAttentionKJ, MarkdownNote, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadImage, MarkdownNote, LoraLoaderModelOnly, QwenImage21Cache, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Groups Muter (rgthree), PixaromaGroupSwitch, UNETLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, EmptyLatentImage, VAEDecode, Any Switch (rgthree), SaveImage, PixaromaLabel, PixaromaLabel, ResolutionSelector, TextEncodeQwenImage21, CR Text Concatenate, GetNode, CR Prompt Text, QwenPERewriteT8, ShowText|pysssss, CR Prompt Text, PixaromaGroupSwitch, PixaromaGroupSwitch, SaveImageAdvanced, Any Switch (rgthree), CR Text Concatenate, CR Prompt Text, LoraLoaderModelOnly, LoraLoaderModelOnly, Fast Bypasser (rgthree), CLIPLoader, CR Prompt Text]
patterns: []
missing: [CR Text Concatenate, CR Text Concatenate, Fast Bypasser (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PixaromaGroupSwitch, PixaromaGroupSwitch, PixaromaGroupSwitch, PixaromaLabel, PixaromaLabel, QwenPERewriteT8, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, SaveImageAdvanced]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 158987411863606, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1 图生图 _ 图像编辑（2026开源最强模型）工作流V1.0_2103948729811300354.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
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
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
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
- `PixaromaLabel`
- `PixaromaLabel`
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

## 关键参数

- `seed` = `158987411863606`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **27%**（27/99）

**有卡**：`LoadImage`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`CLIPLoader`

**缺卡**（37）：`CR Text Concatenate`、`CR Text Concatenate`、`Fast Bypasser (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`Fast Groups Muter (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`PixaromaGroupSwitch`、`PixaromaGroupSwitch`、`PixaromaGroupSwitch`、`PixaromaLabel`、`PixaromaLabel`、`QwenPERewriteT8`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaLabel` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
