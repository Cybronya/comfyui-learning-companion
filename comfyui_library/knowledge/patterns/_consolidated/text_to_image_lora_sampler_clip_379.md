---
name: text_to_image_lora_sampler_clip_379
type: Text To Image
frequency: 5
level: strong
coverage: 0.9308
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3BlockCacheT8, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, ResolutionSelector, SaveVideo, SelfLiftAvatarH3Sampler, SetLatentNoiseMask, SolidMask, SoundFlow_GetLength, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3无限时长极速音频驱动数字人 长视频口播方案_2108997643908243457.json, 视频生成/图生视频/MiniMax H3无限时长极速音频驱动数字人，一张图一段音频生成口播视频_2106835559971901442.json, 视频生成/图生视频/MiniMax H3极速音频驱动数字人图生视频处理工具_2101747277764317185.json, 视频生成/图生视频/MiniMax H3音频驱动数字人｜无限时长极速出片_2106641111426097153.json, 视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人，一张图一段音频生成口播视频_2110540152014729218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_379

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3无限时长极速音频驱动数字人 长视频口播方案_2108997643908243457.json、视频生成/图生视频/MiniMax H3无限时长极速音频驱动数字人，一张图一段音频生成口播视频_2106835559971901442.json、视频生成/图生视频/MiniMax H3极速音频驱动数字人图生视频处理工具_2101747277764317185.json、视频生成/图生视频/MiniMax H3音频驱动数字人｜无限时长极速出片_2106641111426097153.json、视频生成/图生视频/MiniMax_H3无限时长极速音频驱动数字人，一张图一段音频生成口播视频_2110540152014729218.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3BlockCacheT8`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftAvatarH3Sampler`
- `SetLatentNoiseMask`
- `SolidMask`
- `SoundFlow_GetLength`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 4/5 个有
- `BatchImagesNode` —— 4/5 个有
- `ComfySwitchNode` —— 4/5 个有
- `Float` —— 4/5 个有
- `GetImageRangeFromBatch` —— 4/5 个有
- `Int` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `TrimAudioDuration` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `easy compare` —— 4/5 个有
- `easy forLoopEnd` —— 4/5 个有
- `easy forLoopStart` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `RIFE VFI` —— 3/5 个有
- `AuKAudioTrim` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

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
