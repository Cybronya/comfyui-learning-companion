---
key: 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json
name: 文生图Wan2.2 极简+高清_1974421120923340802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json
hash: d2ac19672df4f3c6
coverage: 0.764706
learned_at: 2026-10-09 19:50:53
nodes: [VAELoader, EmptyHunyuanLatentVideo, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, easy cleanGpuUsed, Text, KSamplerAdvanced, VAEDecode, SaveImage, SeedVR2, Image Comparer (rgthree), Anything Everywhere3, LoraLoaderModelOnly, PreviewImage, SeedVR2BlockSwap]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1974421120923340802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `Text`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SeedVR2`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `SeedVR2BlockSwap`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`Text`、`KSamplerAdvanced`、`VAEDecode`、`SaveImage`、`SeedVR2`、`LoraLoaderModelOnly`、`SeedVR2BlockSwap`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
