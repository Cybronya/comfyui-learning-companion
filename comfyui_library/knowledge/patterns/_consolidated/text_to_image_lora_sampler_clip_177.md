---
name: text_to_image_lora_sampler_clip_177
type: Text To Image
frequency: 10
level: strong
coverage: 0.8552
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085422971736383489.json, 视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085791756154654721.json, 视频生成/文生视频/H3官方流程单采极速文戏｜文生视频图生视频快速生成_2106986232776585218.json, 视频生成/文生视频/H3官流mpov版不用加速LoRA工作流，文生视频视频生视频图生视频方案_2107987502211620866.json, 视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107179960334114818.json, 视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107462612324806657.json, 视频生成/文生视频/H3官流终极版 视频生成官方最佳方案稳定出片_2105387723480719362.json, 视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json, 视频生成/文生视频/MiniMax H3单采V2工作流，文生视频视频生视频图生视频方案_2103619711580856322.json, 视频生成/文生视频/MiniMax H3双采工作流，文生视频视频生视频图生视频方案_2103963966656573441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_177

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085422971736383489.json、视频生成/文生视频/H3多参音视频生成开源版（9图3视频3音频）Minimax_2085791756154654721.json、视频生成/文生视频/H3官方流程单采极速文戏｜文生视频图生视频快速生成_2106986232776585218.json、视频生成/文生视频/H3官流mpov版不用加速LoRA工作流，文生视频视频生视频图生视频方案_2107987502211620866.json、视频生成/文生视频/H3官流单采极速文戏工作流，文生视频图生视频高效创作方案_2107179960334114818.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `VHS_LoadVideo` —— 8/10 个有
- `VHS_VideoCombine` —— 8/10 个有
- `BlockSparseAttention` —— 7/10 个有
- `ModelPreviewOverrideKJ` —— 7/10 个有
- `孤海注释` —— 7/10 个有
- `MiniMaxH3SigmaShift` —— 6/10 个有
- `SaveImage` —— 6/10 个有
- `ModelAttentionBackend` —— 5/10 个有
- `ExtendIntermediateSigmas` —— 4/10 个有
- `GetNode` —— 3/10 个有
- `ManualSigmas` —— 3/10 个有
- `PathchSageAttentionKJ` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `CreateVideo` —— 2/10 个有
- `GetVideoComponents` —— 2/10 个有
- `ImageScaleToTotalPixels` —— 2/10 个有
- `LoadVideo` —— 2/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/10 个有
- `PainterVRAM` —— 2/10 个有
- `PreviewAudio` —— 2/10 个有
- `ResizeImageMaskNode` —— 2/10 个有
- `SaveVideo` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `EmptyImage` —— 1/10 个有
- `LTXVConcatAVLatent` —— 1/10 个有
- `LTXVSeparateAVLatent` —— 1/10 个有
- `MinimaxH3LatentUpscaler3D` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `SplitSigmas` —— 1/10 个有
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
