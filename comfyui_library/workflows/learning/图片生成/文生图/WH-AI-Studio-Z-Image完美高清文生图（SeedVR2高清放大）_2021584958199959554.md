---
key: 图片生成/文生图/WH-AI-Studio-Z-Image完美高清文生图（SeedVR2高清放大）_2021584958199959554.json
name: WH-AI-Studio-Z-Image完美高清文生图（SeedVR2高清放大）_2021584958199959554
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WH-AI-Studio-Z-Image完美高清文生图（SeedVR2高清放大）_2021584958199959554.json
hash: 4ead17d6176bccae
coverage: 0.909091
learned_at: 2026-10-19 22:29:55
nodes: [PreviewImage, TTP_Image_Tile_Batch, TTP_Image_Assy, Get Image Size, ImpactMinMax, SeedVR2, ImageCASharpening+, easy cleanGpuUsed, ImageResize+, ImageCASharpening+, ColorMatch, Image Comparer (rgthree), SaveImage, KSampler, ImageResize+, CLIPLoader, VAELoader, ConditioningZeroOut, EmptyLatentImage, CLIPTextEncode, UNETLoader, VAEDecode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 60031329223066, "steps": 9, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/WH-AI-Studio-Z-Image完美高清文生图（SeedVR2高清放大）_2021584958199959554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WH-AI-Studio-Z-Image完美高清文生图（SeedVR2高清放大）_2021584958199959554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `Get Image Size`
- `ImpactMinMax`
- `SeedVR2`
- `ImageCASharpening+`
- `easy cleanGpuUsed`
- `ImageResize+`
- `ImageCASharpening+`
- `ColorMatch`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `ImageResize+`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `60031329223066`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`Get Image Size`、`ImpactMinMax`、`SeedVR2`、`ImageCASharpening+`、`easy cleanGpuUsed`、`ImageResize+`、`ColorMatch`、`SaveImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`EmptyLatentImage`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
