---
name: text_to_image_video_lora_sampler_105
type: Text To Image
frequency: 7
level: strong
coverage: 0.675857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json, 视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json, 视频生成/图生视频/四步加速出片｜H3全能参考二采高清放大带Lora_2096538998759059458.json, 视频生成/文生视频/4步加速二采放大｜MinimaxH3全能参考三模视频_2094739286921928705.json, 视频生成/文生视频/MINIMAX H3多参二采2K直出官方API文生视频图生视频_2088208139706519553.json, 视频生成/文生视频/MinimaxH3全能参考二采高清放大｜4步加速生成_2094517725417787393.json, 视频生成/文生视频/漫剧工作流15秒直出｜Mini Max H3文生图生视频生视频_2088366199813001217.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_105

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/加速放大Minimax参考生视频图生视频高清采样工作流_2088400575028355073.json、视频生成/图生视频/参考生视频加速放大｜Minimax图生视频工作流_2088379811487113218.json、视频生成/图生视频/四步加速出片｜H3全能参考二采高清放大带Lora_2096538998759059458.json、视频生成/文生视频/4步加速二采放大｜MinimaxH3全能参考三模视频_2094739286921928705.json、视频生成/文生视频/MINIMAX H3多参二采2K直出官方API文生视频图生视频_2088208139706519553.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AVDecodeT8` —— 6/7 个有
- `VHS_LoadVideo` —— 6/7 个有
- `CR Prompt Text` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `LoraLoaderBypassModelOnly` —— 5/7 个有
- `MiniMaxH3ReferenceToVideo` —— 5/7 个有
- `GetNode` —— 4/7 个有
- `SetNode` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `VAEEncodeAudio` —— 3/7 个有
- `easy clearCacheAll` —— 3/7 个有
- `ImpactConditionalBranch` —— 2/7 个有
- `Int` —— 2/7 个有
- `MathExpression_UTK` —— 2/7 个有
- `MiniMaxH3AudioConditioningT8` —— 2/7 个有
- `MiniMaxH3DualClockSamplerT8` —— 2/7 个有
- `PrimitiveStringMultiline` —— 2/7 个有
- `RIFE VFI` —— 2/7 个有
- `ResizeShortestToNode` —— 2/7 个有
- `获取视频信息` —— 2/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/7 个有
- `SaveVideo` —— 1/7 个有
- `SigmasGraph` —— 1/7 个有
- `VAEDecodeAudio` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
