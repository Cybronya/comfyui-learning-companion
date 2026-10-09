---
key: 图片生成/文生图/wan2.2文生图工作流_1953829480836026370.json
name: wan2.2文生图工作流_1953829480836026370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图工作流_1953829480836026370.json
hash: ec1af5b27ac967a6
coverage: 1
learned_at: 2026-10-07 23:17:45
nodes: [VAELoader, UNETLoader, UNETLoader, CLIPLoader, KSamplerAdvanced, EmptyHunyuanLatentVideo, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/wan2.2文生图工作流_1953829480836026370.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1953829480836026370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveImage
