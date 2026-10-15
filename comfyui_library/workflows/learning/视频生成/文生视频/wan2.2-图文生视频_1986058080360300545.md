---
key: 视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json
name: wan2.2-图文生视频_1986058080360300545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json
hash: 7d7424df44ae609e
coverage: 1
learned_at: 2026-10-15 22:47:35
nodes: [UNETLoader, UNETLoader, CLIPLoader, WanImageToVideo, CLIPTextEncode, JWInteger, JWInteger, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, CLIPTextEncode, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, MathExpression|pysssss, CLIPVisionEncode, CLIPVisionLoader, Seed (rgthree), KSamplerAdvanced, CR Prompt Text, VAEDecode, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2-图文生视频_1986058080360300545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `JWInteger`
- `JWInteger`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `MathExpression|pysssss`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `CR Prompt Text`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`UNETLoader`、`CLIPLoader`、`WanImageToVideo`、`CLIPTextEncode`、`JWInteger`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`MathExpression|pysssss`、`CLIPVisionEncode`、`CLIPVisionLoader`、`Seed (rgthree)`、`CR Prompt Text`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
