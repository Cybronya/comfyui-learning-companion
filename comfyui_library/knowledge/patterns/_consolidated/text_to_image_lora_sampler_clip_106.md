---
name: text_to_image_lora_sampler_clip_106
type: Text To Image
frequency: 9
level: strong
coverage: 0.86
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全参考三采模式｜MiniMaxH3 sigma强化潜空间放大视频生成_2090215257896738818.json, 视频生成/图生视频/全参考多参专用｜MiniMax H3视频生成工作流_2090224936303554562.json, 视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json, 视频生成/文生视频/MINIMAXH3三采latent放大｜高清无损单次解码零损失_2090058920059555841.json, 视频生成/文生视频/MINIMAXH3三采latent放大｜高速无损单次解码零损失_2089442453534371841.json, 视频生成/文生视频/MiniMax H3 latent放大双采+8步lora｜全能参考顶级质速_2089440965449834498.json, 视频生成/文生视频/MiniMax H3全能参考｜latent放大双采+8步lora质量速度兼得_2089466163435761666.json, 视频生成/文生视频/latent放大双采加速｜MiniMax H3高动态不糊修音频全能_2090837902199709697.json, 视频生成/文生视频/latent放大双采加速｜MiniMax H3高动态不糊修音频全能流_2090657292453769218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_106

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/全参考三采模式｜MiniMaxH3 sigma强化潜空间放大视频生成_2090215257896738818.json、视频生成/图生视频/全参考多参专用｜MiniMax H3视频生成工作流_2090224936303554562.json、视频生成/图生视频/图生视频单图直出｜MiniMax H3 8.20新版模板_2090853514540052482.json、视频生成/文生视频/MINIMAXH3三采latent放大｜高清无损单次解码零损失_2090058920059555841.json、视频生成/文生视频/MINIMAXH3三采latent放大｜高速无损单次解码零损失_2089442453534371841.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
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
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 8/9 个有
- `PrimitiveStringMultiline` —— 8/9 个有
- `LoadAudio` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `DisableNoise` —— 6/9 个有
- `ExtendIntermediateSigmas` —— 6/9 个有
- `PathchSageAttentionKJ` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `LatentUpscaleBy` —— 5/9 个有
- `SigmasToFloat` —— 5/9 个有
- `easy cleanGpuUsed` —— 5/9 个有
- `ComfySwitchNode` —— 4/9 个有
- `H3LatentUpscaleByJingchen573` —— 4/9 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/9 个有
- `ShowText|pysssss` —— 4/9 个有
- `easy boolean` —— 4/9 个有
- `easy showAnything` —— 4/9 个有
- `Lora Loader Stack (rgthree)` —— 3/9 个有
- `ModelAttentionBackend` —— 3/9 个有
- `PixaromaSaveMp4` —— 3/9 个有
- `SolAttnMiniMax` —— 3/9 个有
- `GetImageRangeFromBatch` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `MathExpression|pysssss` —— 2/9 个有
- `MiniMaxChunkFeedForward` —— 2/9 个有
- `MiniMaxH3HybridLoader` —— 2/9 个有
- `MiniMaxH3SigmaShift` —— 2/9 个有
- `MiniMaxLowVRAMAttention` —— 2/9 个有
- `ModelPatchTorchSettings` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `SaveImage` —— 1/9 个有

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
