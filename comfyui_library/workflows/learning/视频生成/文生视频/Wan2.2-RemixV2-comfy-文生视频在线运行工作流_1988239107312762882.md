---
key: 视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json
name: Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json
hash: 7dccabc8573c0752
coverage: 0.85
learned_at: 2026-10-10 23:07:11
nodes: [PathchSageAttentionKJ, EmptyHunyuanLatentVideo, INTConstant, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, INTConstant, UNETLoader, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, VHS_VideoCombine, Note, CLIPLoader, VAELoader, CLIPTextEncode, Note, UNETLoader, MarkdownNote, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-RemixV2-comfy-文生视频在线运行工作流_1988239107312762882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `INTConstant`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `INTConstant`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Note`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`INTConstant`、`ModelSamplingSD3`、`UNETLoader`、`KSamplerAdvanced`、`VAEDecode`、`VHS_VideoCombine`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、INTConstant
