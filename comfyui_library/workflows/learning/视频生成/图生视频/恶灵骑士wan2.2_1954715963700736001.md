---
key: 视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json
name: 恶灵骑士wan2.2_1954715963700736001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1954715963700736001.json
hash: 2bc4b378245e0ece
coverage: 0.964286
learned_at: 2026-10-15 22:31:06
nodes: [CLIPLoader, easy int, KSamplerAdvanced, ModelSamplingSD3, VAELoader, WanImageToVideo, CLIPTextEncode, LoraLoaderModelOnly, SimpleMath+, ModelSamplingSD3, PathchSageAttentionKJ, KSamplerAdvanced, UNETLoader, UNETLoader, VAEDecode, easy int, easy int, LoraLoaderModelOnly, RHHiddenNodes, PathchSageAttentionKJ, VHS_VideoCombine, Note, CR Text, CLIPTextEncode, CR Text Concatenate, CR Text, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/图生视频/恶灵骑士wan2.2_1954715963700736001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1954715963700736001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（28 个）：
- `CLIPLoader`
- `easy int`
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `easy int`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `Note`
- `CR Text`
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `CR Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`CLIPLoader`、`easy int`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAELoader`、`WanImageToVideo`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SimpleMath+`、`PathchSageAttentionKJ`、`UNETLoader`、`VAEDecode`、`RHHiddenNodes`、`VHS_VideoCombine`、`CR Text`、`CR Text Concatenate`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
