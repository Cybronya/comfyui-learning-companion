---
name: text_to_image_ipadapter_lora_sampler
type: Text To Image
frequency: 4
level: moderate
coverage: 0.86825
common_nodes: [BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, DetailTransfer, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GrowMaskWithBlur, ICLightConditioning, IPAdapter, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), InspyrenetRembg, KSampler, LayerUtility: ExtendCanvas, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextJoin, LoadAndApplyICLightUnet, LoadImage, LoraLoader, LoraLoaderModelOnly, MaskPreview+, PreviewImage, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy getNode, easy imageSize, easy setNode, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/【升级版】一键人像换背景+自适应环境打光+FLUX优化+_2022610568435212290.json, 图片生成/图生图/一键人像换背景+自适应环境打光+FLUX优化_1977930130830020609.json, 平台全量/【升级版】一键人像换背景+自适应环境打光+FLUX优化_1920834564716171266.json, 平台全量/一键人像换背景+自适应环境打光+FLUX优化_1915340871951122434.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_lora_sampler

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【升级版】一键人像换背景+自适应环境打光+FLUX优化+_2022610568435212290.json、图片生成/图生图/一键人像换背景+自适应环境打光+FLUX优化_1977930130830020609.json、平台全量/【升级版】一键人像换背景+自适应环境打光+FLUX优化_1920834564716171266.json、平台全量/一键人像换背景+自适应环境打光+FLUX优化_1915340871951122434.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DetailTransfer`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `IPAdapter`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `InspyrenetRembg`
- `KSampler`
- `LayerUtility: ExtendCanvas`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextJoin`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy getNode`
- `easy imageSize`
- `easy setNode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `BodySegment` —— 3/4 个有
- `ControlNetApplyAdvanced` —— 3/4 个有
- `ControlNetLoader` —— 3/4 个有
- `FaceDetailer` —— 3/4 个有
- `Image Overlay` —— 3/4 个有
- `Joy_caption` —— 3/4 个有
- `Joy_caption_load` —— 3/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/4 个有
- `SAMLoader` —— 3/4 个有
- `SUPIR_Upscale` —— 3/4 个有
- `SetLatentNoiseMask` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `UltralyticsDetectorProvider` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy imageColorMatch` —— 3/4 个有
- `preview_mask` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 1 | 4 | 13% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| LoRA 模型强度 | 0.4 | 0.4 - 0.6 | 4 | 81% |
| LoRA 文本强度 | 0.4 | 0.4 - 0.6 | 4 | 81% |
| ControlNet 权重 | 0.25 | 0.25 - 0.25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 1，4 个样本，取值分散，一致性仅 13%
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.4，观测区间 0.4 - 0.6，4 个样本，取值集中（一致性 81%）
- LoRA 文本强度 中位数 0.4，观测区间 0.4 - 0.6，4 个样本，取值集中（一致性 81%）
- ControlNet 权重 中位数 0.25，观测区间 0.25 - 0.25，3 个样本，取值集中（一致性 100%）
