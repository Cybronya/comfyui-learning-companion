---
name: image_to_image_upscale_lora_sampler_4
type: Image To Image
frequency: 29
level: weak
coverage: 0.829793
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Float, FluxGuidance, Image Comparer (rgthree), ImageUpscaleWithModel, ImpactInt, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ReferenceLatent, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Product Retouching 产品精修+万能产品修图_2093154645987389441.json, 图片生成/图生图/Transparent PNG image Product Retouching 产品精修_2106912090878464002.json, 图片生成/图生图/Transparent_PNG_image_Product_Retouching_产品精修_2107651060654493698.json, 图片生成/图生图/flux2全能产品精修，适合所有类型产品，4k直出_2060581652212043777.json, 图片生成/图生图/万能产品修图 美妆产品精修+支持瓶子 罐子 电商产品商业级修复打光_2067298785688113154.json, 图片生成/图生图/万能产品修图_Flux-2-Klein-9B_美妆产品精修_+支持瓶子_罐子_电商产品商业级修复打光_2060903281194524673.json, 图片生成/图生图/万能产品修图_Flux-2-Klein-9B_美妆产品精修_+支持瓶子_罐子_电商产品商业级修复打光_2061261459555971074.json, 图片生成/图生图/个人化妆品玻璃精修_2063358356420644865.json, 图片生成/图生图/个人塑料精修_2063338549637902337.json, 图片生成/图生图/产品精修 电商皮革纹理类产品精修 加强实用版_2088419890930741250.json, 图片生成/图生图/产品精修（标贴会变形，需要去标贴）_2034941844886396930.json, 图片生成/图生图/全能产品精修——适用于金属、饰品、化妆品、服装_2040979371816656897.json, 图片生成/图生图/商业级人像精修，增加皮肤质感、去AI感，4K直出，影楼专用_2033135017852932098.json, 图片生成/图生图/服装精修，衣服去皱，版型整理_2033166281683247106.json, 图片生成/图生图/电商网店首饰精修-图生图_2066321366307139585.json, 平台全量/F.2Klein金属产品精修金属材质。专为金属材质产品打造的高精修工作流，一键实现粗糙到镜面级金属光_2058093396413214722.json, 平台全量/F2 Klein 9B商业级首饰精修_2058464205665300482.json, 平台全量/Flux2_Klein9b-万能产品修图美妆百货产品精修-瓶子_罐子_电商产品商业级修复打光_2071791201761714178.json, 平台全量/flux2-klein商业级首饰精修，包含4k放大，自动抠图_2057737083950817281.json, 平台全量/万能产品修图 Flux-2-Klein-9B 美妆产品精修 +支持瓶子 罐子 电商产品商业级修复打光_2059862009503641601.json, 平台全量/万能产品修图 产品精修 美妆产品精修++支持瓶子+罐子+电商产品修图_2074654188684005378.json, 平台全量/万能产品修图_Flux-2-Klein-9B_美妆产品精修_+支持瓶子_罐子_电商产品商业级修复打光_2066690247844519937.json, 平台全量/万能产品精修 Flux-2-Klein-9B 渲染级质感 美妆产品精修 +支持瓶子 罐子 电商产品商_2059868736844296194.json, 平台全量/产品精修 万能产品修图+Flux-2-Klein-9B+美妆产品精修++支持瓶子+罐子+电商产品商业_2074395129930149890.json, 平台全量/商业级首饰精修——Klein_2051908491601825793.json, 平台全量/最新3.0万能产品修图（变清晰消除任何瑕疵）_2062587070014640130.json, 平台全量/服装精修，衣服去皱，版型整理_2096505032865832961.json, 平台全量/服装精修，衣服去皱，版型整理_2096811796542877697.json, 平台全量/超级修复产品精修+抠图 +渲染级质感+美妆产品精修++支持瓶子+罐子+电商产品商_2072849657738391553.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/Product Retouching 产品精修+万能产品修图_2093154645987389441.json、图片生成/图生图/Transparent PNG image Product Retouching 产品精修_2106912090878464002.json、图片生成/图生图/Transparent_PNG_image_Product_Retouching_产品精修_2107651060654493698.json、图片生成/图生图/flux2全能产品精修，适合所有类型产品，4k直出_2060581652212043777.json、图片生成/图生图/万能产品修图 美妆产品精修+支持瓶子 罐子 电商产品商业级修复打光_2067298785688113154.json…）

- **类型**：Image To Image
- **样本数**：29
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 29 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
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
- `Fast Groups Bypasser (rgthree)` —— 28/29 个有
- `GrowMask` —— 28/29 个有
- `InvertMask` —— 28/29 个有
- `JoinImageWithAlpha` —— 28/29 个有
- `LayerMask: BiRefNetUltraV2` —— 28/29 个有
- `LayerMask: LoadBiRefNetModelV2` —— 28/29 个有
- `ImageListToImageBatch` —— 25/29 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 25/29 个有
- `ModelSamplingSD3` —— 25/29 个有
- `TTP_Image_Assy` —— 25/29 个有
- `TTP_Image_Tile_Batch` —— 25/29 个有
- `TTP_Tile_image_size` —— 25/29 个有
- `Text _O` —— 25/29 个有
- `easy cleanGpuUsed` —— 25/29 个有
- `easy imageBatchToImageList` —— 25/29 个有
- `PreviewImage` —— 20/29 个有
- `Image Filter Adjustments` —— 19/29 个有
- `LayerColor: Brightness & Contrast` —— 19/29 个有
- `LayerColor: ColorTemperature` —— 19/29 个有
- `FluxKontextImageScale` —— 4/29 个有
- `GetImageSize+` —— 4/29 个有
- `ImpactSwitch` —— 4/29 个有
- `LayerUtility: PurgeVRAM V2` —— 4/29 个有
- `AnyBooleanSwitch` —— 3/29 个有
- `孤海注释` —— 3/29 个有
- `RHHiddenNodes` —— 2/29 个有
- `EmptyImage` —— 1/29 个有
- `ExecutionBlocker` —— 1/29 个有
- `Int` —— 1/29 个有
- `PrimitiveBoolean` —— 1/29 个有
- `workflow>加密节点` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 29 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 29 | 100% |
| 采样算法 | heun | - | 29 | 79% |
| 调度器 | beta | - | 29 | 79% |
| 重绘幅度 | 0.1 | 0.1 - 1 | 29 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 53/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，29 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，29 个样本，一致性 79%
- 调度器 最常用 beta，29 个样本，一致性 79%
- 重绘幅度 中位数 0.1，观测区间 0.1 - 1，29 个样本，取值分散，一致性仅 0%
- 高发问题（53/29 个样本）：Steps较低可能导致细节不足
