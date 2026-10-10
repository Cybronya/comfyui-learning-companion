---
key: Wan2.2文生图_1951193822992773122.json
name: Wan2.2文生图_1951193822992773122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1951193822992773122.json
hash: e201e19b7bc847b4
coverage: 0.941176
learned_at: 2026-10-10 20:59:14
nodes: [LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, CLIPLoader, SaveImage, KSamplerAdvanced, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, SaveAnimatedWEBP]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# Wan2.2文生图_1951193822992773122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1951193822992773122.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveAnimatedWEBP`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`KSamplerAdvanced`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`SaveAnimatedWEBP`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
