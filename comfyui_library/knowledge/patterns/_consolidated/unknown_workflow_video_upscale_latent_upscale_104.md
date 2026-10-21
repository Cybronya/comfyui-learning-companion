---
name: unknown_workflow_video_upscale_latent_upscale_104
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.626
common_nodes: [Audio Duration (mtb), CFGGuider, CLIPLoader, CLIPTextEncode, DF_Int_to_Float, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleBy, ImpactExecutionOrderController, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVEmptyLatentAudio, LTXVGemmaEnhancePrompt, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, UNETLoader, VAELoader, WanVideoImageResizeToClosest, easy boolean, easy float, easy ifElse, easy int]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2087430857970769922.json, 视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217.json, 视频生成/图生视频/数字人胶片讲解视频三页一起讲-LTX-25 - 3K_2096823654553317377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_104

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2087430857970769922.json、视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217.json、视频生成/图生视频/数字人胶片讲解视频三页一起讲-LTX-25 - 3K_2096823654553317377.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DF_Int_to_Float`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImpactExecutionOrderController`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVEmptyLatentAudio`
- `LTXVGemmaEnhancePrompt`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAELoader`
- `WanVideoImageResizeToClosest`
- `easy boolean`
- `easy float`
- `easy ifElse`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `1hew_AudioDuration` —— 1/3 个有
- `AudioConcat` —— 1/3 个有
- `BOOLConstant` —— 1/3 个有
- `BiRefNetRMBG` —— 1/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `HeartMuLa_Transcribe` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `Image Blend by Mask` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `JWFloatToInteger` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `JWStringGetLine` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `Qwen3TTSModelLoader` —— 1/3 个有
- `Qwen3TTSVoiceClone` —— 1/3 个有
- `Qwen3_VQA_Plus` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `TextBoxMira` —— 1/3 个有
- `VHS_VideoCombine` —— 1/3 个有
- `VRAM_Debug` —— 1/3 个有
- `easy batchAnything` —— 1/3 个有
- `easy compare` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy mathFloat` —— 1/3 个有
- `easy mathInt` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
