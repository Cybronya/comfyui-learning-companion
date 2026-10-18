---
key: 视频生成/文生视频/Wan2.2文生视频-14B-T2V_1950032228946501633.json
name: Wan2.2文生视频-14B-T2V_1950032228946501633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频-14B-T2V_1950032228946501633.json
hash: 0be7fa5a545cd73e
coverage: 0.952381
learned_at: 2026-10-15 22:43:34
nodes: [ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, UNETLoader, DF_Integer, DF_Integer, DF_Integer, DF_Integer, ModelSamplingSD3, MathExpression|pysssss, EmptyHunyuanLatentVideo, VAEDecode, CreateVideo, SaveVideo, JjkText, CM_IntToFloat, CLIPLoader, VAELoader, UNETLoader, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2文生视频-14B-T2V_1950032228946501633.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950032228946501633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `DF_Integer`
- `DF_Integer`
- `DF_Integer`
- `DF_Integer`
- `ModelSamplingSD3`
- `MathExpression|pysssss`
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `JjkText`
- `CM_IntToFloat`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`KSamplerAdvanced`、`UNETLoader`、`DF_Integer`、`MathExpression|pysssss`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`CM_IntToFloat`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveVideo
