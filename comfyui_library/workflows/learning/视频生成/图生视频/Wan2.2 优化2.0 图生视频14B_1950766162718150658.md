---
key: 视频生成/图生视频/Wan2.2 优化2.0 图生视频14B_1950766162718150658.json
name: Wan2.2 优化2.0 图生视频14B_1950766162718150658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950766162718150658.json
hash: b0c61d94a766b688
coverage: 0.9
learned_at: 2026-10-15 22:30:56
nodes: [KSamplerAdvanced, CLIPTextEncode, UNETLoader, UNETLoader, CLIPLoader, VAELoader, MarkdownNote, VAEDecode, SaveVideo, PrimitiveInt, MathExpression|pysssss, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, WanImageToVideo, GetImageSizeAndCount, ConstrainImage|pysssss, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2 优化2.0 图生视频14B_1950766162718150658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950766162718150658.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveVideo`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `WanImageToVideo`
- `GetImageSizeAndCount`
- `ConstrainImage|pysssss`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`KSamplerAdvanced`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveVideo`、`MathExpression|pysssss`、`ModelSamplingSD3`、`CreateVideo`、`WanImageToVideo`、`GetImageSizeAndCount`、`ConstrainImage|pysssss`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、GetImageSizeAndCount
