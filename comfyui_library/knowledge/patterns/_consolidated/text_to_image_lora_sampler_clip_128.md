---
name: text_to_image_lora_sampler_clip_128
type: Text To Image
frequency: 9
level: strong
coverage: 0.654556
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多参生视频10秒直出｜Minimax二采768P升1080P高清_2090146522963992578.json, 视频生成/图生视频/多参考图生视频｜MiniMax H3一键生成直出_2091663599461814274.json, 视频生成/图生视频/完美解决脸部崩坏｜MiniMax H3电影级人物特效图生视频_2090145072644976641.json, 视频生成/图生视频/小脸不崩动态不糊人物不油｜H3开源双模双采短剧漫剧图生视频_2092028224422371330.json, 视频生成/图生视频/小脸不崩漫剧必备｜Minimax H3双采样sigma强化图生视频_2090216685751066626.json, 视频生成/图生视频/强化二采放大工作流｜MiniMax H3自然去油画质提升_2096318365974491138.json, 视频生成/图生视频/极速图生视频 MinimaxH3 人物场景特效快速生成_2094196531091034114.json, 视频生成/图生视频/海螺智能提示词双采样｜minimaxH3加速高清放大图生视频_2093734526240518145.json, 视频生成/文生视频/StarAI海螺MiniMaxH3智能提示词优化｜四步加速双采样高清放大文生视频_2090090942878535681.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/多参生视频10秒直出｜Minimax二采768P升1080P高清_2090146522963992578.json、视频生成/图生视频/多参考图生视频｜MiniMax H3一键生成直出_2091663599461814274.json、视频生成/图生视频/完美解决脸部崩坏｜MiniMax H3电影级人物特效图生视频_2090145072644976641.json、视频生成/图生视频/小脸不崩动态不糊人物不油｜H3开源双模双采短剧漫剧图生视频_2092028224422371330.json、视频生成/图生视频/小脸不崩漫剧必备｜Minimax H3双采样sigma强化图生视频_2090216685751066626.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 7/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `SolAttnMiniMax` —— 6/9 个有
- `CreateVideo` —— 5/9 个有
- `MinimaxH3LatentUpscaler3D` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `CR Text` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 2/9 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 2/9 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 2/9 个有
- `PathchSageAttentionKJ` —— 2/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `StariAI-MiniMaxH3-Skill` —— 2/9 个有
- `GetVideoComponents` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `LoraLoaderBypassModelOnly` —— 1/9 个有
- `MiniMaxH3BlockCacheT8` —— 1/9 个有
- `MiniMaxH3HybridLoader` —— 1/9 个有
- `MiniMaxH3TurboLoRA` —— 1/9 个有
- `MiniMaxH3VRAMPolicyT8Advanced` —— 1/9 个有
- `MiniMaxLowVRAMAttention` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

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
