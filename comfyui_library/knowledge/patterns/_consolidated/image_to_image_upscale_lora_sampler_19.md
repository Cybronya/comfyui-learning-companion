---
name: image_to_image_upscale_lora_sampler_19
type: Image To Image
frequency: 9
level: strong
coverage: 0.864111
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Klein _ 珠宝首饰渲染级精修+全节点注释_2055634394278309889.json, 平台全量/Klein 电商产品渲染精修 +高清放大_2043201521927589889.json, 平台全量/Klein_ 全能通用白膜 SU渲染_2047966087660179458.json, 平台全量/Klein_亚秒级自然无缝扩图_2031730184612745218.json, 平台全量/Klein_服装3D精修_2063166433131057153.json, 平台全量/Klein_极致肤质人像一致性精修_2057667460144394242.json, 平台全量/Klein_珠宝首饰渲染级精修（去除粘胶）_2085327225020313601.json, 平台全量/最新的Klein模型，亚秒级渲染精修，极致清晰度_2046805085249871873.json, 平台全量/渲染级高精度-电商产品精修_2081630020455452674.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_19

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Klein _ 珠宝首饰渲染级精修+全节点注释_2055634394278309889.json、平台全量/Klein 电商产品渲染精修 +高清放大_2043201521927589889.json、平台全量/Klein_ 全能通用白膜 SU渲染_2047966087660179458.json、平台全量/Klein_亚秒级自然无缝扩图_2031730184612745218.json、平台全量/Klein_服装3D精修_2063166433131057153.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `ImageListToImageBatch` —— 8/9 个有
- `ImpactImageBatchToImageList` —— 8/9 个有
- `ConstrainImage|pysssss` —— 7/9 个有
- `DualCLIPLoader` —— 7/9 个有
- `FluxGuidance` —— 7/9 个有
- `EmptyFlux2LatentImage` —— 5/9 个有
- `GetImageSize` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `Fast Groups Bypasser (rgthree)` —— 4/9 个有
- `Fast Groups Muter (rgthree)` —— 4/9 个有
- `GetImageSize+` —— 4/9 个有
- `GrowMaskWithBlur` —— 3/9 个有
- `Int` —— 3/9 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/9 个有
- `MaskToImage` —— 3/9 个有
- `Mix Images By Mask` —— 3/9 个有
- `easy imageColorMatch` —— 3/9 个有
- `SeedVR2LoadDiTModel` —— 2/9 个有
- `SeedVR2LoadVAEModel` —— 2/9 个有
- `SeedVR2VideoUpscaler` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `CR Text` —— 1/9 个有
- `CR Text Input Switch (4 way)` —— 1/9 个有
- `ImpactInt` —— 1/9 个有
- `JoinStrings` —— 1/9 个有
- `LayerUtility: ExtendCanvasV2` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `ResizeImagesByLongerEdge` —— 1/9 个有
- `easy textSwitch` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | kl_optimal | - | 9 | 78% |
| 重绘幅度 | 0.4 | 0.08 - 0.4 | 9 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 kl_optimal，9 个样本，一致性 78%
- 重绘幅度 中位数 0.4，观测区间 0.08 - 0.4，9 个样本
- 风险：重绘幅度 观测到 0.08，低于常用下限 0.1（）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
