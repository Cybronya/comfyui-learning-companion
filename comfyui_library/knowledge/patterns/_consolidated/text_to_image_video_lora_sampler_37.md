---
name: text_to_image_video_lora_sampler_37
type: Text To Image
frequency: 15
level: strong
coverage: 0.8118
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3打戏T8流大改自用版｜战斗特效拳拳到肉｜图生视频武打场面拉满_2102254012815990786.json, 视频生成/图生视频/H3极速导演台8步双时钟-图生首尾帧多参一体化_2087375481896259586.json, 视频生成/图生视频/Lightx2v正式版8步去油双时钟参考生视频V2｜Minimax图生视频工作流_2088144409752850433.json, 视频生成/图生视频/Lightx2v正式版8步去油双时钟图生视频V1｜Minimax图生视频工作流_2088140753397702657.json, 视频生成/图生视频/MiniMAX-H3-T8双时钟采样｜4步无损加速图生视频出片飞快_2099154403528896514.json, 视频生成/图生视频/MiniMax H3参考生视频电商带货｜创意产品展示新玩法_2108086527170531330.json, 视频生成/图生视频/MiniMax H3参考生视频｜10Eros turbo动态叙事_2095275498304790529.json, 视频生成/图生视频/MiniMax H3参考生视频｜Dasiwa v2叠加singularity双采_2099863444169248769.json, 视频生成/图生视频/MiniMax H3双采V2二采版｜音频驱动数字人电商带货直出_2103050202750996481.json, 视频生成/图生视频/MiniMax H3双采V3语义桥_文戏不油武戏动态强_2106606073850454017.json, 视频生成/图生视频/MiniMax H3双采V3语义桥｜文戏不油武戏动态强_2106606073850454017.json, 视频生成/图生视频/MiniMax H3双采全能V3语义桥 文戏自然武戏动态强长视频_2110355426595401730.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥_文戏不油武戏动态强参考生视频_2105749839286984706.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥，文戏不油武戏动态强参考生视频_2106823219750727681.json, 视频生成/文生视频/MiniMax H3双采全能工作流V3语义桥文生视频版，长视频高清直出方案_2106998489740828674.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_37

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/H3打戏T8流大改自用版｜战斗特效拳拳到肉｜图生视频武打场面拉满_2102254012815990786.json、视频生成/图生视频/H3极速导演台8步双时钟-图生首尾帧多参一体化_2087375481896259586.json、视频生成/图生视频/Lightx2v正式版8步去油双时钟参考生视频V2｜Minimax图生视频工作流_2088144409752850433.json、视频生成/图生视频/Lightx2v正式版8步去油双时钟图生视频V1｜Minimax图生视频工作流_2088140753397702657.json、视频生成/图生视频/MiniMAX-H3-T8双时钟采样｜4步无损加速图生视频出片飞快_2099154403528896514.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：81%

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
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 12/15 个有
- `SolAttnMiniMax` —— 11/15 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 9/15 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 9/15 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 9/15 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 9/15 个有
- `Fast Groups Bypasser (rgthree)` —— 7/15 个有
- `Float` —— 7/15 个有
- `GetNode` —— 7/15 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 7/15 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 7/15 个有
- `SetNode` —— 7/15 个有
- `easy anythingIndexSwitch` —— 6/15 个有
- `Astra` —— 5/15 个有
- `CreateVideo` —— 5/15 个有
- `ImpactFloat` —— 5/15 个有
- `Int` —— 5/15 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 5/15 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 5/15 个有
- `RunningHub Deepcleaner` —— 5/15 个有
- `SaveVideo` —— 5/15 个有
- `SimpleMath+` —— 5/15 个有
- `easy cleanGpuUsed` —— 5/15 个有
- `MiniMaxH3ActivationChunkT8Advanced` —— 4/15 个有
- `SaveImage` —— 4/15 个有
- `ConcatTextOfUtils` —— 2/15 个有
- `CM_IntToFloat` —— 1/15 个有
- `ExtendIntermediateSigmas` —— 1/15 个有
- `GetImageSize` —— 1/15 个有
- `H3SigmaRefiner` —— 1/15 个有
- `ImageScaleToTotalPixels` —— 1/15 个有
- `LoadAudio` —— 1/15 个有
- `LoadVideo` —— 1/15 个有
- `MiniMaxChunkFeedForward` —— 1/15 个有
- `MiniMaxLowVRAMAttention` —— 1/15 个有
- `easy int` —— 1/15 个有

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
