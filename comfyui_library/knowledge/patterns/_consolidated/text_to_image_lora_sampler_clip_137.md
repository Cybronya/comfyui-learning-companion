---
name: text_to_image_lora_sampler_clip_137
type: Text To Image
frequency: 7
level: strong
coverage: 0.761
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnMiniMax, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4K加二采新condition加同模双采加H3加动态修复 视频生成优化_2108981922180452354.json, 视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json, 视频生成/图生视频/H3潜空间放大工作流｜图生视频画质提升_2090444142102011905.json, 视频生成/图生视频/LMS二采新Condition同模双采语义桥图生视频处理工具_2101405530886598657.json, 视频生成/图生视频/LMS二采新condition测试｜同模双采语义桥实战_2101147756453785601.json, 视频生成/图生视频/MiniMax H3双采潜空间放大图生视频处理工作流_2101380889010855937.json, 视频生成/图生视频/MinimaxH3+LMS同模双采｜语义桥分块采样20s+长视频_2101236735660355585.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_137

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/4K加二采新condition加同模双采加H3加动态修复 视频生成优化_2108981922180452354.json、视频生成/图生视频/H3 sigma强化超清放大｜1080P打斗不糊脸不崩视频_2094933026361921538.json、视频生成/图生视频/H3潜空间放大工作流｜图生视频画质提升_2090444142102011905.json、视频生成/图生视频/LMS二采新Condition同模双采语义桥图生视频处理工具_2101405530886598657.json、视频生成/图生视频/LMS二采新condition测试｜同模双采语义桥实战_2101147756453785601.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/7 个有
- `H3SigmaRefiner` —— 6/7 个有
- `KSamplerSelect` —— 6/7 个有
- `LTXVConcatAVLatent` —— 6/7 个有
- `LTXVSeparateAVLatent` —— 6/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/7 个有
- `SplitSigmas` —— 6/7 个有
- `MiniMaxChunkFeedForward` —— 5/7 个有
- `MiniMaxLowVRAMAttention` —— 5/7 个有
- `MinimaxH3LatentUpscaler3D` —— 5/7 个有
- `CR Prompt Text` —— 4/7 个有
- `ConcatTextOfUtils` —— 4/7 个有
- `CreateVideo` —— 4/7 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/7 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `ShellAgentPluginVideoCombineEncrypt` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `MiniMaxH3TurboLoRA` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `LoadAudio` —— 2/7 个有
- `Astra` —— 1/7 个有
- `Float` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `MiniMaxH3BlockCacheT8` —— 1/7 个有
- `MiniMaxH3ChunkedTwoPassPlanT8Advanced` —— 1/7 个有
- `MiniMaxH3ChunkedTwoPassUpscaleT8Advanced` —— 1/7 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/7 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 1/7 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 1/7 个有
- `MiniMaxH3VAEDecodeFast` —— 1/7 个有
- `MinimaxH3LatentUpscalerNode2D` —— 1/7 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
