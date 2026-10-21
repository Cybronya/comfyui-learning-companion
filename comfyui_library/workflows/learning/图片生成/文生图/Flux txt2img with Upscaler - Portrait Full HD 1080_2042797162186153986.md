---
key: 图片生成/文生图/Flux txt2img with Upscaler - Portrait Full HD 1080_2042797162186153986.json
name: Flux txt2img with Upscaler - Portrait Full HD 1080_2042797162186153986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux txt2img with Upscaler - Portrait Full HD 1080_2042797162186153986.json
hash: f9d99d79c757c52f
coverage: 0.888889
learned_at: 2026-10-21 02:52:04
nodes: [CLIPTextEncode, ImageScaleBy, ImageUpscaleWithModel, VAEEncode, UpscaleModelLoader, VAELoader, CLIPTextEncode, DualCLIPLoaderGGUF, FluxGuidance, Label (rgthree), EmptySD3LatentImage, easy cleanGpuUsed, easy cleanGpuUsed, TiledDiffusion, Label (rgthree), KSampler, VAEDecode, ImageScale, MarkdownNote, Label (rgthree), Label (rgthree), MarkdownNote, UnetLoaderGGUF, KSampler, Fast Groups Muter (rgthree), SaveImage, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 450424831808967, "steps": 20}
---

# 图片生成/文生图/Flux txt2img with Upscaler - Portrait Full HD 1080_2042797162186153986.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux txt2img with Upscaler - Portrait Full HD 1080_2042797162186153986.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `DualCLIPLoaderGGUF`
- `FluxGuidance`
- `Label (rgthree)`
- `EmptySD3LatentImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `TiledDiffusion`
- `Label (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScale`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `450424831808967`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPTextEncode`、`ImageScaleBy`、`ImageUpscaleWithModel`、`VAEEncode`、`UpscaleModelLoader`、`VAELoader`、`DualCLIPLoaderGGUF`、`FluxGuidance`、`Label (rgthree)`、`EmptySD3LatentImage`、`easy cleanGpuUsed`、`TiledDiffusion`、`KSampler`、`VAEDecode`、`ImageScale`、`UnetLoaderGGUF`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、FluxGuidance、VAEEncode、ImageUpscaleWithModel、UpscaleModelLoader
