---
key: 视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json
name: 【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json
hash: 56b452bb25c81664
coverage: 0.7
learned_at: 2026-10-15 22:31:06
nodes: [JWInteger, Note, LoadImage, PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, SetNode, VAELoader, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, ModelSamplingSD3, SetNode, PathchSageAttentionKJ, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, RH_LLMAPI_NODE, WanImageToVideo, Note, VAEDecode, ImpactSwitch, easy showAnything, UNETLoader, UNETLoader, KSamplerAdvanced, KSamplerAdvanced, MathExpression|pysssss, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text, JWInteger, VHS_VideoCombine, Primitive integer [Crystools], MathExpression|pysssss]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1954213178995568641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954213178995568641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（40 个）：
- `JWInteger`
- `Note`
- `LoadImage`
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
- `ModelSamplingSD3`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_LLMAPI_NODE`
- `WanImageToVideo`
- `Note`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `easy showAnything`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `MathExpression|pysssss`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `JWInteger`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **70%**（28/40）

**有卡**：`JWInteger`、`LoadImage`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_LLMAPI_NODE`、`WanImageToVideo`、`VAEDecode`、`UNETLoader`、`KSamplerAdvanced`、`MathExpression|pysssss`、`LayerUtility: PurgeVRAM V2`、`LoraLoaderModelOnly`、`CR Text`、`VHS_VideoCombine`、`Primitive integer [Crystools]`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
