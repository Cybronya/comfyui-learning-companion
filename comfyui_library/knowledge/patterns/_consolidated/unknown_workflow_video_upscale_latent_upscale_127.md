---
name: unknown_workflow_video_upscale_latent_upscale_127
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.772
common_nodes: [Astra, BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, ExtendIntermediateSigmas, FLAVR VFI, FlashVSRNode, GetImageRangeFromBatch, GetNode, GoohaiAnySwitch, H3KitSemanticBridge, H3SigmaRefiner, Image Batch, ImageAddNoise, ImpactConditionalBranch, InversionDemoLazySwitch, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3PromptEnhancerT8, MiniMaxH3SigmaShift, MiniMaxH3TurboLoRA, MiniMaxH3TurboSampler, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RH_DLSS5FrameInterpolation, RH_TopazlabsVideoFrameInterpolation, RIFE VFI, RTXVideoSuperResolution, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SeedVR2, SelfLiftAvatarH3Sampler, SelfLiftH3Sampler, SetLatentNoiseMask, SetNode, SolidMask, SoundFlow_GetLength, T8PerformanceDirectorConfig, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VOSR2Upscale, ZML_MergeText, ZML_TextInput, ki_MiniMaxH3ReferenceToVideo, ki_宫格拼图高阶版, llama_cpp_instruct_adv, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/H3 诞生2月可以技术汇总流_2098292736263811073.json, 视频生成/文生视频/H3 诞生2月可以技术汇总流_2098292736263811073.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_127

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3 诞生2月可以技术汇总流_2098292736263811073.json、视频生成/文生视频/H3 诞生2月可以技术汇总流_2098292736263811073.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Astra`
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `ExtendIntermediateSigmas`
- `FLAVR VFI`
- `FlashVSRNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GoohaiAnySwitch`
- `H3KitSemanticBridge`
- `H3SigmaRefiner`
- `Image Batch`
- `ImageAddNoise`
- `ImpactConditionalBranch`
- `InversionDemoLazySwitch`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3PromptEnhancerT8`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3TurboSampler`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_DLSS5FrameInterpolation`
- `RH_TopazlabsVideoFrameInterpolation`
- `RIFE VFI`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SeedVR2`
- `SelfLiftAvatarH3Sampler`
- `SelfLiftH3Sampler`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `SoundFlow_GetLength`
- `T8PerformanceDirectorConfig`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VOSR2Upscale`
- `ZML_MergeText`
- `ZML_TextInput`
- `ki_MiniMaxH3ReferenceToVideo`
- `ki_宫格拼图高阶版`
- `llama_cpp_instruct_adv`
- `忽略多组孤海`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
