---
name: text_to_image_video_lora_sampler_65
type: Text To Image
frequency: 11
level: strong
coverage: 0.888364
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/极速高清直出｜H3文生视频角色一致性视频超分_2089486697900888065.json, 视频生成/图生视频/海螺H3图生视频｜8步极速加速优化t8版，角色表演流畅_2099887065814093826.json, 视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json, 视频生成/图生视频/海螺h3开源版H3数字人单人数字人图生视频口播数字人加速版MiniMax_2086453850634014722.json, 视频生成/图生视频/清晰度天花板超级加强v3｜minimax h3数字人图生视频_2089034956130570241.json, 视频生成/图生视频/自用4步加速图生视频工作流｜极速出片效率翻倍_2100850409333149698.json, 视频生成/图生视频/音频驱动音乐MV｜MiniMax H3数字人加速版V1出片快_2100122889331765250.json, 视频生成/图生视频/首尾帧EMinimax_H3_NG海螺图生视频_2087147808825626625.json, 视频生成/图生视频/首尾帧生视频｜海螺Minimax_H3图生视频生成_2092176988864864257.json, 视频生成/文生视频/H3开源版短剧漫剧文生视频｜8步高质量极速出片_2098741860201226242.json, 视频生成/文生视频/MiniMax H3双时钟采样Turbo LORA双采集多模态文生视频_2088198784831545345.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_65

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/极速高清直出｜H3文生视频角色一致性视频超分_2089486697900888065.json、视频生成/图生视频/海螺H3图生视频｜8步极速加速优化t8版，角色表演流畅_2099887065814093826.json、视频生成/图生视频/海螺h3开源版H3数字人加速四倍MiniMax图生视频口播数字宫格图片_2086452080943919106.json、视频生成/图生视频/海螺h3开源版H3数字人单人数字人图生视频口播数字人加速版MiniMax_2086453850634014722.json、视频生成/图生视频/清晰度天花板超级加强v3｜minimax h3数字人图生视频_2089034956130570241.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3AudioConditioningT8` —— 10/11 个有
- `MiniMaxH3DualClockSamplerT8` —— 10/11 个有
- `ResolutionSelector` —— 10/11 个有
- `LoadImage` —— 9/11 个有
- `LoraLoaderBypassModelOnly` —— 9/11 个有
- `孤海注释` —— 9/11 个有
- `ModelAttentionBackend` —— 5/11 个有
- `CR Prompt Text` —— 4/11 个有
- `LoadAudio` —— 4/11 个有
- `BasicScheduler` —— 3/11 个有
- `CR Text` —— 3/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `KSamplerSelect` —— 3/11 个有
- `PT_H3ConcatAVLatent` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `VAEEncode` —— 2/11 个有
- `AudioConcat` —— 1/11 个有
- `ExtendIntermediateSigmas` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `H3SigmaRefiner` —— 1/11 个有
- `Int` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `LoadVideoUI` —— 1/11 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/11 个有
- `MiniMaxH3ReferenceToVideo` —— 1/11 个有
- `PathchSageAttentionKJ` —— 1/11 个有
- `PixaromaLabel` —— 1/11 个有
- `SolAttnMiniMax` —— 1/11 个有
- `TrimAudioDuration` —— 1/11 个有
- `VAEEncodeAudio` —— 1/11 个有
- `VAEEncodeTiled` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
