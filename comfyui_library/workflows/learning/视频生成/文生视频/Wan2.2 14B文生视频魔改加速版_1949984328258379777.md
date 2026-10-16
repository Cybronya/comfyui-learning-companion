---
key: 视频生成/文生视频/Wan2.2 14B文生视频魔改加速版_1949984328258379777.json
name: Wan2.2 14B文生视频魔改加速版_1949984328258379777.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1949984328258379777.json
hash: d48e01f92fa9f23a
coverage: 0.714286
learned_at: 2026-10-15 22:43:33
nodes: [VAELoader, CLIPLoader, SetNode, SetNode, EmptyHunyuanLatentVideo, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, MathExpression|pysssss, SetNode, UNETLoader, LoraLoaderModelOnly, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, SetNode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, GetNode, GetNode, RH_LLMAPI_NODE, easy showAnything, VHS_VideoCombine, JWInteger, JWInteger, JWInteger, CR Text, KSamplerAdvanced, KSamplerAdvanced, ImpactSwitch]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2 14B文生视频魔改加速版_1949984328258379777.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1949984328258379777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（35 个）：
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `SetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImpactSwitch`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **71%**（25/35）

**有卡**：`VAELoader`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`CLIPTextEncode`、`MathExpression|pysssss`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM V2`、`RH_LLMAPI_NODE`、`VHS_VideoCombine`、`JWInteger`、`CR Text`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
