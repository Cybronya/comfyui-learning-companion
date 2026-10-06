---
key: 图片生成/文生图/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json
name: Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json
hash: b173d2a5f3271b8e
coverage: 0.619048
learned_at: 2026-10-06 21:48:40
nodes: [LoraLoaderModelOnly, PixaromaGroupSwitch, TextEncodeQwenImage21, KSampler, PixaromaResolution, EmptyLatentImage, KSampler, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), Any Switch (rgthree), VAEDecode, VAEDecode, LoraLoaderModelOnly, CR Text Concatenate, CR Text Concatenate, CR Prompt Text, CR Prompt Text, PixaromaGroupSwitch, Any Switch (rgthree), SaveImage, LoadImage, PreviewAny, QwenPERewriteT8, SaveImageAdvanced, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, QwenImage21Cache, PathchSageAttentionKJ, ModelAttentionBackend, QwenPERewriteT8, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text Concatenate, CR Text Concatenate, Fast Bypasser (rgthree), ModelAttentionBackend, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PixaromaGroupSwitch, PixaromaGroupSwitch, QwenPERewriteT8, QwenPERewriteT8, CR Prompt Text, CR Prompt Text, CR Prompt Text, PixaromaResolution, PreviewAny, SaveImageAdvanced, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `PixaromaResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图2026开源最强模型工作流，高质量文本到图像生成方案_2107157719223455746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（63 个）：
- `LoraLoaderModelOnly` ★核心
- `PixaromaGroupSwitch`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `PixaromaResolution`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `PathchSageAttentionKJ`
- `ModelAttentionBackend`
- `QwenPERewriteT8`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **62%**（39/63）

**有卡**：`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`CLIPTextEncode`

**缺卡**（18）：`CR Text Concatenate`、`CR Text Concatenate`、`Fast Bypasser (rgthree)`、`ModelAttentionBackend`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`PixaromaGroupSwitch`、`PixaromaGroupSwitch`、`QwenPERewriteT8`、`QwenPERewriteT8`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`PixaromaResolution`、`PreviewAny`、`SaveImageAdvanced`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ModelAttentionBackend` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `PixaromaResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
