---
key: 视频生成/图生视频/wan2.2 图生视频  wan22 图生视频_2063255807923412994.json
name: wan2.2 图生视频  wan22 图生视频_2063255807923412994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频  wan22 图生视频_2063255807923412994.json
hash: 71fb564a94921f45
coverage: 0.896552
learned_at: 2026-10-15 22:39:12
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CreateVideo, VAEDecode, VAELoader, KSamplerAdvanced, RH_LLMAPI_NODE, ShowText|pysssss, INTConstant, PrimitiveFloat, PathchSageAttentionKJ, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, CLIPTextEncode, SaveVideo, WanImageToVideo, INTConstant, MathExpression|pysssss, Bjornulf_ShowInt, CFGZeroStar, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 图生视频  wan22 图生视频_2063255807923412994.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063255807923412994.json`

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
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`easy cleanGpuUsed`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`VAELoader`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`INTConstant`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`SaveVideo`、`WanImageToVideo`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`CFGZeroStar`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
