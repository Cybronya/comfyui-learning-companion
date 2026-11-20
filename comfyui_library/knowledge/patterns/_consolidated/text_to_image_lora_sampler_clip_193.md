---
name: text_to_image_lora_sampler_clip_193
type: Text To Image
frequency: 10
level: strong
coverage: 0.8049
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Minimax图生视频I2V｜单图驱动动态画面生成稳定流_2112893548440936450.json, 视频生成/图生视频/R2V参考生视频加速版｜5060Ti 16G本地极速跑_2103045635455938561.json, 视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json, 视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json, 视频生成/图生视频/参考生视频玩法升级｜MiniMax H3 视频生视频双通道_2096253067581812737.json, 视频生成/图生视频/双图版全能参考｜MiniMax H3图生视频高质量生成_2094740772443738114.json, 视频生成/图生视频/多图参考直出｜MiniMax H3图生视频一致性生成_2090271687425220609.json, 视频生成/文生视频/H3最优官流｜文生图生视频高质量一键生成_2092047166419324930.json, 视频生成/文生视频/H3最优官流｜文生视频图生视频双模式官方_2089391709946994690.json, 视频生成/文生视频/MiniMax T2V文生视频 写实Lora开关latent续写处理工具_2112967836275658753.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_193

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax图生视频I2V｜单图驱动动态画面生成稳定流_2112893548440936450.json、视频生成/图生视频/R2V参考生视频加速版｜5060Ti 16G本地极速跑_2103045635455938561.json、视频生成/图生视频/r2v参考生视频带TTS｜h3图生视频v2直出_2093853858853376001.json、视频生成/图生视频/三图版全能参考｜MiniMax H3图生视频一键生成_2094737971634335745.json、视频生成/图生视频/参考生视频玩法升级｜MiniMax H3 视频生视频双通道_2096253067581812737.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `ComfySwitchNode` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `LoadAudio` —— 7/10 个有
- `PrimitiveInt` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `EmptyAudio` —— 3/10 个有
- `AudioConcat` —— 2/10 个有
- `AudioInfo` —— 2/10 个有
- `GetNode` —— 2/10 个有
- `ManualSigmas` —— 2/10 个有
- `MiniMaxH3ImageToVideo` —— 2/10 个有
- `MiniMaxH3SaveLatent` —— 2/10 个有
- `ModelPreviewOverrideKJ` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `easy minimaxH3AudioLock` —— 2/10 个有
- `Fast Bypasser (rgthree)` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/10 个有
- `ModelAttentionBackend` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `XB_ReferenceAny` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
