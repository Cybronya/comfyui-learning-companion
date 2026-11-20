---
name: text_to_image_lora_sampler_clip_230
type: Text To Image
frequency: 9
level: strong
coverage: 0.666444
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/7分钟内生成H3视频工作流，免费每天使用文生视频图生视频方案_2103889611805257730.json, 视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json, 视频生成/文生视频/MiniMax H3极速多参视频制作处理生成工具_2101733080221437954.json, 视频生成/文生视频/MiniMax H3极速多参视频制作工作流，文生视频视频生视频图生视频_2107193111117131778.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103244727301795842.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103523327053750273.json, 视频生成/文生视频/MiniMaxH3极速多参视频制作｜文生视频视频生视频图生视频全能_2105547979712192514.json, 视频生成/文生视频/MiniMaxH3极速多参视频｜文生视频图生视频双模式制作_2101561342628028417.json, 视频生成/视频生视频/MiniMax H3极速多参视频制作，文生视频视频生视频图生视频高效方案_2105732529880920065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_230

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/7分钟内生成H3视频工作流，免费每天使用文生视频图生视频方案_2103889611805257730.json、视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json、视频生成/文生视频/MiniMax H3极速多参视频制作处理生成工具_2101733080221437954.json、视频生成/文生视频/MiniMax H3极速多参视频制作工作流，文生视频视频生视频图生视频_2107193111117131778.json、视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103244727301795842.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 9 个 workflow 都包含：
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
- `LoadAudio`
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
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 8/9 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 7/9 个有
- `SaveImage` —— 7/9 个有
- `VHS_LoadVideo` —— 6/9 个有
- `VHS_VideoInfoLoaded` —— 5/9 个有
- `easy showAnything` —— 5/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `LTXVSeparateAVLatent` —— 3/9 个有
- `MiniMaxH3VAEDecodeFast` —— 3/9 个有
- `RunningHub Deepcleaner` —— 3/9 个有
- `Float` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `MemoryManager` —— 1/9 个有
- `PreviewAudio` —— 1/9 个有
- `RH_IndexTTS25_Loader` —— 1/9 个有
- `RH_IndexTTS25_Synthesize` —— 1/9 个有
- `ResizeShortestToNode` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
