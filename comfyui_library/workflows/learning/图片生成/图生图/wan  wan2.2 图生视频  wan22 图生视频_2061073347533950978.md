---
key: 图片生成/图生图/wan  wan2.2 图生视频  wan22 图生视频_2061073347533950978.json
name: wan  wan2.2 图生视频  wan22 图生视频_2061073347533950978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan  wan2.2 图生视频  wan22 图生视频_2061073347533950978.json
hash: 7f22ff1b034073dd
coverage: 0.896552
learned_at: 2026-10-23 11:45:46
nodes: [Bjornulf_ShowInt, CLIPTextEncode, CreateVideo, VAEDecode, KSamplerAdvanced, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, RH_LLMAPI_NODE, VAELoader, CLIPLoader, UNETLoader, ShowText|pysssss, INTConstant, PathchSageAttentionKJ, PrimitiveFloat, INTConstant, CFGZeroStar, UNETLoader, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, PreviewImage, WanImageToVideo, SaveVideo, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/wan  wan2.2 图生视频  wan22 图生视频_2061073347533950978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan  wan2.2 图生视频  wan22 图生视频_2061073347533950978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Bjornulf_ShowInt`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `RH_LLMAPI_NODE`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `INTConstant`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `INTConstant`
- `CFGZeroStar`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `WanImageToVideo`
- `SaveVideo`
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

**有卡**：`Bjornulf_ShowInt`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`KSamplerAdvanced`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`RH_LLMAPI_NODE`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`PathchSageAttentionKJ`、`CFGZeroStar`、`easy cleanGpuUsed`、`WanImageToVideo`、`SaveVideo`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
