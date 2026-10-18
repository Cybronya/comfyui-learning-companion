---
key: 视频生成/图生视频/Qwen_Image_2.1官方流程混合流｜文生图编辑二合一_2107271722138431489.json
name: Qwen_Image_2.1官方流程混合流｜文生图编辑二合一_2107271722138431489
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1官方流程混合流｜文生图编辑二合一_2107271722138431489.json
hash: 9fec129f150a48eb
coverage: 0.910112
learned_at: 2026-10-17 22:18:56
nodes: [UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, CLIPLoader, LoadImage, TextEncodeQwenImage21, CR Prompt Text, LoadImage, ImageResizeKJv2, LoadImage, ImageResizeKJv2, LoadImage, ImageResizeKJv2, LoadImage, TTResolutionSelector, TTResolutionSelector, ImageResizeKJv2, TTResolutionSelector, CR Prompt Text, CLIPLoader, TTResolutionSelector, KSampler, CLIPLoader, easy showAnything, JWStringConcat, easy showAnything, easy showAnything, StringMergeNode, ResolutionSelector, SaveImageAdvanced, CR Prompt Text, Fast Groups Bypasser (rgthree), ImageResizeKJv2, CR Prompt Text, easy cleanGpuUsed, MuyeTextEditOutput, ZML_AnyTypeSwitch, TextGenerate, MuyeTextEditOutput, TextGenerate, TTResolutionSelector, BatchImagesNode, SaveImage, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, LoadImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_Image_2.1官方流程混合流｜文生图编辑二合一_2107271722138431489.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1官方流程混合流｜文生图编辑二合一_2107271722138431489.json`

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
- `LoadImage`
- `PreviewImage`

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

覆盖率 **91%**（81/89）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImage21`、`CR Prompt Text`、`ImageResizeKJv2`、`TTResolutionSelector`、`KSampler`、`JWStringConcat`、`StringMergeNode`、`ResolutionSelector`、`SaveImageAdvanced`、`easy cleanGpuUsed`、`MuyeTextEditOutput`、`ZML_AnyTypeSwitch`、`TextGenerate`、`BatchImagesNode`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
