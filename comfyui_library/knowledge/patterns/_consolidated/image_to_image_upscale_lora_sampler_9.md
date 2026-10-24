---
name: image_to_image_upscale_lora_sampler_9
type: Image To Image
frequency: 15
level: weak
coverage: 0.8114
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Float, FluxGuidance, Image Comparer (rgthree), ImageUpscaleWithModel, ImpactInt, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ReferenceLatent, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Product Retouching 产品精修+万能产品修图_2093154645987389441.json, 图片生成/图生图/Transparent PNG image Product Retouching 产品精修_2106912090878464002.json, 图片生成/图生图/Transparent_PNG_image_Product_Retouching_产品精修_2107651060654493698.json, 图片生成/图生图/flux2全能产品精修，适合所有类型产品，4k直出_2060581652212043777.json, 图片生成/图生图/万能产品修图 美妆产品精修+支持瓶子 罐子 电商产品商业级修复打光_2067298785688113154.json, 图片生成/图生图/万能产品修图_Flux-2-Klein-9B_美妆产品精修_+支持瓶子_罐子_电商产品商业级修复打光_2060903281194524673.json, 图片生成/图生图/万能产品修图_Flux-2-Klein-9B_美妆产品精修_+支持瓶子_罐子_电商产品商业级修复打光_2061261459555971074.json, 图片生成/图生图/个人化妆品玻璃精修_2063358356420644865.json, 图片生成/图生图/个人塑料精修_2063338549637902337.json, 图片生成/图生图/产品精修 电商皮革纹理类产品精修 加强实用版_2088419890930741250.json, 图片生成/图生图/产品精修（标贴会变形，需要去标贴）_2034941844886396930.json, 图片生成/图生图/全能产品精修——适用于金属、饰品、化妆品、服装_2040979371816656897.json, 图片生成/图生图/商业级人像精修，增加皮肤质感、去AI感，4K直出，影楼专用_2033135017852932098.json, 图片生成/图生图/服装精修，衣服去皱，版型整理_2033166281683247106.json, 图片生成/图生图/电商网店首饰精修-图生图_2066321366307139585.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Product Retouching 产品精修+万能产品修图_2093154645987389441.json、图片生成/图生图/Transparent PNG image Product Retouching 产品精修_2106912090878464002.json、图片生成/图生图/Transparent_PNG_image_Product_Retouching_产品精修_2107651060654493698.json、图片生成/图生图/flux2全能产品精修，适合所有类型产品，4k直出_2060581652212043777.json、图片生成/图生图/万能产品修图 美妆产品精修+支持瓶子 罐子 电商产品商业级修复打光_2067298785688113154.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 14/15 个有
- `InvertMask` —— 14/15 个有
- `JoinImageWithAlpha` —— 14/15 个有
- `LayerMask: BiRefNetUltraV2` —— 14/15 个有
- `LayerMask: LoadBiRefNetModelV2` —— 14/15 个有
- `ImageListToImageBatch` —— 11/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/15 个有
- `ModelSamplingSD3` —— 11/15 个有
- `TTP_Image_Assy` —— 11/15 个有
- `TTP_Image_Tile_Batch` —— 11/15 个有
- `TTP_Tile_image_size` —— 11/15 个有
- `Text _O` —— 11/15 个有
- `easy cleanGpuUsed` —— 11/15 个有
- `easy imageBatchToImageList` —— 11/15 个有
- `PreviewImage` —— 8/15 个有
- `Image Filter Adjustments` —— 7/15 个有
- `LayerColor: Brightness & Contrast` —— 7/15 个有
- `LayerColor: ColorTemperature` —— 7/15 个有
- `FluxKontextImageScale` —— 4/15 个有
- `GetImageSize+` —— 4/15 个有
- `ImpactSwitch` —— 4/15 个有
- `LayerUtility: PurgeVRAM V2` —— 4/15 个有
- `AnyBooleanSwitch` —— 3/15 个有
- `孤海注释` —— 3/15 个有
- `EmptyImage` —— 1/15 个有
- `ExecutionBlocker` —— 1/15 个有
- `PrimitiveBoolean` —— 1/15 个有
- `RHHiddenNodes` —— 1/15 个有
- `workflow>加密节点` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 15 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | heun | - | 15 | 67% |
| 调度器 | beta | - | 15 | 67% |
| 重绘幅度 | 0.1 | 0.1 - 1 | 15 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，15 个样本，一致性 67%
- 调度器 最常用 beta，15 个样本，一致性 67%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 1，15 个样本，取值分散，一致性仅 0%
- 高发问题（25/15 个样本）：Steps较低可能导致细节不足
