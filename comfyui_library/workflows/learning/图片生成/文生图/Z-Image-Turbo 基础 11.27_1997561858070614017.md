---
key: 图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json
name: Z-Image-Turbo 基础 11.27_1997561858070614017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json
hash: 4692f1377e7c2517
coverage: 0.909091
learned_at: 2026-10-19 21:47:01
nodes: [UpscaleModelLoader, CLIPTextEncode, VAEDecode, EmptyLatentImage, KSampler, UnetLoaderGGUF, CLIPLoader, VAELoader, PrimitiveNode, ImageUpscaleWithModel, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "dpmpp_2m_sde", "scheduler": "beta57", "seed": 123321123321, "steps": 8, "width": 832}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo 基础 11.27_1997561858070614017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `ImageUpscaleWithModel`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `832`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `123321123321`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m_sde`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`UpscaleModelLoader`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`KSampler`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`ImageUpscaleWithModel`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ImageUpscaleWithModel、UpscaleModelLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
