---
key: 图片生成/图生图/换姿势QwenImage2.1原生controlNet 姿态精准控制_2108672987565223937.json
name: 换姿势QwenImage2.1原生controlNet 姿态精准控制_2108672987565223937
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换姿势QwenImage2.1原生controlNet 姿态精准控制_2108672987565223937.json
hash: 094647043d905009
coverage: 0.830189
learned_at: 2026-10-23 12:56:34
nodes: [QwenImage21Cache, CLIPLoader, VAELoader, ComfySwitchNode, TextGenerate, UNETLoader, JjkText, OpenposePreprocessor, VAEDecode, JjkText, CR Text Concatenate, BatchImagesNode, kkGetImage, TextEncodeQwenImage21, CLIPLoader, EmptySD3LatentImage, SaveImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, PreviewAny, LoadImage, LoadImage, Int, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/换姿势QwenImage2.1原生controlNet 姿态精准控制_2108672987565223937.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换姿势QwenImage2.1原生controlNet 姿态精准控制_2108672987565223937.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `ComfySwitchNode`
- `TextGenerate`
- `UNETLoader` ★核心
- `JjkText`
- `OpenposePreprocessor`
- `VAEDecode` ★核心
- `JjkText`
- `CR Text Concatenate`
- `BatchImagesNode`
- `kkGetImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `EmptySD3LatentImage`
- `SaveImage`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewAny`
- `LoadImage`
- `LoadImage`
- `Int`
- `PreviewImage`
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

覆盖率 **83%**（44/53）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`TextGenerate`、`UNETLoader`、`OpenposePreprocessor`、`VAEDecode`、`CR Text Concatenate`、`BatchImagesNode`、`kkGetImage`、`TextEncodeQwenImage21`、`EmptySD3LatentImage`、`SaveImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`Int`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
