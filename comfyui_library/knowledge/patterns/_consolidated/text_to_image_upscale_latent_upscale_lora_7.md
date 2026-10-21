---
name: text_to_image_upscale_latent_upscale_lora_7
type: Text To Image
frequency: 7
level: strong
coverage: 0.752714
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json, 视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json, 视频生成/图生视频/h3双采样高清流｜图生视频超清画质一键生成_2092887311095783425.json, 视频生成/图生视频/minimax h3二采1080p工作流｜高清图生视频画质增强_2097485061024215042.json, 视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json, 视频生成/图生视频/双模双采小脸不崩｜Minimax H3高动态不崩脸视频_2093486007596437506.json, 视频生成/图生视频/双模双采资源面板短剧助手 MiniMax H3 全能参考生成视频_2094255084355022849.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3图生视频双采，CFG0.5配SAGE加速优化_2110852313752625153.json、视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json、视频生成/图生视频/h3双采样高清流｜图生视频超清画质一键生成_2092887311095783425.json、视频生成/图生视频/minimax h3二采1080p工作流｜高清图生视频画质增强_2097485061024215042.json、视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
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
- `MiniMaxH3SigmaShift`
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
- `BasicGuider` —— 6/7 个有
- `ComfyMathExpression` —— 6/7 个有
- `CreateVideo` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `GetNode` —— 5/7 个有
- `H3SigmaRefiner` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/7 个有
- `MiniMaxLowVRAMAttention` —— 5/7 个有
- `ModelAttentionBackend` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `SaveImage` —— 4/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `ModelPreviewOverrideKJ` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `Anything Everywhere3` —— 1/7 个有
- `CFGGuider` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `DF_Integer` —— 1/7 个有
- `DisableNoise` —— 1/7 个有
- `FlashVSRNode` —— 1/7 个有
- `Int` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/7 个有
- `MiniMaxH3ReferenceSplitter` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `Sleep` —— 1/7 个有
- `StringConcatenate` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有
- `VRAM_Debug` —— 1/7 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/7 个有

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
