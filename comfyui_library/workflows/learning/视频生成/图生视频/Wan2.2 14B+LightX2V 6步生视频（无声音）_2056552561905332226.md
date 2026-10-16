---
key: 视频生成/图生视频/Wan2.2 14B+LightX2V 6步生视频（无声音）_2056552561905332226.json
name: Wan2.2 14B+LightX2V 6步生视频（无声音）_2056552561905332226.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2056552561905332226.json
hash: 884af2baa8cc1d5d
coverage: 1
learned_at: 2026-10-15 22:38:04
nodes: [CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, VAELoader, JWInteger, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, KSamplerAdvanced, PathchSageAttentionKJ, WanImageToVideo, VHS_VideoCombine, UNETLoader, CLIPTextEncode, Text, DF_Int_to_Float, Int, ComfyMathExpression, UNETLoader, CLIPLoader, Int, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 14B+LightX2V 6步生视频（无声音）_2056552561905332226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2056552561905332226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `JWInteger`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `WanImageToVideo`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Text`
- `DF_Int_to_Float`
- `Int`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Int`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VAEDecode`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAELoader`、`JWInteger`、`LayerUtility: PurgeVRAM`、`WanImageToVideo`、`VHS_VideoCombine`、`UNETLoader`、`Text`、`DF_Int_to_Float`、`Int`、`ComfyMathExpression`、`CLIPLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
