---
name: text_to_image_lora_sampler_clip_415
type: Text To Image
frequency: 5
level: strong
coverage: 0.8642
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SigmasToFloat, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全参考三采模式｜MiniMaxH3 sigma强化潜空间放大视频生成_2090215257896738818.json, 视频生成/图生视频/全参考多参专用｜MiniMax H3视频生成工作流_2090224936303554562.json, 视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json, 视频生成/文生视频/MINIMAXH3三采latent放大｜高清无损单次解码零损失_2090058920059555841.json, 视频生成/文生视频/MINIMAXH3三采latent放大｜高速无损单次解码零损失_2089442453534371841.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_415

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/全参考三采模式｜MiniMaxH3 sigma强化潜空间放大视频生成_2090215257896738818.json、视频生成/图生视频/全参考多参专用｜MiniMax H3视频生成工作流_2090224936303554562.json、视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json、视频生成/文生视频/MINIMAXH3三采latent放大｜高清无损单次解码零损失_2090058920059555841.json、视频生成/文生视频/MINIMAXH3三采latent放大｜高速无损单次解码零损失_2089442453534371841.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SigmasToFloat`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `DisableNoise` —— 4/5 个有
- `ExtendIntermediateSigmas` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `easy boolean` —— 4/5 个有
- `LatentUpscaleBy` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `Lora Loader Stack (rgthree)` —— 3/5 个有
- `PixaromaSaveMp4` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `MiniMaxChunkFeedForward` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `ModelAttentionBackend` —— 1/5 个有
- `SolAttnMiniMax` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
