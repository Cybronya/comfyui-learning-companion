---
key: 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1950015498596564993.json
name: wan2.2图生视频-ComfyUI官方_1950015498596564993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1950015498596564993.json
hash: 7eb605644713aef6
coverage: 1
learned_at: 2026-10-15 22:30:51
nodes: [ModelSamplingSD3, KSamplerAdvanced, UNETLoader, MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, LoadImage, ImageResizeKJv2, WanImageToVideo, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, CreateVideo, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频-ComfyUI官方_1950015498596564993.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950015498596564993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `LoadImage`
- `ImageResizeKJv2`
- `WanImageToVideo`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`UNETLoader`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`Text Multiline`、`LoadImage`、`ImageResizeKJv2`、`WanImageToVideo`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
