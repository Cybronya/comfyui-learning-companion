---
name: unknown_workflow_upscale_sampler_clip_28
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.802286
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物换背景（可手动控制位置） Klein Flux2 高清放大_2017792741320695809.json, 图片生成/图生图/万物融图，透明融图 Klein Flux2 高清放大。可手动控制位置_2017797048917041153.json, 图片生成/图生图/融图换背景（电商）-FLUX-Klein版_2015613997852135426.json, 图片生成/图生图/超强图片放大-去除ai感拒绝塑料感_2036681605707730945.json, 图片生成/文生图/最新FK2真实感图像高清重绘放大+seedvr2_2035635722681585665.json, 平台全量/FK2图像高清重绘放大 SeedVR2 图像超清放大 去除AI模糊塑料感 更好一致性 高清修复细节_2036609383450284034.json, 平台全量/电商篇+FastCanvas控图+融图换背景-FLUX-Klein版_2014575770089295873.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/万物换背景（可手动控制位置） Klein Flux2 高清放大_2017792741320695809.json、图片生成/图生图/万物融图，透明融图 Klein Flux2 高清放大。可手动控制位置_2017797048917041153.json、图片生成/图生图/融图换背景（电商）-FLUX-Klein版_2015613997852135426.json、图片生成/图生图/超强图片放大-去除ai感拒绝塑料感_2036681605707730945.json、图片生成/文生图/最新FK2真实感图像高清重绘放大+seedvr2_2035635722681585665.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
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
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 5/7 个有
- `ImageResize+` —— 5/7 个有
- `ImageScaleBy` —— 5/7 个有
- `TTP_Image_Assy` —— 5/7 个有
- `TTP_Image_Tile_Batch` —— 5/7 个有
- `TTP_Tile_image_size` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `FastCanvas` —— 4/7 个有
- `FastCanvasTool` —— 4/7 个有
- `LayerMask: BiRefNetUltraV2` —— 4/7 个有
- `LayerMask: LoadBiRefNetModelV2` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `CR Prompt Text` —— 3/7 个有
- `ColorMatch` —— 3/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `KOOK_ImageCompression` —— 3/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `Seed (rgthree)` —— 3/7 个有
- `ImpactInt` —— 2/7 个有
- `Note _O` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
