---
name: image_to_image_controlnet_upscale_lora_14
type: Image To Image
frequency: 2
level: weak
coverage: 0.821
common_nodes: [ACE_ImageFaceCrop, CFGNorm, CLIPLoader, ColorMatchImage, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), Image Rembg (Remove Background), ImageCompositeMasked, ImageResizeKJv2, ImageUpscaleWithModel, InspyrenetRembgLoader, InspyrenetRembgProcess, InstantIDFaceAnalysis, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask To Image (mtb), MaskFromFaceModel, MaskPreview, MaskPreview+, MaskToImage, ModelSamplingAuraFlow, PreviewImage, ReferenceLatent, SaveImage, SetLatentNoiseMask, SolidMask, TTP_Expand_And_Mask, TextEncodeQwenImageEditPlus, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image Edit Character Pose & Scene Edit_2072999451310202880.json, 图片生成/文生图/Qwen-Image-Edit指定角色姿态场景的图像编辑_1984982919376683010.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Qwen Image Edit Character Pose & Scene Edit_2072999451310202880.json、图片生成/文生图/Qwen-Image-Edit指定角色姿态场景的图像编辑_1984982919376683010.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_ImageFaceCrop`
- `CFGNorm`
- `CLIPLoader`
- `ColorMatchImage`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `Image Rembg (Remove Background)`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `ImageUpscaleWithModel`
- `InspyrenetRembgLoader`
- `InspyrenetRembgProcess`
- `InstantIDFaceAnalysis`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask To Image (mtb)`
- `MaskFromFaceModel`
- `MaskPreview`
- `MaskPreview+`
- `MaskToImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `SetLatentNoiseMask`
- `SolidMask`
- `TTP_Expand_And_Mask`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
