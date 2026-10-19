---
name: text_to_image_video_lora_sampler_78
type: Text To Image
frequency: 10
level: strong
coverage: 0.8064
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [easy clearCacheAll]
members: [视频生成/文生视频/多图参考一键提速｜Minimax_H3 加速工作流三模支持_2096218441563860994.json, 视频生成/文生视频/多图参考加速工作流｜Minimax H3文生图生视频_2092060324655620097.json, 视频生成/文生视频/多图参考加速流｜Minimax_H3文生图生视频生成_2093424367945478146.json, 视频生成/文生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2095931904716533761.json, 视频生成/文生视频/多图参考加速｜Minimax_H3三模视频生成工作流_2093754246821928961.json, 视频生成/文生视频/文生图生视频全能参考三合一｜minimax阿里8步加速_2095811801366745089.json, 视频生成/文生视频/氛围感短视频生成｜H3文生视频光影情绪渲染_2096675059892047874.json, 视频生成/文生视频/漫剧工作流15秒直出｜Mini Max H3文生图生视频生视频_2088366199813001217.json, 视频生成/视频生视频/双模型加强版二采重绘MiniMax H3全能参考RH兼容版_9图参考图生视频_2106499744423043074.json, 视频生成/视频生视频/双模型加强版二采重绘_MinimaxH3全能参考图生视频RH兼容版_2106194718110609410.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/多图参考一键提速｜Minimax_H3 加速工作流三模支持_2096218441563860994.json、视频生成/文生视频/多图参考加速工作流｜Minimax H3文生图生视频_2092060324655620097.json、视频生成/文生视频/多图参考加速流｜Minimax_H3文生图生视频生成_2093424367945478146.json、视频生成/文生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2095931904716533761.json、视频生成/文生视频/多图参考加速｜Minimax_H3三模视频生成工作流_2093754246821928961.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/10 个有
- `BasicGuider` —— 5/10 个有
- `CFGGuider` —— 5/10 个有
- `ConditioningZeroOut` —— 5/10 个有
- `KSamplerSelect` —— 5/10 个有
- `MiniMaxH3TurboLoRA` —— 5/10 个有
- `MiniMaxH3TurboSampler` —— 5/10 个有
- `ModelAttentionBackend` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 4/10 个有
- `GetNode` —— 3/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `PT_H3ConcatAVLatent` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `VAEEncode` —— 3/10 个有
- `VAEEncodeAudio` —— 3/10 个有
- `easy clearCacheAll` —— 3/10 个有
- `EasyCache` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `LoraLoaderBypassModelOnly` —— 2/10 个有
- `MiniMaxChunkFeedForward` —— 2/10 个有
- `MiniMaxLowVRAMAttention` —— 2/10 个有
- `ResizeShortestToNode` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `UniBlockSwap` —— 2/10 个有
- `UniBlockSwapTE` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `ManualSigmas` —— 1/10 个有
- `MiniMaxH3ImageToVideo` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `SigmasGraph` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy clearCacheAll
