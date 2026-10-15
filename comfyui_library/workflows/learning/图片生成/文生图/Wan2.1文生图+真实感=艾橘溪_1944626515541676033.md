---
key: 图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json
name: Wan2.1文生图+真实感=艾橘溪_1944626515541676033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json
hash: db17880c2a8a49a4
coverage: 0.866667
learned_at: 2026-10-10 20:59:13
nodes: [Note, Int, Int, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, VAEDecode, easy cleanGpuUsed, KSampler, CLIPTextEncode, SaveImage]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 952511070311462, "steps": 12}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json`

## 结构

**节点**（15 个）：
- `Note`
- `Int`
- `Int`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `VAEDecode`
- `easy cleanGpuUsed`
- `KSampler`
- `CLIPTextEncode`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `952511070311462`
- `steps` = `12`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`Note`、`Int`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`VAEDecode`、`easy cleanGpuUsed`、`KSampler`

**缺卡**（1）：`easy cleanGpuUsed`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
