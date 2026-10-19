---
name: text_to_image_lora_sampler_clip_35
type: Text To Image
frequency: 17
level: strong
coverage: 0.84
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/润哥教育IP数字人H3参考生视频｜声音克隆口型自动对齐_2111277682607607809.json, 视频生成/图生视频/竖屏640p H3官流无lora12步 视频生成官方最佳方案_2109698060283629570.json, 视频生成/图生视频/竖屏768p H3官流 视频生成官方最佳方案_2108614995943710722.json, 视频生成/图生视频/老李多参生视频 多参考图输入视频生成方案_2104710161666498561.json, 视频生成/图生视频/自动提示词全能参考生视频REF2VA开源版MiniMax_2086806647741177857.json, 视频生成/图生视频/自定义歌曲MV视频生成｜MiniMax音频驱动图生视频直出_2091736922677932033.json, 视频生成/图生视频/自定义歌曲一键出片｜MiniMax MV音乐视频音频生成_2091752275076272130.json, 视频生成/图生视频/自定义歌曲音乐MV｜MiniMax音频图生视频生成工作流_2090222178607386626.json, 视频生成/图生视频/自用H3官流终极版工作流｜视频生视频图生视频全能_2108409143555088385.json, 视频生成/图生视频/超级加速多图参考生视频｜Minimax_h3角色一致性角色表演工作流_2087208437443809281.json, 视频生成/图生视频/高动态打斗模型生成｜Minimax H3更稳更有冲击力图生视频_2096705144170835969.json, 视频生成/文生视频/3视频)3音频全能参考(9图H3加速优化版MiniMax_2086537090464047105.json, 视频生成/文生视频/H3官流mpov版不用加速LoRA工作流，文生视频视频生视频图生视频方案_2107987502211620866.json, 视频生成/文生视频/H3官流终极版 视频生成官方最佳方案稳定出片_2105387723480719362.json, 视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json, 视频生成/文生视频/MiniMax H3单采V2工作流，文生视频视频生视频图生视频方案_2103619711580856322.json, 视频生成/文生视频/MiniMax H3双采工作流，文生视频视频生视频图生视频方案_2103963966656573441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/润哥教育IP数字人H3参考生视频｜声音克隆口型自动对齐_2111277682607607809.json、视频生成/图生视频/竖屏640p H3官流无lora12步 视频生成官方最佳方案_2109698060283629570.json、视频生成/图生视频/竖屏768p H3官流 视频生成官方最佳方案_2108614995943710722.json、视频生成/图生视频/老李多参生视频 多参考图输入视频生成方案_2104710161666498561.json、视频生成/图生视频/自动提示词全能参考生视频REF2VA开源版MiniMax_2086806647741177857.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
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
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 16/17 个有
- `ResolutionSelector` —— 16/17 个有
- `BasicScheduler` —— 15/17 个有
- `VHS_VideoCombine` —— 15/17 个有
- `LoadAudio` —— 13/17 个有
- `ModelPreviewOverrideKJ` —— 9/17 个有
- `BlockSparseAttention` —— 8/17 个有
- `ManualSigmas` —— 7/17 个有
- `MiniMaxH3SigmaShift` —— 7/17 个有
- `ModelAttentionBackend` —— 7/17 个有
- `SaveImage` —— 7/17 个有
- `GetNode` —— 6/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/17 个有
- `SetNode` —— 6/17 个有
- `VHS_LoadVideo` —— 6/17 个有
- `PathchSageAttentionKJ` —— 5/17 个有
- `TrimAudioDuration` —— 5/17 个有
- `ImageResizeKJv2` —— 3/17 个有
- `LoadVideo` —— 3/17 个有
- `CreateVideo` —— 2/17 个有
- `GetVideoComponents` —— 2/17 个有
- `ImageScaleToTotalPixels` —— 2/17 个有
- `PreviewAudio` —— 2/17 个有
- `ResizeImageMaskNode` —— 2/17 个有
- `SaveVideo` —— 2/17 个有
- `Seed (rgthree)` —— 2/17 个有
- `ExtendIntermediateSigmas` —— 1/17 个有
- `Fast Groups Muter (rgthree)` —— 1/17 个有
- `LTXVConcatAVLatent` —— 1/17 个有
- `LTXVSeparateAVLatent` —— 1/17 个有
- `MinimaxH3LatentUpscaler3D` —— 1/17 个有
- `PainterVRAM` —— 1/17 个有
- `RTXVideoSuperResolution` —— 1/17 个有
- `SplitSigmas` —— 1/17 个有
- `Text` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
