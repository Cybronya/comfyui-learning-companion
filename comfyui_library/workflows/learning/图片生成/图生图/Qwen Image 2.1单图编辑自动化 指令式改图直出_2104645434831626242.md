---
key: 图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json
name: Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json
hash: d1504abb11d069b6
coverage: 0.886792
learned_at: 2026-10-21 00:42:23
nodes: [CLIPLoader, VAEDecode, GetImageSizeAndCount, SaveImage, PreviewImage, easy imageConcat, TextEncodeQwenImage21, KSampler, easy seed, easy int, LoadImage, CLIPLoader, TextGenerateLTX2Prompt, UNETLoader, VAELoader, GetImageSizeAndCount, easy positive, easy int, LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, easy saveText, StringFunction|pysssss, easy saveText, easy showAnything, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1单图编辑自动化 指令式改图直出_2104645434831626242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `SaveImage`
- `PreviewImage`
- `easy imageConcat`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `easy seed`
- `easy int`
- `LoadImage`
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `VAELoader`
- `GetImageSizeAndCount`
- `easy positive`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy anythingIndexSwitch`
- `easy saveText`
- `StringFunction|pysssss`
- `easy saveText`
- `easy showAnything`
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

覆盖率 **89%**（47/53）

**有卡**：`CLIPLoader`、`VAEDecode`、`GetImageSizeAndCount`、`SaveImage`、`easy imageConcat`、`TextEncodeQwenImage21`、`KSampler`、`easy seed`、`easy int`、`LoadImage`、`TextGenerateLTX2Prompt`、`UNETLoader`、`VAELoader`、`easy positive`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy anythingIndexSwitch`、`easy saveText`、`StringFunction|pysssss`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
