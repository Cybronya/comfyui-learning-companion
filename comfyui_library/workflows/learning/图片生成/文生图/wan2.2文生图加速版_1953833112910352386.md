---
key: 图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json
name: wan2.2文生图加速版_1953833112910352386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json
hash: 6b80e056b9843355
coverage: 1
learned_at: 2026-10-15 22:27:58
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, UNETLoader, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CR Text Concatenate, KSamplerAdvanced, LoraLoaderModelOnly, ImpactInt, KSamplerAdvanced, VAEDecode, CR Text, LoraLoaderModelOnly, ImpactInt, CR Text, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "randomize"}
---

# 图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图加速版_1953833112910352386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（25 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CR Text Concatenate`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `ImpactInt`
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

覆盖率 **100%**（25/25）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CR Text Concatenate`、`KSamplerAdvanced`、`ImpactInt`、`VAEDecode`、`CR Text`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
