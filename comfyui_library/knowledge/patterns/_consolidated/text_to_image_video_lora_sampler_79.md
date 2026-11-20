---
name: text_to_image_video_lora_sampler_79
type: Text To Image
frequency: 10
level: strong
coverage: 0.7087
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, FeiHouEasyH3RH, FeiHouEasyH3RHLoader, FeiHouEasyH3RHOutput, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3文戏工作流，视频运镜图生视频处理方案_2107531695498022913.json, 视频生成/图生视频/MiniMax H3武戏工作流，战斗特效视频运镜图生视频处理方案_2107555842454282241.json, 视频生成/图生视频/MinimaxH3文戏V1.0版 图生视频自然质感直出_2110365604116000770.json, 视频生成/图生视频/MinimaxH3文戏V1.0版｜图生视频对话运镜自然流畅，剧情党福音_2107298802309885953.json, 视频生成/图生视频/MinimaxH3武戏V1.3版｜战斗特效炸裂运镜带感，武打视频一步到位_2107303436646707202.json, 视频生成/文生视频/MiniMax H3全能参考极简多合一视频处理工作流_2101763281118650370.json, 视频生成/文生视频/MiniMax H3全能参考极简多合一，文生视频视频生视频图生视频三模融合_2102882092685283330.json, 视频生成/文生视频/MiniMax_H3全能参考极简多合一，文生视频视频生视频图生视频三模融合_2105117189677338626.json, 视频生成/文生视频/Minimax H3全能参考极简工作流 文生视频图生视频多合一_2098653013840850945.json, 视频生成/文生视频/minimax h3极简画布满血版｜多参工作流文生视频图生视频全能_2104556954260697090.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3文戏工作流，视频运镜图生视频处理方案_2107531695498022913.json、视频生成/图生视频/MiniMax H3武戏工作流，战斗特效视频运镜图生视频处理方案_2107555842454282241.json、视频生成/图生视频/MinimaxH3文戏V1.0版 图生视频自然质感直出_2110365604116000770.json、视频生成/图生视频/MinimaxH3文戏V1.0版｜图生视频对话运镜自然流畅，剧情党福音_2107298802309885953.json、视频生成/图生视频/MinimaxH3武戏V1.3版｜战斗特效炸裂运镜带感，武打视频一步到位_2107303436646707202.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `FeiHouEasyH3RH`
- `FeiHouEasyH3RHLoader`
- `FeiHouEasyH3RHOutput`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 9/10 个有
- `SaveImage` —— 7/10 个有
- `CreateVideo` —— 5/10 个有
- `MiniMaxChunkFeedForward` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 5/10 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 5/10 个有
- `MiniMaxH3SigmaShift` —— 5/10 个有
- `MiniMaxLowVRAMAttention` —— 5/10 个有
- `RunningHub Deepcleaner` —— 5/10 个有
- `SelfLiftAvatarH3Sampler` —— 5/10 个有
- `SelfLiftH3Sampler` —— 5/10 个有
- `easy clearCacheAll` —— 5/10 个有
- `VRAM_Debug` —— 3/10 个有
- `LoraLoaderBypassModelOnly` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `ResolutionSelector` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
