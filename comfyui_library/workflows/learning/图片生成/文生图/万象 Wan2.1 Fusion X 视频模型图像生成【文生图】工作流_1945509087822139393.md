---
key: 图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json
name: 万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json
hash: d28da2af050a2775
coverage: 0.673913
learned_at: 2026-10-10 20:59:33
nodes: [EmptySD3LatentImage, GetNode, GetNode, KSamplerSelect, BasicScheduler, CFGGuider, SamplerCustomAdvanced, SaveImage, CLIPTextEncode, SetNode, SetNode, DualCLIPLoader, GetNode, VAELoader, VAEDecode, ImageSharpen, BetterFilmGrain, SaveImage, GetNode, KSampler, VAEEncode, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Image Comparer (rgthree), easy cleanGpuUsed, ModelSamplingSD3, easy clearCacheAll, easy cleanGpuUsed, VAEDecode, SetNode, VAELoader, FluxGuidance, CLIPTextEncode, CLIPLoader, GetNode, EsesImageEffectBloom, LoraLoaderModelOnly, UNETLoader, SetNode, CLIPTextEncode, GeminiFLUXResolutions, RandomNoise, CR Text]
patterns: []
missing: [CR Text, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1061465765857073, "steps": 10}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json`

## 结构

**节点**（46 个）：
- `EmptySD3LatentImage`
- `GetNode`
- `GetNode`
- `KSamplerSelect`
- `BasicScheduler`
- `CFGGuider`
- `SamplerCustomAdvanced`
- `SaveImage`
- `CLIPTextEncode`
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `GetNode`
- `VAELoader`
- `VAEDecode`
- `ImageSharpen`
- `BetterFilmGrain`
- `SaveImage`
- `GetNode`
- `KSampler`
- `VAEEncode`
- `CLIPTextEncode`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `Note`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `VAEDecode`
- `SetNode`
- `VAELoader`
- `FluxGuidance`
- `CLIPTextEncode`
- `CLIPLoader`
- `GetNode`
- `EsesImageEffectBloom`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `SetNode`
- `CLIPTextEncode`
- `GeminiFLUXResolutions`
- `RandomNoise`
- `CR Text`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.20000000000000004`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `1061465765857073`
- `steps` = `10`

## 知识

覆盖率 **67%**（31/46）

**有卡**：`EmptySD3LatentImage`、`GetNode`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`SaveImage`、`CLIPTextEncode`、`SetNode`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`ImageSharpen`、`BetterFilmGrain`、`KSampler`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`Note`、`Image Comparer (rgthree)`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`easy clearCacheAll`

**缺卡**（4）：`CR Text`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
