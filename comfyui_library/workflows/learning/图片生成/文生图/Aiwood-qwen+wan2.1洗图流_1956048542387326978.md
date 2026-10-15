---
key: 图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json
name: Aiwood-qwen+wan2.1洗图流_1956048542387326978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json
hash: 9dc5a706121c4614
coverage: 0.846154
learned_at: 2026-10-15 22:26:12
nodes: [CLIPTextEncode, VAEEncode, VAEDecode, ModelSamplingSD3, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, easy showAnything, PreviewImage, ImageSharpen, BetterFilmGrain, Text Multiline, UpscaleModelLoader, EsesImageEffectBloom, BetterFilmGrain, Note, VAEDecode, LoraLoaderModelOnly, KSampler, EmptySD3LatentImage, Image Comparer (rgthree), PreviewImage, KSampler, Text Multiline, PreviewImage, easy promptConcat, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleToMegapixels, UNETLoader, VAELoader, CLIPLoader, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 333, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `PreviewImage`
- `ImageSharpen`
- `BetterFilmGrain`
- `Text Multiline`
- `UpscaleModelLoader`
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `Note`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `Text Multiline`
- `PreviewImage`
- `easy promptConcat`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToMegapixels`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `SaveImage`

## 关键参数

- `seed` = `333`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`ModelSamplingSD3`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`ImageSharpen`、`BetterFilmGrain`、`Text Multiline`、`UpscaleModelLoader`、`EsesImageEffectBloom`、`LoraLoaderModelOnly`、`KSampler`、`EmptySD3LatentImage`、`easy promptConcat`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToMegapixels`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
