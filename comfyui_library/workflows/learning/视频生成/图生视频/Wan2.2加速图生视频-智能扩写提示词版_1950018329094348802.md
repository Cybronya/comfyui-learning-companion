---
key: 视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1950018329094348802.json
name: Wan2.2加速图生视频-智能扩写提示词版_1950018329094348802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950018329094348802.json
hash: dbea2dd1d0fb110f
coverage: 0.684211
learned_at: 2026-10-15 22:30:51
nodes: [JWInteger, Note, LoadImage, JWInteger, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, SetNode, VAELoader, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, MathExpression|pysssss, ModelSamplingSD3, SetNode, PathchSageAttentionKJ, SetNode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, KSamplerAdvanced, RH_LLMAPI_NODE, KSamplerAdvanced, WanImageToVideo, UNETLoader, Note, VAEDecode, ImpactSwitch, CR Text, easy showAnything, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/Wan2.2加速图生视频-智能扩写提示词版_1950018329094348802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950018329094348802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（38 个）：
- `JWInteger`
- `Note`
- `LoadImage`
- `JWInteger`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `KSamplerAdvanced` ★核心
- `RH_LLMAPI_NODE`
- `KSamplerAdvanced` ★核心
- `WanImageToVideo`
- `UNETLoader` ★核心
- `Note`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `CR Text`
- `easy showAnything`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `7`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **68%**（26/38）

**有卡**：`JWInteger`、`LoadImage`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`MathExpression|pysssss`、`LoraLoaderModelOnly`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`KSamplerAdvanced`、`RH_LLMAPI_NODE`、`WanImageToVideo`、`VAEDecode`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
