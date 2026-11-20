---
key: 平台全量/最强动漫转真人 Qwen+Z-Image Base二次元转真人  真实感洗图 SeedVR 高清放大_2016790797810667522.json
name: 最强动漫转真人 Qwen+Z-Image Base二次元转真人  真实感洗图 SeedVR 高清放大_2016790797810667522
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/最强动漫转真人 Qwen+Z-Image Base二次元转真人  真实感洗图 SeedVR 高清放大_2016790797810667522.json
hash: 8369d3494c4ce431
coverage: 0.729167
learned_at: 2026-11-14 02:14:29
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, UNETLoader, LayerUtility: PurgeVRAM V2, easy cleanGpuUsed, VAELoader, ImageScaleBy, easy cleanGpuUsed, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, easy showAnything, SaveImage, ImageScaleToTotalPixels, SetNode, GetNode, WD14Tagger|pysssss, CLIPLoader, LoraLoaderModelOnly, GetNode, KSampler, Fast Groups Bypasser (rgthree), UNETLoader, VAEDecode, CLIPLoader, VAELoader, TextEncodeQwenImageEdit, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, JoinStrings, easy showAnything, ShowText|pysssss, CLIPTextEncode, ConditioningZeroOut, VAEEncode, KSampler, KSampler, LayerUtility: PurgeVRAM V2, easy clearCacheAll, VAEDecode, Fast Groups Bypasser (rgthree), LoadImage, TextEncodeQwenImageEditPlus, Qwen3_VQA, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.6, "denoise": 0.3500000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 210, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/最强动漫转真人 Qwen+Z-Image Base二次元转真人  真实感洗图 SeedVR 高清放大_2016790797810667522.json

> 来源文件 `comfyui_library/workflows/平台全量/最强动漫转真人 Qwen+Z-Image Base二次元转真人  真实感洗图 SeedVR 高清放大_2016790797810667522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `easy cleanGpuUsed`
- `VAELoader`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `easy showAnything`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `WD14Tagger|pysssss`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEdit`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JoinStrings`
- `easy showAnything`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `Qwen3_VQA`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `210`
- `steps` = `10`
- `cfg` = `1.6`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **73%**（35/48）

**有卡**：`UNETLoader`、`LayerUtility: PurgeVRAM V2`、`easy cleanGpuUsed`、`VAELoader`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`ImageScaleToTotalPixels`、`WD14Tagger|pysssss`、`CLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`TextEncodeQwenImageEdit`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`JoinStrings`、`CLIPTextEncode`、`ConditioningZeroOut`、`easy clearCacheAll`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
