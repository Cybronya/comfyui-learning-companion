---
name: text_to_image_lora_sampler_clip_233
type: Text To Image
frequency: 9
level: strong
coverage: 0.904889
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax H3多图参考加速文生视频图生视频工作流_2088178522983587841.json, 视频生成/文生视频/Minimax_H3多图参考加速版｜文图视频都能喂，出视频又快又稳_2099527126897745922.json, 视频生成/文生视频/参考加速工作流｜Minmax H3文生图生视频直出_2091671424758009858.json, 视频生成/文生视频/多图参考一键提速｜Minimax_H3 加速工作流三模支持_2096218441563860994.json, 视频生成/文生视频/多图参考加速工作流｜Minimax H3文生图生视频_2092060324655620097.json, 视频生成/文生视频/多图参考加速流｜Minimax_H3文生图生视频生成_2093424367945478146.json, 视频生成/文生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2095931904716533761.json, 视频生成/文生视频/多图参考加速｜Minimax_H3三模视频生成工作流_2093754246821928961.json, 视频生成/文生视频/极速高质开源版｜MiniMax H3 RE2VA多图参考生视频_2090934908318478338.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_233

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/Minimax H3多图参考加速文生视频图生视频工作流_2088178522983587841.json、视频生成/文生视频/Minimax_H3多图参考加速版｜文图视频都能喂，出视频又快又稳_2099527126897745922.json、视频生成/文生视频/参考加速工作流｜Minmax H3文生图生视频直出_2091671424758009858.json、视频生成/文生视频/多图参考一键提速｜Minimax_H3 加速工作流三模支持_2096218441563860994.json、视频生成/文生视频/多图参考加速工作流｜Minimax H3文生图生视频_2092060324655620097.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 8/9 个有
- `LoadAudio` —— 8/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/9 个有
- `CFGGuider` —— 7/9 个有
- `ConditioningZeroOut` —— 7/9 个有
- `VHS_VideoCombine` —— 7/9 个有
- `MiniMaxH3TurboSampler` —— 6/9 个有
- `MiniMaxH3TurboLoRA` —— 5/9 个有
- `ModelAttentionBackend` —— 4/9 个有
- `KSamplerSelect` —— 3/9 个有
- `BasicGuider` —— 2/9 个有
- `CreateVideo` —— 2/9 个有
- `H3SigmaRefiner` —— 2/9 个有
- `Int` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `SaveVideo` —— 2/9 个有
- `H3AudioRefineSampler` —— 1/9 个有
- `H3FrozenVideoCache` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `LoraLoaderBypassModelOnly` —— 1/9 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/9 个有
- `SigmasPreview` —— 1/9 个有
- `SolAttnPatch` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
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
