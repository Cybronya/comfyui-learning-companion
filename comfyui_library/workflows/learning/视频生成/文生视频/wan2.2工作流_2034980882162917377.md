---
key: 视频生成/文生视频/wan2.2工作流_2034980882162917377.json
name: wan2.2工作流_2034980882162917377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2工作流_2034980882162917377.json
hash: 9c0ee925d2a20ae3
coverage: 1
learned_at: 2026-10-11 03:48:39
nodes: [CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, VAELoader, EmptyHunyuanLatentVideo, CLIPTextEncode, UNETLoader, UNETLoader, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/wan2.2工作流_2034980882162917377.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2工作流_2034980882162917377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`CLIPLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`KSamplerAdvanced`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
