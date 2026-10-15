---
key: 图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json
name: 万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json
hash: d28da2af050a2775
coverage: 0.76087
learned_at: 2026-10-15 22:28:09
nodes: [EmptySD3LatentImage, GetNode, GetNode, KSamplerSelect, BasicScheduler, CFGGuider, SamplerCustomAdvanced, SaveImage, CLIPTextEncode, SetNode, SetNode, DualCLIPLoader, GetNode, VAELoader, VAEDecode, ImageSharpen, BetterFilmGrain, SaveImage, GetNode, KSampler, VAEEncode, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Image Comparer (rgthree), easy cleanGpuUsed, ModelSamplingSD3, easy clearCacheAll, easy cleanGpuUsed, VAEDecode, SetNode, VAELoader, FluxGuidance, CLIPTextEncode, CLIPLoader, GetNode, EsesImageEffectBloom, LoraLoaderModelOnly, UNETLoader, SetNode, CLIPTextEncode, GeminiFLUXResolutions, RandomNoise, CR Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1061465765857073, "steps": 10}
---

# 图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/万象 Wan2.1 Fusion X 视频模型图像生成【文生图】工作流_1945509087822139393.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `EmptySD3LatentImage`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `DualCLIPLoader`
- `GetNode`
- `VAELoader`
- `VAEDecode` ★核心
- `ImageSharpen`
- `BetterFilmGrain`
- `SaveImage`
- `GetNode`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SetNode`
- `VAELoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `GetNode`
- `EsesImageEffectBloom`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `GeminiFLUXResolutions`
- `RandomNoise`
- `CR Text`

## 关键参数

- `seed` = `1061465765857073`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **76%**（35/46）

**有卡**：`EmptySD3LatentImage`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`SaveImage`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`ImageSharpen`、`BetterFilmGrain`、`KSampler`、`VAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`easy clearCacheAll`、`FluxGuidance`、`CLIPLoader`、`EsesImageEffectBloom`、`GeminiFLUXResolutions`、`RandomNoise`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、CFGGuider
