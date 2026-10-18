---
key: 视频生成/文生视频/万相 Wan2.2 14B文生视频工作流_1949831170026594305.json
name: 万相 Wan2.2 14B文生视频工作流_1949831170026594305.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/万相 Wan2.2 14B文生视频工作流_1949831170026594305.json
hash: ed98e81c6ed99812
coverage: 1
learned_at: 2026-10-15 22:43:33
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, EmptyHunyuanLatentVideo, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, ModelSamplingSD3, CR Text, CLIPTextEncode, VHS_VideoCombine, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/万相 Wan2.2 14B文生视频工作流_1949831170026594305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949831170026594305.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `CR Text`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`VAEDecode`、`CR Text`、`VHS_VideoCombine`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3
