---
name: text_to_image_lora_sampler_clip_207
type: Text To Image
frequency: 4
level: strong
coverage: 0.59325
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelPreviewOverrideKJ, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3文生首尾图参多合一二采高清放大视频工具_2101039738512822274.json, 视频生成/文生视频/Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665.json, 视频生成/文生视频/Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577.json, 视频生成/文生视频/Self Lift双采工作流文生图生视频，文生视频图生视频高效创作方案_2105780339426816001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_207

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3文生首尾图参多合一二采高清放大视频工具_2101039738512822274.json、视频生成/文生视频/Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665.json、视频生成/文生视频/Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577.json、视频生成/文生视频/Self Lift双采工作流文生图生视频，文生视频图生视频高效创作方案_2105780339426816001.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 4 个 workflow 都包含：
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
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `H3SigmaRefiner` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `ImpactConditionalBranch` —— 3/4 个有
- `Int` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `MiniMaxH3ReferenceToVideo` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/4 个有
- `布尔孤海` —— 3/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `SolAttnPatch` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
