---
key: 图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json
name: wan2.2文生图加速版_1953833112910352386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json
hash: 6b80e056b9843355
coverage: 0.88
learned_at: 2026-10-10 20:59:27
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, UNETLoader, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CR Text Concatenate, KSamplerAdvanced, LoraLoaderModelOnly, ImpactInt, KSamplerAdvanced, VAEDecode, CR Text, LoraLoaderModelOnly, ImpactInt, CR Text, SaveImage]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate]
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json`

## 结构

**节点**（25 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode`
- `UNETLoader`
- `UNETLoader`
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ImpactInt`
- `KSamplerAdvanced`
- `VAEDecode`
- `CR Text`
- `LoraLoaderModelOnly`
- `ImpactInt`
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

覆盖率 **88%**（22/25）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CR Text Concatenate`、`KSamplerAdvanced`、`ImpactInt`、`VAEDecode`、`CR Text`

**缺卡**（3）：`CR Text`、`CR Text`、`CR Text Concatenate`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
