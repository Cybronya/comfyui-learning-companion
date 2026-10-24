---
name: text_to_image_lora_sampler_clip_537
type: Text To Image
frequency: 3
level: strong
coverage: 0.894333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LoadAudio, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/minimax h3 selflift双采8流程，文生视频图生视频通吃_2110514641985171458.json, 视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json, 视频生成/文生视频/AI音乐MV数字人新二采｜Minimax H3 Selflift联动出片_2100782399897554945.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_537

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/minimax h3 selflift双采8流程，文生视频图生视频通吃_2110514641985171458.json、视频生成/文生视频/AI音乐MV数字人Singualarith与MiniMax H3视频生成工具_2101005333526302721.json、视频生成/文生视频/AI音乐MV数字人新二采｜Minimax H3 Selflift联动出片_2100782399897554945.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 2/3 个有
- `LTXVSeparateAVLatent` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `MiniMaxChunkFeedForward` —— 2/3 个有
- `MiniMaxLowVRAMAttention` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `SoundFlow_GetLength` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `TrimAudioDuration` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `1hew_AudioDuration` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `SaveVideo` —— 1/3 个有
- `TrimAudio` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
