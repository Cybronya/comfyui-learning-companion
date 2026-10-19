---
name: text_to_image_lora_sampler_clip_111
type: Text To Image
frequency: 9
level: strong
coverage: 0.904333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MINIMAX-H3文生视频T8加速版｜快速视频生成工作流_2097789348782628866.json, 视频生成/文生视频/MiniMax H3 BF16 Turbo Sage加速版｜文生图生视频_2092049982156271618.json, 视频生成/文生视频/MiniMax H3 Ref2VA多参考生视频｜9图3视频3音频混搭｜2K超清带立体声_2101845289526185986.json, 视频生成/文生视频/MiniMax H3文生视频V2版｜提示词一键生成视频_2089409853189091329.json, 视频生成/文生视频/MiniMax H3首尾帧图生视频-4步加速文生视频生视频_2087340787251109890.json, 视频生成/文生视频/加速版直出｜MiniMax_H3_BF16_Turbo_Sage_ 文生图生视频高速生成_2089458798560894978.json, 视频生成/文生视频/文武双修均衡版｜MiniMax H3双采动漫短剧_2096624296683720706.json, 视频生成/文生视频/电影质感拉满｜MiniMax H3双采参考文武双修均衡_2096558764462792706.json, 视频生成/文生视频/高动态战斗专属｜BUNNY_H3双采放大FL2VA套件_2096632033136177153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_111

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/MINIMAX-H3文生视频T8加速版｜快速视频生成工作流_2097789348782628866.json、视频生成/文生视频/MiniMax H3 BF16 Turbo Sage加速版｜文生图生视频_2092049982156271618.json、视频生成/文生视频/MiniMax H3 Ref2VA多参考生视频｜9图3视频3音频混搭｜2K超清带立体声_2101845289526185986.json、视频生成/文生视频/MiniMax H3文生视频V2版｜提示词一键生成视频_2089409853189091329.json、视频生成/文生视频/MiniMax H3首尾帧图生视频-4步加速文生视频生视频_2087340787251109890.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

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
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AVDecodeT8` —— 8/9 个有
- `MiniMaxH3AudioConditioningT8` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `LoadImage` —— 7/9 个有
- `CR Prompt Text` —— 5/9 个有
- `LoraLoaderBypassModelOnly` —— 5/9 个有
- `BasicScheduler` —— 4/9 个有
- `KSamplerSelect` —— 4/9 个有
- `MiniMaxH3DualClockSamplerT8` —— 4/9 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 4/9 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 3/9 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 3/9 个有
- `ModelAttentionBackend` —— 2/9 个有
- `SolAttnMiniMax` —— 2/9 个有
- `VAEDecodeAudio` —— 2/9 个有
- `CreateVideo` —— 1/9 个有
- `DiffusionModelLoaderKJ` —— 1/9 个有
- `ImpactSwitch` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `MiniMaxH3ImageToVideo` —— 1/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/9 个有
- `MiniMaxH3ReferenceToVideo` —— 1/9 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SaveVideo` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
