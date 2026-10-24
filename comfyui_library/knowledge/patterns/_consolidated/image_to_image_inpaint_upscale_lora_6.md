---
name: image_to_image_inpaint_upscale_lora_6
type: Image To Image
frequency: 3
level: strong
coverage: 0.78
common_nodes: [AIO_Preprocessor, Anything Everywhere3, AutoCropFaces, BlockifyMask, CFGNorm, CLIPLoader, ConditioningZeroOut, DWPreprocessor, DrawMaskOnImage, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Image Comparer (rgthree), ImageAndMaskPreview, ImageConcanate, ImageResizeKJ, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImitationHueNode, InpaintCrop, InpaintStitch, KSampler, LayerMask: HumanPartsUltra, LayerMask: PersonMaskUltra V2, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageBlend, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/换头_换脸_换身体【2511升级版】_2003287695604506625.json, 图片生成/图生图/换头_换脸_换身体【2511升级版】_2097864093465145346.json, 图片生成/图生图/换头_换脸_换身体【2511升级版】_2099404881617575937.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/换头_换脸_换身体【2511升级版】_2003287695604506625.json、图片生成/图生图/换头_换脸_换身体【2511升级版】_2097864093465145346.json、图片生成/图生图/换头_换脸_换身体【2511升级版】_2099404881617575937.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `AutoCropFaces`
- `BlockifyMask`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImitationHueNode`
- `InpaintCrop`
- `InpaintStitch`
- `KSampler`
- `LayerMask: HumanPartsUltra`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | ddim | - | 3 | 100% |
| 调度器 | linear_quadratic | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，3 个样本，一致性 100%
- 调度器 最常用 linear_quadratic，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
