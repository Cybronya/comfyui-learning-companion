---
key: 视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json
name: Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json
hash: ad5423fcd8cf2d95
coverage: 1
learned_at: 2026-10-15 22:43:35
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, Text, CreateVideo, CLIPTextEncode, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, SimpleMath+, KSamplerAdvanced, SaveVideo, KSamplerAdvanced, UNETLoader, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, PathchSageAttentionKJ, CLIPLoader, VAELoader, ImpactInt, ImpactInt, ImpactInt, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2_14B_文生视频-加速版-KJ模型_1950219353737314306.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950219353737314306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（23 个）：
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `Text`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SimpleMath+`
- `KSamplerAdvanced` ★核心
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`Text`、`CreateVideo`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`SimpleMath+`、`KSamplerAdvanced`、`SaveVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`ImpactInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
