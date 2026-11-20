---
name: unknown_workflow_upscale_sampler_clip_22
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.8425
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageResize+, ImpactMinMax, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/Flux2-klein+zimage单图产品人物打光_2001650697034711041.json, 图片生成/图生图/Flux2kleinzimage单图产品人物打光_2052717140012216322.json, 图片生成/图生图/Flux2kleinzimage单图产品人物打光_2059441442510172161.json, 图片生成/图生图/Flux2kleinzimage单图产品人物打光_2064542050950934529.json, 图片生成/图生图/产品精修_2064532810496565250.json, 图片生成/图生图/单图产品人物打光-Flux2-klein+z image_2037502724975108097.json, 图片生成/图生图/打光_2064264165769961473.json, 平台全量/重新打光 万物合成光影 融图溶图打光电商产品_模特角色人物打光Z_Image+FLUX.2-klei_2038847520192860162.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux2-klein+zimage单图产品人物打光_2001650697034711041.json、图片生成/图生图/Flux2kleinzimage单图产品人物打光_2052717140012216322.json、图片生成/图生图/Flux2kleinzimage单图产品人物打光_2059441442510172161.json、图片生成/图生图/Flux2kleinzimage单图产品人物打光_2064542050950934529.json、图片生成/图生图/产品精修_2064532810496565250.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactMinMax`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 7/8 个有
- `Get Image Size` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `UltimateSDUpscaleCustomSample` —— 6/8 个有
- `UpscaleModelLoader` —— 6/8 个有
- `AdvancedLyingSigmaSampler` —— 5/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `llama_cpp_instruct_adv` —— 5/8 个有
- `llama_cpp_model_loader` —— 5/8 个有
- `llama_cpp_parameters` —— 5/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `Int` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `GetImageSize+` —— 1/8 个有
- `GrowMask` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `ImpactInt` —— 1/8 个有
- `InvertMask` —— 1/8 个有
- `JoinImageWithAlpha` —— 1/8 个有
- `LayerMask: BiRefNetUltraV2` —— 1/8 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/8 个有
- `Upscale Model Loader` —— 1/8 个有
- `YUAN_TXTConvertAny` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
