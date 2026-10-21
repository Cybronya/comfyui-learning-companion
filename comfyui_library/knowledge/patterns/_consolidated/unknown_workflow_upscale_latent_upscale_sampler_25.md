---
name: unknown_workflow_upscale_latent_upscale_sampler_25
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.874
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/文生视频/LTX单人自定义语音-工作流_2033410143752294402.json, 视频生成/文生视频/video_ltx2_custom_voice_kijai_multi_2031409117054640130.json, 视频生成/文生视频/video_ltx2_custom_voice_kijai_single_2031404838935859202.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_25

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/LTX单人自定义语音-工作流_2033410143752294402.json、视频生成/文生视频/video_ltx2_custom_voice_kijai_multi_2031409117054640130.json、视频生成/文生视频/video_ltx2_custom_voice_kijai_single_2031404838935859202.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `MelBandRoFormerModelLoader` —— 2/3 个有
- `MelBandRoFormerSampler` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `SimpleCalculatorKJ` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `1hew_AudioDuration` —— 1/3 个有
- `AudioConcat` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `FB_Qwen3TTSVoiceClone` —— 1/3 个有
- `Float to Int` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Int` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
