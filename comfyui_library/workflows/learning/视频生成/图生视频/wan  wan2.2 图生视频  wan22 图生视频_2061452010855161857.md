---
key: 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2061452010855161857.json
name: wan  wan2.2 图生视频  wan22 图生视频_2061452010855161857.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061452010855161857.json
hash: 988e2f7e2a701284
coverage: 0.896552
learned_at: 2026-10-15 22:38:54
nodes: [KSamplerAdvanced, WanImageToVideo, LoadImage, CR Text, RH_LLMAPI_NODE, UNETLoader, ShowText|pysssss, PrimitiveFloat, PathchSageAttentionKJ, INTConstant, SaveVideo, CreateVideo, VAEDecode, KSamplerAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, ModelSamplingSD3, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, MathExpression|pysssss, Bjornulf_ShowInt, CFGZeroStar, PreviewImage, CLIPTextEncode, CLIPLoader, CLIPTextEncode, ModelSamplingSD3, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2061452010855161857.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061452010855161857.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `LoadImage`
- `CR Text`
- `RH_LLMAPI_NODE`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `PrimitiveFloat`
- `PathchSageAttentionKJ`
- `INTConstant`
- `SaveVideo`
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `MathExpression|pysssss`
- `Bjornulf_ShowInt`
- `CFGZeroStar`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAELoader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`KSamplerAdvanced`、`WanImageToVideo`、`LoadImage`、`CR Text`、`RH_LLMAPI_NODE`、`UNETLoader`、`PathchSageAttentionKJ`、`INTConstant`、`SaveVideo`、`CreateVideo`、`VAEDecode`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`CFGZeroStar`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
