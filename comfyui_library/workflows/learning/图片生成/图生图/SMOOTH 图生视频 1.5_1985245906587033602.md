---
key: 图片生成/图生图/SMOOTH 图生视频 1.5_1985245906587033602.json
name: SMOOTH 图生视频 1.5_1985245906587033602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SMOOTH 图生视频 1.5_1985245906587033602.json
hash: c3c395e734b744d8
coverage: 0.921053
learned_at: 2026-10-23 11:24:03
nodes: [Note, UNETLoader, ModelSamplingSD3, UNETLoader, ModelSamplingSD3, VAELoader, WanImageToVideo, CLIPLoader, CLIPTextEncode, CLIPTextEncode, StringConcatenate, JjkText, CLIPVisionLoader, CLIPVisionEncode, VAEDecode, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, JWInteger, KSamplerAdvanced, KSamplerAdvanced, LoadImage, ImageScaleBy, SimpleMath+, SimpleMath+, SimpleMath+, PrimitiveStringMultiline, Primitive integer [Crystools], Primitive integer [Crystools], LoadImage, CR Prompt Text, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 图片生成/图生图/SMOOTH 图生视频 1.5_1985245906587033602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SMOOTH 图生视频 1.5_1985245906587033602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `Note`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `WanImageToVideo`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `StringConcatenate`
- `JjkText`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `ImageScaleBy`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `PrimitiveStringMultiline`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `LoadImage`
- `CR Prompt Text`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`WanImageToVideo`、`CLIPLoader`、`CLIPTextEncode`、`StringConcatenate`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VAEDecode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`JWInteger`、`KSamplerAdvanced`、`LoadImage`、`ImageScaleBy`、`SimpleMath+`、`Primitive integer [Crystools]`、`CR Prompt Text`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
