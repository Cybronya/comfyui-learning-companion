---
key: 图片生成/文生图/wan2.1_1.3B_self_forcing 超高速高质量视频生成 8帧_2098315061034049537.json
name: wan2.1_1.3B_self_forcing 超高速高质量视频生成 8帧_2098315061034049537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1_1.3B_self_forcing 超高速高质量视频生成 8帧_2098315061034049537.json
hash: a8aebb82a589af94
coverage: 1
learned_at: 2026-10-20 01:35:11
nodes: [CLIPTextEncode, ModelSamplingSD3, EmptyHunyuanLatentVideo, KSampler, VAEDecode, FloatConstant, VAELoader, PathchSageAttentionKJ, PatchModelPatcherOrder, CFGZeroStar, INTConstant, INTConstant, Video_Upscale_With_Model, RIFE VFI, VHS_VideoCombine, UNETLoader, CLIPLoader, VHS_VideoCombine, INTConstant, CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 1046044253153993, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/wan2.1_1.3B_self_forcing 超高速高质量视频生成 8帧_2098315061034049537.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1_1.3B_self_forcing 超高速高质量视频生成 8帧_2098315061034049537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（20 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FloatConstant`
- `VAELoader`
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `CFGZeroStar`
- `INTConstant`
- `INTConstant`
- `Video_Upscale_With_Model`
- `RIFE VFI`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `INTConstant`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `1046044253153993`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`KSampler`、`VAEDecode`、`FloatConstant`、`VAELoader`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`CFGZeroStar`、`INTConstant`、`Video_Upscale_With_Model`、`RIFE VFI`、`VHS_VideoCombine`、`UNETLoader`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGZeroStar、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
