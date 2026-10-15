---
key: 视频生成/文生视频/wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890.json
name: wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890.json
hash: af3d89cec85c2d83
coverage: 0.481481
learned_at: 2026-10-15 22:47:34
nodes: [CLIPTextEncode, CreateVideo, VAEDecode, KSamplerAdvanced, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, VAELoader, CLIPLoader, UNETLoader, INTConstant, PathchSageAttentionKJ, PrimitiveFloat, INTConstant, CFGZeroStar, UNETLoader, WanImageToVideo, SaveVideo, LoadImage, RH_LLMAPI_Pro_Node, CR Text, CLIPTextEncode, ShowText|pysssss, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, RHHiddenNodes]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `INTConstant`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `INTConstant`
- `CFGZeroStar`
- `UNETLoader` ★核心
- `WanImageToVideo`
- `SaveVideo`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `CR Text`
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `RHHiddenNodes`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **48%**（26/54）

**有卡**：`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`KSamplerAdvanced`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`PathchSageAttentionKJ`、`CFGZeroStar`、`WanImageToVideo`、`SaveVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`CR Text`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
