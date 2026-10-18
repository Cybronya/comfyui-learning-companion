---
key: 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2062879411124396034.json
name: wan  wan2.2 图生视频  wan22 图生视频_2062879411124396034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2062879411124396034.json
hash: 5af8510d40a27588
coverage: 0.896552
learned_at: 2026-10-15 22:39:08
nodes: [UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, KSamplerAdvanced, LoadImage, RH_LLMAPI_NODE, ShowText|pysssss, VAEDecode, CreateVideo, SaveVideo, CR Text, PathchSageAttentionKJ, PrimitiveFloat, INTConstant, CLIPLoader, Bjornulf_ShowInt, VAELoader, CFGZeroStar, MathExpression|pysssss, PreviewImage, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, UNETLoader, WanImageToVideo, ModelSamplingSD3, easy cleanGpuUsed, KSamplerAdvanced, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2062879411124396034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062879411124396034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `CR Text`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `INTConstant`
- `CLIPLoader`
- `Bjornulf_ShowInt`
- `VAELoader`
- `CFGZeroStar`
- `MathExpression|pysssss`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `WanImageToVideo`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`KSamplerAdvanced`、`LoadImage`、`RH_LLMAPI_NODE`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`CR Text`、`PathchSageAttentionKJ`、`CLIPLoader`、`Bjornulf_ShowInt`、`VAELoader`、`CFGZeroStar`、`MathExpression|pysssss`、`CLIPTextEncode`、`ModelSamplingSD3`、`WanImageToVideo`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
