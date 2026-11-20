---
key: 平台全量/视频高清修复 Wan2.2低噪修复洗图+SeedVR2放大_2027280368834973698.json
name: 视频高清修复 Wan2.2低噪修复洗图+SeedVR2放大_2027280368834973698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频高清修复 Wan2.2低噪修复洗图+SeedVR2放大_2027280368834973698.json
hash: 2e1eb5982cecebca
coverage: 0.733333
learned_at: 2026-11-14 02:42:24
nodes: [VAELoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, ModelSamplingSD3, PathchSageAttentionKJ, CLIPLoader, VAEDecode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ImageConcanate, Reroute, Reroute, Reroute, Reroute, Reroute, UNETLoader, LoraLoaderModelOnly, KSampler, VHS_VideoCombine, SeedVR2VideoUpscaler, VHS_LoadVideo, VHS_LoadVideo, ImageFromBatch+, ImageFromBatch+, VHS_VideoCombine, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 1, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/视频高清修复 Wan2.2低噪修复洗图+SeedVR2放大_2027280368834973698.json

> 来源文件 `comfyui_library/workflows/平台全量/视频高清修复 Wan2.2低噪修复洗图+SeedVR2放大_2027280368834973698.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（30 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ImageConcanate`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VHS_VideoCombine`
- `SeedVR2VideoUpscaler`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPLoader`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ImageConcanate`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`VHS_VideoCombine`、`SeedVR2VideoUpscaler`、`VHS_LoadVideo`、`ImageFromBatch+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、SeedVR2LoadDiTModel

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
