---
key: 图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json
name: anima_base 1.0 Moebius 风格文生图_2073322108050038785
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json
hash: df638c814efbce69
coverage: 0.769231
learned_at: 2026-10-20 00:01:54
nodes: [CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, SaveImage, Note, Note, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, JjkText, EmptyLatentImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1280, "sampler_name": "er_sde", "scheduler": "beta", "seed": 259755283972668, "steps": 40, "width": 960}
---

# 图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `Note`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `259755283972668`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `960`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（10/13）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
