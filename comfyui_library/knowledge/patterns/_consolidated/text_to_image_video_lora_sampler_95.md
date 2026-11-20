---
name: text_to_image_video_lora_sampler_95
type: Text To Image
frequency: 9
level: strong
coverage: 0.911222
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Minimax H3快速版短剧漫剧创意文生视频｜新加速LORA提效_2111290931298263042.json, 图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化工作流_2090868519985565697.json, 图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化流_2090563536077545474.json, 平台全量/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2112746319839326209.json, 平台全量/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2111728686713102338.json, 视频生成/图生视频/8步去油双时钟参考生视频V2｜Lightx2v正式版Minimax图生视频_2088160534666502145.json, 视频生成/图生视频/H3打戏T8流大改自用版｜战斗特效拳拳到肉｜图生视频武打场面拉满_2102254012815990786.json, 视频生成/图生视频/MiniMax H3打戏战斗特效图生视频处理工作流_2102501974091583489.json, 视频生成/图生视频/多参考图生视频4步加速｜MiniMax H3提示词自动优化美少女_2091298868020473857.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_95

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Minimax H3快速版短剧漫剧创意文生视频｜新加速LORA提效_2111290931298263042.json、图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化工作流_2090868519985565697.json、图片生成/文生图/int8文生视频4步加速｜MiniMax H3提示词优化流_2090563536077545474.json、平台全量/MiniMax_H3视频复刻数字人｜换人换产品文案不换原声保留_2112746319839326209.json、平台全量/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2111728686713102338.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
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

**可变部分**（部分 workflow 才有）：
- `LoraLoaderBypassModelOnly` —— 8/9 个有
- `孤海注释` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `MiniMaxH3DualClockSamplerT8` —— 6/9 个有
- `ModelAttentionBackend` —— 6/9 个有
- `SolAttnMiniMax` —— 4/9 个有
- `Any To String (mtb)` —— 3/9 个有
- `BatchImagesNode` —— 3/9 个有
- `JoinStringMulti` —— 3/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/9 个有
- `PrimitiveStringMultiline` —— 3/9 个有
- `StringConcatenate` —— 3/9 个有
- `UniBlockSwap` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `llama_cpp_instruct_adv` —— 3/9 个有
- `llama_cpp_model_loader` —— 3/9 个有
- `llama_cpp_parameters` —— 3/9 个有
- `ExtendIntermediateSigmas` —— 2/9 个有
- `H3SigmaRefiner` —— 2/9 个有
- `MiniMaxChunkFeedForward` —— 2/9 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 2/9 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 2/9 个有
- `MiniMaxLowVRAMAttention` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 1/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
