---
name: image_to_image_controlnet_ipadapter_upscale_6
type: Image To Image
frequency: 2
level: weak
coverage: 0.7885
common_nodes: [AIO_Preprocessor, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DetailTransfer, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, GrowMaskWithBlur, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), InvertMask, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: ImageBlend, LayerUtility: ImageBlendAdvance, LayerUtility: ImageScaleByAspectRatio V2, LightSource, LoadAndApplyICLightUnet, LoadImage, LoraLoader, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/换背景 _ 电商实用版V5.0_1903714144967626754.json, 平台全量/产品换背景打光加高清放大_1895314794113597442.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换背景 _ 电商实用版V5.0_1903714144967626754.json、平台全量/产品换背景打光加高清放大_1895314794113597442.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

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
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `InvertMask`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LightSource`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `ImageAndMaskPreview` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `JoinImageWithAlpha` —— 1/2 个有
- `LayerUtility: BooleanOperator` —— 1/2 个有
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LayerUtility: ImageCombineAlpha` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LayerUtility: TextImage` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewBridge` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `TextBox` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy imageIndexSwitch` —— 1/2 个有
- `easy imageSizeBySide` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.15 | - | 2 | 67% |
| LoRA 模型强度 | 0.7 | - | 2 | 86% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 4.75 | - | 2 | 74% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.625 | - | 2 | 40% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.15，样本不足，未给区间，2 个样本
- LoRA 模型强度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 4.75，样本不足，未给区间，2 个样本
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.625，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
