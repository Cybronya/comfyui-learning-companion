---
key: 视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json
name: 惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json
hash: 17acced73a6179e8
coverage: 0.944444
learned_at: 2026-10-15 22:48:36
nodes: [PathchSageAttentionKJ, INTConstant, ModelSamplingSD3, PathchSageAttentionKJ, INTConstant, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, CLIPTextEncode, CLIPTextEncode, EmptyHunyuanLatentVideo, Note, UNETLoader, UNETLoader, VAELoader, CLIPLoader, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（18 个）：
- `PathchSageAttentionKJ`
- `INTConstant`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `INTConstant`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`PathchSageAttentionKJ`、`INTConstant`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、INTConstant
