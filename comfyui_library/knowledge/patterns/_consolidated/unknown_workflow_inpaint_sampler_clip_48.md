---
name: unknown_workflow_inpaint_sampler_clip_48
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9154
common_nodes: [CLIPTextEncode, CLIPVisionLoader, FluxGuidance, GrowMask, ImageConcanate, ImageFromBatch+, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage V2, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, ModelSamplingFlux, PreviewImage, RHHiddenNodes, ReduxAdvanced, SaveImage, StyleModelLoader, TTP_Expand_And_Mask, TTP_Image_Tile_Batch, easy imageSize]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/一键模特换鞋（高材质还原）_2038919154325004289.json, 图片生成/图生图/模特自动换鞋_材质搞度还原_2030824095310417921.json, 平台全量/小北换手串-局部_1968215842968186882.json, 平台全量/模特自动换鞋_材质搞度还原_1942859541581074433.json, 平台全量/模特自动换鞋穿鞋V2.0_1961095636047347713.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键模特换鞋（高材质还原）_2038919154325004289.json、图片生成/图生图/模特自动换鞋_材质搞度还原_2030824095310417921.json、平台全量/小北换手串-局部_1968215842968186882.json、平台全量/模特自动换鞋_材质搞度还原_1942859541581074433.json、平台全量/模特自动换鞋穿鞋V2.0_1961095636047347713.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `FluxGuidance`
- `GrowMask`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageMaskScaleAs`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RHHiddenNodes`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `TTP_Expand_And_Mask`
- `TTP_Image_Tile_Batch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: CropByMask V2` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `easy imageSplitGrid` —— 4/5 个有
- `LayerUtility: LayerImageTransform` —— 3/5 个有
- `Mask Fill Holes` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `easy seed` —— 3/5 个有
- `DualCLIPLoader` —— 2/5 个有
- `Image Rotate` —— 2/5 个有
- `SeargeIntegerConstant` —— 2/5 个有
- `UNETLoader` —— 2/5 个有
- `VAELoader` —— 2/5 个有
- `LoadImagesFromURL` —— 1/5 个有
- `easy imageCropFromMask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
