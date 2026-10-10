---
key: Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713.json
name: Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713.json
hash: 65bf5fd0183b67b2
coverage: 0.842697
learned_at: 2026-10-10 20:58:52
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, LoadImage, TextEncodeQwenImage21, CR Prompt Text, LoadImage, ImageResizeKJv2, LoadImage, ImageResizeKJv2, LoadImage, ImageResizeKJv2, LoadImage, TTResolutionSelector, TTResolutionSelector, ImageResizeKJv2, TTResolutionSelector, CR Prompt Text, CLIPLoader, TTResolutionSelector, KSampler, CLIPLoader, easy showAnything, JWStringConcat, easy showAnything, easy showAnything, StringMergeNode, ResolutionSelector, SaveImageAdvanced, CR Prompt Text, Fast Groups Bypasser (rgthree), ImageResizeKJv2, CR Prompt Text, easy cleanGpuUsed, MuyeTextEditOutput, ZML_AnyTypeSwitch, TextGenerate, MuyeTextEditOutput, TextGenerate, TTResolutionSelector, BatchImagesNode, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1官方流程混合流｜文生图编辑二合一_2106946249093107713.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `LoadImage`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `TTResolutionSelector`
- `TTResolutionSelector`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `CR Prompt Text`
- `CLIPLoader`
- `TTResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `easy showAnything`
- `JWStringConcat`
- `easy showAnything`
- `easy showAnything`
- `StringMergeNode`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `CR Prompt Text`
- `easy cleanGpuUsed`
- `MuyeTextEditOutput`
- `ZML_AnyTypeSwitch`
- `TextGenerate`
- `MuyeTextEditOutput`
- `TextGenerate`
- `TTResolutionSelector`
- `BatchImagesNode`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **84%**（75/89）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`TTResolutionSelector`、`KSampler`、`JWStringConcat`、`StringMergeNode`、`ResolutionSelector`、`SaveImageAdvanced`、`MuyeTextEditOutput`、`ZML_AnyTypeSwitch`、`TextGenerate`、`BatchImagesNode`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**缺卡**（5）：`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
