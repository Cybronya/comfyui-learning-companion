---
key: 视频生成/图生视频/wan 图生视频 wan2.2 wan22 图生视频_2063548406781534210.json
name: wan 图生视频 wan2.2 wan22 图生视频_2063548406781534210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan 图生视频 wan2.2 wan22 图生视频_2063548406781534210.json
hash: dfdd72f72887abd6
coverage: 0.896552
learned_at: 2026-10-15 22:39:14
nodes: [PathchSageAttentionKJ, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, VAEDecode, ShowText|pysssss, MathExpression|pysssss, PreviewImage, KSamplerAdvanced, RH_LLMAPI_NODE, easy cleanGpuUsed, easy cleanGpuUsed, ModelSamplingSD3, SaveVideo, LoadImage, CLIPLoader, UNETLoader, UNETLoader, PrimitiveFloat, VAELoader, INTConstant, INTConstant, CR Text]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan 图生视频 wan2.2 wan22 图生视频_2063548406781534210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063548406781534210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `Bjornulf_ShowInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `MathExpression|pysssss`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `SaveVideo`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PrimitiveFloat`
- `VAELoader`
- `INTConstant`
- `INTConstant`
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

**有卡**：`PathchSageAttentionKJ`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`CFGZeroStar`、`WanImageToVideo`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`、`MathExpression|pysssss`、`RH_LLMAPI_NODE`、`easy cleanGpuUsed`、`SaveVideo`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`INTConstant`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
