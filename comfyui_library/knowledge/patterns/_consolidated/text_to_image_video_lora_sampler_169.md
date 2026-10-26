---
name: text_to_image_video_lora_sampler_169
type: Text To Image
frequency: 4
level: strong
coverage: 0.696
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/8步二次采样1088p多参视频｜MinimaxH3文生图生视频生视频工作流_2088128342645104641.json, 视频生成/文生视频/H3全能参考工作流-文生视频生视频图生视频_2087365023227277313.json, 视频生成/文生视频/MINIMAX H3多参二采2K直出官方API文生视频图生视频_2088208139706519553.json, 视频生成/文生视频/Minimax H3文生首尾图参多合一生视频-自用版二采高清放大_2087394737073512450.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/8步二次采样1088p多参视频｜MinimaxH3文生图生视频生视频工作流_2088128342645104641.json、视频生成/文生视频/H3全能参考工作流-文生视频生视频图生视频_2087365023227277313.json、视频生成/文生视频/MINIMAX H3多参二采2K直出官方API文生视频图生视频_2088208139706519553.json、视频生成/文生视频/Minimax H3文生首尾图参多合一生视频-自用版二采高清放大_2087394737073512450.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
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
- `BasicScheduler` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `KSamplerSelect` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `MiniMaxH3AVDecodeT8` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VAEEncode` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `PT_H3ConcatAVLatent` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `VAEEncodeAudio` —— 2/4 个有
- `忽略多组孤海` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `HAIGC_VideoLoader` —— 1/4 个有
- `Int` —— 1/4 个有
- `LTXVConcatAVLatent` —— 1/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxH3BlockCacheT8` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `RH_MinimaxHailuoH3RegenerationMultimodalToVideo` —— 1/4 个有
- `UniBlockSwap` —— 1/4 个有
- `VAEDecodeAudio` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有
- `VRAM_Debug` —— 1/4 个有
- `easy ifElse` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
