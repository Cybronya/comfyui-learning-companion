---
name: text_to_image_lora_sampler_clip_142
type: Text To Image
frequency: 12
level: strong
coverage: 0.708167
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json, 视频生成/图生视频/MiniMax H3不油短剧流｜图生视频质感不塑料_2097161583708434434.json, 视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json, 视频生成/图生视频/MiniMax H3全能参考高配文戏版，文生视频视频生视频图生视频方案_2105748117059620866.json, 视频生成/图生视频/MiniMax H3八月最强文戏修改版 图生视频自然动态_2110358274074832898.json, 视频生成/图生视频/MiniMax H3双采V2二采版｜音频驱动数字人电商带货直出_2103050202750996481.json, 视频生成/图生视频/MiniMax H3双采参考生视频低显存版｜图生视频小显卡也能跑_2104566495551516674.json, 视频生成/图生视频/MiniMax H3文戏工作流，图生视频高质量文戏创作方案_2105710744003239938.json, 视频生成/图生视频/MiniMax H3静态动画图直转视频，潜空间放大一采预览锁种版图生视频_2103177184528658433.json, 视频生成/图生视频/Minimax H3潜空间放大预览 一采锁种版动漫角色图生视频_2098639488330330114.json, 视频生成/图生视频/Minimax H3静态图转动画视频｜一张动图直接活起来_2103042623161331714.json, 视频生成/图生视频/Minimax-H3潜空间放大一采版｜预览锁种稳定出片_2098748687479562242.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 图生视频｜简洁直出好上手_2096906797306171394.json、视频生成/图生视频/MiniMax H3不油短剧流｜图生视频质感不塑料_2097161583708434434.json、视频生成/图生视频/MiniMax H3低显存时间分块前馈分块双采参考生视频工具_2101417333859381250.json、视频生成/图生视频/MiniMax H3全能参考高配文戏版，文生视频视频生视频图生视频方案_2105748117059620866.json、视频生成/图生视频/MiniMax H3八月最强文戏修改版 图生视频自然动态_2110358274074832898.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoraLoaderBypassModelOnly` —— 11/12 个有
- `MiniMaxH3DualClockSamplerT8` —— 11/12 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 11/12 个有
- `ModelAttentionBackend` —— 11/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/12 个有
- `PrimitiveFloat` —— 10/12 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 9/12 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 9/12 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 9/12 个有
- `VHS_VideoCombine` —— 9/12 个有
- `GetNode` —— 8/12 个有
- `LoadAudio` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `SolAttnMiniMax` —— 8/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/12 个有
- `PreviewImage` —— 7/12 个有
- `Fast Groups Bypasser (rgthree)` —— 6/12 个有
- `SaveImage` —— 6/12 个有
- `Fast Groups Muter (rgthree)` —— 4/12 个有
- `Seed (rgthree)` —— 4/12 个有
- `CreateVideo` —— 3/12 个有
- `SaveVideo` —— 3/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `JWFloat` —— 2/12 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 2/12 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 2/12 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 2/12 个有
- `PreviewAny` —— 2/12 个有
- `BasicScheduler` —— 1/12 个有
- `Float` —— 1/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `KSamplerSelect` —— 1/12 个有
- `LTXVConcatAVLatent` —— 1/12 个有
- `MiniMaxH3VDNExecutionPlanT8Advanced` —— 1/12 个有
- `MiniMaxH3VDNModelComposerT8Advanced` —— 1/12 个有
- `VAEDecodeAudio` —— 1/12 个有
- `VAEEncode` —— 1/12 个有
- `VAEEncodeAudio` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
