---
name: unknown_workflow_video_lora_sampler_967
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.694
common_nodes: [AudioConcat, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, Color Correct (mtb), ConditioningZeroOut, EmptyAudio, EmptyLTXVLatentVideo, GetImageRangeFromBatch, GetImageSize, GetNode, ImageConcanate, ImagePadKJ, ImageResizeKJv2, Int, JWIntegerToString, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadAudio, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, NormalizeAudioLoudness, PreviewAny, PreviewAudio, PrimitiveBoolean, PrimitiveStringMultiline, PromptRelayEncode, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetNode, SimpleCalculatorKJ, StringConcatenate, Switch image [Crystools], TrimAudioDuration, VAEDecodeTiled, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy ckptNames, easy showAnything]
problems: []
missing: []
members: [音频生成/音频生成/LTX2.3 V2V时间戳控制Prompt Relay视频4D扩展_2047301031557603329.json, 音频生成/音频生成/LTX2.3 V2V视频分镜全向扩展_2057162951529947137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_967

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/LTX2.3 V2V时间戳控制Prompt Relay视频4D扩展_2047301031557603329.json、音频生成/音频生成/LTX2.3 V2V视频分镜全向扩展_2057162951529947137.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `Color Correct (mtb)`
- `ConditioningZeroOut`
- `EmptyAudio`
- `EmptyLTXVLatentVideo`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetNode`
- `ImageConcanate`
- `ImagePadKJ`
- `ImageResizeKJv2`
- `Int`
- `JWIntegerToString`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `NormalizeAudioLoudness`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleCalculatorKJ`
- `StringConcatenate`
- `Switch image [Crystools]`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy ckptNames`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoConditionOnly` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `TTP_text_mix` —— 1/2 个有

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
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
