---
key: Wan2.1 文生图美学去AI感_1950183203102441473.json
name: Wan2.1 文生图美学去AI感_1950183203102441473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json
hash: 0980f4247922a05e
coverage: 1
learned_at: 2026-10-10 20:59:13
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAEDecode, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 352053746353821, "steps": 20}
---

# Wan2.1 文生图美学去AI感_1950183203102441473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.1 文生图美学去AI感_1950183203102441473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `SaveImage`

## 关键参数

- `seed` = `352053746353821`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo
