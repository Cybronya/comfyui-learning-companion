---
name: unknown_workflow_video_upscale_latent_upscale_177
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4785
common_nodes: [BasicScheduler, BlockifyMask, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyAudio, EmptyImage, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, GetNode, GrowMaskWithBlur, INTConstant, ImageCompositeFromMaskBatch+, ImageCropV2, ImageFromBatch+, ImageResizeKJv2, JWImageResizeByLongerSide, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MaskRepeatBatch, PreviewImage, PrimitiveBoundingBox, PrimitiveFloat, PrimitiveInt, RandomNoise, RecordAudio, ReservedRegionFrameComposer, ResizeImageMaskNode, SamplerCustomAdvanced, SeCModelLoader_Ultra-Fast, SeCVideoSegmentation_Ultra-Fast, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SimpleMath+, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncode, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine, VRAMReserver, easy cleanGpuUsed, easy imageSize, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/视频去字幕（参考）-0.5版本 循环_2048762397640364034.json, 视频生成/文生视频/视频去字幕（参考）-0.5版本_2048741719289630722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_177

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/视频去字幕（参考）-0.5版本 循环_2048762397640364034.json、视频生成/文生视频/视频去字幕（参考）-0.5版本_2048741719289630722.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：48%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyAudio`
- `EmptyImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageCompositeFromMaskBatch+`
- `ImageCropV2`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWImageResizeByLongerSide`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MaskRepeatBatch`
- `PreviewImage`
- `PrimitiveBoundingBox`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `RecordAudio`
- `ReservedRegionFrameComposer`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SeCModelLoader_Ultra-Fast`
- `SeCVideoSegmentation_Ultra-Fast`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SimpleMath+`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRAMReserver`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyLTXVLatentVideo` —— 1/2 个有
- `Int` —— 1/2 个有
- `VHS_BatchManager` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 24 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 24，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
