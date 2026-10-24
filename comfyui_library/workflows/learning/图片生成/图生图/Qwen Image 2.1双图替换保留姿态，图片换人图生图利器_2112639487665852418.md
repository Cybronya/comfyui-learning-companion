---
key: 图片生成/图生图/Qwen Image 2.1双图替换保留姿态，图片换人图生图利器_2112639487665852418.json
name: Qwen Image 2.1双图替换保留姿态，图片换人图生图利器_2112639487665852418
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1双图替换保留姿态，图片换人图生图利器_2112639487665852418.json
hash: 662b939e75d9fba9
coverage: 0.857143
learned_at: 2026-10-23 11:12:51
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, JjkText, LoadImage, PrimitiveInt, QwenImage21Cache, ImageResizeKJv2, ImageResizeKJv2, EmptyLatentImage, TextEncodeQwenImage21, easy imageConcat, ComfySwitchNode, ImageScale, KSampler, VAEDecode, SaveImage, easy imageConcat, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1双图替换保留姿态，图片换人图生图利器_2112639487665852418.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1双图替换保留姿态，图片换人图生图利器_2112639487665852418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `JjkText`
- `LoadImage`
- `PrimitiveInt`
- `QwenImage21Cache`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `easy imageConcat`
- `ComfySwitchNode`
- `ImageScale`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy imageConcat`
- `SaveImage`
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

覆盖率 **86%**（42/49）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`ImageResizeKJv2`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`easy imageConcat`、`ImageScale`、`KSampler`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
