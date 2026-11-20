---
name: image_to_image_inpaint_upscale_lora_8
type: Image To Image
frequency: 2
level: weak
coverage: 0.596
common_nodes: [AdvancedVisionLoader, BBoxesToSAM2, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Color Panel, CR Prompt Text, ConditioningZeroOut, CropMask, DF_Get_image_size, DeepTranslatorTextNode, DifferentialDiffusion, DownloadAndLoadQwenModel, DualCLIPLoader, EmptyImage, FluxGuidance, GetImageSize, GetNode, GrowMask, Image To Mask, ImageComposite+, ImageConcanate, ImageScale, ImageToMask, ImageUpscaleWithModel, Images to RGB, InpaintCrop, InpaintModelConditioning, InpaintStitch, InspyrenetRembgAdvanced, KSampler, KSamplerSelect, LayerMask: LoadSAM2Model, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: SAM2UltraV2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: CropByMask V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, Mask Invert, MaskToImage, ModelSamplingFlux, PreviewImage, QwenVLDetection, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SetNode, StyleModelApply, StyleModelLoader, Switch any [Crystools], UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageScaleDownToSize, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/万物迁移强化版_1935706767508561921.json, 图片生成/图生图/换装｜万物迁移版_1936039237160456194.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_8

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/万物迁移强化版_1935706767508561921.json、图片生成/图生图/换装｜万物迁移版_1936039237160456194.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `AdvancedVisionLoader`
- `BBoxesToSAM2`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Color Panel`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `CropMask`
- `DF_Get_image_size`
- `DeepTranslatorTextNode`
- `DifferentialDiffusion`
- `DownloadAndLoadQwenModel`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GetImageSize`
- `GetNode`
- `GrowMask`
- `Image To Mask`
- `ImageComposite+`
- `ImageConcanate`
- `ImageScale`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `Images to RGB`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembgAdvanced`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: LoadSAM2Model`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `Mask Invert`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `QwenVLDetection`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `Switch any [Crystools]`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageScaleDownToSize`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
