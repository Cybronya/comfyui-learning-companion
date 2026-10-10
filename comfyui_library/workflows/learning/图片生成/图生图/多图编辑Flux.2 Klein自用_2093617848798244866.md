---
key: 图片生成/图生图/多图编辑Flux.2 Klein自用_2093617848798244866.json
name: 多图编辑Flux.2 Klein自用_2093617848798244866
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑Flux.2 Klein自用_2093617848798244866.json
hash: 1ae7643e6a2b5bf2
coverage: 0.92
learned_at: 2026-10-10 20:48:16
nodes: [LoadImage, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, VAEEncode, ImageScale, VAELoader, CLIPLoader, KSampler, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, VAEEncode, VAEDecode, GetImageSize, LayerUtility: PurgeVRAM V2, SaveImage, SeedVR2, CFGNorm, UNETLoader, LoadImage, SDXL Empty Latent Image (rgthree), ImageScale, LoadImage, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: [LayerUtility: PurgeVRAM V2, SDXL Empty Latent Image (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 524766721205993, "steps": 5}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `SDXL Empty Latent Image (rgthree)` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多图编辑Flux.2 Klein自用_2093617848798244866.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑Flux.2 Klein自用_2093617848798244866.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScale`
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `SeedVR2`
- `CFGNorm`
- `UNETLoader` ★核心
- `LoadImage`
- `SDXL Empty Latent Image (rgthree)`
- `ImageScale`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `524766721205993`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`LoadImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`ReferenceLatent`、`ImageScale`、`VAELoader`、`CLIPLoader`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`GetImageSize`、`SaveImage`、`SeedVR2`、`CFGNorm`、`UNETLoader`、`TextEncodeQwenImageEditPlus`

**缺卡**（2）：`LayerUtility: PurgeVRAM V2`、`SDXL Empty Latent Image (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SDXL Empty Latent Image (rgthree)` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
