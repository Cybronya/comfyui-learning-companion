---
key: 图片生成/文生图/wan2.2文生图_1949870290421637121.json
name: wan2.2文生图_1949870290421637121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图_1949870290421637121.json
hash: cb7fce091167ccf8
coverage: 0.896552
learned_at: 2026-10-10 20:59:27
nodes: [EmptyHunyuanLatentVideo, CLIPLoader, CR Text, UNETLoader, UNETLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, LoraLoaderModelOnly, EsesImageEffectBloom, BetterFilmGrain, EsesImageEffectBloom, ImageSharpen, BetterFilmGrain, CR Text, CLIPTextEncode, VAEDecode, VAEDecode, ImageSharpen, CR SDXL Aspect Ratio, LoraLoaderModelOnly, SaveImage, KSampler, SaveImage, LoraLoaderModelOnly, KSampler, KSampler, ModelSamplingSD3, PathchSageAttentionKJ]
patterns: []
missing: [CR Text, CR Text, CR SDXL Aspect Ratio]
parameters: {"cfg": 3.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 340989550490486, "steps": 10}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/wan2.2文生图_1949870290421637121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图_1949870290421637121.json`

## 结构

**节点**（29 个）：
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `CR Text`
- `UNETLoader`
- `UNETLoader`
- `VAELoader`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `EsesImageEffectBloom`
- `ImageSharpen`
- `BetterFilmGrain`
- `CR Text`
- `CLIPTextEncode`
- `VAEDecode`
- `VAEDecode`
- `ImageSharpen`
- `CR SDXL Aspect Ratio`
- `LoraLoaderModelOnly`
- `SaveImage`
- `KSampler`
- `SaveImage`
- `LoraLoaderModelOnly`
- `KSampler`
- `KSampler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`

## 关键参数

- `cfg` = `3.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `340989550490486`
- `steps` = `10`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`EmptyHunyuanLatentVideo`、`CLIPLoader`、`CR Text`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`EsesImageEffectBloom`、`BetterFilmGrain`、`ImageSharpen`、`VAEDecode`、`CR SDXL Aspect Ratio`、`SaveImage`、`KSampler`

**缺卡**（3）：`CR Text`、`CR Text`、`CR SDXL Aspect Ratio`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR SDXL Aspect Ratio` 仅有 Checkpoint 的通用知识，没有该节点自己的说明
