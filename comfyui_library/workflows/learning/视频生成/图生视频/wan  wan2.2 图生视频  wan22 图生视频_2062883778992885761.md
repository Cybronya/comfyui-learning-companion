---
key: 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2062883778992885761.json
name: wan  wan2.2 图生视频  wan22 图生视频_2062883778992885761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2062883778992885761.json
hash: 1166da2e99b6b3fd
coverage: 0.896552
learned_at: 2026-10-15 22:39:08
nodes: [Bjornulf_ShowInt, CLIPTextEncode, CreateVideo, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, VAELoader, CLIPLoader, UNETLoader, PathchSageAttentionKJ, PrimitiveFloat, INTConstant, CFGZeroStar, easy cleanGpuUsed, easy cleanGpuUsed, WanImageToVideo, SaveVideo, CR Text, LoadImage, UNETLoader, RH_LLMAPI_NODE, ShowText|pysssss, INTConstant, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, PreviewImage, ModelSamplingSD3]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan  wan2.2 图生视频  wan22 图生视频_2062883778992885761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2062883778992885761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Bjornulf_ShowInt`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `INTConstant`
- `CFGZeroStar`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanImageToVideo`
- `SaveVideo`
- `CR Text`
- `LoadImage`
- `UNETLoader` ★核心
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `INTConstant`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ModelSamplingSD3`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`Bjornulf_ShowInt`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`INTConstant`、`CFGZeroStar`、`easy cleanGpuUsed`、`WanImageToVideo`、`SaveVideo`、`CR Text`、`LoadImage`、`RH_LLMAPI_NODE`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
