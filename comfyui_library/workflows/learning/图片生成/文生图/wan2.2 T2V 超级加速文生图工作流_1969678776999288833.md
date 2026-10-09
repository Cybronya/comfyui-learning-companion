---
key: 图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json
name: wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json
hash: b26559ffb51e315e
coverage: 0.875
learned_at: 2026-10-09 02:01:39
nodes: [UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, CR Text Concatenate, LoraLoaderModelOnly, ImpactInt, ImpactInt, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, CLIPLoader, VAELoader, VAEDecode, CR Text, CR Text, SaveImage]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate]
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1969678776999288833.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `CR Text`
- `CR Text`
- `SaveImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`ImpactInt`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`

**缺卡**（3）：`CR Text`、`CR Text`、`CR Text Concatenate`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
