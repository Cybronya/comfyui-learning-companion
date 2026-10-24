---
key: 图片生成/图生图/动漫转真人Qwen-Image真实感洗图 Qwen-image-edit_2048279564601794562.json
name: 动漫转真人Qwen-Image真实感洗图 Qwen-image-edit_2048279564601794562
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/动漫转真人Qwen-Image真实感洗图 Qwen-image-edit_2048279564601794562.json
hash: de464f5d0bb877e5
coverage: 0.641509
learned_at: 2026-10-23 12:27:47
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, TextEncodeQwenImageEdit, Reroute, Reroute, Reroute, Reroute, Reroute, UNETLoader, CLIPLoader, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, Reroute, VAELoader, Reroute, UNETLoader, CLIPTextEncode, ConditioningZeroOut, VAELoader, ImageScaleBy, VAEDecode, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, easy clearCacheAll, KSampler, KSampler, CLIPLoader, ImageScaleToTotalPixels, VAEEncode, LoraLoaderModelOnly, KSampler, easy showAnything, easy showAnything, WD14Tagger|pysssss, JoinStrings, VAEDecode, GetNode, Qwen3_VQA, GetNode, TextEncodeQwenImageEditPlus, SaveImage, ShowText|pysssss, Fast Groups Bypasser (rgthree), LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2m", "scheduler": "sgm_uniform", "seed": 603427042170078, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/动漫转真人Qwen-Image真实感洗图 Qwen-image-edit_2048279564601794562.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/动漫转真人Qwen-Image真实感洗图 Qwen-image-edit_2048279564601794562.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEdit`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `VAELoader`
- `Reroute`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `ImageScaleBy`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `easy clearCacheAll`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `easy showAnything`
- `easy showAnything`
- `WD14Tagger|pysssss`
- `JoinStrings`
- `VAEDecode` ★核心
- `GetNode`
- `Qwen3_VQA`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `603427042170078`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **64%**（34/53）

**有卡**：`TextEncodeQwenImageEdit`、`UNETLoader`、`CLIPLoader`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ImageScaleBy`、`VAEDecode`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`easy clearCacheAll`、`KSampler`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`WD14Tagger|pysssss`、`JoinStrings`、`Qwen3_VQA`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
