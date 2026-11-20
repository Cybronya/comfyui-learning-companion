---
name: image_to_image_upscale_sampler_clip_3
type: Image To Image
frequency: 24
level: weak
coverage: 0.850333
common_nodes: [CLIPLoader, CLIPTextEncode, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/-新- 去AI感，提升真实皮肤细节_1981918443526078466.json, 图片生成/图生图/260110010.人像精修增加写实质感_2011257154291896321.json, 图片生成/图生图/4k细节修复放大+去ai感工作流+全节点注释_2061028972196089858.json, 图片生成/图生图/F2 Klein 9B商业级首饰精修_2062013275021336578.json, 图片生成/图生图/Flux2 Klein9b-万能产品修图_2069336085628538882.json, 图片生成/图生图/Flux2 Klein9b-万能产品修图美妆产品精修-瓶子_罐子_电商产品商业级修复打光_2066815723707658242.json, 图片生成/图生图/Flux2 Klein9b-万能产品修图美妆产品精修-瓶子_罐子_电商产品商业级修复打光_2067056854483685378.json, 图片生成/图生图/Flux2 Klein9b-万能产品修图美妆百货产品精修-瓶子_罐子_电商产品商业级修复打光_2067614942446047233.json, 图片生成/图生图/Flux2 Klein9b-万能产品修图美妆百货产品精修-瓶子_罐子_电商产品商业级修复打光_2082435416803860482.json, 图片生成/图生图/Flux2Klein9b产品精修金属类材质修图_2051317750223646722.json, 图片生成/图生图/Flux2Klein金属产品精修金属材质产品_2050127777017417729.json, 图片生成/图生图/Flux2Klein金属产品精修金属材质产品_2050164950986960898.json, 图片生成/图生图/Flux2_Klein9b-万能产品修图美妆百货产品精修-瓶子_罐子_电商产品商业级修复打光_2072132724583911426.json, 图片生成/图生图/Flux2最强全能首饰精修-4k直出_2055119569190178818.json, 图片生成/图生图/Klein——商业级首饰精修_2033181065560461314.json, 图片生成/图生图/Klein——商业级首饰精修_2051502371112534018.json, 图片生成/图生图/Klein——商业级首饰精修_2061625765002825730.json, 图片生成/图生图/Klein——美妆产品精修  支持瓶子、罐子_2033182800261685250.json, 图片生成/图生图/Klein——金属产品精修  适合各种金属材质产品_2033096831265153025.json, 图片生成/图生图/Klein——鞋类、包类产品精修_2033184319757357058.json, 图片生成/图生图/Klein—商业级首饰精修_2061725996973383681.json, 图片生成/图生图/Klein全能产品精修4k版，通用电商精修_2079851701007380482.json, 图片生成/图生图/Klein全能首饰精修直出4K_2090095160850997250.json, 图片生成/图生图/电商美妆专用精修流_2080141595269226497.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/-新- 去AI感，提升真实皮肤细节_1981918443526078466.json、图片生成/图生图/260110010.人像精修增加写实质感_2011257154291896321.json、图片生成/图生图/4k细节修复放大+去ai感工作流+全节点注释_2061028972196089858.json、图片生成/图生图/F2 Klein 9B商业级首饰精修_2062013275021336578.json、图片生成/图生图/Flux2 Klein9b-万能产品修图_2069336085628538882.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float` —— 23/24 个有
- `Image Comparer (rgthree)` —— 23/24 个有
- `ImpactInt` —— 23/24 个有
- `TTP_Image_Assy` —— 23/24 个有
- `TTP_Image_Tile_Batch` —— 23/24 个有
- `TTP_Tile_image_size` —— 23/24 个有
- `ConditioningZeroOut` —— 22/24 个有
- `FluxGuidance` —— 22/24 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 22/24 个有
- `LoraLoaderModelOnly` —— 22/24 个有
- `ReferenceLatent` —— 22/24 个有
- `EmptyFlux2LatentImage` —— 21/24 个有
- `JjkText` —— 21/24 个有
- `MathExpression|pysssss` —— 21/24 个有
- `GrowMask` —— 20/24 个有
- `ImageListToImageBatch` —— 20/24 个有
- `InvertMask` —— 20/24 个有
- `JoinImageWithAlpha` —— 20/24 个有
- `LayerMask: BiRefNetUltraV2` —— 20/24 个有
- `LayerMask: LoadBiRefNetModelV2` —— 20/24 个有
- `ModelSamplingSD3` —— 20/24 个有
- `easy imageBatchToImageList` —— 20/24 个有
- `easy promptConcat` —— 20/24 个有
- `Text _O` —— 18/24 个有
- `PreviewImage` —— 17/24 个有
- `Fast Groups Bypasser (rgthree)` —— 16/24 个有
- `Image Filter Adjustments` —— 16/24 个有
- `LayerColor: Brightness & Contrast` —— 16/24 个有
- `LayerColor: ColorTemperature` —— 16/24 个有
- `ImageScaleToTotalPixels` —— 6/24 个有
- `GetImageSize+` —— 4/24 个有
- `LayerUtility: PurgeVRAM V2` —— 4/24 个有
- `ImageBatchToList` —— 3/24 个有
- `ImageListToBatch+` —— 3/24 个有
- `ImpactSwitch` —— 3/24 个有
- `JanusImageUnderstanding` —— 3/24 个有
- `JanusModelLoader` —— 3/24 个有
- `KSamplerAdvanced` —— 3/24 个有
- `VAEDecodeTiled` —— 3/24 个有
- `CM_IntToFloat` —— 2/24 个有
- `GrowMaskWithBlur` —— 2/24 个有
- `ImageColorMatch+` —— 2/24 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/24 个有
- `MaskToImage` —— 2/24 个有
- `Mix Images By Mask` —— 2/24 个有
- `CR Model Input Switch` —— 1/24 个有
- `CR Text` —— 1/24 个有
- `CR Text Input Switch` —— 1/24 个有
- `DualCLIPLoader` —— 1/24 个有
- `ExecutionBlocker` —— 1/24 个有
- `FluxKontextImageScale` —— 1/24 个有
- `GetNode` —— 1/24 个有
- `Int` —— 1/24 个有
- `LayerUtility: PurgeVRAM` —— 1/24 个有
- `PrimitiveBoolean` —— 1/24 个有
- `SetNode` —— 1/24 个有
- `String Replace (mtb)` —— 1/24 个有
- `忽略多组孤海` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 21 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 24 | 0% |
| 采样算法 | heun | - | 24 | 79% |
| 调度器 | beta | - | 24 | 79% |
| 重绘幅度 | 0.1 | 0.1 - 1 | 21 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 39/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，21 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，24 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 heun，24 个样本，一致性 79%
- 调度器 最常用 beta，24 个样本，一致性 79%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 1，21 个样本，取值分散，一致性仅 0%
- 高发问题（39/24 个样本）：Steps较低可能导致细节不足
