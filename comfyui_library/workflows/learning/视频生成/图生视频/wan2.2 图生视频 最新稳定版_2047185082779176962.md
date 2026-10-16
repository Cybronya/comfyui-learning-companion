---
key: 视频生成/图生视频/wan2.2 图生视频 最新稳定版_2047185082779176962.json
name: wan2.2 图生视频 最新稳定版_2047185082779176962.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047185082779176962.json
hash: e948c6c893e891fb
coverage: 0.896552
learned_at: 2026-10-15 22:37:03
nodes: [PathchSageAttentionKJ, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, easy cleanGpuUsed, easy cleanGpuUsed, PreviewImage, INTConstant, PrimitiveFloat, LoadImage, CR Text, RH_LLMAPI_NODE, MathExpression|pysssss, INTConstant, SaveVideo, ShowText|pysssss, UNETLoader, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, CFGZeroStar, WanImageToVideo, ModelSamplingSD3, KSamplerAdvanced, CreateVideo, VAEDecode, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 图生视频 最新稳定版_2047185082779176962.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047185082779176962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `Bjornulf_ShowInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PreviewImage`
- `INTConstant`
- `PrimitiveFloat`
- `LoadImage`
- `CR Text`
- `RH_LLMAPI_NODE`
- `MathExpression|pysssss`
- `INTConstant`
- `SaveVideo`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CFGZeroStar`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`PathchSageAttentionKJ`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`easy cleanGpuUsed`、`INTConstant`、`LoadImage`、`CR Text`、`RH_LLMAPI_NODE`、`MathExpression|pysssss`、`SaveVideo`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CFGZeroStar`、`WanImageToVideo`、`KSamplerAdvanced`、`CreateVideo`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
