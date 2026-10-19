---
name: text_to_image_video_upscale_latent_upscale_32
type: Text To Image
frequency: 2
level: weak
coverage: 0.7135
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, ConditioningZeroOut, EmptyLatentImage, ExtendIntermediateSigmas, GetNode, H3KitSemanticBridge, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SetNode, SolidMask, SoundFlow_GetLength, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, ZML_MergeText, ZML_TextInput, ki_MiniMaxH3ReferenceToVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [FLAVR VFI, Image Batch, RIFE VFI, Seed (rgthree), ki_宫格拼图高阶版]
members: [视频生成/图生视频/h3最优基础工作流汇总，文生视频图生视频全能_2111282762715062273.json, 视频生成/文生视频/2108068333663903746.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_32

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/h3最优基础工作流汇总，文生视频图生视频全能_2111282762715062273.json、视频生成/文生视频/2108068333663903746.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `GetNode`
- `H3KitSemanticBridge`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ZML_MergeText`
- `ZML_TextInput`
- `ki_MiniMaxH3ReferenceToVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `Astra` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `CustomSigmas` —— 1/2 个有
- `FLAVR VFI` —— 1/2 个有
- `FlashVSRNode` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `GoohaiAnySwitch` —— 1/2 个有
- `H3SigmaRefiner` —— 1/2 个有
- `Image Batch` —— 1/2 个有
- `ImageAddNoise` —— 1/2 个有
- `ImpactConditionalBranch` —— 1/2 个有
- `InversionDemoLazySwitch` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `MiniMaxH3AddGuide` —— 1/2 个有
- `MiniMaxH3PromptEnhancerT8` —— 1/2 个有
- `MiniMaxH3TurboLoRA` —— 1/2 个有
- `MiniMaxH3TurboSampler` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_DLSS5FrameInterpolation` —— 1/2 个有
- `RH_TopazlabsVideoFrameInterpolation` —— 1/2 个有
- `RIFE VFI` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SelfLiftAvatarH3TST` —— 1/2 个有
- `SelfLiftH3Sampler` —— 1/2 个有
- `SplitSigmas` —— 1/2 个有
- `T8PerformanceDirectorConfig` —— 1/2 个有
- `VOSR2Upscale` —— 1/2 个有
- `ki_宫格拼图高阶版` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：FLAVR VFI、Image Batch、RIFE VFI、Seed (rgthree)、ki_宫格拼图高阶版
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
