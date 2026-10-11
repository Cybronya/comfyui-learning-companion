---
key: 视频生成/文生视频/纯净万相 Wan2.2-Remix-Comfy-T2V-文生视频 不带lora,带插帧丝滑_2042646743598243841.json
name: 纯净万相 Wan2.2-Remix-Comfy-T2V-文生视频 不带lora,带插帧丝滑_2042646743598243841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/纯净万相 Wan2.2-Remix-Comfy-T2V-文生视频 不带lora,带插帧丝滑_2042646743598243841.json
hash: ba8811c75be516cf
coverage: 0.894737
learned_at: 2026-10-11 19:49:51
nodes: [ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, EmptyHunyuanLatentVideo, Note, CLIPLoader, UNETLoader, PathchSageAttentionKJ, INTConstant, INTConstant, PathchSageAttentionKJ, UNETLoader, VAELoader, ModelSamplingSD3, VHS_VideoCombine, RIFE VFI, CLIPTextEncode, CLIPTextEncode, VAEDecode]
patterns: []
missing: [RIFE VFI]
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/纯净万相 Wan2.2-Remix-Comfy-T2V-文生视频 不带lora,带插帧丝滑_2042646743598243841.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/纯净万相 Wan2.2-Remix-Comfy-T2V-文生视频 不带lora,带插帧丝滑_2042646743598243841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（19 个）：
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `EmptyHunyuanLatentVideo`
- `Note`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `INTConstant`
- `INTConstant`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `RIFE VFI`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`ModelSamplingSD3`、`KSamplerAdvanced`、`EmptyHunyuanLatentVideo`、`CLIPLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`INTConstant`、`VAELoader`、`VHS_VideoCombine`、`CLIPTextEncode`、`VAEDecode`

**缺卡**（1）：`RIFE VFI`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、INTConstant

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
