---
key: 图片生成/图生图/B妮B妳-N_S_F_W_系列-DarkBeast-Klein9b-BFS_2033122326463651841.json
name: B妮B妳-N_S_F_W_系列-DarkBeast-Klein9b-BFS_2033122326463651841
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/B妮B妳-N_S_F_W_系列-DarkBeast-Klein9b-BFS_2033122326463651841.json
hash: 65d7e533ff85b036
coverage: 0.88
learned_at: 2026-10-23 10:51:43
nodes: [ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ImageScaleToTotalPixels, LoadImage, VAEEncode, LoadImage, CLIPLoader, UNETLoader, LayerUtility: PurgeVRAM V2, VAEDecode, Reroute, KSampler, EmptyFlux2LatentImage, ConditioningZeroOut, GetImageSize, VAELoader, ImageScaleToTotalPixels, Note, CLIPTextEncode, Image Comparer (rgthree), SaveImage, HAIGC_SaveImagesToZip]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 56161982989352, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/B妮B妳-N_S_F_W_系列-DarkBeast-Klein9b-BFS_2033122326463651841.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/B妮B妳-N_S_F_W_系列-DarkBeast-Klein9b-BFS_2033122326463651841.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `VAEEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `Reroute`
- `KSampler` ★核心
- `EmptyFlux2LatentImage`
- `ConditioningZeroOut`
- `GetImageSize`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `Note`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `HAIGC_SaveImagesToZip`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `56161982989352`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`ReferenceLatent`、`VAEEncode`、`ImageScaleToTotalPixels`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`KSampler`、`EmptyFlux2LatentImage`、`ConditioningZeroOut`、`GetImageSize`、`VAELoader`、`CLIPTextEncode`、`SaveImage`、`HAIGC_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
