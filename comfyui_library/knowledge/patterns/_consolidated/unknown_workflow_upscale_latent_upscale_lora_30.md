---
name: unknown_workflow_upscale_latent_upscale_lora_30
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7956
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleMath+, SolidMask, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2037904151203549186.json, 视频生成/图生视频/2039705616616263681.json, 视频生成/图生视频/2032689684190597122.json, 视频生成/图生视频/2033038433718898690.json, 视频生成/图生视频/2057753722972889090.json, 视频生成/图生视频/2033180233595097089.json, 视频生成/图生视频/2038618856104665090.json, 视频生成/图生视频/2044840720346910722.json, 视频生成/图生视频/2033020049098805250.json, 视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_30

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2037904151203549186.json、视频生成/图生视频/2039705616616263681.json、视频生成/图生视频/2032689684190597122.json、视频生成/图生视频/2033038433718898690.json、视频生成/图生视频/2057753722972889090.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 9/10 个有
- `LTXVPreprocess` —— 9/10 个有
- `ResizeImagesByLongerEdge` —— 9/10 个有
- `Bjornulf_ShowInt` —— 8/10 个有
- `CreateVideo` —— 8/10 个有
- `EmptyImage` —— 8/10 个有
- `ImageScaleBy` —— 8/10 个有
- `ImpactInt` —— 8/10 个有
- `LTXVAudioVAEDecode` —— 8/10 个有
- `PainterAudioLength` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `VAEDecode` —— 8/10 个有
- `CR Text` —— 7/10 个有
- `AudioCrop` —— 6/10 个有
- `CR Prompt Text` —— 6/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `FB_Qwen3TTSVoiceClone` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `ShowAnything|Mie` —— 4/10 个有
- `WhisperSTT` —— 4/10 个有
- `easy int` —— 3/10 个有
- `easy seed` —— 3/10 个有
- `BasicScheduler` —— 2/10 个有
- `CM_IntToFloat` —— 2/10 个有
- `LTXVEmptyLatentAudio` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `SoundFlow_GetLength` —— 2/10 个有
- `VAEDecodeTiled` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `AudioConcatenate` —— 1/10 个有
- `ComfyMathExpression` —— 1/10 个有
- `DualCLIPLoader` —— 1/10 个有
- `FloatConstant` —— 1/10 个有
- `ImpactConditionalBranch` —— 1/10 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/10 个有
- `LTXVImgToVideoInplaceKJ` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `ResizeImageMaskNode` —— 1/10 个有
- `Switch any [Crystools]` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `easy imageConcat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
