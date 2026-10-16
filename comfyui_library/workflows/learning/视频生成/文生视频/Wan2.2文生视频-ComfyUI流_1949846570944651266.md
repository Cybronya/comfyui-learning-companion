---
key: 视频生成/文生视频/Wan2.2文生视频-ComfyUI流_1949846570944651266.json
name: Wan2.2文生视频-ComfyUI流_1949846570944651266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949846570944651266.json
hash: 72656a92e1057333
coverage: 0.904762
learned_at: 2026-10-15 22:43:33
nodes: [ModelSamplingSD3, KSamplerAdvanced, CreateVideo, SaveVideo, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, CLIPLoader, KSamplerAdvanced, VAEDecode, VAELoader, EmptyHunyuanLatentVideo, Primitive integer [Crystools], UNETLoader, UNETLoader, Primitive integer [Crystools], Note, Note, Text Multiline, Primitive integer [Crystools], MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2文生视频-ComfyUI流_1949846570944651266.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949846570944651266.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `SaveVideo`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `Primitive integer [Crystools]`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Primitive integer [Crystools]`
- `Note`
- `Note`
- `Text Multiline`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`SaveVideo`、`CLIPTextEncode`、`CLIPLoader`、`VAEDecode`、`VAELoader`、`EmptyHunyuanLatentVideo`、`Primitive integer [Crystools]`、`UNETLoader`、`Text Multiline`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveVideo
