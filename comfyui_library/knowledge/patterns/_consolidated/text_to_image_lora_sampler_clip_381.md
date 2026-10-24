---
name: text_to_image_lora_sampler_clip_381
type: Text To Image
frequency: 5
level: strong
coverage: 0.5998
common_nodes: [BasicGuider, BlockSparseAttention, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3高速大动态，无劣化抗形变模糊文生视频_2111233041338298369.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107444165738057730.json, 视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107958839365689345.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_381

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3高速大动态，无劣化抗形变模糊文生视频_2111233041338298369.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107191447593246721.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107333167064637441.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107444165738057730.json、视频生成/文生视频/H3全能参考漫剧工作流，文生视频视频生视频图生视频方案_2107958839365689345.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `EmptyImage` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `孤海注释` —— 3/5 个有
- `CreateVideo` —— 1/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `MiniMaxChunkFeedForward` —— 1/5 个有
- `MiniMaxH3SigmaShift` —— 1/5 个有
- `MiniMaxLowVRAMAttention` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `SaveVideo` —— 1/5 个有
- `SplitSigmas` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VRAM_Debug` —— 1/5 个有
- `easy ifElse` —— 1/5 个有
- `布尔孤海` —— 1/5 个有

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
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
