---
name: text_to_image_video_upscale_latent_upscale_27
type: Text To Image
frequency: 2
level: weak
coverage: 0.8495
common_nodes: [AudioCrop, CFGGuider, CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, DualCLIPLoader, EmptyLTXVLatentVideo, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TTResolutionSelector, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/数字人LTX2.3-kj版-快速配音_2082252252718391297.json, 视频生成/图生视频/LTX2.3数字人口播长视频稳定版｜图生视频加速加持｜口播内容稳定产出_2102625263141089282.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/数字人LTX2.3-kj版-快速配音_2082252252718391297.json、视频生成/图生视频/LTX2.3数字人口播长视频稳定版｜图生视频加速加持｜口播内容稳定产出_2102625263141089282.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `1hew_AudioDuration` —— 1/2 个有
- `Audio Duration (mtb)` —— 1/2 个有
- `AudioSeparation` —— 1/2 个有
- `Bool` —— 1/2 个有
- `Float` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWString` —— 1/2 个有
- `LTXVAudioVAEDecode` —— 1/2 个有
- `LTXVChunkFeedForward` —— 1/2 个有
- `LTXVPreprocess` —— 1/2 个有
- `LTXVScheduler` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy float` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy setNode` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
