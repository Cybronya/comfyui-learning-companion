---
name: text_to_image_video_lora_sampler_91
type: Text To Image
frequency: 8
level: strong
coverage: 0.890625
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, SelfLiftAvatarH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [RunningHub Deepcleaner]
members: [视频生成/图生视频/MiniMax H3 360度环绕视频加Selflift专用高分辨率生成工作流，图生视频_2106477153318686722.json, 视频生成/图生视频/MiniMax H3 360度环绕视频_Selflift专用高分辨率转场运镜出片_2106207397177024513.json, 视频生成/图生视频/MiniMax H3图生视频高清2K工作流_人像写真音频生成图生视频方案_2106616277656752130.json, 视频生成/图生视频/MiniMax H3锐化高清放大采样工作流_文生视频高清增强方案_2105784930222559233.json, 视频生成/图生视频/MiniMax H3锐化高清放大采样工作流_文生视频高清增强方案_2106131115126910978.json, 视频生成/图生视频/MinimaxH3图生视频高清2K版_人像写真质感细腻出片_2106247039381233666.json, 视频生成/图生视频/Selflift加2xVAE锐化放大模型，图生视频画质增强_2111212774469758978.json, 视频生成/图生视频/selflift加2xVAE锐化放大｜图生视频画质增强方案_2105241932820738050.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 360度环绕视频加Selflift专用高分辨率生成工作流，图生视频_2106477153318686722.json、视频生成/图生视频/MiniMax H3 360度环绕视频_Selflift专用高分辨率转场运镜出片_2106207397177024513.json、视频生成/图生视频/MiniMax H3图生视频高清2K工作流_人像写真音频生成图生视频方案_2106616277656752130.json、视频生成/图生视频/MiniMax H3锐化高清放大采样工作流_文生视频高清增强方案_2105784930222559233.json、视频生成/图生视频/MiniMax H3锐化高清放大采样工作流_文生视频高清增强方案_2106131115126910978.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 6/8 个有
- `LTXVSeparateAVLatent` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `MiniMaxH3VAEDecodeFast` —— 6/8 个有
- `PreviewAny` —— 6/8 个有
- `QwenH3PromptLocal` —— 6/8 个有
- `RunningHub Deepcleaner` —— 6/8 个有
- `Fast Groups Muter (rgthree)` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ImageFromBatch` —— 3/8 个有
- `CR Prompt Text` —— 2/8 个有
- `ExtendIntermediateSigmas` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `MiniMaxH3ImageToVideo` —— 2/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `Text` —— 2/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：RunningHub Deepcleaner
