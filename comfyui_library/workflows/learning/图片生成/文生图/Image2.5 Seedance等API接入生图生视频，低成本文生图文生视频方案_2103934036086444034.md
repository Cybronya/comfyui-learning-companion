---
key: 图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json
name: Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json
hash: 22330a7ec1dfdce5
coverage: 0.885714
learned_at: 2026-10-10 20:58:40
nodes: [RH_Screenwriter, LoadImage, SaveImage, WujiUpscaler2, WujiAPI, WujiClosedSourceGenerator, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json`

## 结构

**节点**（35 个）：
- `RH_Screenwriter`
- `LoadImage`
- `SaveImage`
- `WujiUpscaler2`
- `WujiAPI`
- `WujiClosedSourceGenerator`
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

覆盖率 **89%**（31/35）

**有卡**：`RH_Screenwriter`、`LoadImage`、`SaveImage`、`WujiUpscaler2`、`WujiAPI`、`WujiClosedSourceGenerator`、`孤海注释`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`JjkText`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
