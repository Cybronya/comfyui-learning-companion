---
key: 图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json
name: Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json
hash: 06221ea1d4cf808c
coverage: 0.878049
learned_at: 2026-10-23 11:14:20
nodes: [UNETLoader, LoadImage, SaveImage, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, InpaintModelConditioning, KSampler, VAEDecode, CLIPLoader, TextEncodeQwenImage21, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image2.1万能局部重绘 图片局部修改精准控制_2108621339333578754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
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

覆盖率 **88%**（36/41）

**有卡**：`UNETLoader`、`LoadImage`、`SaveImage`、`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`CLIPLoader`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
