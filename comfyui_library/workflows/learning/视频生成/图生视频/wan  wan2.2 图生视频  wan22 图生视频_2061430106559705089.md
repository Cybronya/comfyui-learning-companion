---
key: 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2061430106559705089.json
name: wan  wan2.2 图生视频  wan22 图生视频_2061430106559705089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061430106559705089.json
hash: c287308a095cd7f0
coverage: 0.896552
learned_at: 2026-10-15 22:38:53
nodes: [CR Text, RH_LLMAPI_NODE, ShowText|pysssss, INTConstant, PrimitiveFloat, UNETLoader, CLIPLoader, MathExpression|pysssss, Bjornulf_ShowInt, PathchSageAttentionKJ, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, VAELoader, CFGZeroStar, WanImageToVideo, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, CreateVideo, SaveVideo, KSamplerAdvanced, ModelSamplingSD3, easy cleanGpuUsed, ModelSamplingSD3, UNETLoader, CLIPTextEncode, PreviewImage, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2061430106559705089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061430106559705089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CR Text`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `INTConstant`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MathExpression|pysssss`
- `Bjornulf_ShowInt`
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `VAELoader`
- `CFGZeroStar`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
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

**有卡**：`CR Text`、`RH_LLMAPI_NODE`、`INTConstant`、`UNETLoader`、`CLIPLoader`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`CFGZeroStar`、`WanImageToVideo`、`KSamplerAdvanced`、`VAEDecode`、`easy cleanGpuUsed`、`CreateVideo`、`SaveVideo`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
