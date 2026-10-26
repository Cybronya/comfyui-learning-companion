---
name: text_to_image_lora_sampler_clip_188
type: Text To Image
frequency: 10
level: strong
coverage: 0.7651
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3官方长视频续接｜图生视频无缝延长生成_2095203720807145474.json, 视频生成/图生视频/Kitchen Attention图生视频 600步EMA模型工具_2114139959656538113.json, 视频生成/图生视频/MiniMax H3全能参考三图版｜三图输入视频生成_2094516324448948226.json, 视频生成/图生视频/MiniMax H3全能参考双图版｜双图输入视频生成_2094519227574218754.json, 视频生成/图生视频/MiniMax H3全能参考四图版｜多图输入视频生成_2094508021375397889.json, 视频生成/图生视频/MiniMax H3参考生视频 官方全能多模态创作工具_2098824046145269762.json, 视频生成/图生视频/MiniMax H3多图参考｜图生视频多图生成_2090449654759645186.json, 视频生成/图生视频/MiniMax R2V多参考图生视频 参考音频视频混合生成处理工具_2112964584029118465.json, 视频生成/图生视频/MiniMax视频续写多帧插入 latent保存图生视频处理工具_2112962732864659458.json, 视频生成/图生视频/Minimax多帧插入视频续写，视频生视频拉长片段神器_2110489536747884545.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_188

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/H3官方长视频续接｜图生视频无缝延长生成_2095203720807145474.json、视频生成/图生视频/Kitchen Attention图生视频 600步EMA模型工具_2114139959656538113.json、视频生成/图生视频/MiniMax H3全能参考三图版｜三图输入视频生成_2094516324448948226.json、视频生成/图生视频/MiniMax H3全能参考双图版｜双图输入视频生成_2094519227574218754.json、视频生成/图生视频/MiniMax H3全能参考四图版｜多图输入视频生成_2094508021375397889.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `PrimitiveInt` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `SaveImage` —— 5/10 个有
- `VHS_LoadVideo` —— 5/10 个有
- `TrimAudioDuration` —— 4/10 个有
- `AudioConcat` —— 3/10 个有
- `GetImageRangeFromBatch` —— 3/10 个有
- `GetNode` —— 3/10 个有
- `ImageAddNoise` —— 3/10 个有
- `MiniMaxH3AddGuide` —— 3/10 个有
- `ModelAttentionBackend` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `easy minimaxH3AudioLock` —— 3/10 个有
- `AudioInfo` —— 2/10 个有
- `ColorMatchV2` —— 2/10 个有
- `EmptyAudio` —— 2/10 个有
- `ExtendIntermediateSigmas` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `Image Batch` —— 2/10 个有
- `ImageFromBatch` —— 2/10 个有
- `ImageScale` —— 2/10 个有
- `MiniMaxH3SaveLatent` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `AnyIsEmpty` —— 1/10 个有
- `AudioCrop` —— 1/10 个有
- `Fast Bypasser (rgthree)` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `Float` —— 1/10 个有
- `Int` —— 1/10 个有
- `LLAIDownloadVideo` —— 1/10 个有
- `MiniMaxH3LoadLatent` —— 1/10 个有
- `MiniMaxH3LoopTrim` —— 1/10 个有
- `MiniMaxH3TurboLoRA` —— 1/10 个有
- `MiniMaxH3VideoExtender` —— 1/10 个有
- `MiniMaxH3VideoMerge` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `ShowAnything|Mie` —— 1/10 个有
- `VHS_VideoInfo` —— 1/10 个有
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
