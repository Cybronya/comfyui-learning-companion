---
key: 视频生成/文生视频/wan2.2文生视频_2087718119883235330.json
name: wan2.2文生视频_2087718119883235330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_2087718119883235330.json
hash: 25b8ba3f5acdac2e
coverage: 1
learned_at: 2026-10-15 22:47:36
nodes: [KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, VAELoader, UNETLoader, PathchSageAttentionKJ, CLIPTextEncode, UNETLoader, KSamplerAdvanced, VAEDecode, CLIPLoader, EmptyHunyuanLatentVideo, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/wan2.2文生视频_2087718119883235330.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2文生视频_2087718119883235330.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（15 个）：
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`KSamplerAdvanced`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelSamplingSD3
