---
key: 视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json
name: 电商模特IP Lora 视频版 wan2.2_1985602072307552257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/电商模特IP Lora 视频版 wan2.2_1985602072307552257.json
hash: 6e310012878adce8
coverage: 0.826087
learned_at: 2026-10-11 02:45:05
nodes: [CLIPLoader, VAELoader, easy seed, UNETLoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, VHS_VideoCombine, WanMoeKSampler, LayerUtility: PurgeVRAM, VAEDecode, LoraLoaderModelOnly, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, Note]
patterns: []
missing: [LayerUtility: PurgeVRAM, easy seed]
parameters: {"cfg": 8, "denoise": "lcm", "sampler_name": 1, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **83%**（19/23）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`WanMoeKSampler`、`VAEDecode`、`Text`

**缺卡**（2）：`LayerUtility: PurgeVRAM`、`easy seed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、WanMoeKSampler、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
