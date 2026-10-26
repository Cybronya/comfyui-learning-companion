---
key: 图片生成/图生图/MOSS图生图 Reference Image洗图 2K极速版Image Generates Ima_2114160836448182274.json
name: MOSS图生图 Reference Image洗图 2K极速版Image Generates Ima_2114160836448182274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/MOSS图生图 Reference Image洗图 2K极速版Image Generates Ima_2114160836448182274.json
hash: f58de88c107265dd
coverage: 0.9375
learned_at: 2026-10-26 22:02:30
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPTextEncode, SaveImage, CLIPTextEncode, SaveImage, ResolutionSelector, EmptyFlux2LatentImage, KSampler, VAEDecode, PrimitiveStringMultiline, ImageConcatMulti, TextGenerate, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1.5, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 7949975849085, "steps": 10}
---

# 图片生成/图生图/MOSS图生图 Reference Image洗图 2K极速版Image Generates Ima_2114160836448182274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/MOSS图生图 Reference Image洗图 2K极速版Image Generates Ima_2114160836448182274.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ResolutionSelector`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `ImageConcatMulti`
- `TextGenerate`
- `LoadImage`

## 关键参数

- `seed` = `7949975849085`
- `steps` = `10`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`SaveImage`、`ResolutionSelector`、`EmptyFlux2LatentImage`、`KSampler`、`VAEDecode`、`ImageConcatMulti`、`TextGenerate`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector
