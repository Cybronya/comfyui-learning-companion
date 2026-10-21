---
name: text_to_image_lora_sampler_clip_154
type: Text To Image
frequency: 8
level: strong
coverage: 0.6925
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3SigmaShift, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/文生图生首尾帧视频｜MiniMax_H3二阶高清直出_2090558225891553281.json, 视频生成/图生视频/潜空间放大｜H3图生视频高清画质增强老八版_2090166759558045698.json, 视频生成/图生视频/电影级人物视频｜MiniMax H3完美解决脸部崩坏人物特效图生视频_2090066539633528834.json, 视频生成/图生视频/自然去油不磨皮｜MiniMax H3强化二采放大_2096579288177926145.json, 视频生成/图生视频/视频衔接无缝续接生成｜H3图生视频工作流_2095490694986166273.json, 视频生成/文生视频/H3全能视频｜vibex文生图生首尾帧通吃，二阶高清更细腻_2099860995895291906.json, 视频生成/文生视频/万象AI+sigma强化潜空间放大｜海螺H3 1080P十秒_2091018350292987905.json, 视频生成/文生视频/多合一生视频V3.0｜Minimax H3文生首尾图参二采高清放大_2090209607414276097.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_154

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/文生图生首尾帧视频｜MiniMax_H3二阶高清直出_2090558225891553281.json、视频生成/图生视频/潜空间放大｜H3图生视频高清画质增强老八版_2090166759558045698.json、视频生成/图生视频/电影级人物视频｜MiniMax H3完美解决脸部崩坏人物特效图生视频_2090066539633528834.json、视频生成/图生视频/自然去油不磨皮｜MiniMax H3强化二采放大_2096579288177926145.json、视频生成/图生视频/视频衔接无缝续接生成｜H3图生视频工作流_2095490694986166273.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `H3SigmaRefiner` —— 6/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 6/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `MiniMaxChunkFeedForward` —— 3/8 个有
- `MiniMaxH3ImageToVideo` —— 3/8 个有
- `MiniMaxLowVRAMAttention` —— 3/8 个有
- `MinimaxH3LatentUpscaler3D` —— 3/8 个有
- `PathchSageAttentionKJ` —— 3/8 个有
- `SolAttnMiniMax` —— 3/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `ManualSigmas` —— 2/8 个有
- `SpectrumApplyMiniMaxH3` —— 2/8 个有
- `Any Switch (rgthree)` —— 1/8 个有
- `FL_UnloadAllModels` —— 1/8 个有
- `GetImageRangeFromBatch` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `MiniMaxH3AddGuide` —— 1/8 个有
- `MiniMaxH3HybridLoader` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `SolAttnPatch` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `忽略多组孤海` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
