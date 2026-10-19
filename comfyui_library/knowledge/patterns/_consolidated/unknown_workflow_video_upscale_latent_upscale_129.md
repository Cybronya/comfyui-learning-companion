---
name: unknown_workflow_video_upscale_latent_upscale_129
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5625
common_nodes: [Any Switch (rgthree), Audio Duration (mtb), CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoaderGGUF, EmptyImage, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetImageSize, GetNode, HeartMuLa_Transcribe, ImageResizeKJv2, ImageScaleBy, ImpactExecutionOrderController, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoaderGGUF, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PathchSageAttentionKJ, PreviewAudio, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, ShowText|pysssss, SolidMask, StringReplace, TrimAudioDuration, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2016443355604983809.json, 视频生成/图生视频/2014681763813007362.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_129

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2016443355604983809.json、视频生成/图生视频/2014681763813007362.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Audio Duration (mtb)`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoaderGGUF`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetNode`
- `HeartMuLa_Transcribe`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImpactExecutionOrderController`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoaderGGUF`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `ShowText|pysssss`
- `SolidMask`
- `StringReplace`
- `TrimAudioDuration`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AudioAdjustVolume` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `FB_Qwen3TTSVoiceClone` —— 1/2 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 1/2 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LTXVAudioVAELoader` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ReservedVRAMSetter` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `easy ckptNames` —— 1/2 个有
- `easy float` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
