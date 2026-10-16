---
key: 视频生成/图生视频/wan2.2 图生视频  wan22 图生视频_2047937613306269697.json
name: wan2.2 图生视频  wan22 图生视频_2047937613306269697.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047937613306269697.json
hash: 0e8bc72c21acdc2f
coverage: 0.896552
learned_at: 2026-10-15 22:37:07
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, CLIPLoader, CreateVideo, VAEDecode, VAELoader, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, LoadImage, CR Text, RH_LLMAPI_NODE, ShowText|pysssss, PrimitiveFloat, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, INTConstant, Bjornulf_ShowInt, INTConstant, MathExpression|pysssss, CFGZeroStar, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, SaveVideo]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 图生视频  wan22 图生视频_2047937613306269697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047937613306269697.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CreateVideo`
- `VAEDecode` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoadImage`
- `CR Text`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `PrimitiveFloat`
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `INTConstant`
- `Bjornulf_ShowInt`
- `INTConstant`
- `MathExpression|pysssss`
- `CFGZeroStar`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `SaveVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`easy cleanGpuUsed`、`UNETLoader`、`CLIPLoader`、`CreateVideo`、`VAEDecode`、`VAELoader`、`KSamplerAdvanced`、`ModelSamplingSD3`、`LoadImage`、`CR Text`、`RH_LLMAPI_NODE`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`Bjornulf_ShowInt`、`MathExpression|pysssss`、`CFGZeroStar`、`CLIPTextEncode`、`WanImageToVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
