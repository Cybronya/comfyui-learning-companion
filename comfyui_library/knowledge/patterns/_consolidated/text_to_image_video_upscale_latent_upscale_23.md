---
name: text_to_image_video_upscale_latent_upscale_23
type: Text To Image
frequency: 3
level: strong
coverage: 0.664
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, DisableNoise, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 Singularity最强工作流 音频驱动生成工具_2114086817615138818.json, 视频生成/图生视频/Minimax H3三采最强工作流，视频无缝续接长片分段创作不断层_2114562167302352897.json, 视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_23

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 Singularity最强工作流 音频驱动生成工具_2114086817615138818.json、视频生成/图生视频/Minimax H3三采最强工作流，视频无缝续接长片分段创作不断层_2114562167302352897.json、视频生成/图生视频/MinimaxH3高动态Singularity新分段采样进阶工作流 视频生成优化_2105351940963131393.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DisableNoise`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 2/3 个有
- `ExtendIntermediateSigmas` —— 2/3 个有
- `GoohaiUniversalSlider` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LoadAudioUI` —— 2/3 个有
- `LoadVideoUI` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `ModelPreviewOverrideKJ` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `VAEDecodeAudio` —— 2/3 个有
- `easy float` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `MiniMaxH3MotionContext` —— 1/3 个有
- `MiniMaxH3MotionContextTrim` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
