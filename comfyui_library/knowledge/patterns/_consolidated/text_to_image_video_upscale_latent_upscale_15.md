---
name: text_to_image_video_upscale_latent_upscale_15
type: Text To Image
frequency: 5
level: strong
coverage: 0.5616
common_nodes: [Bjornulf_ShowInt, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, EmptySD3LatentImage, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, Label (rgthree), LatentUpscaleModelLoader, LayerUtility: NumberCalculatorV2, LayerUtility: TextBox, LoadAudioUI, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, PrimitiveFloat, SamplerCustom, SaveImage, Seed (rgthree), SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VHS_SelectImages, VHS_VideoCombine, VisualizeSigmasKJ, easy convertAnything, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2062165204129112066.json, 视频生成/图生视频/2068328419368194050.json, 视频生成/图生视频/2068613234571169793.json, 视频生成/图生视频/2068625253730967553.json, 视频生成/文生视频/工作流基础系列25-LTX 2.3文生视频工作流_2061941901544222722.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_15

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2062165204129112066.json、视频生成/图生视频/2068328419368194050.json、视频生成/图生视频/2068613234571169793.json、视频生成/图生视频/2068625253730967553.json、视频生成/文生视频/工作流基础系列25-LTX 2.3文生视频工作流_2061941901544222722.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 5 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `GetNode`
- `INTConstant`
- `KSampler`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LatentUpscaleModelLoader`
- `LayerUtility: NumberCalculatorV2`
- `LayerUtility: TextBox`
- `LoadAudioUI`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `SamplerCustom`
- `SaveImage`
- `Seed (rgthree)`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `easy convertAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `LTXVImgToVideoInplace` —— 4/5 个有
- `LTXVPreprocess` —— 4/5 个有
- `LoadVideo` —— 4/5 个有
- `ResizeImageMaskNode` —— 4/5 个有
- `LoadAudio` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 9 - 9 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 121 | 121 - 121 | 5 | 100% |
| 高度 | 24 | 24 - 24 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 9 - 9，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 121，观测区间 121 - 121，5 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
