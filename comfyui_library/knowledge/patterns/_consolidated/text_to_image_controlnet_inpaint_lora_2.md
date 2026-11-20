---
name: text_to_image_controlnet_inpaint_lora_2
type: Text To Image
frequency: 4
level: strong
coverage: 0.85125
common_nodes: [AIO_Preprocessor, ApplyInstantID, ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, ConditioningCombine, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CropMask, DualCLIPLoader, EmptyLatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, GrowMask, Image Comparer (rgthree), ImageColorMatch+, ImageColorTransfer, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, InstructPixToPixConditioning, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LayerColor: ColorAdapter, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskBlur+, MaskToSEGS, ModelSamplingFlux, PreviewImage, PreviewTextNode, PrimitiveFloat, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, RepeatLatentBatch, SEGSPreview, SamplerCustomAdvanced, SaveImage, StringFunction|pysssss, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux_AI摄影人像换服装背景(参考图版)V3.2_1956598460248150017.json, 图片生成/图生图/换服装换背景_2079241532544208897.json, 图片生成/图生图/换服装换背景_2081988689659514881.json, 图片生成/图生图/换服装换背景_2096067015118254081.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux_AI摄影人像换服装背景(参考图版)V3.2_1956598460248150017.json、图片生成/图生图/换服装换背景_2079241532544208897.json、图片生成/图生图/换服装换背景_2081988689659514881.json、图片生成/图生图/换服装换背景_2096067015118254081.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyInstantID`
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningCombine`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropMask`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageColorTransfer`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `InstructPixToPixConditioning`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `KSamplerSelect`
- `LayerColor: ColorAdapter`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskBlur+`
- `MaskToSEGS`
- `ModelSamplingFlux`
- `PreviewImage`
- `PreviewTextNode`
- `PrimitiveFloat`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `RepeatLatentBatch`
- `SEGSPreview`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringFunction|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 4 | 100% |
| 采样步数 | 15 | 15 - 15 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.5 | 1.5 - 1.5 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 15，观测区间 15 - 15，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1.5 - 1.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，4 个样本，取值集中（一致性 100%）
