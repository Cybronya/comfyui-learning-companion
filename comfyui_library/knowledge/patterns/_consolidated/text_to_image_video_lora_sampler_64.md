---
name: text_to_image_video_lora_sampler_64
type: Text To Image
frequency: 12
level: strong
coverage: 0.897667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3图生视频高清2K工作流，人像写真音频生成图生视频方案_2106616277656752130.json, 视频生成/图生视频/MiniMax H3锐化高清放大采样工作流，文生视频高清增强方案_2105784930222559233.json, 视频生成/图生视频/MiniMax H3锐化高清放大采样工作流，文生视频高清增强方案_2106131115126910978.json, 视频生成/图生视频/Minimax H3多参视频生成不油不偏色及一致性好工作流，图生视频处理方案_2107954357282099202.json, 视频生成/图生视频/Minimax h3多参视频生成不油不偏色及一致性好 多模态输入_2109712427955871745.json, 视频生成/图生视频/Minimax-H3开源加速双采工作流｜self-lift图生视频生成_2097766070177320962.json, 视频生成/图生视频/Minimax-H3开源黑科技加速双采｜self-lift图生视频战斗特效_2097917181681029122.json, 视频生成/图生视频/MinimaxH3图生视频高清2K版｜人像写真质感细腻出片_2106247039381233666.json, 视频生成/图生视频/SelfLift优化加速视频_2111462433582833666.json, 视频生成/图生视频/SelfLift优化速度流 视频生成加速方案_2108986698486079490.json, 视频生成/图生视频/Selflift加2xVAE锐化放大模型，图生视频画质增强_2111212774469758978.json, 视频生成/图生视频/selflift加2xVAE锐化放大｜图生视频画质增强方案_2105241932820738050.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频高清2K工作流，人像写真音频生成图生视频方案_2106616277656752130.json、视频生成/图生视频/MiniMax H3锐化高清放大采样工作流，文生视频高清增强方案_2105784930222559233.json、视频生成/图生视频/MiniMax H3锐化高清放大采样工作流，文生视频高清增强方案_2106131115126910978.json、视频生成/图生视频/Minimax H3多参视频生成不油不偏色及一致性好工作流，图生视频处理方案_2107954357282099202.json、视频生成/图生视频/Minimax h3多参视频生成不油不偏色及一致性好 多模态输入_2109712427955871745.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/12 个有
- `SelfLiftAvatarH3Sampler` —— 8/12 个有
- `PrimitiveStringMultiline` —— 7/12 个有
- `LTXVSeparateAVLatent` —— 6/12 个有
- `MiniMaxH3VAEDecodeFast` —— 6/12 个有
- `PreviewAny` —— 6/12 个有
- `QwenH3PromptLocal` —— 6/12 个有
- `RunningHub Deepcleaner` —— 6/12 个有
- `Fast Groups Muter (rgthree)` —— 5/12 个有
- `ImageFromBatch` —— 5/12 个有
- `SelfLiftH3Sampler` —— 4/12 个有
- `Image Comparer (rgthree)` —— 3/12 个有
- `CreateVideo` —— 2/12 个有
- `ImageScaleBy` —— 2/12 个有
- `LTXVConcatAVLatent` —— 2/12 个有
- `LoadAudio` —— 2/12 个有
- `SetLatentNoiseMask` —— 2/12 个有
- `SolidMask` —— 2/12 个有
- `Text` —— 2/12 个有
- `VAEEncodeAudio` —— 2/12 个有
- `VOSR2ModelLoader` —— 2/12 个有
- `VOSR2Upscale` —— 2/12 个有
- `VedaSparseAttention` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
