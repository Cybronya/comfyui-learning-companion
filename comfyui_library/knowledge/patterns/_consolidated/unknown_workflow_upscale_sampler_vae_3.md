---
name: unknown_workflow_upscale_sampler_vae_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7235
common_nodes: [CLIPLoader, ConditioningZeroOut, ConstrainImage|pysssss, DF_Integer, DWPreprocessor, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, Image Comparer (rgthree), ImageCASharpening+, ImageConcatMulti, ImageListToImageBatch, ImpactMinMax, ImpactSwitch, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll, easy imageBatchToImageList, easy imageSize, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/迄今超强人物迁移人物单_双人_多人换脸终极版平替全能图片V1Pro-无需涂抹遮罩一键支持侧脸_1968485665270845442.json, 图片生成/图生图/迄今超强模特（支持单_双人多人）全自动换装保留细节+可选姿势参考可选8K高清放大_1952666911089864705.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/迄今超强人物迁移人物单_双人_多人换脸终极版平替全能图片V1Pro-无需涂抹遮罩一键支持侧脸_1968485665270845442.json、图片生成/图生图/迄今超强模特（支持单_双人多人）全自动换装保留细节+可选姿势参考可选8K高清放大_1952666911089864705.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DF_Integer`
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageConcatMulti`
- `ImageListToImageBatch`
- `ImpactMinMax`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `ClothesSegment` —— 1/2 个有
- `ConcatTextOfUtils` —— 1/2 个有
- `ControlNetApplySD3` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `Convert Masks to Images` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `Int` —— 1/2 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LayerUtility: ImageBlendAdvance` —— 1/2 个有
- `Mask Fill Holes` —— 1/2 个有
- `MaskFillHoles` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `ToBinaryMask` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有
- `easy isMaskEmpty` —— 1/2 个有
- `图像缩放V2_孤海` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 2 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
