---
name: text_to_image_lora_sampler_clip_93
type: Text To Image
frequency: 9
level: strong
coverage: 0.888667
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LTX2.5导演台工作流｜文生视频图生视频全能生成_2106063537062891522.json, 数字人/数字人/LTX2.5商业级数字人｜口播数字人直出优化版_2095097464675201026.json, 数字人/数字人/LTX2.5商业级数字人｜目前最好的口播数字人直出_2091657124752482306.json, 数字人/数字人/LTX2.5商业级数字人｜目前最好的口播数字人直出_优化版_2094753534322503681.json, 数字人/数字人/商业级数字人之最｜LTX2.5高清数字人生成_2091824539599728641.json, 视频生成/图生视频/LTX2.5导演台图生数字人数字人图生视频生成_2088201956547448834.json, 视频生成/图生视频/剪辑台导演台2.5｜LTX2.5角色设计表演图生视频_2092594475766992898.json, 视频生成/文生视频/LTX2.5导演台工作流｜文生视频图生视频全能生成_2097116077540069378.json, 视频生成/文生视频/LTX2.5导演台文生数字人文生视频生成工作流_2088219152287887361.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/LTX2.5导演台工作流｜文生视频图生视频全能生成_2106063537062891522.json、数字人/数字人/LTX2.5商业级数字人｜口播数字人直出优化版_2095097464675201026.json、数字人/数字人/LTX2.5商业级数字人｜目前最好的口播数字人直出_2091657124752482306.json、数字人/数字人/LTX2.5商业级数字人｜目前最好的口播数字人直出_优化版_2094753534322503681.json、数字人/数字人/商业级数字人之最｜LTX2.5高清数字人生成_2091824539599728641.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXDirector` —— 7/9 个有
- `LTXDirectorCropGuides` —— 7/9 个有
- `LTXDirectorGuide` —— 7/9 个有
- `LTX2_NAG` —— 5/9 个有
- `LTXVDualCFGGuider` —— 5/9 个有
- `LTXVLatentUpsampler` —— 5/9 个有
- `LatentUpscaleModelLoader` —— 5/9 个有
- `LoadVideoUI` —— 5/9 个有
- `ManualSigmas` —— 5/9 个有
- `BasicScheduler` —— 4/9 个有
- `CFGGuider` —— 4/9 个有
- `DiffusionModelLoaderKJ` —— 4/9 个有
- `TTResolutionSelector` —— 4/9 个有
- `VAELoaderKJ` —— 4/9 个有
- `ConditioningZeroOut` —— 2/9 个有
- `GetNode` —— 2/9 个有
- `Label (rgthree)` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `YusuLTXDirector` —— 2/9 个有
- `YusuLTXDirectorCropGuides` —— 2/9 个有
- `YusuLTXDirectorGuide` —— 2/9 个有

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
