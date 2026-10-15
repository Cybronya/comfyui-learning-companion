---
key: 图片生成/文生图/Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602.json
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

# 图片生成/文生图/Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Aiwood-SRPO+Wan2.2LN模型美学+质感兼得_1966814186120601602.json`

## 结构

**节点**（40 个）：
- `RandomNoise`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `BasicScheduler`
- `VAELoader`
- `easy cleanGpuUsed`
- `CLIPTextEncode`
- `SamplerCustomAdvanced`
- `FluxGuidance`
- `BasicGuider`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `UpscaleModelLoader`
- `PreviewImage`
- `LoraLoaderModelOnly`
- `VAEEncode`
- `ImageScaleToMegapixels`
- `CLIPTextEncode`
- `ImageScaleToMegapixels`
- `VAEDecode`
- `ImageStitch`
- `VAEDecode`
- `KSampler`
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `PreviewImage`
- `VAELoader`
- `UNETLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `DualCLIPLoader`
- `SaveImage`
- `ImageSharpen`
- `SaveImage`
- `Text`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `1038`
- `steps` = `10`

## 知识

覆盖率 **88%**（35/40）

**有卡**：`RandomNoise`、`EmptySD3LatentImage`、`PrimitiveNode`、`KSamplerSelect`、`ModelSamplingFlux`、`BasicScheduler`、`VAELoader`、`easy cleanGpuUsed`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`FluxGuidance`、`BasicGuider`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`PreviewImage`、`VAEEncode`、`ImageScaleToMegapixels`、`VAEDecode`、`ImageStitch`、`KSampler`、`EsesImageEffectBloom`、`BetterFilmGrain`、`UNETLoader`、`CLIPLoader`

**缺卡**（1）：`easy cleanGpuUsed`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
