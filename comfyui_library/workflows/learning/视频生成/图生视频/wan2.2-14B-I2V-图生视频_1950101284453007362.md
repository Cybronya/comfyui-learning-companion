---
key: 视频生成/图生视频/wan2.2-14B-I2V-图生视频_1950101284453007362.json
name: wan2.2-14B-I2V-图生视频_1950101284453007362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950101284453007362.json
hash: aa9da88a77d87fef
coverage: 0.869565
learned_at: 2026-10-15 22:30:52
nodes: [KSamplerAdvanced, ModelSamplingSD3, UNETLoader, UNETLoader, ModelSamplingSD3, KSamplerAdvanced, VAEDecode, CreateVideo, JjkText, LoadImage, DF_Integer, DF_Integer, CLIPLoader, CLIPTextEncode, CLIPTextEncode, VAELoader, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, WanImageToVideo, PreviewImage, PreviewImage, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2-14B-I2V-图生视频_1950101284453007362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950101284453007362.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `JjkText`
- `LoadImage`
- `DF_Integer`
- `DF_Integer`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `WanImageToVideo`
- `PreviewImage`
- `PreviewImage`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`KSamplerAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`VAEDecode`、`CreateVideo`、`LoadImage`、`DF_Integer`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`WanImageToVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
