---
name: text_to_image_video_upscale_latent_upscale_10
type: Text To Image
frequency: 7
level: strong
coverage: 0.933857
common_nodes: [BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, CLIPTextEncode, EmptyLatentImage, GoohaiMinimaxH3TiledSampler, H3DistanceAttentionPatcher, JZL_HailuoH3VideoParamsPro, JZL_MiniMaxH3CondSync, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3AudioConditioningT8, MiniMaxH3SemanticBridgeConfigT8, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PlaySound|pysssss, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参二采低显存版｜直出2K高清视频省显存方案_2113508895313453057.json, 视频生成/图生视频/MiniMax-H3 fl2va二采首帧 低显存2K视频直出工具_2114056463613255681.json, 视频生成/图生视频/MiniMax-H3+fl2va二采首尾帧低显存｜2K视频直出版_2114017143107964930.json, 视频生成/图生视频/MiniMax-H3+fl2va二采首帧低显存｜2K视频直出流畅_2114004899871678465.json, 视频生成/图生视频/MiniMax-H3多参二采 低显存直出2K文戏武戏工具_2113698782394273793.json, 视频生成/文生视频/MiniMax-H3 fl2va二采文生视频 低显存2K直出工具_2114101988198801409.json, 视频生成/文生视频/MiniMax-H3+fl2va二采文生视频｜低显存2K直出神器_2113997341488410625.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_10

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参二采低显存版｜直出2K高清视频省显存方案_2113508895313453057.json、视频生成/图生视频/MiniMax-H3 fl2va二采首帧 低显存2K视频直出工具_2114056463613255681.json、视频生成/图生视频/MiniMax-H3+fl2va二采首尾帧低显存｜2K视频直出版_2114017143107964930.json、视频生成/图生视频/MiniMax-H3+fl2va二采首帧低显存｜2K视频直出流畅_2114004899871678465.json、视频生成/图生视频/MiniMax-H3多参二采 低显存直出2K文戏武戏工具_2113698782394273793.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GoohaiMinimaxH3TiledSampler`
- `H3DistanceAttentionPatcher`
- `JZL_HailuoH3VideoParamsPro`
- `JZL_MiniMaxH3CondSync`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3SemanticBridgeConfigT8`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PlaySound|pysssss`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/7 个有
- `GoohaiRatioAndResolution` —— 5/7 个有
- `LoadImage` —— 5/7 个有
- `MiniMaxH3PromptEnhancerT8` —— 5/7 个有
- `StringToInt` —— 5/7 个有
- `SaveImage` —— 3/7 个有
- `JindouyunNumberSlider` —— 2/7 个有
- `ModelPreviewOverrideKJ` —— 2/7 个有
- `Seed (rgthree)` —— 2/7 个有
- `VHS_LoadAudioUpload` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `VRAM_Debug` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
