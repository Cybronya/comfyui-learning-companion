---
key: 图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json
name: SD1.5生图加高清放大_1901648928868343810
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json
hash: 73b8eead885eaa70
coverage: 1
learned_at: 2026-10-07 03:18:01
nodes: [KSampler, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, VAEEncode, EmptyLatentImage, CLIPTextEncode, CLIPTextEncode, KSampler, SaveImage, VAEDecode, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "超绝精美古风大模型 _v1.0.safetensors", "denoise": 0.75, "height": 768, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 477381964747527, "steps": 50, "width": 512}
---

# 图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5生图加高清放大_1901648928868343810.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output

**节点**（12 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `477381964747527`
- `steps` = `50`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.75`
- `width` = `512`
- `height` = `768`
- `batch_size` = `1`
- `checkpoint` = `超绝精美古风大模型 _v1.0.safetensors`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`KSampler`、`VAEDecode`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VAEEncode`、`EmptyLatentImage`、`CLIPTextEncode`、`SaveImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、VAEEncode、ImageUpscaleWithModel、UpscaleModelLoader
