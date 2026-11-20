---
name: text_to_image_video_lora_sampler_62
type: Text To Image
frequency: 14
level: strong
coverage: 0.903786
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3多图参考加速工作流 单采不油腻不破音_2099563905008889858.json, 视频生成/文生视频/H3官方流程单采极速文戏｜文生视频图生视频快速生成_2106986232776585218.json, 视频生成/文生视频/H3官流mpov版不用加速LoRA工作流，文生视频视频生视频图生视频方案_2107987502211620866.json, 视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107179960334114818.json, 视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107462612324806657.json, 视频生成/文生视频/H3官流终极版 视频生成官方最佳方案稳定出片_2105387723480719362.json, 视频生成/文生视频/MiniMax H3多图参考加速工作流 单采不油腻不破音_2099185147278090242.json, 视频生成/文生视频/Minimax_H3多图参考加速版｜文图视频都能喂，出视频又快又稳_2099527126897745922.json, 视频生成/文生视频/多图参考一键提速｜Minimax_H3 加速工作流三模支持_2096218441563860994.json, 视频生成/文生视频/多图参考加速工作流｜Minimax H3文生图生视频_2092060324655620097.json, 视频生成/文生视频/多图参考加速流｜Minimax_H3文生图生视频生成_2093424367945478146.json, 视频生成/文生视频/多图参考加速生成｜Minimax H3高质量视频工作流_2095931904716533761.json, 视频生成/文生视频/多图参考加速｜Minimax_H3三模视频生成工作流_2093754246821928961.json, 视频生成/文生视频/氛围感短视频生成｜H3文生视频光影情绪渲染_2096675059892047874.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/H3多图参考加速工作流 单采不油腻不破音_2099563905008889858.json、视频生成/文生视频/H3官方流程单采极速文戏｜文生视频图生视频快速生成_2106986232776585218.json、视频生成/文生视频/H3官流mpov版不用加速LoRA工作流，文生视频视频生视频图生视频方案_2107987502211620866.json、视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107179960334114818.json、视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107462612324806657.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 14 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 13/14 个有
- `孤海注释` —— 13/14 个有
- `ModelAttentionBackend` —— 10/14 个有
- `KSamplerSelect` —— 9/14 个有
- `CFGGuider` —— 8/14 个有
- `ConditioningZeroOut` —— 8/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/14 个有
- `MiniMaxH3TurboSampler` —— 8/14 个有
- `BasicGuider` —— 6/14 个有
- `MiniMaxH3SigmaShift` —— 6/14 个有
- `ModelPreviewOverrideKJ` —— 6/14 个有
- `SaveImage` —— 6/14 个有
- `BlockSparseAttention` —— 5/14 个有
- `MiniMaxH3TurboLoRA` —— 5/14 个有
- `VHS_LoadVideo` —— 5/14 个有
- `ExtendIntermediateSigmas` —— 3/14 个有
- `H3AudioRefineSampler` —— 3/14 个有
- `H3FrozenVideoCache` —— 3/14 个有
- `ManualSigmas` —— 3/14 个有
- `PreviewAny` —— 3/14 个有
- `SolAttnPatch` —— 3/14 个有
- `EmptyImage` —— 1/14 个有
- `PreviewImage` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
