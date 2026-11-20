---
name: text_to_image_video_lora_sampler_79
type: Text To Image
frequency: 11
level: strong
coverage: 0.832273
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2114339811321536514.json, 视频生成/图生视频/多图参考加速生成｜Minimax_H3高质量视频工作流_2115293471622914050.json, 视频生成/图生视频/多图参考短剧制作加速工作流｜Minimax_H3图生视频_2088347597277843458.json, 视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2090555558922383362.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3开源手动版_2095937261144731649.json, 视频生成/图生视频/文戏多图参考｜MINIMAX-H3图生视频生成_2094025328523042818.json, 视频生成/文生视频/4步加速二采放大｜MinimaxH3全能参考三模视频_2094739286921928705.json, 视频生成/文生视频/8步二次采样1088p多参视频｜MinimaxH3文生图生视频生视频工作流_2088128342645104641.json, 视频生成/文生视频/MinimaxH3全能参考二采高清放大｜4步加速生成_2094517725417787393.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2114339811321536514.json、视频生成/图生视频/多图参考加速生成｜Minimax_H3高质量视频工作流_2115293471622914050.json、视频生成/图生视频/多图参考短剧制作加速工作流｜Minimax_H3图生视频_2088347597277843458.json、视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json、视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
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
- `BasicScheduler` —— 10/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `孤海注释` —— 9/11 个有
- `BasicGuider` —— 8/11 个有
- `KSamplerSelect` —— 8/11 个有
- `VAEDecodeAudio` —— 8/11 个有
- `LoraLoaderBypassModelOnly` —— 7/11 个有
- `ExtendIntermediateSigmas` —— 5/11 个有
- `H3SigmaRefiner` —— 5/11 个有
- `INTConstant` —— 5/11 个有
- `ImageResizeKJv2` —— 5/11 个有
- `MiniMaxH3AVDecodeT8` —— 5/11 个有
- `VAEEncode` —— 5/11 个有
- `ConditioningZeroOut` —— 4/11 个有
- `PT_H3ConcatAVLatent` —— 4/11 个有
- `CFGGuider` —— 3/11 个有
- `GetNode` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `VAEEncodeAudio` —— 3/11 个有
- `CR Prompt Text` —— 2/11 个有
- `EmptyFlux2LatentImage` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `MiniMaxH3TurboLoRA` —— 2/11 个有
- `MiniMaxH3TurboSampler` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `HAIGC_VideoLoader` —— 1/11 个有
- `LTXVConcatAVLatent` —— 1/11 个有
- `MiniMaxH3BlockCacheT8` —— 1/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/11 个有
- `UniBlockSwap` —— 1/11 个有
- `VRAM_Debug` —— 1/11 个有
- `easy ifElse` —— 1/11 个有
- `忽略多组孤海` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 11 | 67% |
| Prompt 约束强度(CFG) | 4.5 | 1.1 - 4.5 | 11 | 66% |
| 采样算法 | er_sde | - | 11 | 82% |
| 调度器 | beta | - | 11 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，11 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.1 - 4.5，11 个样本
- 采样算法 最常用 er_sde，11 个样本，一致性 82%
- 调度器 最常用 beta，11 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（15/11 个样本）：Steps较低可能导致细节不足
