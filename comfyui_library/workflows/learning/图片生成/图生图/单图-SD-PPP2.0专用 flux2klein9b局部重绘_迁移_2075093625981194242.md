---
key: 图片生成/图生图/单图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075093625981194242.json
name: 单图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075093625981194242
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075093625981194242.json
hash: f7811cb66f8fa417
coverage: 0.9375
learned_at: 2026-10-23 12:32:03
nodes: [LoadImage, Int, Text Multiline, CLIPLoader, ReferenceLatent, Kontext Inpainting Conditioning, ConditioningZeroOut, KSampler, UNETLoader, SaveImage, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), VAEEncode, CLIPTextEncode, VAELoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 426759133830007, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/单图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075093625981194242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图-SD-PPP2.0专用 flux2klein9b局部重绘_迁移_2075093625981194242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `LoadImage`
- `Int`
- `Text Multiline`
- `CLIPLoader`
- `ReferenceLatent`
- `Kontext Inpainting Conditioning`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `426759133830007`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`LoadImage`、`Int`、`Text Multiline`、`CLIPLoader`、`ReferenceLatent`、`Kontext Inpainting Conditioning`、`ConditioningZeroOut`、`KSampler`、`UNETLoader`、`SaveImage`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`CLIPTextEncode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
