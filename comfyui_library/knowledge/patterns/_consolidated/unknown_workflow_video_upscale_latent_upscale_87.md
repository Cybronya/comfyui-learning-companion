---
name: unknown_workflow_video_upscale_latent_upscale_87
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.48175
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, Label (rgthree), LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), PrimitiveBoolean, PrimitiveFloat, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleCalculatorKJ, SolidMask, StringConcatenate, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine, VRAM_Debug, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3 I2V_T2V+OmniVoice-TTS多人数字人语音克隆生成_2052262074620891137.json, 视频生成/图生视频/LTX-2.3_-_I2V_T2V_Music-Video-MV制作超长视频_2077784625778348033.json, 视频生成/图生视频/【阿良绘】LTX-2.3_MV制作 _ 超长视频制作-10+续写版本(正式版)_2059931856744837121.json, 视频生成/图生视频/【阿良绘】LTX2.3_超长MV制作 _ 可无线续杯 - 续写版本(高质量)_V2_2059971603806642177.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_87

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3 I2V_T2V+OmniVoice-TTS多人数字人语音克隆生成_2052262074620891137.json、视频生成/图生视频/LTX-2.3_-_I2V_T2V_Music-Video-MV制作超长视频_2077784625778348033.json、视频生成/图生视频/【阿良绘】LTX-2.3_MV制作 _ 超长视频制作-10+续写版本(正式版)_2059931856744837121.json、视频生成/图生视频/【阿良绘】LTX2.3_超长MV制作 _ 可无线续杯 - 续写版本(高质量)_V2_2059971603806642177.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `Label (rgthree)`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleCalculatorKJ`
- `SolidMask`
- `StringConcatenate`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 3/4 个有
- `ComfySwitchNode` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `CreateVideo` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `LoadVideosFromFolder` —— 3/4 个有
- `MelBandRoFormerModelLoader` —— 3/4 个有
- `MelBandRoFormerSampler` —— 3/4 个有
- `PrimitiveInt` —— 3/4 个有
- `PrimitiveString` —— 3/4 个有
- `PromptRelayEncodeTimeline` —— 3/4 个有
- `ResizeImagesByLongerEdge` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `TrimAudioDuration` —— 3/4 个有
- `VAEDecode` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `DualCLIPLoaderGGUF` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `UnetLoaderGGUF` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `Audio Duration (mtb)` —— 1/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageBatch` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `LTX2_NAG` —— 1/4 个有
- `LazySwitchKJ` —— 1/4 个有
- `OmniVoiceMultiSpeakerTTS` —— 1/4 个有
- `OmniVoiceVoiceCloneTTS` —— 1/4 个有
- `OmniVoiceWhisperLoader` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `SeedGenerator` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
