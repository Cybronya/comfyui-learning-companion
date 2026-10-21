---
key: 图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json
name: Wan2.2图片生成  文生图_2038151225899749378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json
hash: f6ec9b93d21ee83d
coverage: 1
learned_at: 2026-10-21 02:55:25
nodes: [LoraLoaderModelOnly, CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, SeedVR2BlockSwap, EmptyHunyuanLatentVideo, UNETLoader, SeedVR2, CLIPTextEncode, KSamplerAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2图片生成  文生图_2038151225899749378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SeedVR2BlockSwap`
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `SeedVR2`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`SeedVR2BlockSwap`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`SeedVR2`、`KSamplerAdvanced`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SeedVR2
