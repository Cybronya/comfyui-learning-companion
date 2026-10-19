---
name: unknown_workflow_upscale_latent_upscale_lora_66
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8345
common_nodes: [BlockifyMask, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, FaceSegment, GetImageRangeFromBatch, GetImageSize, ImageResizeKJv2, KSamplerSelect, LTXVAddLatentGuide, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocessMasks, LTXVSeparateAVLatent, LTXVSetVideoLatentNoiseMasks, LatentUpscaleModelLoader, LoadAudio, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeMask, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, TrimAudioDuration, VAEDecodeTiled, VAEEncode, VHS_LoadVideoFFmpeg, VHS_VideoInfo]
problems: []
missing: []
members: [视频生成/图生视频/2073317542965366785.json, 音频生成/音频生成/LTX2.3 V2V 视频对口型_2039622711588167681.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_66

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2073317542965366785.json、音频生成/音频生成/LTX2.3 V2V 视频对口型_2039622711588167681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `FaceSegment`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAddLatentGuide`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocessMasks`
- `LTXVSeparateAVLatent`
- `LTXVSetVideoLatentNoiseMasks`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeMask`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VAEEncode`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoaderGGUF` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
