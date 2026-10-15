---
key: 视频生成/文生视频/Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001.json
name: Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001.json
hash: 37eb074caf7d6219
coverage: 0.909091
learned_at: 2026-10-15 22:47:11
nodes: [CLIPTextEncode, VAEDecode, CLIPLoader, VAELoader, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, RIFE VFI, PrimitiveStringMultiline, easy int, VHS_VideoCombine, PathchSageAttentionKJ, easy int, CLIPTextEncode, EmptyHunyuanLatentVideo, UNETLoader, UNETLoader, 孤海注释]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 smoothmix v2 文生视频+ 补帧_2064601257079296001.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（22 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `RIFE VFI`
- `PrimitiveStringMultiline`
- `easy int`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `easy int`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `孤海注释`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSamplerAdvanced`、`RIFE VFI`、`easy int`、`VHS_VideoCombine`、`EmptyHunyuanLatentVideo`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo、ModelPatchTorchSettings
