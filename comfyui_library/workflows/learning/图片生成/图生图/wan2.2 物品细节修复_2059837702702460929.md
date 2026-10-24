---
key: 图片生成/图生图/wan2.2 物品细节修复_2059837702702460929.json
name: wan2.2 物品细节修复_2059837702702460929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2 物品细节修复_2059837702702460929.json
hash: c8db2db4054d887c
coverage: 0.869565
learned_at: 2026-10-23 11:45:55
nodes: [easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, VAEEncode, ImageUpscaleWithModel, ImageResize+, UNETLoader, LoraLoaderModelOnly, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, Note, Float, UpscaleModelLoader, VAELoader, ImpactInt, SaveImage, Note, LoadImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.05, "sampler_name": "euler", "scheduler": "simple", "seed": 341483423109670, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/wan2.2 物品细节修复_2059837702702460929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2 物品细节修复_2059837702702460929.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `ImageUpscaleWithModel`
- `ImageResize+`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Note`
- `Float`
- `UpscaleModelLoader`
- `VAELoader`
- `ImpactInt`
- `SaveImage`
- `Note`
- `LoadImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `341483423109670`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.05`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`easy cleanGpuUsed`、`easy clearCacheAll`、`VAEEncode`、`ImageUpscaleWithModel`、`ImageResize+`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`Float`、`UpscaleModelLoader`、`VAELoader`、`ImpactInt`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
