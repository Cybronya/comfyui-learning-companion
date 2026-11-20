---
name: text_to_image_lora_sampler_clip_269
type: Text To Image
frequency: 8
level: strong
coverage: 0.831625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ChainAssemble, MiniMaxH3ChainContext, MiniMaxH3ChainCurrent, MiniMaxH3ChainLoopEnd, MiniMaxH3ChainLoopStart, MiniMaxH3ChainPlan, MiniMaxH3ChainSegmentSave, MiniMaxH3LoopTrim, MiniMaxH3SigmaShift, PixaromaSizes, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy mergeVideosFromPaths, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 多图参考无限长视频｜满血版+加速双管齐下_2096885543597596673.json, 视频生成/图生视频/MiniMax H3全能参考无限长视频｜满血加速版生成_2094931597387714562.json, 视频生成/图生视频/无限长视频满血+加速｜MiniMax H3全能参考生成_2095109673274929154.json, 视频生成/图生视频/满血加速二代｜MiniMax H3全能参考无限长视频_2096635244383395842.json, 视频生成/图生视频/首尾帧无限续接｜MiniMax H3满血加速长视频_2096582675971796994.json, 视频生成/图生视频/首尾帧无限长视频生成｜MiniMax H3满血加速版_2095933426183524354.json, 视频生成/图生视频/首尾帧无限长视频｜MiniMax H3 满血加速双模式_2096220120661188609.json, 视频生成/图生视频/首尾帧无限长视频｜MiniMax H3满血版加速生成_2096303474995716097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_269

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 多图参考无限长视频｜满血版+加速双管齐下_2096885543597596673.json、视频生成/图生视频/MiniMax H3全能参考无限长视频｜满血加速版生成_2094931597387714562.json、视频生成/图生视频/无限长视频满血+加速｜MiniMax H3全能参考生成_2095109673274929154.json、视频生成/图生视频/满血加速二代｜MiniMax H3全能参考无限长视频_2096635244383395842.json、视频生成/图生视频/首尾帧无限续接｜MiniMax H3满血加速长视频_2096582675971796994.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ChainAssemble`
- `MiniMaxH3ChainContext`
- `MiniMaxH3ChainCurrent`
- `MiniMaxH3ChainLoopEnd`
- `MiniMaxH3ChainLoopStart`
- `MiniMaxH3ChainPlan`
- `MiniMaxH3ChainSegmentSave`
- `MiniMaxH3LoopTrim`
- `MiniMaxH3SigmaShift`
- `PixaromaSizes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy mergeVideosFromPaths`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `MiniMaxH3ChainReview` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `SolAttnPatch` —— 6/8 个有
- `MiniMaxH3ChainScenePromptEditor` —— 5/8 个有
- `MiniMaxH3ImageToVideo` —— 4/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `Int` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `MiniMaxH3ChainManifestLoad` —— 3/8 个有
- `PrimitiveBoolean` —— 3/8 个有
- `MiniMaxH3ReferenceToVideo` —— 2/8 个有
- `MiniMaxH3ScheduledPictureReference` —— 2/8 个有
- `MiniMaxH3ScheduledReferenceToVideo` —— 2/8 个有
- `LoadVideo` —— 1/8 个有
- `MiniMaxH3ChainPlanStudio` —— 1/8 个有
- `MiniMaxH3ChainRichScenePromptEditor` —— 1/8 个有
- `MiniMaxH3ChainRunManager` —— 1/8 个有
- `MiniMaxH3ReferenceVideoPrepare` —— 1/8 个有
- `MiniMaxH3ScheduledAudioReference` —— 1/8 个有
- `MiniMaxH3ScheduledVideoReference` —— 1/8 个有
- `ModelAttentionBackend` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
