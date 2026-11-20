---
name: unknown_workflow_lora_sampler_unet_328
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9125
common_nodes: [1hew_AudioDuration, BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LoadAudio, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, TrimAudio, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/mInimax h3 sol attention 提速工作流_2113180576420294657.json, 视频生成/图生视频/minimax h3 selflift 双采8工作流_2109955158095519746.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_328

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/mInimax h3 sol attention 提速工作流_2113180576420294657.json、视频生成/图生视频/minimax h3 selflift 双采8工作流_2109955158095519746.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_AudioDuration`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 1/2 个有
- `CreateVideo` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `LTXVSeparateAVLatent` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `QwenH3PromptLocal` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `VAEDecodeAudio` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
