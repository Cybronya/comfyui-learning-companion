---
key: 图片生成/图生图/影视分镜关键帧提示词｜GP-T2.0多图版反推图生图_2092574881362833409.json
name: 影视分镜关键帧提示词｜GP-T2.0多图版反推图生图_2092574881362833409
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/影视分镜关键帧提示词｜GP-T2.0多图版反推图生图_2092574881362833409.json
hash: c94cf022e299ceae
coverage: 0.745455
learned_at: 2026-10-21 00:52:30
nodes: [SaveImage, LoadImage, JjkText, MultiTextConcatenate, ttN concat, JjkText, MultiTextConcatenate, ttN concat, ttN concat, easy cleanGpuUsed, ImageLoader, MultiTextConcatenate, Text, MultiTextConcatenate, JjkText, JjkText, JjkText, JjkText, JjkText, ImageLoader, ImageLoader, ImageLoader, JjkText, RH_RhartImageG2ImageToImage, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, easy showAnything, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/影视分镜关键帧提示词｜GP-T2.0多图版反推图生图_2092574881362833409.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/影视分镜关键帧提示词｜GP-T2.0多图版反推图生图_2092574881362833409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `SaveImage`
- `LoadImage`
- `JjkText`
- `MultiTextConcatenate`
- `ttN concat`
- `JjkText`
- `MultiTextConcatenate`
- `ttN concat`
- `ttN concat`
- `easy cleanGpuUsed`
- `ImageLoader`
- `MultiTextConcatenate`
- `Text`
- `MultiTextConcatenate`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `ImageLoader`
- `ImageLoader`
- `ImageLoader`
- `JjkText`
- `RH_RhartImageG2ImageToImage`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `easy showAnything`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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

覆盖率 **75%**（41/55）

**有卡**：`SaveImage`、`LoadImage`、`MultiTextConcatenate`、`ttN concat`、`easy cleanGpuUsed`、`ImageLoader`、`Text`、`RH_RhartImageG2ImageToImage`、`RH_LLMAPI_Pro_Node`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
