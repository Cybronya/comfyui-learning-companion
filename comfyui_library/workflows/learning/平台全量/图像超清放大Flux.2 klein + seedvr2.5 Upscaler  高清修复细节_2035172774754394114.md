---
key: 平台全量/图像超清放大Flux.2 klein + seedvr2.5 Upscaler  高清修复细节_2035172774754394114.json
name: 图像超清放大Flux.2 klein + seedvr2.5 Upscaler  高清修复细节_2035172774754394114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/图像超清放大Flux.2 klein + seedvr2.5 Upscaler  高清修复细节_2035172774754394114.json
hash: 9ddeeb1534fd10e5
coverage: 0.869565
learned_at: 2026-11-14 01:53:53
nodes: [GetImageSizeAndCount, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio V2, ImageScale, SeedVR2VideoUpscaler, TilePreprocessor, Anything Everywhere, CLIPLoader, UNETLoader, CFGGuider, Anything Everywhere, RepeatLatentBatch, RebatchLatents, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, BasicScheduler, VAEEncode, LayerFilter: FilmV2, ImageSmartSharpen+, ImagePass, Any Switch (rgthree), Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), Image H264 Compression (mtb), SaveImage, RandomNoise, KSamplerSelect, VAELoader, Anything Everywhere, LoraLoaderModelOnly, LoraLoaderModelOnly, LG_Color_Match_V2, INTConstant, LoadImage, CLIPTextEncode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, ConditioningZeroOut, VAEDecode, easy cleanGpuUsed]
patterns: []
missing: []
---

# 平台全量/图像超清放大Flux.2 klein + seedvr2.5 Upscaler  高清修复细节_2035172774754394114.json

> 来源文件 `comfyui_library/workflows/平台全量/图像超清放大Flux.2 klein + seedvr2.5 Upscaler  高清修复细节_2035172774754394114.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `GetImageSizeAndCount`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScale`
- `SeedVR2VideoUpscaler`
- `TilePreprocessor`
- `Anything Everywhere`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CFGGuider`
- `Anything Everywhere`
- `RepeatLatentBatch`
- `RebatchLatents`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BasicScheduler`
- `VAEEncode` ★核心
- `LayerFilter: FilmV2`
- `ImageSmartSharpen+`
- `ImagePass`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image H264 Compression (mtb)`
- `SaveImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAELoader`
- `Anything Everywhere`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LG_Color_Match_V2`
- `INTConstant`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`GetImageSizeAndCount`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScale`、`SeedVR2VideoUpscaler`、`TilePreprocessor`、`CLIPLoader`、`UNETLoader`、`CFGGuider`、`RepeatLatentBatch`、`RebatchLatents`、`SamplerCustomAdvanced`、`VAEEncode`、`ReferenceLatent`、`BasicScheduler`、`LayerFilter: FilmV2`、`ImageSmartSharpen+`、`ImagePass`、`SaveImage`、`Image H264 Compression (mtb)`、`RandomNoise`、`KSamplerSelect`、`VAELoader`、`LoraLoaderModelOnly`、`LG_Color_Match_V2`、`INTConstant`、`LoadImage`、`CLIPTextEncode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`ConditioningZeroOut`、`VAEDecode`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
