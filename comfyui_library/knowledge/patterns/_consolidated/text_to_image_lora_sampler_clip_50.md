---
name: text_to_image_lora_sampler_clip_50
type: Text To Image
frequency: 15
level: strong
coverage: 0.716667
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
members: [视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json, 视频生成/图生视频/MiniMax H3不油短剧流｜图生视频质感不塑料_2097161583708434434.json, 视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json, 视频生成/图生视频/MiniMax H3全能参考高配文戏版_文生视频视频生视频图生视频方案_2105748117059620866.json, 视频生成/图生视频/MiniMax H3八月最强文戏修改版 图生视频自然动态_2110358274074832898.json, 视频生成/图生视频/MiniMax H3双采V2二采版｜音频驱动数字人电商带货直出_2103050202750996481.json, 视频生成/图生视频/MiniMax H3双采全能V2文戏不油武戏动态强，电商带货参考生视频方案_2103180413962383361.json, 视频生成/图生视频/MiniMax H3双采全能V2音频驱动数字人，电商带货二采图生视频工作流_2103182055260647425.json, 视频生成/图生视频/MiniMax H3双采全能V2｜文戏细腻武戏动态强电商带货参考生视频_2103048629668892674.json, 视频生成/图生视频/MiniMax H3双采参考生视频低显存版｜图生视频小显卡也能跑_2104566495551516674.json, 视频生成/图生视频/MiniMax H3文戏工作流_图生视频高质量文戏创作方案_2105710744003239938.json, 视频生成/图生视频/MiniMax H3静态动画图直转视频，潜空间放大一采预览锁种版图生视频_2103177184528658433.json, 视频生成/图生视频/Minimax H3潜空间放大预览 一采锁种版动漫角色图生视频_2098639488330330114.json, 视频生成/图生视频/Minimax H3静态图转动画视频｜一张动图直接活起来_2103042623161331714.json, 视频生成/图生视频/低显存也能跑 MiniMax H3双采参考生视频方案_2104650144351346689.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json、视频生成/图生视频/MiniMax H3不油短剧流｜图生视频质感不塑料_2097161583708434434.json、视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json、视频生成/图生视频/MiniMax H3全能参考高配文戏版_文生视频视频生视频图生视频方案_2105748117059620866.json、视频生成/图生视频/MiniMax H3八月最强文戏修改版 图生视频自然动态_2110358274074832898.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 14/15 个有
- `MiniMaxH3DualClockSamplerT8` —— 14/15 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 14/15 个有
- `ModelAttentionBackend` —— 14/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 13/15 个有
- `PrimitiveFloat` —— 12/15 个有
- `SolAttnMiniMax` —— 12/15 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 11/15 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 11/15 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 11/15 个有
- `VHS_VideoCombine` —— 11/15 个有
- `GetNode` —— 10/15 个有
- `SetNode` —— 10/15 个有
- `SaveImage` —— 9/15 个有
- `Fast Groups Bypasser (rgthree)` —— 8/15 个有
- `LoadAudio` —— 8/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/15 个有
- `PreviewImage` —— 6/15 个有
- `CreateVideo` —— 4/15 个有
- `Float` —— 4/15 个有
- `SaveVideo` —— 4/15 个有
- `easy cleanGpuUsed` —— 4/15 个有
- `Fast Groups Muter (rgthree)` —— 3/15 个有
- `JWFloat` —— 3/15 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 3/15 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 3/15 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 3/15 个有
- `PreviewAny` —— 3/15 个有
- `Seed (rgthree)` —— 3/15 个有
- `BasicScheduler` —— 1/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `KSamplerSelect` —— 1/15 个有
- `LTXVConcatAVLatent` —— 1/15 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/15 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/15 个有
- `VAEDecodeAudio` —— 1/15 个有
- `VAEEncode` —— 1/15 个有
- `VAEEncodeAudio` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、CR Prompt Text
