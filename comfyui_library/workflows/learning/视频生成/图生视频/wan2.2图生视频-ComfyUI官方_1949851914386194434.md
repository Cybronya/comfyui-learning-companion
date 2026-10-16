---
key: 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1949851914386194434.json
name: wan2.2图生视频-ComfyUI官方_1949851914386194434.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949851914386194434.json
hash: 0d49fc7ce3620eee
coverage: 0.875
learned_at: 2026-10-15 22:30:50
nodes: [SaveVideo, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, WanImageToVideo, KSamplerAdvanced, VAEDecode, CreateVideo, KSamplerAdvanced, VAELoader, Primitive integer [Crystools], Primitive integer [Crystools], ImageResizeKJv2, UNETLoader, UNETLoader, Text Multiline, LoadImage, Note, Note, Note, Primitive integer [Crystools], MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1949851914386194434.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949851914386194434.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Text Multiline`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`SaveVideo`、`CLIPTextEncode`、`ModelSamplingSD3`、`CLIPLoader`、`WanImageToVideo`、`KSamplerAdvanced`、`VAEDecode`、`CreateVideo`、`VAELoader`、`Primitive integer [Crystools]`、`ImageResizeKJv2`、`UNETLoader`、`Text Multiline`、`LoadImage`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
