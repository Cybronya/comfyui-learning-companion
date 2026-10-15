---
key: 图片生成/文生图/Wan2.2文生图(高低噪)_1951482093362688001.json
name: Wan2.2文生图(高低噪)_1951482093362688001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图(高低噪)_1951482093362688001.json
hash: fa6584249d3f562e
coverage: 0.904762
learned_at: 2026-10-10 20:59:14
nodes: [easy cleanGpuUsed, easy clearCacheAll, CLIPTextEncode, KSamplerAdvanced, UNETLoader, VAEDecode, CLIPLoader, VAELoader, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, KSamplerAdvanced, SaveImage, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, WanVideoNAG, SaveImage, FastFilmGrain]
patterns: []
missing: [easy cleanGpuUsed, easy clearCacheAll]
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2文生图(高低噪)_1951482093362688001.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图(高低噪)_1951482093362688001.json`

## 结构

**节点**（21 个）：
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `UNETLoader`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `KSamplerAdvanced`
- `SaveImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `WanVideoNAG`
- `SaveImage`
- `FastFilmGrain`

## 关键参数

- `cfg` = `10`
- `denoise` = `beta`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `seed` = `enable`
- `steps` = `fixed`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`easy cleanGpuUsed`、`easy clearCacheAll`、`CLIPTextEncode`、`KSamplerAdvanced`、`UNETLoader`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`、`SaveImage`、`ModelSamplingSD3`、`WanVideoNAG`

**缺卡**（2）：`easy cleanGpuUsed`、`easy clearCacheAll`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
