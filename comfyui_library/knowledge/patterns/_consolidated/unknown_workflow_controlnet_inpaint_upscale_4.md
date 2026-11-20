---
name: unknown_workflow_controlnet_inpaint_upscale_4
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.721
common_nodes: [ApplyInstantID, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BitwiseAndMask, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorMatch, ControlNetLoader, CropFaces, DetectFaces, DifferentialDiffusion, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, GetNode, GroundingDinoModelLoader (segment anything2), GroundingDinoSAMSegment (segment anything), GrowMaskWithBlur, Image Comparer (rgthree), Image Tiled, ImageCompositeMasked, ImageConcanate, ImageConcatMulti, ImageFromBatch, ImageScaleBy, ImageToMask, ImageUpscaleWithModel, InpaintCrop, InpaintModelConditioning, InpaintStitch, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: ColorImage, LayerUtility: ColorImage V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, MaskToImage, PreviewImage, ReduxAdvanced, SAMLoader, SaveImage, SetNode, StyleModelLoader, SubtractMask, Switch mask [Crystools], UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, WarpFacesBack, easy cleanGpuUsed, easy imageInsetCrop, easy imageSize, easy showAnything, easy showTensorShape]
problems: []
missing: []
members: [图片生成/图生图/一键换装工作流v2.0_1917201394632163329.json, 平台全量/一键换装工作流_1892487724052471810.json, 平台全量/一键换装工作流v2.0_1904211212974854146.json, 平台全量/一键换装工作流v2.0_1904517353562935297.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_upscale_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换装工作流v2.0_1917201394632163329.json、平台全量/一键换装工作流_1892487724052471810.json、平台全量/一键换装工作流v2.0_1904211212974854146.json、平台全量/一键换装工作流v2.0_1904517353562935297.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyInstantID`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `BitwiseAndMask`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ControlNetLoader`
- `CropFaces`
- `DetectFaces`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetNode`
- `GroundingDinoModelLoader (segment anything2)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `Image Tiled`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageScaleBy`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SAMLoader`
- `SaveImage`
- `SetNode`
- `StyleModelLoader`
- `SubtractMask`
- `Switch mask [Crystools]`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `WarpFacesBack`
- `easy cleanGpuUsed`
- `easy imageInsetCrop`
- `easy imageSize`
- `easy showAnything`
- `easy showTensorShape`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `Fast Muter (rgthree)` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 35 - 35 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 100% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，观测区间 35 - 35，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
