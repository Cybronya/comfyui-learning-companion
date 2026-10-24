---
key: 图片生成/图生图/文生图（Flux+Wan2.1）国风美学优化_1958762603436728322.json
name: 文生图（Flux+Wan2.1）国风美学优化_1958762603436728322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/文生图（Flux+Wan2.1）国风美学优化_1958762603436728322.json
hash: a5cb83a86fa66caa
coverage: 0.911765
learned_at: 2026-10-23 13:03:48
nodes: [CLIPTextEncode, CLIPTextEncode, FluxGuidance, CLIPTextEncode, CLIPTextEncode, ImageSharpen, VAEEncode, ModelSamplingSD3, EsesImageEffectBloom, EmptySD3LatentImage, DualCLIPLoader, VAELoader, VAELoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, BetterFilmGrain, VAEDecode, easy cleanGpuUsed, PreviewImage, LoraLoaderModelOnly, KSampler, Text Multiline, KSampler, ImageConcanate, ImageScaleToMegapixels, Upscale Model Loader, VAEDecode, PreviewImage, SaveImage, PreviewImage, DeepTranslatorTextNode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1015, "steps": 10}
---

# 图片生成/图生图/文生图（Flux+Wan2.1）国风美学优化_1958762603436728322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/文生图（Flux+Wan2.1）国风美学优化_1958762603436728322.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageSharpen`
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `EsesImageEffectBloom`
- `EmptySD3LatentImage`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `BetterFilmGrain`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Text Multiline`
- `KSampler` ★核心
- `ImageConcanate`
- `ImageScaleToMegapixels`
- `Upscale Model Loader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `DeepTranslatorTextNode`

## 关键参数

- `seed` = `1015`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`CLIPTextEncode`、`FluxGuidance`、`ImageSharpen`、`VAEEncode`、`ModelSamplingSD3`、`EsesImageEffectBloom`、`EmptySD3LatentImage`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`BetterFilmGrain`、`VAEDecode`、`easy cleanGpuUsed`、`KSampler`、`Text Multiline`、`ImageConcanate`、`ImageScaleToMegapixels`、`Upscale Model Loader`、`SaveImage`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance
