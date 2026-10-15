---
key: 图片生成/文生图/Wan2.2 最强最写实去AI感文生图_1958332452488024065.json
name: Wan2.2 最强最写实去AI感文生图_1958332452488024065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 最强最写实去AI感文生图_1958332452488024065.json
hash: c8424c7fa951156a
coverage: 0.964286
learned_at: 2026-10-15 22:27:35
nodes: [CR Text Concatenate, CR Text, RH_LLMAPI_NODE, KSamplerAdvanced, EmptyHunyuanLatentVideo, ModelSamplingSD3, PathchSageAttentionKJ, CFGZeroStarAndInit, ModelSamplingSD3, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, CLIPLoader, CR Text, UNETLoader, CR Text, CLIPTextEncode, VAELoader, VAEDecode, SaveImage, KSamplerAdvanced, ImpactInt, ImpactInt, CR Text, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 图片生成/文生图/Wan2.2 最强最写实去AI感文生图_1958332452488024065.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 最强最写实去AI感文生图_1958332452488024065.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（28 个）：
- `CR Text Concatenate`
- `CR Text`
- `RH_LLMAPI_NODE`
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CFGZeroStarAndInit`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CR Text`
- `UNETLoader` ★核心
- `CR Text`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `ImpactInt`
- `ImpactInt`
- `CR Text`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **96%**（27/28）

**有卡**：`CR Text Concatenate`、`CR Text`、`RH_LLMAPI_NODE`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CFGZeroStarAndInit`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`ImpactInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、CFGZeroStarAndInit
