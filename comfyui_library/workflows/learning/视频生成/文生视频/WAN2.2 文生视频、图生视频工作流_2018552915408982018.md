---
key: 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json
name: WAN2.2 文生视频、图生视频工作流_2018552915408982018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json
hash: 7dbb8445312c7292
coverage: 0.857143
learned_at: 2026-10-11 03:16:49
nodes: [CLIPLoader, VAEDecode, VAELoader, CLIPLoader, VAELoader, VHS_VideoCombine, Note, Note, CLIPTextEncode, UNETLoader, UNETLoader, UNETLoader, UNETLoader, WanImageToVideo, EmptyHunyuanLatentVideo, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, Note, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, KSamplerAdvanced, Note, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, Note, ModelSamplingSD3, ModelSamplingSD3, Note, CLIPTextEncode, LoadVideo, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_2018552915408982018.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（42 个）：
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `WanImageToVideo`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Note`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Note`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadVideo`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`CLIPLoader`、`VAEDecode`、`VAELoader`、`VHS_VideoCombine`、`CLIPTextEncode`、`UNETLoader`、`WanImageToVideo`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`LoadVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
