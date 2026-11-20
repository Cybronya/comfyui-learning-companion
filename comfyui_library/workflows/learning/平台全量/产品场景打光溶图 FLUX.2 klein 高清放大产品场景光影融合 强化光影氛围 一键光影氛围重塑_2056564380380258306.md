---
key: 平台全量/产品场景打光溶图 FLUX.2 klein 高清放大产品场景光影融合 强化光影氛围 一键光影氛围重塑_2056564380380258306.json
name: 产品场景打光溶图 FLUX.2 klein 高清放大产品场景光影融合 强化光影氛围 一键光影氛围重塑_2056564380380258306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/产品场景打光溶图 FLUX.2 klein 高清放大产品场景光影融合 强化光影氛围 一键光影氛围重塑_2056564380380258306.json
hash: 6fa0347b7dcdf07f
coverage: 0.916667
learned_at: 2026-11-14 01:34:58
nodes: [CLIPLoader, VAELoader, UNETLoader, PainterFluxImageEdit, KSampler, GetImageSize+, Image Comparer (rgthree), ResizeImagesByLongerEdge, VAEDecode, SaveImage, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 0.7000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 131502043306118, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/产品场景打光溶图 FLUX.2 klein 高清放大产品场景光影融合 强化光影氛围 一键光影氛围重塑_2056564380380258306.json

> 来源文件 `comfyui_library/workflows/平台全量/产品场景打光溶图 FLUX.2 klein 高清放大产品场景光影融合 强化光影氛围 一键光影氛围重塑_2056564380380258306.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `PainterFluxImageEdit`
- `KSampler` ★核心
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ResizeImagesByLongerEdge`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 关键参数

- `seed` = `131502043306118`
- `steps` = `5`
- `cfg` = `0.7000000000000001`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`PainterFluxImageEdit`、`KSampler`、`GetImageSize+`、`ResizeImagesByLongerEdge`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
