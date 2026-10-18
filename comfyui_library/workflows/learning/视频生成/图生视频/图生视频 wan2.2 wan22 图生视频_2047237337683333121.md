---
key: 视频生成/图生视频/图生视频 wan2.2 wan22 图生视频_2047237337683333121.json
name: 图生视频 wan2.2 wan22 图生视频_2047237337683333121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 wan2.2 wan22 图生视频_2047237337683333121.json
hash: 7ccf14c04d26f747
coverage: 0.896552
learned_at: 2026-10-15 22:37:04
nodes: [PathchSageAttentionKJ, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, VAEDecode, VAELoader, ShowText|pysssss, MathExpression|pysssss, RH_LLMAPI_NODE, INTConstant, PrimitiveFloat, PreviewImage, SaveVideo, LoadImage, CR Text, INTConstant, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/图生视频 wan2.2 wan22 图生视频_2047237337683333121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047237337683333121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `Bjornulf_ShowInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAELoader`
- `ShowText|pysssss`
- `MathExpression|pysssss`
- `RH_LLMAPI_NODE`
- `INTConstant`
- `PrimitiveFloat`
- `PreviewImage`
- `SaveVideo`
- `LoadImage`
- `CR Text`
- `INTConstant`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`PathchSageAttentionKJ`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStar`、`WanImageToVideo`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`VAELoader`、`MathExpression|pysssss`、`RH_LLMAPI_NODE`、`INTConstant`、`SaveVideo`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
