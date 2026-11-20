---
name: image_to_image_inpaint_lora_sampler_13
type: Image To Image
frequency: 3
level: strong
coverage: 0.804667
common_nodes: [Any Switch (rgthree), CLIPTextEncode, CR Image Input Switch, CR Integer Range List, ConditioningZeroOut, CropMask, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, Fast Groups Bypasser (rgthree), FeatherMask, Florence2Run, FluxGuidance, GetImageSize, GetMaskSizeAndCount, GrowMaskWithBlur, HAIGC_LoadImagesFromZip, IfInnerExecute, Image Comparer (rgthree), ImageAndMaskPreview, ImageListToImageBatch, ImageResize+, ImageToMask, InpaintModelConditioning, Int, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, MaskToImage, ModelSamplingFlux, PreviewImage, RH_BatchImages, RH_ExtractImage, ResizeMask, SaveImage, ShowText|pysssss, SimpleMath+, Text, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy int, easy isMaskEmpty, solarL_SaveImagesToZip, 遮罩比例扩展]
problems: []
missing: []
members: [图片生成/图生图/自动化控制批量清除工作流_2063093427805442050.json, 平台全量/自动化控制批量清除工作流_2047337684347133954.json, 平台全量/自动化控制批量清除工作流_2064157278634340354.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/自动化控制批量清除工作流_2063093427805442050.json、平台全量/自动化控制批量清除工作流_2047337684347133954.json、平台全量/自动化控制批量清除工作流_2064157278634340354.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPTextEncode`
- `CR Image Input Switch`
- `CR Integer Range List`
- `ConditioningZeroOut`
- `CropMask`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FeatherMask`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize`
- `GetMaskSizeAndCount`
- `GrowMaskWithBlur`
- `HAIGC_LoadImagesFromZip`
- `IfInnerExecute`
- `Image Comparer (rgthree)`
- `ImageAndMaskPreview`
- `ImageListToImageBatch`
- `ImageResize+`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RH_BatchImages`
- `RH_ExtractImage`
- `ResizeMask`
- `SaveImage`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy int`
- `easy isMaskEmpty`
- `solarL_SaveImagesToZip`
- `遮罩比例扩展`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 30 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 30，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
