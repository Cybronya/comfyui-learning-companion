---
name: unknown_workflow_inpaint_lora_sampler_24
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9232
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Color Panel, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GrowMask, ImageConcanate, ImageScale, ImageToMask, Images to RGB, InpaintCrop, InpaintModelConditioning, InpaintStitch, InspyrenetRembgAdvanced, KSamplerSelect, LayerMask: MaskGrow, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed (rgthree), StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX-fill-onereword万物迁移优化版V7.1_2015794339158433793.json, 图片生成/图生图/万物迁移优化版V3_1911432833443819521.json, 图片生成/图生图/头部迁移_1991460536573444097.json, 平台全量/reducx384和512模型全系对比_1912401300745846786.json, 平台全量/万物迁移优化版V6.1_1912873196691910657.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX-fill-onereword万物迁移优化版V7.1_2015794339158433793.json、图片生成/图生图/万物迁移优化版V3_1911432833443819521.json、图片生成/图生图/头部迁移_1991460536573444097.json、平台全量/reducx384和512模型全系对比_1912401300745846786.json、平台全量/万物迁移优化版V6.1_1912873196691910657.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Color Panel`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GrowMask`
- `ImageConcanate`
- `ImageScale`
- `ImageToMask`
- `Images to RGB`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembgAdvanced`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 4/5 个有
- `LayerUtility: CropByMask` —— 4/5 个有
- `LayerUtility: CropByMask V2` —— 4/5 个有
- `AdvancedVisionLoader` —— 3/5 个有
- `Anything Everywhere` —— 3/5 个有
- `CLIPVisionEncode` —— 3/5 个有
- `CLIPVisionLoader` —— 3/5 个有
- `ChinesePrompt_Mix` —— 3/5 个有
- `DF_Get_image_size` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `IsMaskEmpty` —— 3/5 个有
- `MaskPreview+` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ReduxAdvanced` —— 3/5 个有
- `StyleModelApply` —— 3/5 个有
- `easy anythingIndexSwitch` —— 3/5 个有
- `easy convertAnything` —— 3/5 个有
- `CropMask` —— 2/5 个有
- `FL_ImageSlicer` —— 2/5 个有
- `Get resolution [Crystools]` —— 2/5 个有
- `Image To Mask` —— 2/5 个有
- `ImageComposite+` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `ImpactSwitch` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: CropBoxResolve` —— 2/5 个有
- `Mask Fill Holes` —— 2/5 个有
- `Mask Invert` —— 2/5 个有
- `Switch any [Crystools]` —— 2/5 个有
- `CheckpointLoaderSimple` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `Get Image Size` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `JWImageResizeByLongerSide` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `easy imageCropFromMask` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
