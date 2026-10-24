---
key: 图片生成/图生图/Qwen Image 2.1多图编辑V1.0，角色一致性设计开源最强图生图_2112676635475533826.json
name: Qwen Image 2.1多图编辑V1.0，角色一致性设计开源最强图生图_2112676635475533826
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑V1.0，角色一致性设计开源最强图生图_2112676635475533826.json
hash: 6adae0d1bcbf55aa
coverage: 0.614754
learned_at: 2026-10-23 11:12:53
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PathchSageAttentionKJ, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, QwenImage21Cache, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Groups Muter (rgthree), UNETLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, EmptyLatentImage, VAEDecode, Any Switch (rgthree), SaveImage, GetNode, QwenPERewriteT8, ShowText|pysssss, SaveImageAdvanced, Any Switch (rgthree), CR Text Concatenate, CR Prompt Text, LoraLoaderModelOnly, CLIPLoader, PixaromaGroupSwitch, CR Text Concatenate, CR Prompt Text, CR Prompt Text, PixaromaGroupSwitch, Fast Bypasser (rgthree), PixaromaGroupSwitch, LoraLoaderModelOnly, TextEncodeQwenImage21, ResolutionSelector, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1多图编辑V1.0，角色一致性设计开源最强图生图_2112676635475533826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多图编辑V1.0，角色一致性设计开源最强图生图_2112676635475533826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（122 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（75/122）

**有卡**：`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`Mute / Bypass Repeater (rgthree)`、`UNETLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`EmptyLatentImage`、`SaveImage`、`QwenPERewriteT8`、`SaveImageAdvanced`、`CR Text Concatenate`、`CR Prompt Text`、`CLIPLoader`、`PixaromaGroupSwitch`、`Fast Bypasser (rgthree)`、`TextEncodeQwenImage21`、`ResolutionSelector`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
