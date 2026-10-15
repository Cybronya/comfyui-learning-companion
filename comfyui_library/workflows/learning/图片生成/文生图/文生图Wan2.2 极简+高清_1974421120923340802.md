---
key: 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json
name: 文生图Wan2.2 极简+高清_1974421120923340802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json
hash: d2ac19672df4f3c6
coverage: 0.823529
learned_at: 2026-10-15 22:28:48
nodes: [VAELoader, EmptyHunyuanLatentVideo, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, easy cleanGpuUsed, Text, KSamplerAdvanced, VAEDecode, SaveImage, SeedVR2, Image Comparer (rgthree), Anything Everywhere3, LoraLoaderModelOnly, PreviewImage, SeedVR2BlockSwap]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图Wan2.2 极简+高清_1974421120923340802.json`

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

覆盖率 **82%**（14/17）

**有卡**：`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`easy cleanGpuUsed`、`Text`、`KSamplerAdvanced`、`VAEDecode`、`SaveImage`、`SeedVR2`、`LoraLoaderModelOnly`、`SeedVR2BlockSwap`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2
