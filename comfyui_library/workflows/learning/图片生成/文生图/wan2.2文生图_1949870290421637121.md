---
key: 图片生成/文生图/wan2.2文生图_1949870290421637121.json
name: wan2.2文生图_1949870290421637121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图_1949870290421637121.json
hash: cb7fce091167ccf8
coverage: 1
learned_at: 2026-10-15 22:27:58
nodes: [EmptyHunyuanLatentVideo, CLIPLoader, CR Text, UNETLoader, UNETLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, LoraLoaderModelOnly, EsesImageEffectBloom, BetterFilmGrain, EsesImageEffectBloom, ImageSharpen, BetterFilmGrain, CR Text, CLIPTextEncode, VAEDecode, VAEDecode, ImageSharpen, CR SDXL Aspect Ratio, LoraLoaderModelOnly, SaveImage, KSampler, SaveImage, LoraLoaderModelOnly, KSampler, KSampler, ModelSamplingSD3, PathchSageAttentionKJ]
patterns: []
missing: []
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 340989550490486, "steps": 10}
---

# 图片生成/文生图/wan2.2文生图_1949870290421637121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图_1949870290421637121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `CR Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `EsesImageEffectBloom`
- `ImageSharpen`
- `BetterFilmGrain`
- `CR Text`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageSharpen`
- `CR SDXL Aspect Ratio`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`

## 关键参数

- `seed` = `340989550490486`
- `steps` = `10`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`EmptyHunyuanLatentVideo`、`CLIPLoader`、`CR Text`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`EsesImageEffectBloom`、`BetterFilmGrain`、`ImageSharpen`、`VAEDecode`、`CR SDXL Aspect Ratio`、`SaveImage`、`KSampler`、`PathchSageAttentionKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyHunyuanLatentVideo
