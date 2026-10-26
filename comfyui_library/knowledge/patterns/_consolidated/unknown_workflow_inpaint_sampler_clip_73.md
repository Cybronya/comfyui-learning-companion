---
name: unknown_workflow_inpaint_sampler_clip_73
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.901
common_nodes: [CLIPTextEncode, CLIPVisionLoader, FluxGuidance, GrowMask, ImageConcanate, ImageFromBatch+, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LayerUtility: ColorImage V2, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, ModelSamplingFlux, PreviewImage, RHHiddenNodes, ReduxAdvanced, SaveImage, StyleModelLoader, TTP_Expand_And_Mask, TTP_Image_Tile_Batch, easy imageSize]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/一键模特换鞋（高材质还原）_2038919154325004289.json, 图片生成/图生图/模特自动换鞋_材质搞度还原_2030824095310417921.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键模特换鞋（高材质还原）_2038919154325004289.json、图片生成/图生图/模特自动换鞋_材质搞度还原_2030824095310417921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
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
- `DualCLIPLoader` —— 1/2 个有
- `Image Rotate` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `LayerUtility: LayerImageTransform` —— 1/2 个有
- `LoadImagesFromURL` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `SeargeIntegerConstant` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy imageCropFromMask` —— 1/2 个有
- `easy imageSplitGrid` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
