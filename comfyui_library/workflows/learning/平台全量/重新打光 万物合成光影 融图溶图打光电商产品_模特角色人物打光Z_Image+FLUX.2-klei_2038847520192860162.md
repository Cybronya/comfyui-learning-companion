---
key: 平台全量/重新打光 万物合成光影 融图溶图打光电商产品_模特角色人物打光Z_Image+FLUX.2-klei_2038847520192860162.json
name: 重新打光 万物合成光影 融图溶图打光电商产品_模特角色人物打光Z_Image+FLUX.2-klei_2038847520192860162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/重新打光 万物合成光影 融图溶图打光电商产品_模特角色人物打光Z_Image+FLUX.2-klei_2038847520192860162.json
hash: 4cf245a5675cee63
coverage: 0.803571
learned_at: 2026-11-14 02:49:00
nodes: [ConditioningZeroOut, RandomNoise, VAEDecode, easy cleanGpuUsed, ImageResize+, SimpleMath+, ImpactMinMax, TTP_Image_Tile_Batch, Get Image Size, Get Image Size, ImpactMinMax, ImageResize+, SimpleMath+, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, DF_Integer, ImpactMinMax, CLIPLoader, VAELoader, ConditioningZeroOut, KSamplerSelect, AdvancedLyingSigmaSampler, UpscaleModelLoader, UNETLoader, CLIPTextEncode, Note, Note, Note, Note, SamplerCustomAdvanced, UNETLoader, CLIPLoader, VAELoader, Flux2Scheduler, KSamplerSelect, CFGGuider, ReferenceLatent, ImageResize+, LoraLoaderModelOnly, GetImageSize, VAEEncode, ReferenceLatent, EmptyFlux2LatentImage, Note, Note, UltimateSDUpscaleCustomSample, PreviewImage, CLIPTextEncode, TTP_Image_Assy, PreviewImage, SeedVR2LoadDiTModel, SaveImage, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage]
patterns: []
missing: []
---

# 平台全量/重新打光 万物合成光影 融图溶图打光电商产品_模特角色人物打光Z_Image+FLUX.2-klei_2038847520192860162.json

> 来源文件 `comfyui_library/workflows/平台全量/重新打光 万物合成光影 融图溶图打光电商产品_模特角色人物打光Z_Image+FLUX.2-klei_2038847520192860162.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `ConditioningZeroOut`
- `RandomNoise`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ImageResize+`
- `SimpleMath+`
- `ImpactMinMax`
- `TTP_Image_Tile_Batch`
- `Get Image Size`
- `Get Image Size`
- `ImpactMinMax`
- `ImageResize+`
- `SimpleMath+`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `DF_Integer`
- `ImpactMinMax`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `AdvancedLyingSigmaSampler` ★核心
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ReferenceLatent`
- `ImageResize+`
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `Note`
- `Note`
- `UltimateSDUpscaleCustomSample`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `TTP_Image_Assy`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`

## 知识

覆盖率 **80%**（45/56）

**有卡**：`ConditioningZeroOut`、`RandomNoise`、`VAEDecode`、`easy cleanGpuUsed`、`ImageResize+`、`SimpleMath+`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`Get Image Size`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`DF_Integer`、`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`AdvancedLyingSigmaSampler`、`UpscaleModelLoader`、`UNETLoader`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`CFGGuider`、`ReferenceLatent`、`LoraLoaderModelOnly`、`GetImageSize`、`VAEEncode`、`EmptyFlux2LatentImage`、`UltimateSDUpscaleCustomSample`、`TTP_Image_Assy`、`SeedVR2LoadDiTModel`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
