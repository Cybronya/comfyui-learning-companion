---
key: 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json
name: 文生图Wan2.2 极简+高清_1974421120923340802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json
hash: d2ac19672df4f3c6
coverage: 0.764706
learned_at: 2026-10-10 20:59:47
nodes: [VAELoader, EmptyHunyuanLatentVideo, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, easy cleanGpuUsed, Text, KSamplerAdvanced, VAEDecode, SaveImage, SeedVR2, Image Comparer (rgthree), Anything Everywhere3, LoraLoaderModelOnly, PreviewImage, SeedVR2BlockSwap]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json`

## 结构

**节点**（17 个）：
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `CLIPLoader`
- `UNETLoader`
- `easy cleanGpuUsed`
- `Text`
- `KSamplerAdvanced`
- `VAEDecode`
- `SaveImage`
- `SeedVR2`
- `Image Comparer (rgthree)`
- `Anything Everywhere3`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SeedVR2BlockSwap`

## 关键参数

- `cfg` = `8`
- `denoise` = `simple`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `seed` = `enable`
- `steps` = `fixed`

## 知识

覆盖率 **76%**（13/17）

**有卡**：`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`easy cleanGpuUsed`、`Text`、`KSamplerAdvanced`、`VAEDecode`、`SaveImage`、`SeedVR2`、`Image Comparer (rgthree)`

**缺卡**（1）：`easy cleanGpuUsed`

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
