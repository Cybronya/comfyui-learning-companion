---
name: text_to_image_upscale_latent_upscale_lora_10
type: Text To Image
frequency: 6
level: strong
coverage: 0.789333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json, 视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json, 视频生成/图生视频/h3双采样高清流｜图生视频超清画质一键生成_2092887311095783425.json, 视频生成/图生视频/minimax h3二采1080p工作流｜高清图生视频画质增强_2097485061024215042.json, 视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json, 视频生成/图生视频/双采去油优化版工作流，图生视频高质量文戏创作方案_2106138649183211522.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_10

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json、视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json、视频生成/图生视频/h3双采样高清流｜图生视频超清画质一键生成_2092887311095783425.json、视频生成/图生视频/minimax h3二采1080p工作流｜高清图生视频画质增强_2097485061024215042.json、视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `ComfyMathExpression` —— 5/6 个有
- `CreateVideo` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MiniMaxH3SigmaShift` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `MiniMaxLowVRAMAttention` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `H3SigmaRefiner` —— 3/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `LoadAudio` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `CFGGuider` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `DisableNoise` —— 1/6 个有
- `ExtendIntermediateSigmas` —— 1/6 个有
- `FlashVSRNode` —— 1/6 个有
- `H3LatentUpscaleByJingchen573` —— 1/6 个有
- `Int` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `Sleep` —— 1/6 个有
- `SolAttnMiniMax` —— 1/6 个有
- `StringConcatenate` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `VRAM_Debug` —— 1/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/6 个有
- `WujiAudioLoader` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

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
