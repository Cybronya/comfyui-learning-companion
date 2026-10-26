---
name: unknown_workflow_video_upscale_latent_upscale_71
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.518
common_nodes: [BasicScheduler, BlockifyMask, CFGGuider, CLIPTextEncode, ComfyMathExpression, Float to Int, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAddLatentGuide, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVPreprocessMasks, LTXVSeparateAVLatent, LTXVSetVideoLatentNoiseMasks, LatentUpscaleModelLoader, LayerUtility: PurgeVRAM, LazySwitchKJ, LoadAudio, LoraLoaderModelOnly, ManualSigmas, MaskToImage, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncode, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy sam3ModelLoader, easy sam3VideoSegmentation, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/LTX2.3上传视频改口型！B站艾橘溪_2047297756296908801.json, 数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2060596774003367937.json, 数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2080257073954246658.json, 数字人/数字人/LTX2.3视频改口型加强版_2060295017062821889.json, 视频生成/图生视频/LTX2.3视频改口型加强版_2080261317948170241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_71

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/LTX2.3上传视频改口型！B站艾橘溪_2047297756296908801.json、数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2060596774003367937.json、数字人/数字人/LTX2.3视频改口型加强版 视频生视频 数字人复刻短视频 复刻克隆数字人形象说话_2080257073954246658.json、数字人/数字人/LTX2.3视频改口型加强版_2060295017062821889.json、视频生成/图生视频/LTX2.3视频改口型加强版_2080261317948170241.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `Float to Int`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAddLatentGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVPreprocessMasks`
- `LTXVSeparateAVLatent`
- `LTXVSetVideoLatentNoiseMasks`
- `LatentUpscaleModelLoader`
- `LayerUtility: PurgeVRAM`
- `LazySwitchKJ`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskToImage`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTX2AttentionTunerPatch` —— 2/5 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
