---
name: text_to_image_video_lora_sampler_206
type: Text To Image
frequency: 2
level: weak
coverage: 0.636
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ResolutionSelector, SaveImage, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SetNode, SolidMask, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax-H3二采MV长视频生成，数字人图生视频一站式_2110491230802108418.json, 视频生成/图生视频/短视频复刻v3，视频生视频图生视频快速仿拍出片_2110520972825681922.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_206

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax-H3二采MV长视频生成，数字人图生视频一站式_2110491230802108418.json、视频生成/图生视频/短视频复刻v3，视频生视频图生视频快速仿拍出片_2110520972825681922.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
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
- `SaveImage`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

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
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
