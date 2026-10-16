---
key: 视频生成/文生视频/wan2.2 优化2.0 文生视频5B_1951324116144041986.json
name: wan2.2 优化2.0 文生视频5B_1951324116144041986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1951324116144041986.json
hash: 728414a2f8b2e21a
coverage: 1
learned_at: 2026-10-15 22:43:37
nodes: [CLIPTextEncode, ModelSamplingSD3, SaveVideo, CLIPTextEncode, VAEDecodeTiled, CreateVideo, KSampler, CLIPLoader, VAELoader, MathExpression|pysssss, UNETLoader, Int, EmptyHunyuanLatentVideo, Text, Int, Int]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 465324138481625, "steps": 25}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/wan2.2 优化2.0 文生视频5B_1951324116144041986.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1951324116144041986.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `MathExpression|pysssss`
- `UNETLoader` ★核心
- `Int`
- `EmptyHunyuanLatentVideo`
- `Text`
- `Int`
- `Int`

## 关键参数

- `seed` = `465324138481625`
- `steps` = `25`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`SaveVideo`、`VAEDecodeTiled`、`CreateVideo`、`KSampler`、`CLIPLoader`、`VAELoader`、`MathExpression|pysssss`、`UNETLoader`、`Int`、`EmptyHunyuanLatentVideo`、`Text`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、VAEDecodeTiled、EmptyHunyuanLatentVideo、SaveVideo

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
