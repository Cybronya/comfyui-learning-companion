---
name: unknown_workflow_video_upscale_latent_upscale_119
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.422333
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAddVideoICLoRAGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PreviewAny, PrimitiveBoolean, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetNode, StringConcatenate, TextGenerateLTX2Prompt, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideoFFmpeg, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/LTX-2.3视频扩展（增亮色彩版）_2045866940337491969.json, 音频生成/音频生成/LTX-2.3视频扩展（完美扩展版）_2045860108604805122.json, 音频生成/音频生成/LTX2.3 视频配音角色对口型_2062400772872167426.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_119

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/LTX-2.3视频扩展（增亮色彩版）_2045866940337491969.json、音频生成/音频生成/LTX-2.3视频扩展（完美扩展版）_2045860108604805122.json、音频生成/音频生成/LTX2.3 视频配音角色对口型_2062400772872167426.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：42%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetNode`
- `StringConcatenate`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImagePadKJ` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LTXICLoRALoaderModelOnly` —— 2/3 个有
- `LazySwitchKJ` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `VHS_VideoInfo` —— 2/3 个有
- `BasicScheduler` —— 1/3 个有
- `Color Correct (mtb)` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `LTXVAudioVAEEncode` —— 1/3 个有
- `LTXVChunkFeedForward` —— 1/3 个有
- `LTXVLatentUpsampler` —— 1/3 个有
- `LTXVSetAudioRefTokens` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `SimpleCalculatorKJ` —— 1/3 个有
- `easy convertAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 24 - 25 | 3 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，3 个样本，取值集中（一致性 98%）
