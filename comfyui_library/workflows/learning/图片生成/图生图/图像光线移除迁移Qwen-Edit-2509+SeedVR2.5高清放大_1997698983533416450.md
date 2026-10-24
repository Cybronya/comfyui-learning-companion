---
key: 图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json
name: 图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json
hash: 9dd730f1d68732c4
coverage: 0.925926
learned_at: 2026-10-23 12:38:10
nodes: [ModelSamplingAuraFlow, VAELoader, CLIPLoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEDecode, ImageScaleBy, LayerUtility: PurgeVRAM V2, SeedVR2LoadVAEModel, TextEncodeQwenImageEditPlus, ConditioningZeroOut, KSampler, SaveImage, SeedVR2LoadDiTModel, Fast Groups Muter (rgthree), Note, Int, LoraLoaderModelOnly, SeedVR2VideoUpscaler, LoadImage, VAEEncode, UNETLoader, LoraLoaderModelOnly, LoadImage, easy imageConcat, easy imageConcat, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 136614790253745, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像光线移除迁移Qwen-Edit-2509+SeedVR2.5高清放大_1997698983533416450.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ModelSamplingAuraFlow`
- `VAELoader`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2LoadVAEModel`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `Fast Groups Muter (rgthree)`
- `Note`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy imageConcat`
- `easy imageConcat`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `136614790253745`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`ModelSamplingAuraFlow`、`VAELoader`、`CLIPLoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`ImageScaleBy`、`LayerUtility: PurgeVRAM V2`、`SeedVR2LoadVAEModel`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`KSampler`、`SaveImage`、`SeedVR2LoadDiTModel`、`Int`、`LoraLoaderModelOnly`、`SeedVR2VideoUpscaler`、`LoadImage`、`VAEEncode`、`UNETLoader`、`easy imageConcat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
