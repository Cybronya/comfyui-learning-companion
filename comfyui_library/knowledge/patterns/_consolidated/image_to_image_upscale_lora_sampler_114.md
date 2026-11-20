---
name: image_to_image_upscale_lora_sampler_114
type: Image To Image
frequency: 2
level: weak
coverage: 0.802
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, DetailTransfer, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, Int Input [Dream], KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerMask: MaskGrow, LayerUtility: ImageBlendAdvance V2, LayerUtility: ImageMaskScaleAs, LoadImage, LoraLoaderModelOnly, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, RHHiddenNodes, RepeatLatentBatch, SaveImage, Text Input [Dream], UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy ifElse, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/产品和背景融合(保留细节)工作流_1972876042950086657.json, 平台全量/完美还原细节的电商模特和场景(溶图)_1973012924652498946.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_114

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品和背景融合(保留细节)工作流_1972876042950086657.json、平台全量/完美还原细节的电商模特和场景(溶图)_1973012924652498946.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DetailTransfer`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `Int Input [Dream]`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageBlendAdvance V2`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RHHiddenNodes`
- `RepeatLatentBatch`
- `SaveImage`
- `Text Input [Dream]`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ifElse`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `LayerMask: SegformerClothesPipelineLoader` —— 1/2 个有
- `LayerMask: SegformerUltraV2` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `SeedSelector` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
