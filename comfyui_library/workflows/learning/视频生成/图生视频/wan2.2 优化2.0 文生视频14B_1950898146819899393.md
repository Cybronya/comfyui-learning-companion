---
key: 视频生成/图生视频/wan2.2 优化2.0 文生视频14B_1950898146819899393.json
name: wan2.2 优化2.0 文生视频14B_1950898146819899393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950898146819899393.json
hash: 5e57742fb66a69ce
coverage: 0.947368
learned_at: 2026-10-15 22:30:57
nodes: [CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, SaveVideo, KSamplerAdvanced, VAEDecode, CreateVideo, CLIPTextEncode, KSamplerAdvanced, UNETLoader, VAELoader, CLIPLoader, UNETLoader, Int, MarkdownNote, Int, Int, MathExpression|pysssss, EmptyHunyuanLatentVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 优化2.0 文生视频14B_1950898146819899393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950898146819899393.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Int`
- `MarkdownNote`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`SaveVideo`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`Int`、`MathExpression|pysssss`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、SaveVideo
