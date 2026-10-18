---
key: 视频生成/图生视频/图生视频 wan2.2 图生视频_2048243390151659521.json
name: 图生视频 wan2.2 图生视频_2048243390151659521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 wan2.2 图生视频_2048243390151659521.json
hash: da878fb226985747
coverage: 0.896552
learned_at: 2026-10-15 22:37:08
nodes: [LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, CreateVideo, VAEDecode, KSamplerAdvanced, PreviewImage, SaveVideo, MathExpression|pysssss, Bjornulf_ShowInt, CR Text, UNETLoader, CLIPLoader, UNETLoader, PrimitiveFloat, INTConstant, INTConstant, VAELoader, LoadImage, ShowText|pysssss, RH_LLMAPI_NODE, PathchSageAttentionKJ, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/图生视频 wan2.2 图生视频_2048243390151659521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048243390151659521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PreviewImage`
- `SaveVideo`
- `MathExpression|pysssss`
- `Bjornulf_ShowInt`
- `CR Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `INTConstant`
- `INTConstant`
- `VAELoader`
- `LoadImage`
- `ShowText|pysssss`
- `RH_LLMAPI_NODE`
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`CLIPTextEncode`、`CFGZeroStar`、`CreateVideo`、`VAEDecode`、`KSamplerAdvanced`、`SaveVideo`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`CR Text`、`UNETLoader`、`CLIPLoader`、`INTConstant`、`VAELoader`、`LoadImage`、`RH_LLMAPI_NODE`、`PathchSageAttentionKJ`、`WanImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
