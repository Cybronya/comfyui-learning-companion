---
key: 视频生成/文生视频/Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418.json
name: Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418.json
hash: a4e2988200ce248b
coverage: 0.904762
learned_at: 2026-10-10 23:08:07
nodes: [CLIPLoader, VAELoader, Note, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, VAEDecode, easy cleanGpuUsed, CLIPTextEncode, WanVideoNAG, CFGZeroStar, VHS_VideoCombine, UNETLoader, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, LoraLoaderModelOnly, Text, EmptyHunyuanLatentVideo]
patterns: []
missing: [easy cleanGpuUsed]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2特效 盒子装世界 Wan2.2 Jason版_1973586919907004418.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `Note`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `WanVideoNAG`
- `CFGZeroStar`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`
- `EmptyHunyuanLatentVideo`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`CLIPTextEncode`、`WanVideoNAG`、`CFGZeroStar`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`Text`、`EmptyHunyuanLatentVideo`

**缺卡**（1）：`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStar

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
