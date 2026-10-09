---
key: 图片生成/文生图/Wan2.2文生图(低噪版)_1951900115835498497.json
name: Wan2.2文生图(低噪版)_1951900115835498497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图(低噪版)_1951900115835498497.json
hash: 38505e6b4630b98d
coverage: 0.882353
learned_at: 2026-10-07 23:04:28
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, CLIPLoader, easy clearCacheAll, easy cleanGpuUsed, FastFilmGrain, SaveImage, ModelSamplingSD3, WanVideoNAG, VAELoader, UNETLoader, CLIPTextEncode, SaveImage, EmptyHunyuanLatentVideo, KSampler, CLIPTextEncode]
patterns: []
missing: [easy cleanGpuUsed, easy clearCacheAll]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 655799065515777, "steps": 10}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.2文生图(低噪版)_1951900115835498497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1951900115835498497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `FastFilmGrain`
- `SaveImage`
- `ModelSamplingSD3`
- `WanVideoNAG`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `655799065515777`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`LoraLoaderModelOnly`、`VAEDecode`、`CLIPLoader`、`FastFilmGrain`、`SaveImage`、`ModelSamplingSD3`、`WanVideoNAG`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSampler`

**缺卡**（2）：`easy cleanGpuUsed`、`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
