---
name: text_to_image_video_upscale_latent_upscale_16
type: Text To Image
frequency: 5
level: strong
coverage: 0.8946
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: NumberCalculatorV2, LoraLoaderModelOnly, MiniMaxH3AudioLock, MiniMaxH3MediaLoaderFantastic, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MultimodalChat, MiniMaxH3ReferenceSplitter, MiniMaxH3SigmaShift, MiniMaxH3TiledSampler, MiniMaxH3UnifiedToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, VRAM_Debug, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 全能生视频 V4｜文生图生视频四代升级版_2097532242695385090.json, 视频生成/文生视频/MiniMax H3全能生视频V4 Latent分块二采处理工作流_2102113094515380226.json, 视频生成/文生视频/MiniMax H3全能生视频V4工作流，latent分块二采加速方案文图参考三合一_2103526635537522689.json, 视频生成/文生视频/MiniMax-H3全能生视频V4工作流｜文生图生参考生三合一加速_2097396393961943041.json, 视频生成/文生视频/MiniMax-H3全能生视频V4｜latent分块二采｜文生图生参考三合一_2101864233825824769.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 全能生视频 V4｜文生图生视频四代升级版_2097532242695385090.json、视频生成/文生视频/MiniMax H3全能生视频V4 Latent分块二采处理工作流_2102113094515380226.json、视频生成/文生视频/MiniMax H3全能生视频V4工作流，latent分块二采加速方案文图参考三合一_2103526635537522689.json、视频生成/文生视频/MiniMax-H3全能生视频V4工作流｜文生图生参考生三合一加速_2097396393961943041.json、视频生成/文生视频/MiniMax-H3全能生视频V4｜latent分块二采｜文生图生参考三合一_2101864233825824769.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: NumberCalculatorV2`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioLock`
- `MiniMaxH3MediaLoaderFantastic`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MultimodalChat`
- `MiniMaxH3ReferenceSplitter`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3TiledSampler`
- `MiniMaxH3UnifiedToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
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
- `SaveImage` —— 3/5 个有
- `Any Switch (rgthree)` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
