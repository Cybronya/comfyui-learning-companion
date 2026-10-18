---
key: 视频生成/图生视频/首尾帧Wan2.2动漫模型DaSiWa10_2053001977566638081.json
name: 首尾帧Wan2.2动漫模型DaSiWa10_2053001977566638081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧Wan2.2动漫模型DaSiWa10_2053001977566638081.json
hash: 90ba634a6e5d3af9
coverage: 0.744186
learned_at: 2026-10-15 22:37:34
nodes: [wanBlockSwap, wanBlockSwap, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, GetNode, SetNode, ModelSamplingSD3, ModelSamplingSD3, SetNode, ImageConcanate, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPVisionEncode, VAEDecode, CLIPLoader, VAELoader, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, ImageResizeKJ, GetNode, CLIPVisionLoader, SetNode, Note, KSamplerAdvanced, GetNode, RH_LLMAPI_NODE, ImpactSwitch, MathExpression|pysssss, JWInteger, UNETLoader, UNETLoader, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, VHS_VideoCombine, LoadImage, LoadImage, easy showAnything, CR Text]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/首尾帧Wan2.2动漫模型DaSiWa10_2053001977566638081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053001977566638081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（43 个）：
- `wanBlockSwap`
- `wanBlockSwap`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `GetNode`
- `SetNode`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `SetNode`
- `ImageConcanate`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `CLIPVisionEncode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `Note`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `MathExpression|pysssss`
- `JWInteger`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `CR Text`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`wanBlockSwap`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`ImageConcanate`、`CLIPVisionEncode`、`WanFirstLastFrameToVideo`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResizeKJ`、`CLIPVisionLoader`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`MathExpression|pysssss`、`JWInteger`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
