---
name: image_to_image_upscale_lora_sampler_21
type: Image To Image
frequency: 6
level: strong
coverage: 0.865333
common_nodes: [CLIPLoader, CLIPTextEncode, Float, FluxGuidance, Image Comparer (rgthree), ImageListToImageBatch, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, ReferenceLatent, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/Flux 2 双图编辑Dual image editing-电商产品编辑人像等_1993505200942104577.json, 图片生成/图生图/Flux2万物迁移、首饰迁移、首饰上身，饰品穿戴，产品迁移，可指定位置，控制大小_2091875319920816129.json, 图片生成/图生图/Kontext增加人像皮肤纹理 +wan2.2降噪放大_1979393417379745794.json, 图片生成/图生图/flux 2-单图编辑+高清修复美颜Single image editing_1994679298504134657.json, 图片生成/图生图/flux 2-单图编辑+高清修复美颜_1994613527627374593.json, 图片生成/图生图/flux2单图编辑Single-image editing_1994766506879803394.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux 2 双图编辑Dual image editing-电商产品编辑人像等_1993505200942104577.json、图片生成/图生图/Flux2万物迁移、首饰迁移、首饰上身，饰品穿戴，产品迁移，可指定位置，控制大小_2091875319920816129.json、图片生成/图生图/Kontext增加人像皮肤纹理 +wan2.2降噪放大_1979393417379745794.json、图片生成/图生图/flux 2-单图编辑+高清修复美颜Single image editing_1994679298504134657.json、图片生成/图生图/flux 2-单图编辑+高清修复美颜_1994613527627374593.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Float`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `ReferenceLatent`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `DualCLIPLoader` —— 5/6 个有
- `EmptyFlux2LatentImage` —— 5/6 个有
- `Flux2Scheduler` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 5/6 个有
- `KSamplerSelect` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `RandomNoise` —— 5/6 个有
- `SamplerCustomAdvanced` —— 5/6 个有
- `Anything Everywhere` —— 4/6 个有
- `CR Text` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `easy clearCacheAll` —— 4/6 个有
- `easy imageConcat` —— 4/6 个有
- `ImpactInt` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `Text Find and Replace` —— 1/6 个有
- `Text _O` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | heun | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 0.15 | 0.1 - 0.15 | 6 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 0.15，观测区间 0.1 - 0.15，6 个样本，取值集中（一致性 82%）
