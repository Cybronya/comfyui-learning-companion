---
name: text_to_image_video_upscale_latent_upscale_21
type: Text To Image
frequency: 3
level: strong
coverage: 0.661667
common_nodes: [ApplyFaceProcessor, AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EasyCache, EmptyLatentImage, FaceProcessorLoader, GetNode, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PathchSageAttentionKJ, PreviewImage, PrimitiveString, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SeedVR2, SeedVR2BlockSwap, SetNode, SoundFlow_GetLength, SplitSigmas, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, easy float, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/shuzirenzhufu数字人祝福｜口播祝福视频自动生成_2103102956919939074.json, 视频生成/文生视频/参考音视频数字人｜MiniMax H3图生视频生成_2094475690098909186.json, 视频生成/文生视频/视频参考编辑替换｜MiniMax H3三模视频工作流_2094365213192712193.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/shuzirenzhufu数字人祝福｜口播祝福视频自动生成_2103102956919939074.json、视频生成/文生视频/参考音视频数字人｜MiniMax H3图生视频生成_2094475690098909186.json、视频生成/文生视频/视频参考编辑替换｜MiniMax H3三模视频工作流_2094365213192712193.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFaceProcessor`
- `AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EasyCache`
- `EmptyLatentImage`
- `FaceProcessorLoader`
- `GetNode`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveString`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `SoundFlow_GetLength`
- `SplitSigmas`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `easy float`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `ZML_MergeText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
