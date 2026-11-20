---
name: unknown_workflow_lora_sampler_unet_322
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7745
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ImageResizeKJv2, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ChainAssemble, MiniMaxH3ChainContext, MiniMaxH3ChainCurrent, MiniMaxH3ChainLoopEnd, MiniMaxH3ChainLoopStart, MiniMaxH3ChainPlan, MiniMaxH3ChainReview, MiniMaxH3ChainSegmentSave, MiniMaxH3LoopTrim, MiniMaxH3SigmaShift, MiniMaxH3TaggedAudioReference, MiniMaxH3TaggedPictureReference, MiniMaxH3TaggedReferenceToVideo, ModelAttentionBackend, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, StringBatch, StringReplace, StringSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [数字人/数字人/H3_无限数字人对口型 8 步版_2095888155911217154.json, 视频生成/图生视频/H3 音色克隆 微表情控制+语气控制数字人_2098276286266437633.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_322

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/H3_无限数字人对口型 8 步版_2095888155911217154.json、视频生成/图生视频/H3 音色克隆 微表情控制+语气控制数字人_2098276286266437633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ChainAssemble`
- `MiniMaxH3ChainContext`
- `MiniMaxH3ChainCurrent`
- `MiniMaxH3ChainLoopEnd`
- `MiniMaxH3ChainLoopStart`
- `MiniMaxH3ChainPlan`
- `MiniMaxH3ChainReview`
- `MiniMaxH3ChainSegmentSave`
- `MiniMaxH3LoopTrim`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3TaggedAudioReference`
- `MiniMaxH3TaggedPictureReference`
- `MiniMaxH3TaggedReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StringBatch`
- `StringReplace`
- `StringSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioBeforeAfterSilence` —— 1/2 个有
- `LTXVConcatAVLatent` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SolidMask` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
