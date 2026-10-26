---
name: text_to_image_video_lora_sampler_91
type: Text To Image
frequency: 9
level: strong
coverage: 0.707222
common_nodes: [BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MediaLoaderFantastic, MiniMaxH3MultimodalChat, MiniMaxH3ReferenceSplitter, MiniMaxH3SigmaShift, MiniMaxH3UnifiedToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, ShowText|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, VRAM_Debug, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3全能生视频V5二采进阶｜latent分块采样直出高画质视频工作流_2113439401262010369.json, 视频生成/图生视频/MiniMax H3全能生视频V5单采版｜2K直出高效文生图生视频三合一工作流_2113436913909723138.json, 视频生成/图生视频/MiniMax-H3全能生视频V5 latent分块二采视频处理工具_2113685904308137985.json, 视频生成/图生视频/MiniMax-H3全能生视频V5 单采2K直出三合一处理工具_2113683958109130753.json, 视频生成/文生视频/MiniMax H3 全能生视频 V4｜文生图生视频四代升级版_2097532242695385090.json, 视频生成/文生视频/MiniMax H3全能生视频V4 Latent分块二采处理工作流_2102113094515380226.json, 视频生成/文生视频/MiniMax H3全能生视频V4工作流，latent分块二采加速方案文图参考三合一_2103526635537522689.json, 视频生成/文生视频/MiniMax-H3全能生视频V4工作流｜文生图生参考生三合一加速_2097396393961943041.json, 视频生成/文生视频/MiniMax-H3全能生视频V4｜latent分块二采｜文生图生参考三合一_2101864233825824769.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_91

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全能生视频V5二采进阶｜latent分块采样直出高画质视频工作流_2113439401262010369.json、视频生成/图生视频/MiniMax H3全能生视频V5单采版｜2K直出高效文生图生视频三合一工作流_2113436913909723138.json、视频生成/图生视频/MiniMax-H3全能生视频V5 latent分块二采视频处理工具_2113685904308137985.json、视频生成/图生视频/MiniMax-H3全能生视频V5 单采2K直出三合一处理工具_2113683958109130753.json、视频生成/文生视频/MiniMax H3 全能生视频 V4｜文生图生视频四代升级版_2097532242695385090.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MediaLoaderFantastic`
- `MiniMaxH3MultimodalChat`
- `MiniMaxH3ReferenceSplitter`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3UnifiedToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 7/9 个有
- `LTXVConcatAVLatent` —— 7/9 个有
- `LTXVSeparateAVLatent` —— 7/9 个有
- `MiniMaxH3TiledSampler` —— 7/9 个有
- `MinimaxH3LatentUpscaler3D` —— 7/9 个有
- `RandomNoise` —— 7/9 个有
- `SamplerCustomAdvanced` —— 7/9 个有
- `Any Switch (rgthree)` —— 6/9 个有
- `ComfySwitchNode` —— 5/9 个有
- `LayerUtility: NumberCalculatorV2` —— 5/9 个有
- `MiniMaxH3AudioLock` —— 5/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/9 个有
- `SaveImage` —— 5/9 个有
- `ComfyMathExpression` —— 4/9 个有
- `GetNode` —— 4/9 个有
- `GoohaiUniversalSlider` —— 4/9 个有
- `MiniMaxChunkFeedForward` —— 4/9 个有
- `MiniMaxH3AudioSelect` —— 4/9 个有
- `MiniMaxH3SparkAttentionSM89` —— 4/9 个有
- `RTXVideoFrameGeneration` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `ConditioningZeroOut` —— 2/9 个有
- `MiniMaxH3SigmaRefiner` —— 2/9 个有
- `SelfLiftAvatarH3Sampler` —— 2/9 个有
- `ManualSigmas` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
