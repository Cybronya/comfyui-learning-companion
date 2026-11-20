---
name: text_to_image_lora_sampler_clip_222
type: Text To Image
frequency: 9
level: strong
coverage: 0.719111
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3官方长视频续接｜图生视频无缝延长生成_2095203720807145474.json, 视频生成/图生视频/H3长视频音频驱动数字人唱歌30秒1分钟切换_2099933503063412738.json, 视频生成/图生视频/MiniMax H3单采工作流，文生视频图生视频轻量简洁快速上手_2114479769403346945.json, 视频生成/图生视频/MiniMax_H3单采工作流，文生视频图生视频轻量简洁快速上手_2116822096780292097.json, 视频生成/图生视频/官方长视频续接无缝｜H3图生视频接续工作流_2095480320987582466.json, 视频生成/文生视频/MiniMax H3单采V2工作流，文生视频视频生视频图生视频方案_2103619711580856322.json, 视频生成/文生视频/MiniMax H3双采工作流，文生视频视频生视频图生视频方案_2103963966656573441.json, 视频生成/文生视频/minimax-H3 官方版去油提质｜长视频续接无限延长手动版_2096903551057481730.json, 视频生成/文生视频/去油提画质长视频续接｜MiniMax H3官方版无限延长手动生成_2096782492383666177.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_222

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/H3官方长视频续接｜图生视频无缝延长生成_2095203720807145474.json、视频生成/图生视频/H3长视频音频驱动数字人唱歌30秒1分钟切换_2099933503063412738.json、视频生成/图生视频/MiniMax H3单采工作流，文生视频图生视频轻量简洁快速上手_2114479769403346945.json、视频生成/图生视频/MiniMax_H3单采工作流，文生视频图生视频轻量简洁快速上手_2116822096780292097.json、视频生成/图生视频/官方长视频续接无缝｜H3图生视频接续工作流_2095480320987582466.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 8/9 个有
- `ModelPreviewOverrideKJ` —— 8/9 个有
- `孤海注释` —— 8/9 个有
- `ExtendIntermediateSigmas` —— 7/9 个有
- `GetNode` —— 7/9 个有
- `SetNode` —— 7/9 个有
- `TrimAudioDuration` —— 7/9 个有
- `easy showAnything` —— 7/9 个有
- `ComfySwitchNode` —— 6/9 个有
- `SaveImage` —— 6/9 个有
- `MiniMaxH3AddGuide` —— 5/9 个有
- `MiniMaxH3SigmaShift` —— 5/9 个有
- `BlockSparseAttention` —— 4/9 个有
- `GetImageRangeFromBatch` —— 4/9 个有
- `GetVideoComponents` —— 4/9 个有
- `ImageAddNoise` —— 4/9 个有
- `ImageScaleToTotalPixels` —— 4/9 个有
- `LoadVideo` —— 4/9 个有
- `PreviewAudio` —— 4/9 个有
- `PrimitiveBoolean` —— 4/9 个有
- `ResizeImageMaskNode` —— 4/9 个有
- `Seed (rgthree)` —— 4/9 个有
- `VHS_LoadVideo` —— 4/9 个有
- `ManualSigmas` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `AudioConcat` —— 1/9 个有
- `ImageBatch` —— 1/9 个有
- `LTXVConcatAVLatent` —— 1/9 个有
- `LTXVSeparateAVLatent` —— 1/9 个有
- `MinimaxH3LatentUpscaler3D` —— 1/9 个有
- `SelectImages` —— 1/9 个有
- `SplitSigmas` —— 1/9 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/9 个有
- `忽略多组孤海` —— 1/9 个有

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
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
