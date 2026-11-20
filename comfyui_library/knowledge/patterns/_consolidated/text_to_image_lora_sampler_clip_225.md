---
name: text_to_image_lora_sampler_clip_225
type: Text To Image
frequency: 9
level: strong
coverage: 0.862222
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetVideoComponents, ImageConcatMulti, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3BlockCacheT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VRAM_Debug, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3动作迁移图生视频 二采放大高清视频输出工作流_2094358912484073473.json, 视频生成/图生视频/ref turbo加速图生视频动作模仿｜MiniMax-H3动作迁移视频生视频_2088380985703485441.json, 视频生成/图生视频/动作模仿ref turbo加速MiniMax H3图生视频动作迁移工作流_2088402060675997697.json, 视频生成/图生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2094024779476062210.json, 视频生成/图生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2097104058355113986.json, 视频生成/图生视频/多参格斗动作迁移背景替换｜MiniMax-H3开源8步加速_2093774376658366465.json, 视频生成/图生视频/多参格斗动作迁移背景替换｜MiniMax-H3开源8步加速_2094009514365374466.json, 视频生成/图生视频/格斗动作迁移背景替换8步加速 MiniMax-H3多参数图生视频方案_2093216713595768833.json, 视频生成/视频生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2106163123605561346.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_225

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3动作迁移图生视频 二采放大高清视频输出工作流_2094358912484073473.json、视频生成/图生视频/ref turbo加速图生视频动作模仿｜MiniMax-H3动作迁移视频生视频_2088380985703485441.json、视频生成/图生视频/动作模仿ref turbo加速MiniMax H3图生视频动作迁移工作流_2088402060675997697.json、视频生成/图生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2094024779476062210.json、视频生成/图生视频/多参格斗动作迁移背景替换8步加速 MiniMax-H3开源版视频生视频_2097104058355113986.json…）

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
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetVideoComponents`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VRAM_Debug`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `ComfyMathExpression` —— 6/9 个有
- `GetImageRangeFromBatch` —— 6/9 个有
- `Int` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `RMBG` —— 6/9 个有
- `VHS_GetImageCount` —— 6/9 个有
- `VHS_LoadVideo` —— 6/9 个有
- `ComfySwitchNode` —— 3/9 个有
- `LoadAudio` —— 3/9 个有
- `LoadVideo` —— 3/9 个有
- `PixaromaDuration` —— 3/9 个有
- `PixaromaSizes` —— 3/9 个有
- `TrimAudioDuration` —— 3/9 个有
- `Video Slice` —— 3/9 个有
- `LTXVConcatAVLatent` —— 1/9 个有
- `LTXVSeparateAVLatent` —— 1/9 个有
- `ManualSigmas` —— 1/9 个有
- `MinimaxH3LatentUpscaler3D` —— 1/9 个有
- `ModelPreviewOverrideKJ` —— 1/9 个有

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
