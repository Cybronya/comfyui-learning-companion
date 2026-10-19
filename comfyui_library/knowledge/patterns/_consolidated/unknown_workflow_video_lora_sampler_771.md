---
name: unknown_workflow_video_lora_sampler_771
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5565
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, GetNode, JjkText, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SetNode, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MV_长视频生成_Minimax-H3（二采）_2101970637429493762.json, 视频生成/图生视频/短视频复刻-v3_2109928843170631681.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_771

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MV_长视频生成_Minimax-H3（二采）_2101970637429493762.json、视频生成/图生视频/短视频复刻-v3_2109928843170631681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `JjkText`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `ImageBatchExtendWithOverlap` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MiniMaxH3MotionContext` —— 1/2 个有
- `MiniMaxH3MotionContextLoadLatent` —— 1/2 个有
- `MiniMaxH3MotionContextSaveLatent` —— 1/2 个有
- `MiniMaxH3MotionContextTrim` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
