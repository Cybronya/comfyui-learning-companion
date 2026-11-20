---
name: unknown_workflow_lora_sampler_clip_343
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.367
common_nodes: [AudioConcat, BasicScheduler, CFGGuider, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, GetNode, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVideoMask, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadAudio, LoraLoaderModelOnly, ManualSigmas, NormalizeAudioLoudness, PathchSageAttentionKJ, PreviewAudio, PreviewImage, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, PromptRelayEncode, RandomNoise, SamplerCustomAdvanced, SamplerEulerAncestral, SaveVideo, SetNode, TrimAudioDuration, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VAELoaderKJ, VHS_LoadVideo]
problems: []
missing: []
members: [视频生成/文生视频/ltx2.3全能参考_2051856553040457729.json, 视频生成/文生视频/参考视频，保持人物特征出视频ltx_2048592373965398018.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_343

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/ltx2.3全能参考_2051856553040457729.json、视频生成/文生视频/参考视频，保持人物特征出视频ltx_2048592373965398018.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：37%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `GetNode`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVideoMask`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `NormalizeAudioLoudness`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveVideo`
- `SetNode`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_LoadVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `LTX2SamplingPreviewOverride` —— 1/2 个有
- `LTXAVTextEncoderLoader` —— 1/2 个有
- `LTXVEnhanceAVideoKJ` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

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
