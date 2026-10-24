---
key: 图片生成/图生图/小红书FireRed-Image-Edit1.1（单图、双图、三图编辑）_2029922206393831425.json
name: 小红书FireRed-Image-Edit1.1（单图、双图、三图编辑）_2029922206393831425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-Edit1.1（单图、双图、三图编辑）_2029922206393831425.json
hash: 89593167a2764cec
coverage: 0.882353
learned_at: 2026-10-23 12:49:06
nodes: [Image Comparer (rgthree), Seed (rgthree), CLIPLoader, VAELoader, SaveImage, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, KSampler, VAEDecode, LoadImage, LoadImage, Easy_QwenEdit2509]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 468310134826000, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书FireRed-Image-Edit1.1（单图、双图、三图编辑）_2029922206393831425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书FireRed-Image-Edit1.1（单图、双图、三图编辑）_2029922206393831425.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `Image Comparer (rgthree)`
- `Seed (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `Easy_QwenEdit2509`

## 关键参数

- `seed` = `468310134826000`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`Seed (rgthree)`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`Easy_QwenEdit2509`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、Seed (rgthree)

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
