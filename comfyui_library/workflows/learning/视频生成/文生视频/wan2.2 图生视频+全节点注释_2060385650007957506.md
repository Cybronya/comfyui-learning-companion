---
key: 视频生成/文生视频/wan2.2 图生视频+全节点注释_2060385650007957506.json
name: wan2.2 图生视频+全节点注释_2060385650007957506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频+全节点注释_2060385650007957506.json
hash: 8d22720047a9b259
coverage: 0.5
learned_at: 2026-10-15 22:47:34
nodes: [UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CreateVideo, VAEDecode, VAELoader, SaveVideo, KSamplerAdvanced, INTConstant, PrimitiveFloat, MathExpression|pysssss, PathchSageAttentionKJ, CFGZeroStar, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, ModelSamplingSD3, LoadImage, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2 图生视频+全节点注释_2060385650007957506.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频+全节点注释_2060385650007957506.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAELoader`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `LoadImage`
- `CR Text`
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
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **50%**（24/48）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`VAELoader`、`SaveVideo`、`KSamplerAdvanced`、`INTConstant`、`MathExpression|pysssss`、`PathchSageAttentionKJ`、`CFGZeroStar`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingSD3`、`WanImageToVideo`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
