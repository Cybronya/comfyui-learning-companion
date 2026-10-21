---
name: text_to_image_lora_sampler_clip_213
type: Text To Image
frequency: 6
level: strong
coverage: 0.714667
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3极速多参视频制作 多模态输入高效生成_2108989902074499074.json, 视频生成/图生视频/MiniMax_H3极速多参视频制作工作流，文生视频视频生视频图生视频_2109450817471344642.json, 视频生成/图生视频/Minimax H3加速双采self-lift流｜两次采样提质量，速度还不打折_2099494675802583042.json, 视频生成/图生视频/Minimax H3加速双采｜self-lift工作流高效出片_2101155630626201602.json, 视频生成/文生视频/7分钟内生成H3视频工作流，免费每天使用文生视频图生视频方案_2103889611805257730.json, 视频生成/文生视频/MiniMax H3极速多参视频制作工作流，文生视频视频生视频图生视频_2107193111117131778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_213

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3极速多参视频制作 多模态输入高效生成_2108989902074499074.json、视频生成/图生视频/MiniMax_H3极速多参视频制作工作流，文生视频视频生视频图生视频_2109450817471344642.json、视频生成/图生视频/Minimax H3加速双采self-lift流｜两次采样提质量，速度还不打折_2099494675802583042.json、视频生成/图生视频/Minimax H3加速双采｜self-lift工作流高效出片_2101155630626201602.json、视频生成/文生视频/7分钟内生成H3视频工作流，免费每天使用文生视频图生视频方案_2103889611805257730.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 5/6 个有
- `SelfLiftH3Sampler` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/6 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `VHS_LoadVideo` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `LTXVSeparateAVLatent` —— 3/6 个有
- `MiniMaxH3VAEDecodeFast` —— 3/6 个有
- `RunningHub Deepcleaner` —— 3/6 个有
- `VHS_VideoInfoLoaded` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `Float` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `MemoryManager` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RH_IndexTTS25_Loader` —— 1/6 个有
- `RH_IndexTTS25_Synthesize` —— 1/6 个有
- `ResizeShortestToNode` —— 1/6 个有
- `SelfLiftAvatarH3Sampler` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
