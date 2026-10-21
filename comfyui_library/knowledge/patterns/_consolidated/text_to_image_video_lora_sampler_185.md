---
name: text_to_image_video_lora_sampler_185
type: Text To Image
frequency: 3
level: strong
coverage: 0.919
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, ComfyMathExpression, Display Any (rgthree), EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageResizeKJv2, ImageScaleToMaxDimension, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_VideoCombine, VRAM_Debug, easy seed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Turbo加速优化文生视频九宫格四视图｜MiniMax H3视频全能编辑工作流_2087164070075133953.json, 视频生成/文生视频/九宫格四视图视频全能编辑｜H3长视频文生图生视频_2091606897832054785.json, 视频生成/文生视频/长视频九宫格四视图｜MiniMax H3文生视频全能编辑_2091778572640940033.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Turbo加速优化文生视频九宫格四视图｜MiniMax H3视频全能编辑工作流_2087164070075133953.json、视频生成/文生视频/九宫格四视图视频全能编辑｜H3长视频文生图生视频_2091606897832054785.json、视频生成/文生视频/长视频九宫格四视图｜MiniMax H3文生视频全能编辑_2091778572640940033.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ComfyMathExpression`
- `Display Any (rgthree)`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRAM_Debug`
- `easy seed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `MiniMaxChunkFeedForward` —— 2/3 个有
- `MiniMaxH3MotionContext` —— 2/3 个有
- `MiniMaxH3MotionContextLoadLatent` —— 2/3 个有
- `MiniMaxH3MotionContextSaveLatent` —— 2/3 个有
- `MiniMaxH3MotionContextTrim` —— 2/3 个有
- `MiniMaxLowVRAMAttention` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `SpectrumApplyMiniMaxH3` —— 2/3 个有
- `VHS_MergeImages` —— 2/3 个有
- `EasyCache` —— 1/3 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
