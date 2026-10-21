---
key: 图片生成/文生图/工作流基础系列20-Flux.1文生图_图生图_局部重绘工作流_2047848807601278978.json
name: 工作流基础系列20-Flux.1文生图_图生图_局部重绘工作流_2047848807601278978
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/工作流基础系列20-Flux.1文生图_图生图_局部重绘工作流_2047848807601278978.json
hash: 743071c08a28d059
coverage: 0.857143
learned_at: 2026-10-21 02:59:55
nodes: [VAEDecode, KSampler, VAELoader, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), PreviewImage, FluxGuidance, UNETLoader, CLIPTextEncode, VAELoader, CLIPTextEncode, ConditioningZeroOut, FluxGuidance, VAEDecode, PreviewImage, LoadImage, KSampler, Seed (rgthree), DualCLIPLoader, VAELoader, Seed (rgthree), CLIPTextEncode, FluxGuidance, ConditioningZeroOut, KSampler, UNETLoader, PreviewImage, UltimateSDUpscale, DualCLIPLoader, EmptySD3LatentImage, Seed (rgthree), LoadImage, UNETLoader, VAEEncode, Image Comparer (rgthree), VAEDecode, UpscaleModelLoader, SaveImage, VAEEncode, SetLatentNoiseMask, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 423831166134004, "steps": 20}
---

# 图片生成/文生图/工作流基础系列20-Flux.1文生图_图生图_局部重绘工作流_2047848807601278978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/工作流基础系列20-Flux.1文生图_图生图_局部重绘工作流_2047848807601278978.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `FluxGuidance`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`
- `KSampler` ★核心
- `Seed (rgthree)`
- `DualCLIPLoader`
- `VAELoader`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `UltimateSDUpscale`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Seed (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `SaveImage`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `423831166134004`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`VAEDecode`、`KSampler`、`VAELoader`、`ConditioningZeroOut`、`DualCLIPLoader`、`FluxGuidance`、`UNETLoader`、`CLIPTextEncode`、`LoadImage`、`Seed (rgthree)`、`UltimateSDUpscale`、`EmptySD3LatentImage`、`VAEEncode`、`UpscaleModelLoader`、`SaveImage`、`SetLatentNoiseMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
