---
key: 平台全量/视频高清放大修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 视频高清放大_2016358403949469697.json
name: 视频高清放大修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 视频高清放大_2016358403949469697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频高清放大修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 视频高清放大_2016358403949469697.json
hash: 9c82d05f0d885c8a
coverage: 0.684211
learned_at: 2026-11-14 02:43:11
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfoSource, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), PreviewImage, SeedVR2LoadVAEModel, GetNode, Int, Int, SetNode, GetNode, GetNode, VHS_LoadVideo, SeedVR2VideoUpscaler, VHS_VideoCombine, SeedVR2LoadDiTModel, VAELoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, VAEEncode, ModelSamplingSD3, PathchSageAttentionKJ, easy cleanGpuUsed, CLIPLoader, LoraLoaderModelOnly, VAEDecode, KSampler, VHS_VideoCombine, easy cleanGpuUsed, ImageConcanate, VHS_VideoCombine, VHS_LoadVideo, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/视频高清放大修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 视频高清放大_2016358403949469697.json

> 来源文件 `comfyui_library/workflows/平台全量/视频高清放大修复  Wan2.2低噪洗图+SeedVR2放大 视频补帧放大 视频高清放大_2016358403949469697.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoSource`
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `GetNode`
- `Int`
- `Int`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `SeedVR2VideoUpscaler`
- `VHS_VideoCombine`
- `SeedVR2LoadDiTModel`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `1`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **68%**（26/38）

**有卡**：`VHS_VideoInfoSource`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`Int`、`VHS_LoadVideo`、`SeedVR2VideoUpscaler`、`VHS_VideoCombine`、`SeedVR2LoadDiTModel`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`VAEEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`easy cleanGpuUsed`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`KSampler`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
