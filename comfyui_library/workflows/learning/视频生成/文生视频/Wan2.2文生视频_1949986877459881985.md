---
key: 视频生成/文生视频/Wan2.2文生视频_1949986877459881985.json
name: Wan2.2文生视频_1949986877459881985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949986877459881985.json
hash: 47d075542de0c6d0
coverage: 1
learned_at: 2026-10-15 22:43:33
nodes: [CreateVideo, UNETLoader, Primitive integer [Crystools], MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools], ModelSamplingSD3, KSamplerAdvanced, UNETLoader, ModelSamplingSD3, KSamplerAdvanced, VAELoader, VAEDecode, SaveVideo, EmptyHunyuanLatentVideo, CLIPLoader, CLIPTextEncode, CLIPTextEncode, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2文生视频_1949986877459881985.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949986877459881985.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CreateVideo`
- `UNETLoader` ★核心
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveVideo`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`CreateVideo`、`UNETLoader`、`Primitive integer [Crystools]`、`MathExpression|pysssss`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAELoader`、`VAEDecode`、`SaveVideo`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`CLIPTextEncode`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveVideo
