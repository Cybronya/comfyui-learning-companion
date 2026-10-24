---
key: 图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json
name: Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json
hash: 001e9a8f582f7007
coverage: 0.650794
learned_at: 2026-10-23 10:58:48
nodes: [GetImageSizeAndCount, Bjornulf_ShowInt, Bjornulf_ShowInt, Reroute, Bjornulf_ShowInt, Reroute, ImageScale, Anything Everywhere, CFGGuider, KSamplerSelect, Anything Everywhere, ConditioningZeroOut, SetNode, Bjornulf_ShowInt, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, GetNode, SamplerCustomAdvanced, RebatchLatents, GetNode, RepeatLatentBatch, GetNode, VAEEncode, ImageSmartSharpen+, VAEEncode, ReferenceLatent, LoadImage, SaveImage, GetNode, SetNode, SetNode, SaveImage, TilePreprocessor, INTConstant, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, Image Comparer (rgthree), CLIPTextEncode, VAEDecode, Reroute, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), RandomNoise, LG_Color_Match_V2, LayerUtility: ImageScaleByAspectRatio V2, ImagePass, LayerFilter: FilmV2, GetNode, Any Switch (rgthree), GetNode, Anything Everywhere, VAELoader, CLIPLoader, UNETLoader, SeedVR2VideoUpscaler, SetNode, GetNode, Image H264 Compression (mtb), ImpactControlBridge, Fast Groups Bypasser (rgthree), Note]
patterns: []
missing: []
---

# 图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2 klein + seedvr2.5 Upscaler 参考图像超清放大_2012982565870772226.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `GetImageSizeAndCount`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `Reroute`
- `Bjornulf_ShowInt`
- `Reroute`
- `ImageScale`
- `Anything Everywhere`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Anything Everywhere`
- `ConditioningZeroOut`
- `SetNode`
- `Bjornulf_ShowInt`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `RebatchLatents`
- `GetNode`
- `RepeatLatentBatch`
- `GetNode`
- `VAEEncode` ★核心
- `ImageSmartSharpen+`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `SaveImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `TilePreprocessor`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `RandomNoise`
- `LG_Color_Match_V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePass`
- `LayerFilter: FilmV2`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `Anything Everywhere`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SeedVR2VideoUpscaler`
- `SetNode`
- `GetNode`
- `Image H264 Compression (mtb)`
- `ImpactControlBridge`
- `Fast Groups Bypasser (rgthree)`
- `Note`

## 知识

覆盖率 **65%**（41/63）

**有卡**：`GetImageSizeAndCount`、`Bjornulf_ShowInt`、`ImageScale`、`CFGGuider`、`KSamplerSelect`、`ConditioningZeroOut`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SamplerCustomAdvanced`、`RebatchLatents`、`RepeatLatentBatch`、`VAEEncode`、`ImageSmartSharpen+`、`ReferenceLatent`、`LoadImage`、`SaveImage`、`TilePreprocessor`、`INTConstant`、`LoraLoaderModelOnly`、`BasicScheduler`、`CLIPTextEncode`、`VAEDecode`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`RandomNoise`、`LG_Color_Match_V2`、`ImagePass`、`LayerFilter: FilmV2`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`SeedVR2VideoUpscaler`、`Image H264 Compression (mtb)`、`ImpactControlBridge`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
