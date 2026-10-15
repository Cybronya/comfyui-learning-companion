---
key: 图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json
name: Aiwood-qwen+wan2.1洗图流_1956048542387326978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json
hash: 9dc5a706121c4614
coverage: 0.769231
learned_at: 2026-10-10 21:26:10
nodes: [CLIPTextEncode, VAEEncode, VAEDecode, ModelSamplingSD3, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, easy showAnything, PreviewImage, ImageSharpen, BetterFilmGrain, Text Multiline, UpscaleModelLoader, EsesImageEffectBloom, BetterFilmGrain, Note, VAEDecode, LoraLoaderModelOnly, KSampler, EmptySD3LatentImage, Image Comparer (rgthree), PreviewImage, KSampler, Text Multiline, PreviewImage, easy promptConcat, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageScaleToMegapixels, UNETLoader, VAELoader, CLIPLoader, SaveImage]
patterns: []
missing: [Text Multiline, Text Multiline, easy promptConcat]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 333, "steps": 4}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Aiwood-qwen+wan2.1洗图流_1956048542387326978.json`

## 结构

**节点**（39 个）：
- `CLIPTextEncode`
- `VAEEncode`
- `VAEDecode`
- `ModelSamplingSD3`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `easy showAnything`
- `PreviewImage`
- `ImageSharpen`
- `BetterFilmGrain`
- `Text Multiline`
- `UpscaleModelLoader`
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `Note`
- `VAEDecode`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `KSampler`
- `Text Multiline`
- `PreviewImage`
- `easy promptConcat`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `ImageScaleToMegapixels`
- `UNETLoader`
- `VAELoader`
- `CLIPLoader`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `333`
- `steps` = `4`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`VAEDecode`、`ModelSamplingSD3`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`、`easy showAnything`、`PreviewImage`、`ImageSharpen`、`BetterFilmGrain`、`Text Multiline`、`UpscaleModelLoader`、`EsesImageEffectBloom`、`Note`、`LoraLoaderModelOnly`、`KSampler`、`EmptySD3LatentImage`、`Image Comparer (rgthree)`、`easy promptConcat`、`UNETLoader`、`CLIPLoader`

**缺卡**（3）：`Text Multiline`、`Text Multiline`、`easy promptConcat`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptConcat` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
