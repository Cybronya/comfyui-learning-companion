---
name: text_to_image_controlnet_inpaint_lora_3
type: Text To Image
frequency: 4
level: strong
coverage: 0.8985
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetImageSize+, GrowMaskWithBlur, Image Comparer (rgthree), ImageAndMaskPreview, ImageConcanate, ImageCrop, ImageResizeKJ, ImpactDilateMask, InpaintModelConditioning, JjkText, KSampler, LayerMask: LoadSegmentAnythingModels, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V3, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleRestore V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoader, LoraLoaderModelOnly, Mask Fill Holes, MaskComposite, PreviewImage, ReduxAdvanced, SaveImage, SetUnionControlNetType, StyleModelLoader, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, easy cleanGpuUsed, easy makeImageForICLora, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物迁移涂抹版 物体位置精准控制批量处理_2109326755302563841.json, 图片生成/图生图/万物迁移涂抹版商品图案迁移图生图处理工具包_2101000237560193026.json, 图片生成/图生图/万物迁移涂抹版，商品替换图案迁移图生图神器_2110800098853744641.json, 图片生成/图生图/涂抹版万物迁移｜商品替换图案迁移一键生成_2092201039402459138.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/万物迁移涂抹版 物体位置精准控制批量处理_2109326755302563841.json、图片生成/图生图/万物迁移涂抹版商品图案迁移图生图处理工具包_2101000237560193026.json、图片生成/图生图/万物迁移涂抹版，商品替换图案迁移图生图神器_2110800098853744641.json、图片生成/图生图/涂抹版万物迁移｜商品替换图案迁移一键生成_2092201039402459138.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetImageSize+`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageCrop`
- `ImageResizeKJ`
- `ImpactDilateMask`
- `InpaintModelConditioning`
- `JjkText`
- `KSampler`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskComposite`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy makeImageForICLora`
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.7 | 0.7 - 0.7 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.7，观测区间 0.7 - 0.7，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
