---
name: text_to_image_lora_sampler_clip_126
type: Text To Image
frequency: 13
level: strong
coverage: 0.906846
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/文戏不油武戏带感 MiniMax H3双采全能参考生视频V2_2104287266226139138.json, 视频生成/文生视频/文武双修均衡版｜MiniMax H3双采动漫短剧_2096624296683720706.json, 视频生成/文生视频/极速8步开源版｜MiniMax H3跳舞漫剧角色表演文生视频_2093768920888074242.json, 视频生成/文生视频/电影质感拉满｜MiniMax H3双采参考文武双修均衡_2096558764462792706.json, 视频生成/文生视频/短剧漫剧创意视频｜Minimax H3开源版8步极速文生视频（600步新加速LORA）_2090842404969598977.json, 视频生成/文生视频/短剧漫剧文生视频｜Minimax H3开源8步极速，600步新加速LORA_2099884404595314689.json, 视频生成/文生视频/短剧漫剧文生视频｜Minimax H3开源8步极速，600步新加速LORA_2104930009243799553.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2094027470818332673.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2097107105957367810.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2098918238603272193.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2106165786128773121.json, 视频生成/文生视频/跳舞短剧漫剧视频生成｜8步极速高质量文生视频_2095939063923691522.json, 视频生成/文生视频/高动态战斗专属｜BUNNY_H3双采放大FL2VA套件_2096632033136177153.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/文戏不油武戏带感 MiniMax H3双采全能参考生视频V2_2104287266226139138.json、视频生成/文生视频/文武双修均衡版｜MiniMax H3双采动漫短剧_2096624296683720706.json、视频生成/文生视频/极速8步开源版｜MiniMax H3跳舞漫剧角色表演文生视频_2093768920888074242.json、视频生成/文生视频/电影质感拉满｜MiniMax H3双采参考文武双修均衡_2096558764462792706.json、视频生成/文生视频/短剧漫剧创意视频｜Minimax H3开源版8步极速文生视频（600步新加速LORA）_2090842404969598977.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 12/13 个有
- `ModelAttentionBackend` —— 12/13 个有
- `VHS_VideoCombine` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `CR Prompt Text` —— 11/13 个有
- `LoadImage` —— 4/13 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 4/13 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 4/13 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 4/13 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 4/13 个有
- `SolAttnMiniMax` —— 3/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `CR Load LoRA` —— 1/13 个有
- `CreateVideo` —— 1/13 个有
- `FastGroupsBypassSwitch` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `SaveVideo` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
