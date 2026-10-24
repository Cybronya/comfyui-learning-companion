---
key: 图片生成/图生图/一键精修+超清放大One-click+retouching+++ultra-high+definit_2043887145068273666.json
name: 一键精修+超清放大One-click+retouching+++ultra-high+definit_2043887145068273666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键精修+超清放大One-click+retouching+++ultra-high+definit_2043887145068273666.json
hash: 217c4610a2859f51
coverage: 0.823529
learned_at: 2026-10-23 11:58:30
nodes: [Int Literal, LayerUtility: ImageScaleByAspectRatio V2, PainterFluxImageEdit, SaveImage, LoadImage, Anything Everywhere3, CLIPLoader, UNETLoader, VAELoader, SeedVR2ExtraArgs, KSampler, MemoryCleaner, VAEDecode, Image Comparer (rgthree), SaveImage, MarkdownNote, SeedVR2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 357584505875863, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/一键精修+超清放大One-click+retouching+++ultra-high+definit_2043887145068273666.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键精修+超清放大One-click+retouching+++ultra-high+definit_2043887145068273666.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `Int Literal`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PainterFluxImageEdit`
- `SaveImage`
- `LoadImage`
- `Anything Everywhere3`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `SeedVR2ExtraArgs`
- `KSampler` ★核心
- `MemoryCleaner`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `MarkdownNote`
- `SeedVR2`

## 关键参数

- `seed` = `357584505875863`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`Int Literal`、`LayerUtility: ImageScaleByAspectRatio V2`、`PainterFluxImageEdit`、`SaveImage`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`SeedVR2ExtraArgs`、`KSampler`、`MemoryCleaner`、`VAEDecode`、`SeedVR2`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、LoadImage、SeedVR2、SeedVR2ExtraArgs

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
