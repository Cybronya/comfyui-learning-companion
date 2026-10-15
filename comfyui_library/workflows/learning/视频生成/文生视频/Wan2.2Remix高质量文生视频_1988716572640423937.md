---
key: 视频生成/文生视频/Wan2.2Remix高质量文生视频_1988716572640423937.json
name: Wan2.2Remix高质量文生视频_1988716572640423937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2Remix高质量文生视频_1988716572640423937.json
hash: dd60dd6889bbb50a
coverage: 1
learned_at: 2026-10-15 22:47:13
nodes: [PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, KSamplerAdvanced, CLIPLoader, VAELoader, CLIPTextEncode, UNETLoader, UNETLoader, INTConstant, INTConstant, EmptyHunyuanLatentVideo, Int, Int, Int, KSamplerAdvanced, VAEDecode, CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2Remix高质量文生视频_1988716572640423937.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2Remix高质量文生视频_1988716572640423937.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（20 个）：
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `INTConstant`
- `INTConstant`
- `EmptyHunyuanLatentVideo`
- `Int`
- `Int`
- `Int`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`INTConstant`、`EmptyHunyuanLatentVideo`、`Int`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、Int
