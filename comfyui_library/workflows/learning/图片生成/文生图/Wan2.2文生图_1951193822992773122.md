---
key: 图片生成/文生图/Wan2.2文生图_1951193822992773122.json
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

# 图片生成/文生图/Wan2.2文生图_1951193822992773122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图_1951193822992773122.json`

## 结构

**节点**（17 个）：
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `VAELoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader`
- `UNETLoader`
- `CLIPLoader`
- `SaveImage`
- `KSamplerAdvanced`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `VAEDecode`
- `easy cleanGpuUsed`
- `SaveAnimatedWEBP`

## 关键参数

- `cfg` = `20`
- `denoise` = `simple`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `seed` = `enable`
- `steps` = `randomize`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`LoraLoaderModelOnly`、`VAELoader`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`KSamplerAdvanced`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`easy cleanGpuUsed`

**缺卡**（1）：`easy cleanGpuUsed`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
