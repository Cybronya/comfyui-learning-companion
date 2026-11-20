---
name: unknown_workflow_inpaint_upscale_lora_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.847
common_nodes: [CLIPTextEncode, ConditioningZeroOut, ConstrainImage|pysssss, DifferentialDiffusion, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, If ANY execute A else B, ImageFromBatch+, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, InpaintCrop, InpaintModelConditioning, InpaintStitch, InspyrenetRembg, InvertMask, IsMaskEmpty, KSampler (Efficient), LayerMask: LoadFlorence2Model, LayerMask: MaskPreview, LayerMask: ObjectDetectorFL2, LayerMask: SAM2Ultra, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, PreviewImage, RHHiddenNodes, Replace Text _O, SaveImage, String Literal, Switch any [Crystools], TTP_Expand_And_Mask, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy clearCacheAll, easy imageBatchToImageList, easy imageSplitGrid, easy seed, easy showAnything, image_concat_mask(rh)]
problems: []
missing: []
members: ["图片生成/图生图/项链,玉石,小装饰品佩戴王_1908812323018911745.json", 平台全量/小饰品佩戴王_1898754696822378498.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/项链,玉石,小装饰品佩戴王_1908812323018911745.json、平台全量/小饰品佩戴王_1898754696822378498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DifferentialDiffusion`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `If ANY execute A else B`
- `ImageFromBatch+`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembg`
- `InvertMask`
- `IsMaskEmpty`
- `KSampler (Efficient)`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: MaskPreview`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: SAM2Ultra`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RHHiddenNodes`
- `Replace Text _O`
- `SaveImage`
- `String Literal`
- `Switch any [Crystools]`
- `TTP_Expand_And_Mask`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy clearCacheAll`
- `easy imageBatchToImageList`
- `easy imageSplitGrid`
- `easy seed`
- `easy showAnything`
- `image_concat_mask(rh)`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `ModelSamplingFlux` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `StyleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | - | 2 | 25% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，样本不足，未给区间，2 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
