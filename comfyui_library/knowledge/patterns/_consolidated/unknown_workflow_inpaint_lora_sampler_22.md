---
name: unknown_workflow_inpaint_lora_sampler_22
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9425
common_nodes: [AddMask, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_FloatBinaryOperation, CM_FloatToInt, CM_IntBinaryOperation, CM_IntToFloat, CM_NumberToInt, CR Image Input Switch, CR Text Concatenate, ConditioningZeroOut, CutForInpaint, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, EmptyImage, Florence2Run, FluxGuidance, GetImageSize, GrowMask, Image Flip, Image Rotate, ImageAndMaskPreview, ImageConcanate, ImageMaskSwitch, ImageToMask, InpaintModelConditioning, InspyrenetRembg, Int Literal, IsMaskEmpty, KSampler, LG_LoadImage, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LazySwitch1way, LoraLoaderModelOnly, Mask Fill Holes, MaskSmooth+, MaskToImage, PreviewImage, RHHiddenNodes, RepeatLatentBatch, SaveImage, Seed (rgthree), String Literal, StyleModelApply, StyleModelLoader, SubtractMask, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/万物迁移_1991726963586969601.json, 图片生成/图生图/商品迁移丨FLUX Fill OneReward丨主体替换·场景融合_2099792986455498753.json, 图片生成/图生图/首饰迁移_1958364959468109825.json, 图片生成/图生图/高精度万物迁移_1991838968941703169.json, 平台全量/万物迁移--高精度--顶级2025年11月4日更新_1908788425720537089.json, 平台全量/万物迁移--高精度--顶级_1985633659778674690.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_22

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/万物迁移_1991726963586969601.json、图片生成/图生图/商品迁移丨FLUX Fill OneReward丨主体替换·场景融合_2099792986455498753.json、图片生成/图生图/首饰迁移_1958364959468109825.json、图片生成/图生图/高精度万物迁移_1991838968941703169.json、平台全量/万物迁移--高精度--顶级2025年11月4日更新_1908788425720537089.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `AddMask`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_FloatBinaryOperation`
- `CM_FloatToInt`
- `CM_IntBinaryOperation`
- `CM_IntToFloat`
- `CM_NumberToInt`
- `CR Image Input Switch`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `CutForInpaint`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `EmptyImage`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize`
- `GrowMask`
- `Image Flip`
- `Image Rotate`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageMaskSwitch`
- `ImageToMask`
- `InpaintModelConditioning`
- `InspyrenetRembg`
- `Int Literal`
- `IsMaskEmpty`
- `KSampler`
- `LG_LoadImage`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LazySwitch1way`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskSmooth+`
- `MaskToImage`
- `PreviewImage`
- `RHHiddenNodes`
- `RepeatLatentBatch`
- `SaveImage`
- `Seed (rgthree)`
- `String Literal`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 5/6 个有
- `CachePreviewBridge` —— 5/6 个有
- `ControlNetApplyAdvanced` —— 5/6 个有
- `ControlNetLoader` —— 5/6 个有
- `PreviewBridge` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| ControlNet 权重 | 0.6 | 0.6 - 0.6 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.6，5 个样本，取值集中（一致性 100%）
