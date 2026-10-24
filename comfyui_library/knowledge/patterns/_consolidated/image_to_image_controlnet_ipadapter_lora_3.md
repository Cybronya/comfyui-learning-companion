---
name: image_to_image_controlnet_ipadapter_lora_3
type: Image To Image
frequency: 2
level: weak
coverage: 0.921
common_nodes: [AIO_Preprocessor, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), InvertMask (segment anything), KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, LayerUtility: ImageBlendAdvance, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LightSource, LoadAndApplyICLightUnet, LoadImage, LoraLoader, LoraLoaderModelOnly, MaskPreview+, PreviewImage, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/XL产品换背景+FLUX优化+打光+细节还原_1978152934099804162.json, 图片生成/图生图/最强产品换背景+FLUX细节优化+LOGO文字100%还原（新增参考图擦除产品功能）_1917229961717940226.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/XL产品换背景+FLUX优化+打光+细节还原_1978152934099804162.json、图片生成/图生图/最强产品换背景+FLUX细节优化+LOGO文字100%还原（新增参考图擦除产品功能）_1917229961717940226.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DetailTransfer`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `InvertMask (segment anything)`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LightSource`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `AnimeLineArtPreprocessor` —— 1/2 个有
- `CR Upscale Image` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `GrowMask` —— 1/2 个有
- `INPAINT_ApplyFooocusInpaint` —— 1/2 个有
- `INPAINT_LoadFooocusInpaint` —— 1/2 个有
- `Image Blank` —— 1/2 个有
- `ImageCompositeMasked` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `ImpactDilateMask` —— 1/2 个有
- `LayerUtility: LaMa` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `VAEEncodeForInpaint` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy setNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.65 | - | 2 | 46% |
| LoRA 模型强度 | 0.5 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
