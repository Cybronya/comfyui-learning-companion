---
key: 视频生成/图生视频/wan2.2无限首尾帧_2015253596383748097.json
name: wan2.2无限首尾帧_2015253596383748097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2015253596383748097.json
hash: 0ee347523cec71aa
coverage: 0.890909
learned_at: 2026-10-15 22:34:38
nodes: [ModelSamplingSD3, ModelSamplingSD3, WanFirstLastFrameToVideo, Int, MathExpression|pysssss, CLIPTextEncode, LoraLoaderModelOnly, Int, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, Int, VAELoader, ImageBatchMulti, KSamplerAdvanced, RH_LLMAPI_NODE, UNETLoader, UNETLoader, UNETLoader, UNETLoader, SimpleMath+, ImageFromBatch, CLIPLoader, easy showAnything, CM_IntToFloat, PreviewImage, MathExpression|pysssss, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSamplerAdvanced, easy showAnything, Int, Int, easy batchAnything, VHS_VideoCombine, easy forLoopEnd, VHS_VideoCombine, PreviewImage, ImageFromBatch, easy showAnything, ImageBatchMulti, SimpleMath+, PreviewImage, easy forLoopStart, CR Text, ImageBatchMulti]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2无限首尾帧_2015253596383748097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2015253596383748097.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanFirstLastFrameToVideo`
- `Int`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Int`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Int`
- `VAELoader`
- `ImageBatchMulti`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SimpleMath+`
- `ImageFromBatch`
- `CLIPLoader`
- `easy showAnything`
- `CM_IntToFloat`
- `PreviewImage`
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `Int`
- `Int`
- `easy batchAnything`
- `VHS_VideoCombine`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `PreviewImage`
- `ImageFromBatch`
- `easy showAnything`
- `ImageBatchMulti`
- `SimpleMath+`
- `PreviewImage`
- `easy forLoopStart`
- `CR Text`
- `ImageBatchMulti`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（49/55）

**有卡**：`ModelSamplingSD3`、`WanFirstLastFrameToVideo`、`Int`、`MathExpression|pysssss`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAEDecode`、`VAELoader`、`ImageBatchMulti`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`UNETLoader`、`SimpleMath+`、`ImageFromBatch`、`CLIPLoader`、`CM_IntToFloat`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`easy batchAnything`、`VHS_VideoCombine`、`easy forLoopEnd`、`easy forLoopStart`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
