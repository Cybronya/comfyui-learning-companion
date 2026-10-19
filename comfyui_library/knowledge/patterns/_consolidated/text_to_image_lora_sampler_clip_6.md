---
name: text_to_image_lora_sampler_clip_6
type: Text To Image
frequency: 31
level: strong
coverage: 0.891903
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text]
members: [视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json, 视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json, 视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json, 视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流_文生视频视频生视频图生视频_2106140143164936194.json, 视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json, 视频生成/图生视频/Dasiwa-MiniMax H3动态最强｜单采参考生视频_2095225077049683969.json, 视频生成/图生视频/Dasiwa参考图生视频｜MinimaxH3一键生成直出_2092358488738586626.json, 视频生成/图生视频/H3双时钟采样4步无损加速图生视频 极速高质量_2098839241043304449.json, 视频生成/图生视频/H3稳定加速版整合打斗和脸部修复Lora_2100265879845040129.json, 视频生成/图生视频/H3高动态双采放大，图生视频高清增强分辨率提升工作流_2103273133582147585.json, 视频生成/图生视频/MiniMAX-H3-T8双时钟采样｜4步无损加速图生视频出片飞快_2099154403528896514.json, 视频生成/图生视频/MiniMax H3 参考生视频多图参考｜最强战斗特效效果拉满_2096865093039513601.json, 视频生成/图生视频/MiniMax H3不油文剧工作流｜图生视频剧情质感生成_2097099800738095105.json, 视频生成/图生视频/MiniMax H3参考生视频｜10Eros turbo动态叙事_2095275498304790529.json, 视频生成/图生视频/MiniMax H3参考生视频｜Dasiwa v2叠加singularity双采_2099863444169248769.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥_文戏不油武戏动态强参考生视频_2105749839286984706.json, 视频生成/图生视频/MiniMax H3多参双采参考长视频Pov第一视角 沉浸式视频生成_2105369174095785985.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜POV第一视角沉浸感｜参考生视频出新招_2104794146677551106.json, 视频生成/图生视频/MiniMax H3多参双采长视频｜Pov第一视角沉浸体验_2105259470069784577.json, 视频生成/图生视频/MiniMax H3多图参考双采生视频｜HyperVae 2X高清图生视频_2111058302082830338.json, 视频生成/图生视频/MiniMax H3多图参考双采，HyperVae 2X高清图生视频_2111259409954459649.json, 视频生成/图生视频/MiniMax H3长视频POV第一视角｜多参考双采样图生视频｜人物特效角色设计_2104751091027103746.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参工作流，角色一致性图生视频方案_2107184502861819906.json, 视频生成/图生视频/MiniMax H3长视频直出双采多参｜角色一致性运镜图生视频_2106998238581714946.json, 视频生成/图生视频/MiniMax_H3长视频直出双采多参工作流，角色一致性图生视频方案_2109461992850419714.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105001173613899778.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105078692375519233.json, 视频生成/图生视频/长视频Pov第一视角 MiniMax H3多参双采参考生视频_2105444809631686658.json, 视频生成/文生视频/30秒长视频文武双修均衡版高清 视频生成方案_2105053597879848962.json, 视频生成/文生视频/H3长视频优化版｜文生视频视频生视频图生视频全支持_2106981562544902146.json, 视频生成/文生视频/长视频优化版H3工作流，文生视频视频生视频图生视频方案_2107243300871827458.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（视频生成/图生视频/8步增速最新版｜Minimax H3 图生视频_2089273029355466753.json、视频生成/图生视频/8步极速图生视频t8版｜Minimax海螺h3 高质量出片就是这么快_2105519643300548609.json、视频生成/图生视频/8步极速海螺h3图生视频｜Minimax高质量加速优化版 角色设计在线_2105518161696223233.json、视频生成/图生视频/8步高质量极速MiniMax H3开源版工作流_文生视频视频生视频图生视频_2106140143164936194.json、视频生成/图生视频/8步高质量极速Minimax H3开源版｜图生视频高效出片_2108379019711438850.json…）

- **类型**：Text To Image
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 31 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 30/31 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 30/31 个有
- `ResolutionSelector` —— 30/31 个有
- `孤海注释` —— 30/31 个有
- `MiniMaxH3AVDecodeT8` —— 29/31 个有
- `VHS_VideoCombine` —— 29/31 个有
- `CR Prompt Text` —— 27/31 个有
- `ModelAttentionBackend` —— 25/31 个有
- `SolAttnMiniMax` —— 22/31 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 21/31 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 21/31 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 21/31 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 21/31 个有
- `CreateVideo` —— 16/31 个有
- `Float` —— 16/31 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 16/31 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 16/31 个有
- `SaveImage` —— 16/31 个有
- `SaveVideo` —— 16/31 个有
- `easy anythingIndexSwitch` —— 16/31 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 15/31 个有
- `RunningHub Deepcleaner` —— 15/31 个有
- `easy cleanGpuUsed` —— 15/31 个有
- `Astra` —— 13/31 个有
- `GetNode` —— 4/31 个有
- `SetNode` —— 4/31 个有
- `LoadAudio` —— 3/31 个有
- `PrimitiveStringMultiline` —— 3/31 个有
- `easy int` —— 3/31 个有
- `CM_IntToFloat` —— 2/31 个有
- `ConcatTextOfUtils` —— 2/31 个有
- `GetImageSize` —— 2/31 个有
- `ImageScaleToTotalPixels` —— 2/31 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 2/31 个有
- `MiniMaxH3OutputTrimT8` —— 2/31 个有
- `VAEDecodeAudio` —— 2/31 个有
- `BasicScheduler` —— 1/31 个有
- `DuckHideNode` —— 1/31 个有
- `EmptyImage` —— 1/31 个有
- `Fast Groups Bypasser (rgthree)` —— 1/31 个有
- `KSamplerSelect` —— 1/31 个有
- `MiniMaxH3ImageToVideo` —— 1/31 个有
- `PreviewImage` —— 1/31 个有
- `TimbreAudioLoader` —— 1/31 个有
- `WujiAudioLoader` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 31 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 31 | 100% |
| 采样算法 | er_sde | - | 31 | 100% |
| 调度器 | beta | - | 31 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 31 | 100% |
| 宽度 | 80 | 80 - 80 | 31 | 100% |
| 高度 | 80 | 80 - 80 | 31 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/31 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，31 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，31 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，31 个样本，一致性 100%
- 调度器 最常用 beta，31 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，31 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，31 个样本，取值集中（一致性 100%）
- 高发问题（32/31 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
