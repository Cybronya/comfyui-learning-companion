---
key: 图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json
name: wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json
hash: bc5e65a10ca2d964
coverage: 0.952381
learned_at: 2026-10-15 22:27:58
nodes: [MathExpression|pysssss, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, INTConstant, EmptyHunyuanLatentVideo, easy cleanGpuUsed, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, CreateVideo, KSamplerAdvanced, Note, INTConstant, INTConstant, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生视频稳定版（wan2.2_14B_t2v）_1950957566572568577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `EmptyHunyuanLatentVideo`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `Note`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`MathExpression|pysssss`、`ModelSamplingSD3`、`CLIPTextEncode`、`INTConstant`、`EmptyHunyuanLatentVideo`、`easy cleanGpuUsed`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveVideo
