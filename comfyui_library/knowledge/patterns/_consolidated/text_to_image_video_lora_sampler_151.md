---
name: text_to_image_video_lora_sampler_151
type: Text To Image
frequency: 4
level: strong
coverage: 0.8855
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/加速版双时钟版官流原版合集｜MinimaxH3视频参考生成视频生视频_2088138270730444801.json, 视频生成/图生视频/换装加动作迁移视频编辑｜MiniMaxH3全节点注释视频生视频_2088735225936441345.json, 视频生成/图生视频/视频编辑换装动作迁移｜MiniMaxH3全节点注释版_2090911739268390914.json, 视频生成/文生视频/Turbo加速优化文生视频九宫格四视图｜MiniMax H3视频全能编辑工作流_2087164070075133953.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_151

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/加速版双时钟版官流原版合集｜MinimaxH3视频参考生成视频生视频_2088138270730444801.json、视频生成/图生视频/换装加动作迁移视频编辑｜MiniMaxH3全节点注释视频生视频_2088735225936441345.json、视频生成/图生视频/视频编辑换装动作迁移｜MiniMaxH3全节点注释版_2090911739268390914.json、视频生成/文生视频/Turbo加速优化文生视频九宫格四视图｜MiniMax H3视频全能编辑工作流_2087164070075133953.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/4 个有
- `VRAM_Debug` —— 3/4 个有
- `EasyCache` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `VAEDecodeAudio` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `Display Any (rgthree)` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetCurrentTimeNode` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `ImageScaleToMaxDimension` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `LazySwitch1way` —— 1/4 个有
- `MiniMaxH3ImageToVideo` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `PurgeVRAM_UTK` —— 1/4 个有
- `SomethingToString` —— 1/4 个有
- `VHS_LoadAudioUpload` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy seed` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
