---
name: unknown_workflow_controlnet_video_lora_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8905
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, H3SigmaRefiner, ImageConcatMulti, KSamplerSelect, LTXVConcatAVLatent, LayerUtility: ImageBlend V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadMoGeModel, LoraLoaderModelOnly, MiniMaxH3FunControlNetApply, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MoGeInference, MoGeRender, ModelAttentionBackend, ModelPatchLoader, ModelPreviewOverrideKJ, PrimitiveFloat, RMBG, ResolutionSelector, SelfLiftAvatarH3Sampler, SelfLiftAvatarH3TST, SetLatentNoiseMask, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy positive, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1-Aiden-动作迁移升级版本！法线参考！固定提示词！_2109297773538537473.json, 视频生成/图生视频/MiniMax H3 动作迁移（稳定版）_2110563071742799873.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1-Aiden-动作迁移升级版本！法线参考！固定提示词！_2109297773538537473.json、视频生成/图生视频/MiniMax H3 动作迁移（稳定版）_2110563071742799873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `H3SigmaRefiner`
- `ImageConcatMulti`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LayerUtility: ImageBlend V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadMoGeModel`
- `LoraLoaderModelOnly`
- `MiniMaxH3FunControlNetApply`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MoGeInference`
- `MoGeRender`
- `ModelAttentionBackend`
- `ModelPatchLoader`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RMBG`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SelfLiftAvatarH3TST`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEEncodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `MMH3LatentUpscaleWithModelParams` —— 1/2 个有
- `MMH3TemporalSplitParams` —— 1/2 个有
- `MMH3UltimateUpscale` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `VOSR2ModelLoader` —— 1/2 个有
- `VOSR2Upscale` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
