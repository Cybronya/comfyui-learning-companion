---
name: image_to_image_controlnet_ipadapter_inpaint_2
type: Image To Image
frequency: 2
level: weak
coverage: 0.76
common_nodes: [AddMask, Anything Everywhere3, BasicScheduler, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DWPreprocessor, DeepTranslatorTextNode, DepthAnythingV2Preprocessor, DifferentialDiffusion, DualCLIPLoader, Fast Groups Bypasser (rgthree), FeatherMask, FluxGuidance, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageToMask, InpaintModelConditioning, InvertMask (segment anything), Joy_caption_two_advanced, Joy_caption_two_load, Joy_extra_options, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerMask: SegmentAnythingUltra V2, LayerStyle: ColorOverlay V2, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MaskPreview+, MaskToImage, PrepImageForClipVision, SamplerCustom, SaveImage, ShowText|pysssss, SubtractMask, Text Concatenate, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy clearCacheAll, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/敦煌人像_2076041450332188673.json, 平台全量/敦煌人像写真工作流-AI摄影写真（人脸不变+姿势固定）_1896098216989884418.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_inpaint_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/敦煌人像_2076041450332188673.json、平台全量/敦煌人像写真工作流-AI摄影写真（人脸不变+姿势固定）_1896098216989884418.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `AddMask`
- `Anything Everywhere3`
- `BasicScheduler`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DWPreprocessor`
- `DeepTranslatorTextNode`
- `DepthAnythingV2Preprocessor`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FeatherMask`
- `FluxGuidance`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `InpaintModelConditioning`
- `InvertMask (segment anything)`
- `Joy_caption_two_advanced`
- `Joy_caption_two_load`
- `Joy_extra_options`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerStyle: ColorOverlay V2`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `MaskToImage`
- `PrepImageForClipVision`
- `SamplerCustom`
- `SaveImage`
- `ShowText|pysssss`
- `SubtractMask`
- `Text Concatenate`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy clearCacheAll`
- `easy imageColorMatch`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.9 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
