---
key: 视频生成/图生视频/wan2.2 图生视频  简洁版工作流_2079469610755256322.json
name: wan2.2 图生视频  简洁版工作流_2079469610755256322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 图生视频  简洁版工作流_2079469610755256322.json
hash: 51739dfbd6c173e4
coverage: 0.892857
learned_at: 2026-10-15 22:42:02
nodes: [RH_LLMAPI_NODE, ModelSamplingSD3, WanImageToVideo, CR Text, LoadImage, UNETLoader, UNETLoader, CLIPLoader, VAELoader, INTConstant, PrimitiveFloat, PathchSageAttentionKJ, ShowText|pysssss, LayerUtility: ImageScaleByAspectRatio V2, CFGZeroStar, Bjornulf_ShowInt, MathExpression|pysssss, CLIPTextEncode, CLIPTextEncode, PreviewImage, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, easy cleanGpuUsed, VAEDecode, SaveVideo, CreateVideo, PreviewVideoNode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2 图生视频  简洁版工作流_2079469610755256322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2079469610755256322.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `RH_LLMAPI_NODE`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `CR Text`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `PrimitiveFloat`
- `PathchSageAttentionKJ`
- `ShowText|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CFGZeroStar`
- `Bjornulf_ShowInt`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `SaveVideo`
- `CreateVideo`
- `PreviewVideoNode`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`RH_LLMAPI_NODE`、`ModelSamplingSD3`、`WanImageToVideo`、`CR Text`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`INTConstant`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`CFGZeroStar`、`Bjornulf_ShowInt`、`MathExpression|pysssss`、`CLIPTextEncode`、`KSamplerAdvanced`、`easy cleanGpuUsed`、`VAEDecode`、`SaveVideo`、`CreateVideo`、`PreviewVideoNode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CFGZeroStar
