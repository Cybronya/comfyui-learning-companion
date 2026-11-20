---
name: text_to_image_lora_sampler_clip_186
type: Text To Image
frequency: 10
level: strong
coverage: 0.8653
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json, 视频生成/图生视频/Minimax H3参考生视频电商带货8步加速版工作流，服装展示图生视频方案_2108285549428699137.json, 视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json, 视频生成/图生视频/Minimax H3多参生视频sag backend block cache 2倍速加速版_2088271045022277634.json, 视频生成/图生视频/Minimax H3多图参考视频流｜全节点中文注释齐全，新手也能看懂_2099470227150032898.json, 视频生成/图生视频/Minimax H3电商带货参考生视频 8步加速版服装展示_2110352251444355074.json, 视频生成/图生视频/h3双采样高清流｜图生视频超清画质一键生成_2092887311095783425.json, 视频生成/图生视频/minimax h3二采1080p工作流｜高清图生视频画质增强_2097485061024215042.json, 视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json, 视频生成/图生视频/双采去油优化版工作流，图生视频高质量文戏创作方案_2106138649183211522.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_186

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json、视频生成/图生视频/Minimax H3参考生视频电商带货8步加速版工作流，服装展示图生视频方案_2108285549428699137.json、视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json、视频生成/图生视频/Minimax H3多参生视频sag backend block cache 2倍速加速版_2088271045022277634.json、视频生成/图生视频/Minimax H3多图参考视频流｜全节点中文注释齐全，新手也能看懂_2099470227150032898.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 9/10 个有
- `ComfyMathExpression` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `SaveImage` —— 6/10 个有
- `LTXVConcatAVLatent` —— 5/10 个有
- `LTXVSeparateAVLatent` —— 5/10 个有
- `MinimaxH3LatentUpscaler3D` —— 5/10 个有
- `ModelAttentionBackend` —— 5/10 个有
- `PathchSageAttentionKJ` —— 5/10 个有
- `SplitSigmas` —— 5/10 个有
- `LoadAudio` —— 4/10 个有
- `MiniMaxH3SigmaShift` —— 4/10 个有
- `MiniMaxLowVRAMAttention` —— 4/10 个有
- `H3SigmaRefiner` —— 3/10 个有
- `GetNode` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `CFGGuider` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `EasyCache` —— 1/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `FlashVSRNode` —— 1/10 个有
- `H3LatentUpscaleByJingchen573` —— 1/10 个有
- `Int` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `ShowText|pysssss` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `Sleep` —— 1/10 个有
- `SolAttnMiniMax` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有
- `VRAM_Debug` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有
- `WujiAudioLoader` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
