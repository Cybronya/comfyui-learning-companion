---
name: text_to_image_video_lora_sampler_168
type: Text To Image
frequency: 3
level: strong
coverage: 0.554333
common_nodes: [AudioConcatenate, BasicScheduler, CLIPLoader, CLIPTextEncode, CM_FloatBinaryOperation, CM_IntBinaryOperation, CM_IntToFloat, ConditioningZeroOut, CreateVideo, EmptyLatentImage, FloatConstant, GetImageSize, H3SigmaRefiner, INTConstant, ImageBatch, ImageExpandBatch+, ImageFromBatch+, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy compare, easy forLoopEnd, easy forLoopStart, easy ifElse, easy mathInt, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax动作迁移官方接续版，人物参考图主场景参考关键帧视频生视频方案_2106437908533170178.json, 视频生成/图生视频/Minimax动作迁移 动作复刻视频生成方案_2105384636460388353.json, 视频生成/图生视频/Minimax动作迁移官方接续版｜视频生视频流畅复刻人物动作_2106198656264265729.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_168

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax动作迁移官方接续版，人物参考图主场景参考关键帧视频生视频方案_2106437908533170178.json、视频生成/图生视频/Minimax动作迁移 动作复刻视频生成方案_2105384636460388353.json、视频生成/图生视频/Minimax动作迁移官方接续版｜视频生视频流畅复刻人物动作_2106198656264265729.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioConcatenate`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_FloatBinaryOperation`
- `CM_IntBinaryOperation`
- `CM_IntToFloat`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `FloatConstant`
- `GetImageSize`
- `H3SigmaRefiner`
- `INTConstant`
- `ImageBatch`
- `ImageExpandBatch+`
- `ImageFromBatch+`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy ifElse`
- `easy mathInt`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 2/3 个有
- `MiniMaxH3AddGuide` —— 2/3 个有
- `ModelPreviewOverrideKJ` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `MiniMaxH3MotionContext` —— 1/3 个有
- `MiniMaxH3MotionContextTrim` —— 1/3 个有

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
