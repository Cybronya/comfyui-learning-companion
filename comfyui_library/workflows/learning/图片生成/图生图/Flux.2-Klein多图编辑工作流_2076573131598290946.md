---
key: 图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json
name: Flux.2-Klein多图编辑工作流_2076573131598290946
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json
hash: 87b310d80aeddfe3
coverage: 0.958333
learned_at: 2026-10-23 10:58:51
nodes: [CLIPLoader, CLIPTextEncode, ReferenceLatent, UNETLoader, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, VAELoader, KSampler, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, VAEEncode, ReferenceLatent, ReferenceLatent, ImageScaleToTotalPixels, VAEEncode, LoadImage, Image Comparer (rgthree), LoadImage, CLIPTextEncode, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 316229828415739, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Klein多图编辑工作流_2076573131598290946.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `316229828415739`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（23/24）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ReferenceLatent`、`UNETLoader`、`VAEEncode`、`VAELoader`、`KSampler`、`ImageScaleToTotalPixels`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
