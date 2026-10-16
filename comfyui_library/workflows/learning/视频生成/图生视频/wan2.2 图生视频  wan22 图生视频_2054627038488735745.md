---
key: 视频生成/图生视频/wan2.2 图生视频  wan22 图生视频_2054627038488735745.json
name: wan2.2 图生视频  wan22 图生视频_2054627038488735745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2054627038488735745.json
hash: e7c3cfbd7cadd725
coverage: 0.896552
learned_at: 2026-10-15 22:37:50
nodes: [easy cleanGpuUsed, UNETLoader, UNETLoader, CLIPLoader, CreateVideo, VAEDecode, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, PrimitiveFloat, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, Bjornulf_ShowInt, INTConstant, MathExpression|pysssss, CFGZeroStar, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, KSamplerAdvanced, SaveVideo, ShowText|pysssss, VAELoader, RH_LLMAPI_NODE, easy cleanGpuUsed, PreviewImage, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 图生视频  wan22 图生视频_2054627038488735745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054627038488735745.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PrimitiveFloat`
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `Bjornulf_ShowInt`
- `INTConstant`
- `MathExpression|pysssss`
- `CFGZeroStar`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `ShowText|pysssss`
- `VAELoader`
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `PreviewImage`
- `CR Text`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`easy cleanGpuUsed`、`UNETLoader`、`CLIPLoader`、`CreateVideo`、`VAEDecode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`Bjornulf_ShowInt`、`MathExpression|pysssss`、`CFGZeroStar`、`CLIPTextEncode`、`WanImageToVideo`、`SaveVideo`、`VAELoader`、`RH_LLMAPI_NODE`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
