---
name: text_to_image_lora_sampler_clip_74
type: Text To Image
frequency: 16
level: strong
coverage: 0.890687
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/文生图生视频通用工作流｜多模式视频快速生成_2097522046669508609.json, 视频生成/文生视频/文生视频｜720P双时钟高质量加速0.8 图生视频视频生视频全能直出_2089415507794550786.json, 视频生成/文生视频/极速8步开源版｜MiniMax H3跳舞漫剧角色表演文生视频_2093768920888074242.json, 视频生成/文生视频/真实打斗多参考生成｜MiniMax H3 B25-49 768P lora_2095941865878147073.json, 视频生成/文生视频/短剧漫剧创意视频｜Minimax H3开源版8步极速文生视频（600步新加速LORA）_2090842404969598977.json, 视频生成/文生视频/短剧漫剧文生视频｜Minimax H3开源8步极速，600步新加速LORA_2099884404595314689.json, 视频生成/文生视频/短剧漫剧文生视频｜Minimax H3开源8步极速，600步新加速LORA_2104930009243799553.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2094027470818332673.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2097107105957367810.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2098918238603272193.json, 视频生成/文生视频/跳舞短剧漫剧创意视频 8步高质量极速Minimax H3开源版文生视频_2106165786128773121.json, 视频生成/文生视频/跳舞短剧漫剧视频生成｜8步极速高质量文生视频_2095939063923691522.json, 视频生成/文生视频/首尾帧生视频｜MiniMax-H3文生视频图生视频全能_2089683499384135682.json, 视频生成/文生视频/高画质BF16剪枝版｜Minimax H3采样器调度器无加速_2093808070471282690.json, 视频生成/文生视频/高速运动BF16剪枝版｜Minimax H3采样器调度器无加速_2093806594449563650.json, 视频生成/视频生视频/参考视频驱动动作迁移 MiniMax_H3 Ref2VA视频生视频工作流_2106160686563942401.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_74

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/文生图生视频通用工作流｜多模式视频快速生成_2097522046669508609.json、视频生成/文生视频/文生视频｜720P双时钟高质量加速0.8 图生视频视频生视频全能直出_2089415507794550786.json、视频生成/文生视频/极速8步开源版｜MiniMax H3跳舞漫剧角色表演文生视频_2093768920888074242.json、视频生成/文生视频/真实打斗多参考生成｜MiniMax H3 B25-49 768P lora_2095941865878147073.json、视频生成/文生视频/短剧漫剧创意视频｜Minimax H3开源版8步极速文生视频（600步新加速LORA）_2090842404969598977.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 15/16 个有
- `MiniMaxH3AVDecodeT8` —— 15/16 个有
- `PrimitiveFloat` —— 15/16 个有
- `VHS_VideoCombine` —— 15/16 个有
- `孤海注释` —— 15/16 个有
- `CR Prompt Text` —— 14/16 个有
- `MiniMaxH3AudioConditioningT8` —— 14/16 个有
- `MiniMaxH3DualClockSamplerT8` —— 11/16 个有
- `LoraLoaderBypassModelOnly` —— 10/16 个有
- `ModelAttentionBackend` —— 9/16 个有
- `LoadImage` —— 6/16 个有
- `BasicScheduler` —— 5/16 个有
- `KSamplerSelect` —— 5/16 个有
- `LayerUtility: PurgeVRAM V2` —— 3/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `PathchSageAttentionKJ` —— 2/16 个有
- `VAEDecodeAudio` —— 2/16 个有
- `CR Text` —— 1/16 个有
- `CreateVideo` —— 1/16 个有
- `MiniMaxH3ImageToVideo` —— 1/16 个有
- `MiniMaxH3Unified` —— 1/16 个有
- `SaveImage` —— 1/16 个有
- `SaveVideo` —— 1/16 个有
- `VHS_LoadVideo` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（16/16 个样本）：Steps较低可能导致细节不足
