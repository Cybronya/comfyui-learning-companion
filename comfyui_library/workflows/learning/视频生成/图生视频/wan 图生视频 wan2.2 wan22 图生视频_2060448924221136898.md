---
key: 视频生成/图生视频/wan 图生视频 wan2.2 wan22 图生视频_2060448924221136898.json
name: wan 图生视频 wan2.2 wan22 图生视频_2060448924221136898.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan 图生视频 wan2.2 wan22 图生视频_2060448924221136898.json
hash: 97ca8148ff3ab679
coverage: 0.896552
learned_at: 2026-10-15 22:38:48
nodes: [PathchSageAttentionKJ, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, VAEDecode, VAELoader, ShowText|pysssss, MathExpression|pysssss, INTConstant, PrimitiveFloat, PreviewImage, SaveVideo, INTConstant, KSamplerAdvanced, RH_LLMAPI_NODE, easy cleanGpuUsed, easy cleanGpuUsed, ModelSamplingSD3, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan 图生视频 wan2.2 wan22 图生视频_2060448924221136898.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060448924221136898.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `Bjornulf_ShowInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `INTConstant`
- `PrimitiveFloat`
- `PreviewImage`
- `SaveVideo`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`PathchSageAttentionKJ`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStar`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`VAELoader`、`MathExpression|pysssss`、`INTConstant`、`SaveVideo`、`RH_LLMAPI_NODE`、`easy cleanGpuUsed`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
