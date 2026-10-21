---
name: text_to_image_lora_sampler_clip_215
type: Text To Image
frequency: 6
level: strong
coverage: 0.8775
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/双采去油优化版工作流，图生视频高质量文戏创作方案_2106138649183211522.json, 视频生成/图生视频/双采样高清画质流｜H3图生视频画质增强直出_2092695582556114946.json, 视频生成/图生视频/我自用的H3-w1_2094228023120846849.json, 视频生成/图生视频/视频同款滔博MV工作流，音频驱动图生视频MV生成工具_2103601280408182786.json, 视频生成/文生视频/latent放大双采加速｜MiniMax H3高动态不糊修音频全能_2090837902199709697.json, 视频生成/文生视频/latent放大双采加速｜MiniMax H3高动态不糊修音频全能流_2090657292453769218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_215

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/双采去油优化版工作流，图生视频高质量文戏创作方案_2106138649183211522.json、视频生成/图生视频/双采样高清画质流｜H3图生视频画质增强直出_2092695582556114946.json、视频生成/图生视频/我自用的H3-w1_2094228023120846849.json、视频生成/图生视频/视频同款滔博MV工作流，音频驱动图生视频MV生成工具_2103601280408182786.json、视频生成/文生视频/latent放大双采加速｜MiniMax H3高动态不糊修音频全能_2090837902199709697.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `MiniMaxH3ReferenceToVideo` —— 5/6 个有
- `MiniMaxLowVRAMAttention` —— 5/6 个有
- `SplitSigmas` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `孤海注释` —— 5/6 个有
- `ExtendIntermediateSigmas` —— 4/6 个有
- `LoadAudio` —— 4/6 个有
- `MinimaxH3LatentUpscaler3D` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `H3LatentUpscaleByJingchen573` —— 3/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `SolAttnMiniMax` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/6 个有
- `1hew_AudioDuration` —— 1/6 个有
- `DisableNoise` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `H3SigmaRefiner` —— 1/6 个有
- `LatentUpscale` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxH3AudioConditioningT8` —— 1/6 个有
- `MiniMaxH3SigmaShift` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `Sleep` —— 1/6 个有
- `SplitSigmasDenoise` —— 1/6 个有
- `WujiAudioLoader` —— 1/6 个有
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
