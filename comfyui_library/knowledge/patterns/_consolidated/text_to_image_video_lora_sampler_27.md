---
name: text_to_image_video_lora_sampler_27
type: Text To Image
frequency: 22
level: strong
coverage: 0.719091
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3打戏T8流大改自用版｜战斗特效拳拳到肉｜图生视频武打场面拉满_2102254012815990786.json, 视频生成/图生视频/H3极速导演台8步双时钟-图生首尾帧多参一体化_2087375481896259586.json, 视频生成/图生视频/Lightx2v正式版8步去油双时钟参考生视频V2｜Minimax图生视频工作流_2088144409752850433.json, 视频生成/图生视频/Lightx2v正式版8步去油双时钟图生视频V1｜Minimax图生视频工作流_2088140753397702657.json, 视频生成/图生视频/MiniMax H3 参考生视频多图参考｜最强战斗特效效果拉满_2096865093039513601.json, 视频生成/图生视频/MiniMax H3不油文剧工作流｜图生视频剧情质感生成_2097099800738095105.json, 视频生成/图生视频/MiniMax H3不油短剧流｜图生视频质感不塑料_2097161583708434434.json, 视频生成/图生视频/MiniMax H3全能参考高配文戏版，文生视频视频生视频图生视频方案_2105748117059620866.json, 视频生成/图生视频/MiniMax H3八月最强文戏修改版 图生视频自然动态_2110358274074832898.json, 视频生成/图生视频/MiniMax H3双采V2二采版｜音频驱动数字人电商带货直出_2103050202750996481.json, 视频生成/图生视频/MiniMax H3双采全能V2文戏不油武戏动态强，电商带货参考生视频方案_2103180413962383361.json, 视频生成/图生视频/MiniMax H3双采全能V2音频驱动数字人，电商带货二采图生视频工作流_2103182055260647425.json, 视频生成/图生视频/MiniMax H3双采全能V2｜文戏细腻武戏动态强电商带货参考生视频_2103048629668892674.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥，文戏不油武戏动态强参考生视频_2105749839286984706.json, 视频生成/图生视频/MiniMax H3文戏工作流，图生视频高质量文戏创作方案_2105710744003239938.json, 视频生成/图生视频/MiniMax H3静态动画图直转视频，潜空间放大一采预览锁种版图生视频_2103177184528658433.json, 视频生成/图生视频/MiniMax_H3九图三音多参二采工作流，文生视频图生视频多参考方案_2109441522717515777.json, 视频生成/图生视频/Minima H3武戏工作流 动作场景视频生成_2109003959313719297.json, 视频生成/图生视频/Minimax H3潜空间放大预览 一采锁种版动漫角色图生视频_2098639488330330114.json, 视频生成/图生视频/Minimax H3静态图转动画视频｜一张动图直接活起来_2103042623161331714.json, 视频生成/图生视频/Minimax-H3潜空间放大一采版｜预览锁种稳定出片_2098748687479562242.json, 视频生成/图生视频/Minimax-H3电商宣传广告｜产品视频高质量生成_2095594718758531074.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/H3打戏T8流大改自用版｜战斗特效拳拳到肉｜图生视频武打场面拉满_2102254012815990786.json、视频生成/图生视频/H3极速导演台8步双时钟-图生首尾帧多参一体化_2087375481896259586.json、视频生成/图生视频/Lightx2v正式版8步去油双时钟参考生视频V2｜Minimax图生视频工作流_2088144409752850433.json、视频生成/图生视频/Lightx2v正式版8步去油双时钟图生视频V1｜Minimax图生视频工作流_2088140753397702657.json、视频生成/图生视频/MiniMax H3 参考生视频多图参考｜最强战斗特效效果拉满_2096865093039513601.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 21/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 20/22 个有
- `ModelAttentionBackend` —— 20/22 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 18/22 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 18/22 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 18/22 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 18/22 个有
- `GetNode` —— 15/22 个有
- `SetNode` —— 15/22 个有
- `SolAttnMiniMax` —— 15/22 个有
- `Fast Groups Bypasser (rgthree)` —— 12/22 个有
- `LoadAudio` —— 11/22 个有
- `SaveImage` —— 11/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/22 个有
- `PreviewImage` —— 10/22 个有
- `Float` —— 5/22 个有
- `Fast Groups Muter (rgthree)` —— 4/22 个有
- `Seed (rgthree)` —— 4/22 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/22 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/22 个有
- `ConcatTextOfUtils` —— 2/22 个有
- `MiniMaxChunkFeedForward` —— 2/22 个有
- `MiniMaxLowVRAMAttention` —— 2/22 个有
- `BasicScheduler` —— 1/22 个有
- `EmptyImage` —— 1/22 个有
- `ExtendIntermediateSigmas` —— 1/22 个有
- `H3SigmaRefiner` —— 1/22 个有
- `ImageResizeKJv2` —— 1/22 个有
- `KSamplerSelect` —— 1/22 个有
- `LTXVConcatAVLatent` —— 1/22 个有
- `VAEDecodeAudio` —— 1/22 个有
- `VAEEncode` —— 1/22 个有
- `VAEEncodeAudio` —— 1/22 个有
- `easy anythingIndexSwitch` —— 1/22 个有
- `easy cleanGpuUsed` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 高发问题（22/22 个样本）：Steps较低可能导致细节不足
