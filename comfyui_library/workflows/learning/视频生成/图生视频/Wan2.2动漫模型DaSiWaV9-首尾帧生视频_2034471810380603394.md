---
key: 视频生成/图生视频/Wan2.2动漫模型DaSiWaV9-首尾帧生视频_2034471810380603394.json
name: Wan2.2动漫模型DaSiWaV9-首尾帧生视频_2034471810380603394.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2动漫模型DaSiWaV9-首尾帧生视频_2034471810380603394.json
hash: f8c54a89a6343931
coverage: 0.897436
learned_at: 2026-10-15 22:35:44
nodes: [CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, CLIPLoader, MathExpression|pysssss, LoadImage, Text, CR Text, LoadImage, CLIPTextEncode, CLIPVisionLoader, RHHiddenNodes, LayerUtility: ImageMaskScaleAs, easy imageConcat, LoadImage, ImageResizeKJv2, PreviewImage, Text, PreviewAny, LoadImage, CR Text Concatenate, CR Text Replace, WanFirstLastFrameToVideo, Reroute, Reroute, CLIPVisionEncode, CLIPVisionEncode, VAELoader, VAEDecode, Int, Int, Int, Int, IntToString, Qwen3_VQA_Plus, RIFE VFI, easy int, VHS_VideoCombine, MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2动漫模型DaSiWaV9-首尾帧生视频_2034471810380603394.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034471810380603394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `MathExpression|pysssss`
- `LoadImage`
- `Text`
- `CR Text`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `RHHiddenNodes`
- `LayerUtility: ImageMaskScaleAs`
- `easy imageConcat`
- `LoadImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `Text`
- `PreviewAny`
- `LoadImage`
- `CR Text Concatenate`
- `CR Text Replace`
- `WanFirstLastFrameToVideo`
- `Reroute`
- `Reroute`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAELoader`
- `VAEDecode` ★核心
- `Int`
- `Int`
- `Int`
- `Int`
- `IntToString`
- `Qwen3_VQA_Plus`
- `RIFE VFI`
- `easy int`
- `VHS_VideoCombine`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（35/39）

**有卡**：`CLIPTextEncode`、`KSamplerAdvanced`、`CLIPLoader`、`MathExpression|pysssss`、`LoadImage`、`Text`、`CR Text`、`CLIPVisionLoader`、`RHHiddenNodes`、`LayerUtility: ImageMaskScaleAs`、`easy imageConcat`、`ImageResizeKJv2`、`CR Text Concatenate`、`CR Text Replace`、`WanFirstLastFrameToVideo`、`CLIPVisionEncode`、`VAELoader`、`VAEDecode`、`Int`、`IntToString`、`Qwen3_VQA_Plus`、`RIFE VFI`、`easy int`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CLIPVisionEncode、CLIPVisionLoader
