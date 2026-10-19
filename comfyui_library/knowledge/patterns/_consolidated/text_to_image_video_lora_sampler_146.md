---
name: text_to_image_video_lora_sampler_146
type: Text To Image
frequency: 4
level: strong
coverage: 0.616
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxH3SemanticBridgeApplyT8, MiniMaxH3SemanticBridgeConfigT8, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3极速多参视频制作 多模态输入高效生成_2108989902074499074.json, 视频生成/图生视频/MiniMax_H3极速多参视频制作工作流，文生视频视频生视频图生视频_2109450817471344642.json, 视频生成/文生视频/7分钟内生成H3视频工作流，免费每天使用文生视频图生视频方案_2103889611805257730.json, 视频生成/文生视频/MiniMax H3极速多参视频制作工作流，文生视频视频生视频图生视频_2107193111117131778.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_146

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3极速多参视频制作 多模态输入高效生成_2108989902074499074.json、视频生成/图生视频/MiniMax_H3极速多参视频制作工作流，文生视频视频生视频图生视频_2109450817471344642.json、视频生成/文生视频/7分钟内生成H3视频工作流，免费每天使用文生视频图生视频方案_2103889611805257730.json、视频生成/文生视频/MiniMax H3极速多参视频制作工作流，文生视频视频生视频图生视频_2107193111117131778.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SemanticBridgeApplyT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LTXVSeparateAVLatent` —— 3/4 个有
- `MiniMaxH3VAEDecodeFast` —— 3/4 个有
- `RunningHub Deepcleaner` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `SelfLiftH3Sampler` —— 3/4 个有
- `VHS_VideoInfoLoaded` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `Float` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `MemoryManager` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `RH_IndexTTS25_Loader` —— 1/4 个有
- `RH_IndexTTS25_Synthesize` —— 1/4 个有
- `ResizeShortestToNode` —— 1/4 个有
- `SelfLiftAvatarH3Sampler` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

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
