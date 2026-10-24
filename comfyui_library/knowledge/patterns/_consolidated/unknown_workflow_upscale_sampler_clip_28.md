---
name: unknown_workflow_upscale_sampler_clip_28
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7988
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物换背景（可手动控制位置） Klein Flux2 高清放大_2017792741320695809.json, 图片生成/图生图/万物融图，透明融图 Klein Flux2 高清放大。可手动控制位置_2017797048917041153.json, 图片生成/图生图/融图换背景（电商）-FLUX-Klein版_2015613997852135426.json, 图片生成/图生图/超强图片放大-去除ai感拒绝塑料感_2036681605707730945.json, 图片生成/文生图/最新FK2真实感图像高清重绘放大+seedvr2_2035635722681585665.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/万物换背景（可手动控制位置） Klein Flux2 高清放大_2017792741320695809.json、图片生成/图生图/万物融图，透明融图 Klein Flux2 高清放大。可手动控制位置_2017797048917041153.json、图片生成/图生图/融图换背景（电商）-FLUX-Klein版_2015613997852135426.json、图片生成/图生图/超强图片放大-去除ai感拒绝塑料感_2036681605707730945.json、图片生成/文生图/最新FK2真实感图像高清重绘放大+seedvr2_2035635722681585665.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 5 个 workflow 都包含：
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
- `GetImageSize+` —— 4/5 个有
- `ImageResize+` —— 4/5 个有
- `ImageScaleBy` —— 4/5 个有
- `TTP_Image_Assy` —— 4/5 个有
- `TTP_Image_Tile_Batch` —— 4/5 个有
- `TTP_Tile_image_size` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `FastCanvas` —— 3/5 个有
- `FastCanvasTool` —— 3/5 个有
- `LayerMask: BiRefNetUltraV2` —— 3/5 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `ColorMatch` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `KOOK_ImageCompression` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `Note _O` —— 2/5 个有
- `Seed (rgthree)` —— 2/5 个有
- `ImpactInt` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
