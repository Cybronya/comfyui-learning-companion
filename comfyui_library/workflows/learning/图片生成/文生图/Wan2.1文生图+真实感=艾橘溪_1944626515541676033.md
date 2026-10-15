---
key: 图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json
name: Wan2.1文生图+真实感=艾橘溪_1944626515541676033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json
hash: db17880c2a8a49a4
coverage: 0.933333
learned_at: 2026-10-15 22:27:34
nodes: [Note, Int, Int, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, VAEDecode, easy cleanGpuUsed, KSampler, CLIPTextEncode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 952511070311462, "steps": 12}
---

# 图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `Note`
- `Int`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `952511070311462`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`Int`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`VAEDecode`、`easy cleanGpuUsed`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo
