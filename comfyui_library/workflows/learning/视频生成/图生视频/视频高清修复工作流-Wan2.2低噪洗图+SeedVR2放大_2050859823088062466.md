---
key: 视频生成/图生视频/视频高清修复工作流-Wan2.2低噪洗图+SeedVR2放大_2050859823088062466.json
name: 视频高清修复工作流-Wan2.2低噪洗图+SeedVR2放大_2050859823088062466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频高清修复工作流-Wan2.2低噪洗图+SeedVR2放大_2050859823088062466.json
hash: fdaec77566a54803
coverage: 0.958333
learned_at: 2026-10-15 22:37:20
nodes: [UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, KSampler, CLIPTextEncode, CLIPTextEncode, VAEEncode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, SaveImage, ImageFromBatch+, ImageFromBatch+, Image Comparer (rgthree), VHS_LoadVideo, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, ImageConcanate, VHS_VideoCombine, CLIPLoader, VAELoader, VHS_LoadVideo]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 459036920110621, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/视频高清修复工作流-Wan2.2低噪洗图+SeedVR2放大_2050859823088062466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050859823088062466.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `Image Comparer (rgthree)`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_VideoCombine`
- `CLIPLoader`
- `VAELoader`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `459036920110621`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`KSampler`、`CLIPTextEncode`、`VAEEncode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2VideoUpscaler`、`ImageFromBatch+`、`VHS_LoadVideo`、`VHS_VideoCombine`、`VAEDecode`、`ImageConcanate`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
