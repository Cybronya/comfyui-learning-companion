---
key: 视频生成/图生视频/图生视频 wan2.2 图生视频 最新稳定版_2047204612649783298.json
name: 图生视频 wan2.2 图生视频 最新稳定版_2047204612649783298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 wan2.2 图生视频 最新稳定版_2047204612649783298.json
hash: 507b065a6e54a7f4
coverage: 0.896552
learned_at: 2026-10-15 22:37:04
nodes: [PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, PreviewImage, INTConstant, PrimitiveFloat, MathExpression|pysssss, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, VAEDecode, KSamplerAdvanced, LoadImage, INTConstant, CR Text, RH_LLMAPI_NODE, ShowText|pysssss, Bjornulf_ShowInt, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频 wan2.2 图生视频 最新稳定版_2047204612649783298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047204612649783298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PreviewImage`
- `INTConstant`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `INTConstant`
- `CR Text`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `Bjornulf_ShowInt`
- `SaveVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`INTConstant`、`MathExpression|pysssss`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CFGZeroStar`、`WanImageToVideo`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`LoadImage`、`CR Text`、`RH_LLMAPI_NODE`、`Bjornulf_ShowInt`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
