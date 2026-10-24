---
key: 图片生成/图生图/Qwen.图生图-加速高清放大_1988499224629264385.json
name: Qwen.图生图-加速高清放大_1988499224629264385
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen.图生图-加速高清放大_1988499224629264385.json
hash: 895625f3d5e22e2a
coverage: 0.807692
learned_at: 2026-10-23 11:19:02
nodes: [ConditioningZeroOut, VAEDecode, PreviewImage, Image Comparer (rgthree), SaveImage, VAEDecode, Reroute, VAEEncode, Seed Everywhere, PreviewImage, CLIPLoader, UNETLoader, ImageScaleBy, Fast Groups Bypasser (rgthree), VAELoader, VAEEncode, JWImageResizeByLongerSide, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, LoadImage, CLIPTextEncode, CFGNorm]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 852446921997554, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen.图生图-加速高清放大_1988499224629264385.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen.图生图-加速高清放大_1988499224629264385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `Reroute`
- `VAEEncode` ★核心
- `Seed Everywhere`
- `PreviewImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ImageScaleBy`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `VAEEncode` ★核心
- `JWImageResizeByLongerSide`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CFGNorm`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `852446921997554`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`VAEEncode`、`Seed Everywhere`、`CLIPLoader`、`UNETLoader`、`ImageScaleBy`、`VAELoader`、`JWImageResizeByLongerSide`、`KSampler`、`LoraLoaderModelOnly`、`LoadImage`、`CLIPTextEncode`、`CFGNorm`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
