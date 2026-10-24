---
name: text_to_image_lora_sampler_clip_280
type: Text To Image
frequency: 7
level: strong
coverage: 0.829286
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, ColorTransfer, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, ExtendIntermediateSigmas, GetImageRangeFromBatch, GetVideoComponents, ImageAddNoise, ImageBatchMulti, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3AudioGuideFeather, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VideoFrameSample, VideoTemporalCrop, easy float, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3上下文无缝无色差长视频 SelfLift双采简易版_2110367360174608385.json, 视频生成/图生视频/MiniMax H3真上下文无缝无色差长视频SelfLift双采简易版工作流，图生视频_2107916415729758210.json, 视频生成/图生视频/MiniMax_H3真上下文无缝无色差长视频｜SelfLift双采简易版_2107273229961359361.json, 视频生成/图生视频/MiniMax_H3真上下文无缝无色差长视频｜SelfLift双采简易版_2109454531175206913.json, 视频生成/文生视频/MiniMax H3真上下文无缝无色差长视频SelfLift双采简易版，图生视频方案_2107162334690103298.json, 视频生成/文生视频/MiniMax H3真上下文无缝无色差长视频｜SelfLift双采简易版_2106944066033381378.json, 视频生成/视频生视频/MiniMax H3上下文无缝无色差长视频SelfLift双采简易版方案_2106119335801606145.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_280

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3上下文无缝无色差长视频 SelfLift双采简易版_2110367360174608385.json、视频生成/图生视频/MiniMax H3真上下文无缝无色差长视频SelfLift双采简易版工作流，图生视频_2107916415729758210.json、视频生成/图生视频/MiniMax_H3真上下文无缝无色差长视频｜SelfLift双采简易版_2107273229961359361.json、视频生成/图生视频/MiniMax_H3真上下文无缝无色差长视频｜SelfLift双采简易版_2109454531175206913.json、视频生成/文生视频/MiniMax H3真上下文无缝无色差长视频SelfLift双采简易版，图生视频方案_2107162334690103298.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorTransfer`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `GetImageRangeFromBatch`
- `GetVideoComponents`
- `ImageAddNoise`
- `ImageBatchMulti`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3AudioGuideFeather`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VideoFrameSample`
- `VideoTemporalCrop`
- `easy float`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `孤海注释` —— 5/7 个有
- `SaveImage` —— 4/7 个有
- `EmptyImage` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `GetNode` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
