---
key: 平台全量/Edit R2i模糊图像超高清放大 Flux2 klein +Seedvr2.5 Upscaler_2033050185214988289.json
name: Edit R2i模糊图像超高清放大 Flux2 klein +Seedvr2.5 Upscaler_2033050185214988289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Edit R2i模糊图像超高清放大 Flux2 klein +Seedvr2.5 Upscaler_2033050185214988289.json
hash: f7e2296e5cd3a1f5
coverage: 0.869565
learned_at: 2026-11-14 00:23:59
nodes: [SeedVR2LoadVAEModel, GetImageSizeAndCount, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, Bjornulf_ShowInt, LayerUtility: ImageScaleByAspectRatio V2, ImageScale, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, TilePreprocessor, CFGGuider, RepeatLatentBatch, RebatchLatents, SamplerCustomAdvanced, VAEEncode, ReferenceLatent, LayerUtility: ImageScaleByAspectRatio V2, BasicScheduler, VAEEncode, ImageSmartSharpen+, LoraLoaderModelOnly, ImagePass, RandomNoise, Image Comparer (rgthree), Image Comparer (rgthree), Image H264 Compression (mtb), LayerFilter: FilmV2, ConditioningZeroOut, VAELoader, CLIPLoader, Anything Everywhere, Anything Everywhere, easy cleanGpuUsed, VAEDecode, Any Switch (rgthree), LoraLoaderModelOnly, Anything Everywhere, UNETLoader, KSamplerSelect, INTConstant, LoadImage, CLIPTextEncode, SaveImage, easy imageColorMatch, SaveImage]
patterns: []
missing: []
---

# 平台全量/Edit R2i模糊图像超高清放大 Flux2 klein +Seedvr2.5 Upscaler_2033050185214988289.json

> 来源文件 `comfyui_library/workflows/平台全量/Edit R2i模糊图像超高清放大 Flux2 klein +Seedvr2.5 Upscaler_2033050185214988289.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `SeedVR2LoadVAEModel`
- `GetImageSizeAndCount`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScale`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `TilePreprocessor`
- `CFGGuider`
- `RepeatLatentBatch`
- `RebatchLatents`
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BasicScheduler`
- `VAEEncode` ★核心
- `ImageSmartSharpen+`
- `LoraLoaderModelOnly` ★核心
- `ImagePass`
- `RandomNoise`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image H264 Compression (mtb)`
- `LayerFilter: FilmV2`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `INTConstant`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `easy imageColorMatch`
- `SaveImage`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`SeedVR2LoadVAEModel`、`GetImageSizeAndCount`、`Bjornulf_ShowInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScale`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`TilePreprocessor`、`CFGGuider`、`RepeatLatentBatch`、`RebatchLatents`、`SamplerCustomAdvanced`、`VAEEncode`、`ReferenceLatent`、`BasicScheduler`、`ImageSmartSharpen+`、`LoraLoaderModelOnly`、`ImagePass`、`RandomNoise`、`Image H264 Compression (mtb)`、`LayerFilter: FilmV2`、`ConditioningZeroOut`、`VAELoader`、`CLIPLoader`、`easy cleanGpuUsed`、`VAEDecode`、`UNETLoader`、`KSamplerSelect`、`INTConstant`、`LoadImage`、`CLIPTextEncode`、`SaveImage`、`easy imageColorMatch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
