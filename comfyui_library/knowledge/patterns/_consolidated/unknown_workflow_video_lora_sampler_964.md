---
name: unknown_workflow_video_lora_sampler_964
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8065
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LayerUtility: ImageBlend V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadMoGeModel, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MoGeInference, MoGeRender, ModelAttentionBackend, ModelPreviewOverrideKJ, RHLLMChatNode, RMBG, RTXTrueHDR, RTXVideoFrameGeneration, RTXVideoSuperResolution, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, SelfLiftH3TST, SetLatentNoiseMask, ShowText|pysssss, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy int, easy positive, easy promptReplace, easy showAnything, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [平台全量/1-Aiden-动作迁移！提示词尽量用Agent！_2110841349133135874.json, 视频生成/图生视频/1-Aiden-动作迁移！提示词尽量用Agent！_2115236829317386242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_964

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/1-Aiden-动作迁移！提示词尽量用Agent！_2110841349133135874.json、视频生成/图生视频/1-Aiden-动作迁移！提示词尽量用Agent！_2115236829317386242.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LayerUtility: ImageBlend V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadMoGeModel`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MoGeInference`
- `MoGeRender`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RHLLMChatNode`
- `RMBG`
- `RTXTrueHDR`
- `RTXVideoFrameGeneration`
- `RTXVideoSuperResolution`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `SelfLiftH3TST`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy int`
- `easy positive`
- `easy promptReplace`
- `easy showAnything`
- `孤海注释`
- `忽略多组孤海`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
