---
key: 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_1949440813809467394.json
name: WAN2.2 文生视频、图生视频工作流_1949440813809467394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_1949440813809467394.json
hash: 434c7c424b159754
coverage: 0.840909
learned_at: 2026-10-10 23:05:54
nodes: [CLIPLoader, VAEDecode, VAELoader, CLIPLoader, VAELoader, VHS_VideoCombine, Note, Note, CLIPTextEncode, UNETLoader, UNETLoader, UNETLoader, UNETLoader, WanImageToVideo, EmptyHunyuanLatentVideo, KSamplerAdvanced, KSamplerAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, Note, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, KSamplerAdvanced, Note, PathchSageAttentionKJ, ModelPatchTorchSettings, VHS_VideoCombine, VAEDecode, KSamplerAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, Note, ModelSamplingSD3, ModelSamplingSD3, LoadImage, Note, Note, CLIPTextEncode, LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_1949440813809467394.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.2 文生视频、图生视频工作流_1949440813809467394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（44 个）：
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
- `LoadImage`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadVideo`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（37/44）

**有卡**：`CLIPLoader`、`VAEDecode`、`VAELoader`、`VHS_VideoCombine`、`CLIPTextEncode`、`UNETLoader`、`WanImageToVideo`、`EmptyHunyuanLatentVideo`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`LoadImage`、`LoadVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
