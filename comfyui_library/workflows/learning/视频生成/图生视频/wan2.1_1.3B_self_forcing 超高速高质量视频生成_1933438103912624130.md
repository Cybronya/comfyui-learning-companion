---
key: 视频生成/图生视频/wan2.1_1.3B_self_forcing 超高速高质量视频生成_1933438103912624130.json
name: wan2.1_1.3B_self_forcing 超高速高质量视频生成_1933438103912624130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1_1.3B_self_forcing 超高速高质量视频生成_1933438103912624130.json
hash: b3c72ba9b81a5252
coverage: 1
learned_at: 2026-10-15 22:30:13
nodes: [CLIPTextEncode, ModelSamplingSD3, EmptyHunyuanLatentVideo, KSampler, VAEDecode, INTConstant, FloatConstant, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader, PathchSageAttentionKJ, PatchModelPatcherOrder, CFGZeroStar, INTConstant, INTConstant, VHS_VideoCombine, Video_Upscale_With_Model, RIFE VFI, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 152071707697057, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/wan2.1_1.3B_self_forcing 超高速高质量视频生成_1933438103912624130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933438103912624130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `FloatConstant`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `CFGZeroStar`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `Video_Upscale_With_Model`
- `RIFE VFI`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `152071707697057`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`KSampler`、`VAEDecode`、`INTConstant`、`FloatConstant`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`CFGZeroStar`、`VHS_VideoCombine`、`Video_Upscale_With_Model`、`RIFE VFI`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStar、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
