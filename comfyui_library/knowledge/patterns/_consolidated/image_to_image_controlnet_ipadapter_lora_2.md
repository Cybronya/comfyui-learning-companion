---
name: image_to_image_controlnet_ipadapter_lora_2
type: Image To Image
frequency: 4
level: strong
coverage: 0.933
common_nodes: [AIO_Preprocessor, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), InvertMask (segment anything), KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, LayerUtility: ImageBlendAdvance, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LightSource, LoadAndApplyICLightUnet, LoadImage, LoraLoader, LoraLoaderModelOnly, PreviewImage, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/XL产品换背景+FLUX优化+打光+细节还原_1978152934099804162.json, 图片生成/图生图/最强产品换背景+FLUX细节优化+LOGO文字100%还原（新增参考图擦除产品功能）_1917229961717940226.json, 平台全量/XL产品换背景+FLUX优化+打光+细节还原_1902914479410065410.json, 平台全量/XL产品换背景+FLUX优化+打光+细节还原_1909197556327264258.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_lora_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/XL产品换背景+FLUX优化+打光+细节还原_1978152934099804162.json、图片生成/图生图/最强产品换背景+FLUX细节优化+LOGO文字100%还原（新增参考图擦除产品功能）_1917229961717940226.json、平台全量/XL产品换背景+FLUX优化+打光+细节还原_1902914479410065410.json、平台全量/XL产品换背景+FLUX优化+打光+细节还原_1909197556327264258.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PreviewImage`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 3/4 个有
- `Florence2ModelLoader` —— 3/4 个有
- `Florence2Run` —— 3/4 个有
- `easy getNode` —— 3/4 个有
- `easy setNode` —— 3/4 个有
- `MaskPreview+` —— 2/4 个有
- `AnimeLineArtPreprocessor` —— 1/4 个有
- `CR Upscale Image` —— 1/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GrowMask` —— 1/4 个有
- `INPAINT_ApplyFooocusInpaint` —— 1/4 个有
- `INPAINT_LoadFooocusInpaint` —— 1/4 个有
- `Image Blank` —— 1/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `ImageToMask` —— 1/4 个有
- `ImpactDilateMask` —— 1/4 个有
- `LayerUtility: LaMa` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `SetLatentNoiseMask` —— 1/4 个有
- `ShowText` —— 1/4 个有
- `VAEEncodeForInpaint` —— 1/4 个有
- `WD14Tagger|pysssss` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 4 | 65% |
| 采样算法 | dpm_2 | - | 4 | 50% |
| 调度器 | karras | - | 4 | 75% |
| 重绘幅度 | 0.8 | 0.3 - 1 | 4 | 64% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，4 个样本
- 采样算法 最常用 dpm_2，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 75%
- 重绘幅度 中位数 0.8，观测区间 0.3 - 1，4 个样本
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，4 个样本，取值集中（一致性 100%）
