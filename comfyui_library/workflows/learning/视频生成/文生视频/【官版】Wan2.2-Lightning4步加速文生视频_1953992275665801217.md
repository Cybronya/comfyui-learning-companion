---
key: 视频生成/文生视频/【官版】Wan2.2-Lightning4步加速文生视频_1953992275665801217.json
name: 【官版】Wan2.2-Lightning4步加速文生视频_1953992275665801217.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1953992275665801217.json
hash: dc7f7cb19387c06a
coverage: 0.72973
learned_at: 2026-10-15 22:43:39
nodes: [VAELoader, CLIPLoader, SetNode, SetNode, EmptyHunyuanLatentVideo, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, SetNode, VAEDecode, SetNode, GetNode, GetNode, RH_LLMAPI_NODE, easy showAnything, JWInteger, JWInteger, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, MathExpression|pysssss, JWInteger, MathExpression|pysssss, Primitive integer [Crystools], KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, CR Text, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/【官版】Wan2.2-Lightning4步加速文生视频_1953992275665801217.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1953992275665801217.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（37 个）：
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `JWInteger`
- `JWInteger`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MathExpression|pysssss`
- `JWInteger`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `CR Text`
- `ImpactSwitch`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（27/37）

**有卡**：`VAELoader`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`VAEDecode`、`RH_LLMAPI_NODE`、`JWInteger`、`LayerUtility: PurgeVRAM V2`、`LoraLoaderModelOnly`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`MathExpression|pysssss`、`Primitive integer [Crystools]`、`KSamplerAdvanced`、`VHS_VideoCombine`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
