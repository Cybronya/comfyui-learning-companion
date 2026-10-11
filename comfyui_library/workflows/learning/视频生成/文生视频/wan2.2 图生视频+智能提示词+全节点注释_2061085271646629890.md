---
key: 视频生成/文生视频/wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890.json
name: wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频+智能提示词+全节点注释_2061085271646629890.json
hash: af3d89cec85c2d83
coverage: 0.425926
learned_at: 2026-10-11 19:49:45
nodes: [CLIPTextEncode, CreateVideo, VAEDecode, KSamplerAdvanced, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, VAELoader, CLIPLoader, UNETLoader, INTConstant, PathchSageAttentionKJ, PrimitiveFloat, INTConstant, CFGZeroStar, UNETLoader, WanImageToVideo, SaveVideo, LoadImage, RH_LLMAPI_Pro_Node, CR Text, CLIPTextEncode, ShowText|pysssss, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, LoadImage, RHHiddenNodes]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
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

覆盖率 **43%**（23/54）

**有卡**：`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`INTConstant`、`PathchSageAttentionKJ`、`CFGZeroStar`、`WanImageToVideo`、`SaveVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`RHHiddenNodes`

**缺卡**（3）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
