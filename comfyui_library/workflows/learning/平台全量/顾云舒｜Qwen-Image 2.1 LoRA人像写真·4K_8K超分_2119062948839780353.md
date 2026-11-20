---
key: 平台全量/顾云舒｜Qwen-Image 2.1 LoRA人像写真·4K_8K超分_2119062948839780353.json
name: 顾云舒｜Qwen-Image 2.1 LoRA人像写真·4K_8K超分_2119062948839780353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/顾云舒｜Qwen-Image 2.1 LoRA人像写真·4K_8K超分_2119062948839780353.json
hash: f9634330b11e8cb4
coverage: 0.888889
learned_at: 2026-11-14 02:50:41
nodes: [UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, QwenImage21Cache, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, SaveImage, Note, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleToMaxDimension, SaveImage, ImageScaleToMaxDimension, SaveImage, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 20261107, "steps": 40, "width": 1080}
---

# 平台全量/顾云舒｜Qwen-Image 2.1 LoRA人像写真·4K_8K超分_2119062948839780353.json

> 来源文件 `comfyui_library/workflows/平台全量/顾云舒｜Qwen-Image 2.1 LoRA人像写真·4K_8K超分_2119062948839780353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleToMaxDimension`
- `SaveImage`
- `ImageScaleToMaxDimension`
- `SaveImage`
- `Note`

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `20261107`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleToMaxDimension`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、QwenImage21Cache
