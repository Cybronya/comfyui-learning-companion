---
key: 视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json
name: 电商模特IP Lora 视频版 wan2.2_1985602072307552257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json
hash: 6e310012878adce8
coverage: 0.913043
learned_at: 2026-10-15 22:48:55
nodes: [CLIPLoader, VAELoader, easy seed, UNETLoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, VHS_VideoCombine, WanMoeKSampler, LayerUtility: PurgeVRAM, VAEDecode, LoraLoaderModelOnly, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Note]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "lcm", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（23 个）：
- `CLIPLoader`
- `VAELoader`
- `easy seed`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `WanMoeKSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `1`
- `denoise` = `lcm`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPLoader`、`VAELoader`、`easy seed`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`WanMoeKSampler`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、easy seed
