---
key: 视频生成/文生视频/wan2.2文生视频-官方极速版_1950456441427693570.json
name: wan2.2文生视频-官方极速版_1950456441427693570.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950456441427693570.json
hash: 02c9a2749251f466
coverage: 0.894737
learned_at: 2026-10-15 22:43:35
nodes: [CLIPLoader, UNETLoader, VAELoader, VAEDecode, UNETLoader, Note, ModelSamplingSD3, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, VHS_VideoCombine, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "increment"}
---

# 视频生成/文生视频/wan2.2文生视频-官方极速版_1950456441427693570.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950456441427693570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Note`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `MarkdownNote`

## 关键参数

- `seed` = `enable`
- `steps` = `increment`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`VAEDecode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
