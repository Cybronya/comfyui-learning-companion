---
name: text_to_image_lora_sampler_clip_32
type: Text To Image
frequency: 19
level: strong
coverage: 0.788684
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2]
members: [视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json, 视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json, 视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json, 视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流_文生视频视频生视频图生视频_2106140143164936194.json, 视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json, 视频生成/图生视频/Dasiwa-MiniMax H3动态最强｜单采参考生视频_2095225077049683969.json, 视频生成/图生视频/Dasiwa参考图生视频｜MinimaxH3一键生成直出_2092358488738586626.json, 视频生成/图生视频/H3双时钟采样4步无损加速图生视频 极速高质量_2098839241043304449.json, 视频生成/图生视频/H3高动态双采放大，图生视频高清增强分辨率提升工作流_2103273133582147585.json, 视频生成/图生视频/MiniMax H3 参考生视频多图参考｜最强战斗特效效果拉满_2096865093039513601.json, 视频生成/图生视频/MiniMax H3不油文剧工作流｜图生视频剧情质感生成_2097099800738095105.json, 视频生成/图生视频/MiniMax H3不油短剧流｜图生视频质感不塑料_2097161583708434434.json, 视频生成/图生视频/MiniMax H3全能参考高配文戏版_文生视频视频生视频图生视频方案_2105748117059620866.json, 视频生成/图生视频/MiniMax H3八月最强文戏修改版 图生视频自然动态_2110358274074832898.json, 视频生成/图生视频/MiniMax H3文戏工作流_图生视频高质量文戏创作方案_2105710744003239938.json, 视频生成/图生视频/MiniMax H3静态动画图直转视频，潜空间放大一采预览锁种版图生视频_2103177184528658433.json, 视频生成/图生视频/Minimax H3潜空间放大预览 一采锁种版动漫角色图生视频_2098639488330330114.json, 视频生成/图生视频/Minimax H3静态图转动画视频｜一张动图直接活起来_2103042623161331714.json, 视频生成/图生视频/Minimax-H3潜空间放大一采版｜预览锁种稳定出片_2098748687479562242.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json、视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json、视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json、视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流_文生视频视频生视频图生视频_2106140143164936194.json、视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3DualClockSamplerT8`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AVDecodeT8` —— 18/19 个有
- `MiniMaxH3AudioConditioningT8` —— 18/19 个有
- `ResolutionSelector` —— 18/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/19 个有
- `VHS_VideoCombine` —— 17/19 个有
- `CR Prompt Text` —— 16/19 个有
- `ModelAttentionBackend` —— 15/19 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 11/19 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 11/19 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 11/19 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 11/19 个有
- `SaveImage` —— 10/19 个有
- `LoadAudio` —— 9/19 个有
- `SolAttnMiniMax` —— 8/19 个有
- `GetNode` —— 7/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/19 个有
- `PreviewImage` —— 7/19 个有
- `SetNode` —— 7/19 个有
- `Fast Groups Bypasser (rgthree)` —— 5/19 个有
- `Fast Groups Muter (rgthree)` —— 4/19 个有
- `Seed (rgthree)` —— 4/19 个有
- `CreateVideo` —— 2/19 个有
- `PrimitiveStringMultiline` —— 2/19 个有
- `SaveVideo` —— 2/19 个有
- `VAEDecodeAudio` —— 2/19 个有
- `easy int` —— 2/19 个有
- `BasicScheduler` —— 1/19 个有
- `CM_IntToFloat` —— 1/19 个有
- `DuckHideNode` —— 1/19 个有
- `GetImageSize` —— 1/19 个有
- `ImageResizeKJv2` —— 1/19 个有
- `ImageScaleToTotalPixels` —— 1/19 个有
- `KSamplerSelect` —— 1/19 个有
- `LTXVConcatAVLatent` —— 1/19 个有
- `MiniMaxH3ImageToVideo` —— 1/19 个有
- `TimbreAudioLoader` —— 1/19 个有
- `VAEEncode` —— 1/19 个有
- `VAEEncodeAudio` —— 1/19 个有
- `WujiAudioLoader` —— 1/19 个有
- `easy cleanGpuUsed` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、LayerUtility: ImageScaleByAspectRatio V2
