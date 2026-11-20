---
name: text_to_image_lora_sampler_clip_432
type: Text To Image
frequency: 5
level: strong
coverage: 0.6518
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax R2V多参考图生视频 参考音频视频混合生成处理工具_2112964584029118465.json, 视频生成/图生视频/MiniMax h3开源加速版 海螺多参文生视频图生视频音频参考_2085303974785273857.json, 视频生成/图生视频/MiniMax多参考生成视频R2V图生视频处理工具_2102478493312442370.json, 视频生成/图生视频/MiniMax视频续写多帧插入 latent保存图生视频处理工具_2112962732864659458.json, 视频生成/图生视频/Minimax多帧插入视频续写，视频生视频拉长片段神器_2110489536747884545.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_432

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax R2V多参考图生视频 参考音频视频混合生成处理工具_2112964584029118465.json、视频生成/图生视频/MiniMax h3开源加速版 海螺多参文生视频图生视频音频参考_2085303974785273857.json、视频生成/图生视频/MiniMax多参考生成视频R2V图生视频处理工具_2102478493312442370.json、视频生成/图生视频/MiniMax视频续写多帧插入 latent保存图生视频处理工具_2112962732864659458.json、视频生成/图生视频/Minimax多帧插入视频续写，视频生视频拉长片段神器_2110489536747884545.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `GetNode`
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
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `AudioConcat` —— 3/5 个有
- `TrimAudioDuration` —— 3/5 个有
- `easy minimaxH3AudioLock` —— 3/5 个有
- `AudioInfo` —— 2/5 个有
- `ColorMatchV2` —— 2/5 个有
- `EmptyAudio` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `Image Batch` —— 2/5 个有
- `ImageAddNoise` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `ImageScale` —— 2/5 个有
- `MiniMaxH3AddGuide` —— 2/5 个有
- `MiniMaxH3SaveLatent` —— 2/5 个有
- `MiniMaxH3SigmaShift` —— 2/5 个有
- `ModelAttentionBackend` —— 2/5 个有
- `AnyIsEmpty` —— 1/5 个有
- `AudioCrop` —— 1/5 个有
- `Float` —— 1/5 个有
- `Int` —— 1/5 个有
- `LLAIDownloadVideo` —— 1/5 个有
- `MiniMaxH3LoadLatent` —— 1/5 个有
- `MiniMaxH3LoopTrim` —— 1/5 个有
- `MiniMaxH3VideoExtender` —— 1/5 个有
- `MiniMaxH3VideoMerge` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `ShowAnything|Mie` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有

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
