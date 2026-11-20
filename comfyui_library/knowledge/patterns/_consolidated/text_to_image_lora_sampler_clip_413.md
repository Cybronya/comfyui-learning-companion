---
name: text_to_image_lora_sampler_clip_413
type: Text To Image
frequency: 5
level: strong
coverage: 0.8962
common_nodes: [1hew_AudioDuration, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LoadAudio, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, TrimAudio, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 SelfLift双采8步加速 文生视频图生视频处理工具_2112989919818903554.json, 视频生成/图生视频/MiniMax H3 sol attention提速 混合模型视频生成工具_2113764953873272833.json, 视频生成/图生视频/minimax h3 selflift双采8工作流｜文图双入口稳定出片_2112902722549805057.json, 视频生成/图生视频/minimax h3 selflift双采8流程，文生视频图生视频通吃_2110514641985171458.json, 视频生成/图生视频/minimax h3 sol attention提速｜注意力机制加速生视频_2113534762492186626.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_413

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 SelfLift双采8步加速 文生视频图生视频处理工具_2112989919818903554.json、视频生成/图生视频/MiniMax H3 sol attention提速 混合模型视频生成工具_2113764953873272833.json、视频生成/图生视频/minimax h3 selflift双采8工作流｜文图双入口稳定出片_2112902722549805057.json、视频生成/图生视频/minimax h3 selflift双采8流程，文生视频图生视频通吃_2110514641985171458.json、视频生成/图生视频/minimax h3 sol attention提速｜注意力机制加速生视频_2113534762492186626.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `1hew_AudioDuration`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 4/5 个有
- `SaveImage` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `BlockSparseAttention` —— 2/5 个有
- `H3SigmaRefiner` —— 2/5 个有
- `LTXVSeparateAVLatent` —— 2/5 个有
- `MiniMaxH3SigmaRefiner` —— 2/5 个有
- `QwenH3PromptLocal` —— 2/5 个有
- `VAEDecodeAudio` —— 2/5 个有
- `CreateVideo` —— 1/5 个有
- `LoadVideo` —— 1/5 个有
- `SaveVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
