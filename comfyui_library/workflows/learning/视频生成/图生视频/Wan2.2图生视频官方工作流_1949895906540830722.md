---
key: 视频生成/图生视频/Wan2.2图生视频官方工作流_1949895906540830722.json
name: Wan2.2图生视频官方工作流_1949895906540830722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949895906540830722.json
hash: 30d62146257bbdf2
coverage: 0.92
learned_at: 2026-10-15 22:30:50
nodes: [CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, UNETLoader, UNETLoader, LoadImage, Note, VAELoader, CLIPTextEncode, easy showAnything, MathExpression|pysssss, Int, Int, JWInteger, WanImageToVideo, ImageResizeKJv2, CLIPTextEncode, CreateVideo, SaveVideo, GetVideoComponents, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, VHS_VideoCombine, RH_Translator]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2图生视频官方工作流_1949895906540830722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949895906540830722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `Note`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `JWInteger`
- `WanImageToVideo`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `SaveVideo`
- `GetVideoComponents`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `RH_Translator`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`UNETLoader`、`LoadImage`、`VAELoader`、`CLIPTextEncode`、`MathExpression|pysssss`、`Int`、`JWInteger`、`WanImageToVideo`、`ImageResizeKJv2`、`CreateVideo`、`SaveVideo`、`GetVideoComponents`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageResizeKJv2
