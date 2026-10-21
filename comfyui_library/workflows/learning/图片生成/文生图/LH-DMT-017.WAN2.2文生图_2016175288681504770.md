---
key: 图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json
name: LH-DMT-017.WAN2.2文生图_2016175288681504770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json
hash: 801f8244231d0b7f
coverage: 0.952381
learned_at: 2026-10-19 22:15:12
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, ImpactInt, ImpactInt, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, SaveImage, MarkdownNote, easy positive, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, VAELoader, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "beta", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LH-DMT-017.WAN2.2文生图_2016175288681504770.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（21 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ImpactInt`
- `ImpactInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `MarkdownNote`
- `easy positive`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`ImpactInt`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`VAEDecode`、`KSamplerAdvanced`、`SaveImage`、`easy positive`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
