---
key: 视频生成/文生视频/最强文生视频 wan2.2_1952267409933717505.json
name: 最强文生视频 wan2.2_1952267409933717505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/最强文生视频 wan2.2_1952267409933717505.json
hash: 0ff9490b772b3c90
coverage: 0.913043
learned_at: 2026-10-15 22:43:38
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, CLIPLoader, CLIPTextEncode, VAELoader, PathchSageAttentionKJ, ModelSamplingSD3, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, Note, CLIPTextEncode, easy seed, Text, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyHunyuanLatentVideo, Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/最强文生视频 wan2.2_1952267409933717505.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1952267409933717505.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `Note`
- `CLIPTextEncode` ★核心
- `easy seed`
- `Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyHunyuanLatentVideo`
- `Note`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`KSamplerAdvanced`、`VHS_VideoCombine`、`easy seed`、`Text`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、easy seed
