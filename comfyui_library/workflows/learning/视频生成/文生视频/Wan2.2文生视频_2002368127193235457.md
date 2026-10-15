---
key: 视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json
name: Wan2.2文生视频_2002368127193235457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json
hash: e2cd50489c1064d4
coverage: 1
learned_at: 2026-10-15 22:47:15
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, INTConstant, INTConstant, VAEDecode, CLIPTextEncode, UNETLoader, UNETLoader, EmptyHunyuanLatentVideo, KSamplerAdvanced, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频_2002368127193235457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`INTConstant`、`VAEDecode`、`UNETLoader`、`EmptyHunyuanLatentVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、INTConstant
