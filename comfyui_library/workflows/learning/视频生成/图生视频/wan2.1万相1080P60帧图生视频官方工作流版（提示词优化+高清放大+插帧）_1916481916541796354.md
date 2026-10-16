---
key: 视频生成/图生视频/wan2.1万相1080P60帧图生视频官方工作流版（提示词优化+高清放大+插帧）_1916481916541796354.json
name: wan2.1万相1080P60帧图生视频官方工作流版（提示词优化+高清放大+插帧）_1916481916541796354.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1916481916541796354.json
hash: 31152cdcde687e45
coverage: 0.913043
learned_at: 2026-10-15 22:29:38
nodes: [CLIPLoader, CLIPTextEncode, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, GetImageSize, WanImageToVideo, ModelSamplingSD3, VAELoader, UNETLoader, SkipLayerGuidanceWanVideo, VAEDecodeTiled, UpscaleImageByUsingModel, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, Int, JjkText, LoadImage, easy showAnything, WanVideoTeaCacheKJ, RHHiddenNodes, KSampler]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 865840747523374, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.1万相1080P60帧图生视频官方工作流版（提示词优化+高清放大+插帧）_1916481916541796354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1916481916541796354.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（23 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `GetImageSize`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `VAELoader`
- `UNETLoader` ★核心
- `SkipLayerGuidanceWanVideo`
- `VAEDecodeTiled` ★核心
- `UpscaleImageByUsingModel`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `Int`
- `JjkText`
- `LoadImage`
- `easy showAnything`
- `WanVideoTeaCacheKJ`
- `RHHiddenNodes`
- `KSampler` ★核心

## 关键参数

- `seed` = `865840747523374`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`CLIPVisionEncode`、`GetImageSize`、`WanImageToVideo`、`ModelSamplingSD3`、`VAELoader`、`UNETLoader`、`SkipLayerGuidanceWanVideo`、`VAEDecodeTiled`、`UpscaleImageByUsingModel`、`RIFE VFI`、`UpscaleModelLoader`、`VHS_VideoCombine`、`Int`、`LoadImage`、`WanVideoTeaCacheKJ`、`RHHiddenNodes`、`KSampler`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SkipLayerGuidanceWanVideo、VAEDecodeTiled

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
