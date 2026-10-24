---
key: 图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json
name: FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json
hash: 98f5981e1b6b3b9a
coverage: 0.9375
learned_at: 2026-10-23 10:54:11
nodes: [UNETLoader, CLIPLoader, LoadImage, VAELoader, ReferenceLatent, KSampler, ConditioningZeroOut, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, SeedVR2LoadVAEModel, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, VAEDecode, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 329368434443917, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-4b-单图编辑-标准版-（必收藏）_2052395682006347778.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `VAELoader`
- `ReferenceLatent`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `329368434443917`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoadImage`、`VAELoader`、`ReferenceLatent`、`KSampler`、`ConditioningZeroOut`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`SeedVR2LoadVAEModel`、`SaveImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
