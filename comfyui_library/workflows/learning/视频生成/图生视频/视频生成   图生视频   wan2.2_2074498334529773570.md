---
key: 视频生成/图生视频/视频生成   图生视频   wan2.2_2074498334529773570.json
name: 视频生成   图生视频   wan2.2_2074498334529773570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2074498334529773570.json
hash: 5ff5665aad08a804
coverage: 0.896552
learned_at: 2026-10-15 22:41:16
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CreateVideo, VAEDecode, VAELoader, KSamplerAdvanced, RH_LLMAPI_NODE, ShowText|pysssss, INTConstant, PrimitiveFloat, PathchSageAttentionKJ, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, CLIPTextEncode, SaveVideo, WanImageToVideo, INTConstant, MathExpression|pysssss, Bjornulf_ShowInt, CFGZeroStar, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/视频生成   图生视频   wan2.2_2074498334529773570.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074498334529773570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `INTConstant`
- `PrimitiveFloat`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `WanImageToVideo`
- `INTConstant`
- `MathExpression|pysssss`
- `Bjornulf_ShowInt`
- `CFGZeroStar`
- `LayerUtility: ImageScaleByAspectRatio V2`
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

**有卡**：`easy cleanGpuUsed`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`VAELoader`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`INTConstant`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`SaveVideo`、`WanImageToVideo`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`CFGZeroStar`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
