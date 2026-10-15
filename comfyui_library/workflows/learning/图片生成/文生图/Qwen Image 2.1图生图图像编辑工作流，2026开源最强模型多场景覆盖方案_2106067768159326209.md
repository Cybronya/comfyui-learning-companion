---
key: 图片生成/文生图/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json
name: Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json
hash: 479ad089750cd454
coverage: 0.466667
learned_at: 2026-10-10 21:27:45
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PathchSageAttentionKJ, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenImage21Cache, LoraLoaderModelOnly, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Groups Muter (rgthree), PixaromaGroupSwitch, UNETLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, EmptyLatentImage, CLIPLoader, VAEDecode, Any Switch (rgthree), SaveImage, Fast Bypasser (rgthree), ResolutionSelector, TextEncodeQwenImage21, CR Text Concatenate, GetNode, CR Prompt Text, CR Prompt Text, QwenPERewriteT8, ShowText|pysssss, CR Prompt Text, Any Switch (rgthree), PixaromaGroupSwitch, PixaromaGroupSwitch, SaveImageAdvanced, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text Concatenate, Fast Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图生图图像编辑工作流，2026开源最强模型多场景覆盖方案_2106067768159326209.json`

## 结构

**节点**（120 个）：
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
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `LoraLoaderModelOnly`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Groups Muter (rgthree)`
- `PixaromaGroupSwitch`
- `UNETLoader`
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
- `KSampler`
- `VAEDecode`
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
- `KSampler`
- `EmptyLatentImage`
- `CLIPLoader`
- `VAEDecode`
- `Any Switch (rgthree)`
- `SaveImage`
- `Fast Bypasser (rgthree)`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `CR Text Concatenate`
- `GetNode`
- `CR Prompt Text`
- `CR Prompt Text`
- `QwenPERewriteT8`
- `ShowText|pysssss`
- `CR Prompt Text`
- `Any Switch (rgthree)`
- `PixaromaGroupSwitch`
- `PixaromaGroupSwitch`
- `SaveImageAdvanced`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **47%**（56/120）

**有卡**：`SetNode`、`Fast Groups Muter (rgthree)`、`PathchSageAttentionKJ`、`GetNode`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`Mute / Bypass Repeater (rgthree)`、`PixaromaGroupSwitch`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`

**缺卡**（17）：`CR Text Concatenate`、`Fast Bypasser (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
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
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
