---
key: Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602.json
name: Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602.json
hash: 6d81dfeee32e8fa9
coverage: 0.875
learned_at: 2026-10-10 21:26:09
nodes: [RandomNoise, EmptySD3LatentImage, PrimitiveNode, PrimitiveNode, KSamplerSelect, ModelSamplingFlux, BasicScheduler, VAELoader, easy cleanGpuUsed, CLIPTextEncode, SamplerCustomAdvanced, FluxGuidance, BasicGuider, CLIPTextEncode, ModelSamplingSD3, LoraLoaderModelOnly, UpscaleModelLoader, PreviewImage, LoraLoaderModelOnly, VAEEncode, ImageScaleToMegapixels, CLIPTextEncode, ImageScaleToMegapixels, VAEDecode, ImageStitch, VAEDecode, KSampler, EsesImageEffectBloom, BetterFilmGrain, PreviewImage, VAELoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, DualCLIPLoader, SaveImage, ImageSharpen, SaveImage, Text]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 1, "denoise": 0.1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1038, "steps": 10}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `RandomNoise`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `KSamplerSelect` ★核心
- `ModelSamplingFlux`
- `BasicScheduler`
- `VAELoader`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `ImageScaleToMegapixels`
- `CLIPTextEncode` ★核心
- `ImageScaleToMegapixels`
- `VAEDecode` ★核心
- `ImageStitch`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `PreviewImage`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SaveImage`
- `ImageSharpen`
- `SaveImage`
- `Text`

## 关键参数

- `seed` = `1038`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.1`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`RandomNoise`、`EmptySD3LatentImage`、`KSamplerSelect`、`ModelSamplingFlux`、`BasicScheduler`、`VAELoader`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`FluxGuidance`、`BasicGuider`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`VAEEncode`、`ImageScaleToMegapixels`、`VAEDecode`、`ImageStitch`、`KSampler`、`EsesImageEffectBloom`、`BetterFilmGrain`、`UNETLoader`、`CLIPLoader`、`DualCLIPLoader`、`SaveImage`、`ImageSharpen`、`Text`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
