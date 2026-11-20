---
name: unknown_workflow_inpaint_upscale_lora_10
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7845
common_nodes: [Anything Everywhere3, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BasicGuider, BasicScheduler, Bjornulf_ShowInt, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, ColorMatch, DifferentialDiffusion, DualCLIPLoader, EmptyImage, Fast Groups Muter (rgthree), FluxGuidance, FluxResolutionNode, GetImageSize, GetImageSizeAndCount, Image Comparer (rgthree), Image Overlay, Image To Mask, ImageCrop+, ImageMaskSwitch, ImagePadForOutpaint, ImageResize+, ImageResizeKJ, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, InpaintModelConditioning, InvertMask, JjkText, KSamplerSelect, Label (rgthree), LayerMask: MaskGrow, LayerUtility: ColorImage, LayerUtility: ColorPicker, LayerUtility: GetImageSize, LoadImage, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, PreviewImage, PrimitiveFloat, RH_Captioner, RH_Translator, RMBG, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextCombinerTwo, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy makeImageForICLora, easy showAnything, preview_mask]
problems: []
missing: []
members: [平台全量/电商产品一致性 换背景_1916419582029139970.json, 平台全量/电商产品一致性 换背景_1920317556681277442.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/电商产品一致性 换背景_1916419582029139970.json、平台全量/电商产品一致性 换背景_1920317556681277442.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_ShowInt`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ColorMatch`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `Fast Groups Muter (rgthree)`
- `FluxGuidance`
- `FluxResolutionNode`
- `GetImageSize`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `Image Overlay`
- `Image To Mask`
- `ImageCrop+`
- `ImageMaskSwitch`
- `ImagePadForOutpaint`
- `ImageResize+`
- `ImageResizeKJ`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `InvertMask`
- `JjkText`
- `KSamplerSelect`
- `Label (rgthree)`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `LayerUtility: GetImageSize`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MathExpression|pysssss`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_Captioner`
- `RH_Translator`
- `RMBG`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextCombinerTwo`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy makeImageForICLora`
- `easy showAnything`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
