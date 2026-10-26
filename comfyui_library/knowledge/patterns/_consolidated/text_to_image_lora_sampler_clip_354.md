---
name: text_to_image_lora_sampler_clip_354
type: Text To Image
frequency: 6
level: strong
coverage: 0.719833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json, 视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json, 视频生成/图生视频/H3长视频衔接尾帧22帧锚点 视频生成连贯性优化_2109025859695890434.json, 视频生成/图生视频/H3长视频音频驱动数字人唱歌30秒1分钟切换_2099933503063412738.json, 视频生成/图生视频/MinimaxH3全自动长视频数字人工作流｜图生视频一站式出片_2101897607634317313.json, 视频生成/图生视频/数字人对口型生成｜H3视频生视频图生视频直出_2092730251368558593.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_354

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/H3数字人对口型｜视频生视频图生视频生成_2092934748694990850.json、视频生成/图生视频/H3质变音频驱动数字人｜全能参考升级版｜精准可控说话表演_2104819764299386881.json、视频生成/图生视频/H3长视频衔接尾帧22帧锚点 视频生成连贯性优化_2109025859695890434.json、视频生成/图生视频/H3长视频音频驱动数字人唱歌30秒1分钟切换_2099933503063412738.json、视频生成/图生视频/MinimaxH3全自动长视频数字人工作流｜图生视频一站式出片_2101897607634317313.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 5/6 个有
- `TrimAudioDuration` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `ModelPreviewOverrideKJ` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `MiniMaxH3AddGuide` —— 3/6 个有
- `PrimitiveFloat` —— 3/6 个有
- `SoundFlow_GetLength` —— 3/6 个有
- `AudioConcat` —— 2/6 个有
- `GetImageRangeFromBatch` —— 2/6 个有
- `PreviewAudio` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `ShowAnything|Mie` —— 2/6 个有
- `VAEDecodeAudio` —— 2/6 个有
- `AudioCrop` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `ExtendIntermediateSigmas` —— 1/6 个有
- `Float` —— 1/6 个有
- `ImageBatch` —— 1/6 个有
- `ImageBatchMulti` —— 1/6 个有
- `MiniMaxChunkFeedForward` —— 1/6 个有
- `MiniMaxLowVRAMAttention` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `SelectImages` —— 1/6 个有
- `VHS_LoadVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
