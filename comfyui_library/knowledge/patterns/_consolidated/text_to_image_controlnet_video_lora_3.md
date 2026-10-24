---
name: text_to_image_controlnet_video_lora_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.914
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, ImageConcatMulti, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LayerUtility: ImageBlend V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadMoGeModel, LoraLoaderModelOnly, MiniMaxH3FunControlNetApply, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MoGeInference, MoGeRender, ModelAttentionBackend, ModelPatchLoader, ModelPreviewOverrideKJ, PrimitiveFloat, RMBG, ResolutionSelector, SaveImage, SelfLiftAvatarH3Sampler, SelfLiftAvatarH3TST, SetLatentNoiseMask, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAEEncodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy positive, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3动作迁移稳定版，文生视频视频生视频_2111245635704938498.json, 视频生成/图生视频/动作迁移升级版本法线参考固定提示词 动作复刻视频生成_2109693290554679297.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_video_lora_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3动作迁移稳定版，文生视频视频生视频_2111245635704938498.json、视频生成/图生视频/动作迁移升级版本法线参考固定提示词 动作复刻视频生成_2109693290554679297.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `ImageConcatMulti`
- `JjkText`
- `KSampler`
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
- `SaveImage`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MMH3LatentUpscaleWithModelParams` —— 1/2 个有
- `MMH3TemporalSplitParams` —— 1/2 个有
- `MMH3UltimateUpscale` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `VOSR2ModelLoader` —— 1/2 个有
- `VOSR2Upscale` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | - | 2 | 100% |
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

- ControlNet 权重 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
