---
name: text_to_image_video_lora_sampler_61
type: Text To Image
frequency: 13
level: strong
coverage: 0.765077
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2114339811321536514.json, 视频生成/图生视频/多图参考生视频｜MiniMaxH3图生视频一键生成_2092741832886276098.json, 视频生成/图生视频/多图参考短剧制作加速工作流｜Minimax_H3图生视频_2088347597277843458.json, 视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json, 视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json, 视频生成/图生视频/文戏多图参考｜MINIMAX-H3图生视频生成_2094025328523042818.json, 视频生成/图生视频/最强文戏低配版｜MINIMAX-H3开源角色一致性生成_2095074002149662722.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2104719643922493441.json, 视频生成/文生视频/MINIMAX H3原本fl2va分布高低解码二采 视频生成优化方案_2105066230074920961.json, 视频生成/文生视频/MINIMAX-H3原版fl2va高低解码二采｜视频画质精修方案_2104483718219001858.json, 视频生成/文生视频/MiniMax H3 SelfLift加二采加音频参考工作流，文生视频视频生视频图生视频_2106518365966786562.json, 视频生成/文生视频/MiniMax H3打斗版二采视频生视频处理生成工具_2101749624259309569.json, 视频生成/文生视频/武戏专用参考｜MiniMax H3提示词手输自动可选_2096598519665750017.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2114339811321536514.json、视频生成/图生视频/多图参考生视频｜MiniMaxH3图生视频一键生成_2092741832886276098.json、视频生成/图生视频/多图参考短剧制作加速工作流｜Minimax_H3图生视频_2088347597277843458.json、视频生成/图生视频/文戏向多图参考生视频｜MINIMAX-H3剧情图生视频_2093803832823336961.json、视频生成/图生视频/文戏多图参考生视频｜MINIMAX-H3剧情向图生视频_2093777220228702209.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 12/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `BasicGuider` —— 11/13 个有
- `KSamplerSelect` —— 11/13 个有
- `H3SigmaRefiner` —— 10/13 个有
- `ExtendIntermediateSigmas` —— 9/13 个有
- `INTConstant` —— 8/13 个有
- `PrimitiveStringMultiline` —— 8/13 个有
- `GetNode` —— 7/13 个有
- `ModelAttentionBackend` —— 7/13 个有
- `SetNode` —— 7/13 个有
- `CR Prompt Text` —— 6/13 个有
- `LTXVConcatAVLatent` —— 6/13 个有
- `LTXVSeparateAVLatent` —— 6/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/13 个有
- `MinimaxH3LatentUpscaler3D` —— 6/13 个有
- `PreviewImage` —— 6/13 个有
- `PlaySound|pysssss` —— 4/13 个有
- `SaveImage` —— 4/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `LoraLoaderBypassModelOnly` —— 3/13 个有
- `CFGGuider` —— 2/13 个有
- `MiniMaxChunkFeedForward` —— 2/13 个有
- `MiniMaxLowVRAMAttention` —— 2/13 个有
- `RH_LLMAPI_Pro_Node` —— 2/13 个有
- `Any Switch (rgthree)` —— 1/13 个有
- `CreateVideo` —— 1/13 个有
- `EmptyFlux2LatentImage` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/13 个有
- `MiniMaxH3TurboLoRA` —— 1/13 个有
- `MiniMaxH3TurboSampler` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有
- `MuyeTextEditOutput` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `SelfLiftAvatarH3Sampler` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 13 | 75% |
| Prompt 约束强度(CFG) | 4.5 | 1.1 - 4.5 | 13 | 79% |
| 采样算法 | er_sde | - | 13 | 92% |
| 调度器 | beta | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，13 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.1 - 4.5，13 个样本
- 采样算法 最常用 er_sde，13 个样本，一致性 92%
- 调度器 最常用 beta，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（16/13 个样本）：Steps较低可能导致细节不足
