---
key: 视频生成/文生视频/wan2.2 图生视频+全节点注释_2060385650007957506.json
name: wan2.2 图生视频+全节点注释_2060385650007957506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频+全节点注释_2060385650007957506.json
hash: 8d22720047a9b259
coverage: 0.4375
learned_at: 2026-10-11 19:49:45
nodes: [UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CreateVideo, VAEDecode, VAELoader, SaveVideo, KSamplerAdvanced, INTConstant, PrimitiveFloat, MathExpression|pysssss, PathchSageAttentionKJ, CFGZeroStar, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, ModelSamplingSD3, LoadImage, CR Text, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
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

覆盖率 **44%**（21/48）

**有卡**：`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`VAELoader`、`SaveVideo`、`KSamplerAdvanced`、`INTConstant`、`PathchSageAttentionKJ`、`CFGZeroStar`、`ModelSamplingSD3`、`WanImageToVideo`、`LoadImage`

**缺卡**（3）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
