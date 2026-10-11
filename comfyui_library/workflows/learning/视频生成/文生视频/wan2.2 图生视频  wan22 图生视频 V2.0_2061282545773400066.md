---
key: 视频生成/文生视频/wan2.2 图生视频  wan22 图生视频 V2.0_2061282545773400066.json
name: wan2.2 图生视频  wan22 图生视频 V2.0_2061282545773400066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频  wan22 图生视频 V2.0_2061282545773400066.json
hash: 5a5aaf7a57e750a2
coverage: 0.724138
learned_at: 2026-10-11 19:49:45
nodes: [Bjornulf_ShowInt, easy cleanGpuUsed, easy cleanGpuUsed, UNETLoader, UNETLoader, CLIPLoader, CLIPTextEncode, CreateVideo, VAEDecode, VAELoader, SaveVideo, KSamplerAdvanced, RH_LLMAPI_NODE, ShowText|pysssss, INTConstant, PrimitiveFloat, MathExpression|pysssss, PathchSageAttentionKJ, CFGZeroStar, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ModelSamplingSD3, WanImageToVideo, KSamplerAdvanced, ModelSamplingSD3, CLIPTextEncode, LoadImage, CR Text, INTConstant]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2 图生视频  wan22 图生视频 V2.0_2061282545773400066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2 图生视频  wan22 图生视频 V2.0_2061282545773400066.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Bjornulf_ShowInt`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAELoader`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `INTConstant`
- `PrimitiveFloat`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `CFGZeroStar`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Text`
- `INTConstant`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（21/29）

**有卡**：`Bjornulf_ShowInt`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`CreateVideo`、`VAEDecode`、`VAELoader`、`SaveVideo`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`INTConstant`、`PathchSageAttentionKJ`、`CFGZeroStar`、`ModelSamplingSD3`、`WanImageToVideo`、`LoadImage`

**缺卡**（5）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
