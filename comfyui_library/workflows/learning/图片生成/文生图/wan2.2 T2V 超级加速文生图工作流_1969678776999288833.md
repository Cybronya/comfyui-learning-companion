---
key: 图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json
name: wan2.2 T2V 超级加速文生图工作流_1969678776999288833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json
hash: b26559ffb51e315e
coverage: 0.875
learned_at: 2026-10-10 20:59:27
nodes: [UNETLoader, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, CR Text Concatenate, LoraLoaderModelOnly, ImpactInt, ImpactInt, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, CLIPLoader, VAELoader, VAEDecode, CR Text, CR Text, SaveImage]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate]
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2 T2V 超级加速文生图工作流_1969678776999288833.json`

## 结构

**节点**（24 个）：
- `UNETLoader`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `KSamplerAdvanced`
- `CR Text Concatenate`
- `LoraLoaderModelOnly`
- `ImpactInt`
- `ImpactInt`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode`
- `CR Text`
- `CR Text`
- `SaveImage`

## 关键参数

- `cfg` = `12`
- `denoise` = `bong_tangent`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `seed` = `disable`
- `steps` = `randomize`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CR Text Concatenate`、`ImpactInt`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`VAELoader`、`VAEDecode`

**缺卡**（3）：`CR Text`、`CR Text`、`CR Text Concatenate`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
