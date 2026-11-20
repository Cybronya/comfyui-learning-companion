---
name: unknown_workflow_video_upscale_latent_upscale_145
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.845
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CheckpointLoaderSimple, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, GetImageRangeFromBatch, GetImageSize, GetImageSize+, GetNode, GuiderParameters, INTConstant, ImageConcatMulti, ImagePadForOutpaint, ImageResizeKJv2, InsertImagesToBatchIndexed, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoader, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultimodalGuider, PreviewImage, PrimitiveFloat, RandomNoise, RepeatImageBatch, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SigmasPreview, SimpleCalculatorKJ, SolidMask, TrimAudioDuration, UnetLoaderGGUF, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/(Bfs Klein版)Ltx-2视频换脸V1_2018540820999184385.json, 视频生成/图生视频/（首帧上传版）Ltx-2视频换脸V1_2019433627276288001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_145

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/(Bfs Klein版)Ltx-2视频换脸V1_2018540820999184385.json、视频生成/图生视频/（首帧上传版）Ltx-2视频换脸V1_2019433627276288001.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CheckpointLoaderSimple`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `GuiderParameters`
- `INTConstant`
- `ImageConcatMulti`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `InsertImagesToBatchIndexed`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultimodalGuider`
- `PreviewImage`
- `PrimitiveFloat`
- `RandomNoise`
- `RepeatImageBatch`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SigmasPreview`
- `SimpleCalculatorKJ`
- `SolidMask`
- `TrimAudioDuration`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `FastCanvas` —— 1/2 个有
- `FastCanvasTool` —— 1/2 个有
- `Flux2Scheduler` —— 1/2 个有
- `Image Rembg (Remove Background)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
