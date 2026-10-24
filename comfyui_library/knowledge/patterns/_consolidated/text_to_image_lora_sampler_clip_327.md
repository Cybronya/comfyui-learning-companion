---
name: text_to_image_lora_sampler_clip_327
type: Text To Image
frequency: 6
level: strong
coverage: 0.620333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, ResolutionSelector, SelfLiftH3Sampler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/YZ金鱼改MiniMax H3终极篇文武双全｜无限画布漫剧利器_2111305187406209025.json, 视频生成/文生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json, 视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2106907557137838082.json, 视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频方案_2107577744304459778.json, 视频生成/文生视频/MiniMax_H3_SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2108377073327894530.json, 视频生成/文生视频/Self Lift双采工作流文生图生视频，文生视频图生视频高效创作方案_2105780339426816001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_327

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/YZ金鱼改MiniMax H3终极篇文武双全｜无限画布漫剧利器_2111305187406209025.json、视频生成/文生视频/AITUDOU-H3+SelfLift组合｜影视级情绪表达出片_2106620640190095361.json、视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2106907557137838082.json、视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频方案_2107577744304459778.json、视频生成/文生视频/MiniMax_H3_SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2108377073327894530.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `H3SigmaRefiner` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `Text` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `Float` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `SolAttnMiniMax` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `CreateVideo` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `ModelPreviewOverrideKJ` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `BlockSparseAttention` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3ImageToVideo` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有
- `easy loraStack` —— 1/6 个有
- `easy loraStackApply` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
