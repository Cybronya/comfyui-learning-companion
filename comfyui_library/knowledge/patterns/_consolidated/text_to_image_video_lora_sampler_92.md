---
name: text_to_image_video_lora_sampler_92
type: Text To Image
frequency: 8
level: strong
coverage: 0.894
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3打戏T8流大改自用版｜战斗特效拳拳到肉｜图生视频武打场面拉满_2102254012815990786.json, 视频生成/图生视频/H3极速导演台8步双时钟-图生首尾帧多参一体化_2087375481896259586.json, 视频生成/图生视频/H3高保真图生视频 静止图像动态化运镜重构_2099924808850042881.json, 视频生成/图生视频/Lightx2v正式版8步去油双时钟参考生视频V2｜Minimax图生视频工作流_2088144409752850433.json, 视频生成/图生视频/Lightx2v正式版8步去油双时钟图生视频V1｜Minimax图生视频工作流_2088140753397702657.json, 视频生成/图生视频/MiniMax H3全能参考工作流｜文生视频单图生视频图生视频_2090446719375990786.json, 视频生成/图生视频/MiniMax H3全能参考生视频加速版 多重加速高清输出_2098827453300039682.json, 视频生成/图生视频/MiniMax H3打戏战斗特效图生视频处理工作流_2102501974091583489.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_92

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/H3打戏T8流大改自用版｜战斗特效拳拳到肉｜图生视频武打场面拉满_2102254012815990786.json、视频生成/图生视频/H3极速导演台8步双时钟-图生首尾帧多参一体化_2087375481896259586.json、视频生成/图生视频/H3高保真图生视频 静止图像动态化运镜重构_2099924808850042881.json、视频生成/图生视频/Lightx2v正式版8步去油双时钟参考生视频V2｜Minimax图生视频工作流_2088144409752850433.json、视频生成/图生视频/Lightx2v正式版8步去油双时钟图生视频V1｜Minimax图生视频工作流_2088140753397702657.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
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
- `LoraLoaderBypassModelOnly` —— 7/8 个有
- `MiniMaxH3DualClockSamplerT8` —— 6/8 个有
- `CR Prompt Text` —— 5/8 个有
- `ModelAttentionBackend` —— 4/8 个有
- `ExtendIntermediateSigmas` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `SolAttnMiniMax` —— 3/8 个有
- `H3SigmaRefiner` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `MiniMaxChunkFeedForward` —— 2/8 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/8 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/8 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/8 个有
- `MiniMaxLowVRAMAttention` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `IntToString` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有
- `Seed_` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `text-util-join-text` —— 1/8 个有

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
