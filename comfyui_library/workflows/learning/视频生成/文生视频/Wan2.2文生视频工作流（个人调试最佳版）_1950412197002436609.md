---
key: 视频生成/文生视频/Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json
name: Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json
hash: f470388ce04cafb1
coverage: 1
learned_at: 2026-10-15 22:43:35
nodes: [CLIPTextEncode, CreateVideo, UNETLoader, UNETLoader, CLIPLoader, VAELoader, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, KSamplerAdvanced, SaveVideo, CLIPTextEncode, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2文生视频工作流（个人调试最佳版）_1950412197002436609.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950412197002436609.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPTextEncode`、`CreateVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`SaveVideo`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveVideo
