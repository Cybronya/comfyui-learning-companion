---
key: 图片生成/文生图/🈚️造相 Z-image+DyPE+seedvr2.5 文生图+反推 4k大图_2004964277360492545.json
name: 🈚️造相 Z-image+DyPE+seedvr2.5 文生图+反推 4k大图_2004964277360492545
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🈚️造相 Z-image+DyPE+seedvr2.5 文生图+反推 4k大图_2004964277360492545.json
hash: 27a1c2c42613e2fc
coverage: 0.614035
learned_at: 2026-10-19 22:01:48
nodes: [easy cleanGpuUsed, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, easy showAnything, GetNode, SetNode, SetNode, SetNode, easy seed, GetNode, Anything Everywhere, Anything Everywhere, ConditioningZeroOut, VAELoader, Text, ImpactSwitch, UNETLoader, GetNode, GetNode, ImageSmartSharpen+, GetNode, ImageSmartSharpen+, SeedVarianceEnhancer, CLIPTextEncode, GetNode, CLIPLoader, ImpactSwitch, SubtitleTextProcessor, easy promptLine, SetNode, GetNode, GetNode, JWInteger, JWInteger, SetNode, GetNode, DyPE_FLUX, VAEDecodeTiled, AILab_QwenVL, SetNode, Image H264 Compression (mtb), LayerFilter: FilmV2, LayerUtility: ImageScaleByAspectRatio V2, ImageScale, EmptyLatentImage, SeedVR2VideoUpscaler, LoadImage, SeedVR2LoadVAEModel, KSampler, SeedVR2LoadDiTModel, LoraLoaderModelOnly, SaveImage, SaveImage, easy int, easy cleanGpuUsed, TilePreprocessor]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 3, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 124828871572742, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/文生图/🈚️造相 Z-image+DyPE+seedvr2.5 文生图+反推 4k大图_2004964277360492545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/🈚️造相 Z-image+DyPE+seedvr2.5 文生图+反推 4k大图_2004964277360492545.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `easy cleanGpuUsed`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy seed`
- `GetNode`
- `Anything Everywhere`
- `Anything Everywhere`
- `ConditioningZeroOut`
- `VAELoader`
- `Text`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `ImageSmartSharpen+`
- `SeedVarianceEnhancer`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPLoader`
- `ImpactSwitch`
- `SubtitleTextProcessor`
- `easy promptLine`
- `SetNode`
- `GetNode`
- `GetNode`
- `JWInteger`
- `JWInteger`
- `SetNode`
- `GetNode`
- `DyPE_FLUX`
- `VAEDecodeTiled` ★核心
- `AILab_QwenVL`
- `SetNode`
- `Image H264 Compression (mtb)`
- `LayerFilter: FilmV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScale`
- `EmptyLatentImage` ★核心
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `KSampler` ★核心
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `easy int`
- `easy cleanGpuUsed`
- `TilePreprocessor`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `3`
- `seed` = `124828871572742`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **61%**（35/57）

**有卡**：`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy seed`、`ConditioningZeroOut`、`VAELoader`、`Text`、`UNETLoader`、`ImageSmartSharpen+`、`SeedVarianceEnhancer`、`CLIPTextEncode`、`CLIPLoader`、`SubtitleTextProcessor`、`easy promptLine`、`JWInteger`、`DyPE_FLUX`、`VAEDecodeTiled`、`AILab_QwenVL`、`Image H264 Compression (mtb)`、`LayerFilter: FilmV2`、`ImageScale`、`EmptyLatentImage`、`SeedVR2VideoUpscaler`、`LoadImage`、`SeedVR2LoadVAEModel`、`KSampler`、`SeedVR2LoadDiTModel`、`LoraLoaderModelOnly`、`SaveImage`、`easy int`、`TilePreprocessor`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
