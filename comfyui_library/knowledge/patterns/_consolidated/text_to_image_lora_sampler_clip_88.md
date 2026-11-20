---
name: text_to_image_lora_sampler_clip_88
type: Text To Image
frequency: 15
level: strong
coverage: 0.763
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json, 视频生成/图生视频/我自用的H3-w1_2094228023120846849.json, 视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json, 视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json, 视频生成/图生视频/深度视频参考动作迁移｜H3视频图生视频直出_2091029816312156162.json, 视频生成/图生视频/深度视频参考动作迁移｜H3视频生视频生成_2091213094801465345.json, 视频生成/图生视频/满血FP16+剪枝int8二采｜MinimaxH3浅空间放大v4_2093250532080185346.json, 视频生成/图生视频/满血FP16剪枝int8加速｜MinimaxH3浅空间放大二采v4_2093092897481650178.json, 视频生成/图生视频/满血int8单采八步加速｜MinimaxH3 Sigma版V4生成_2093254483198439425.json, 视频生成/图生视频/潜空间放大｜H3图生视频高清画质增强老八版_2090166759558045698.json, 视频生成/图生视频/电影级人物视频｜MiniMax H3完美解决脸部崩坏人物特效图生视频_2090066539633528834.json, 视频生成/图生视频/自然去油不磨皮｜MiniMax H3强化二采放大_2096579288177926145.json, 视频生成/文生视频/小脸不崩运动不糊｜H3高清优化版文生图生视频_2089773922295304193.json, 视频生成/文生视频/极速版二采潜空间直接放大 minimaxh3 去油画质提升_2094233661909585921.json, 视频生成/文生视频/高清人脸｜海螺H3 sigma强化潜空间放大视频生成_2089812873718624257.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/开源版数字人 MiniMax-H3 视频文案一体全节点注释_2094256504005292034.json、视频生成/图生视频/我自用的H3-w1_2094228023120846849.json、视频生成/图生视频/战斗场面动态拉满｜Minimax H3最佳战斗版二代_2096534069990486018.json、视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json、视频生成/图生视频/深度视频参考动作迁移｜H3视频图生视频直出_2091029816312156162.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/15 个有
- `孤海注释` —— 14/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/15 个有
- `LTXVConcatAVLatent` —— 11/15 个有
- `LTXVSeparateAVLatent` —— 11/15 个有
- `ModelAttentionBackend` —— 11/15 个有
- `ModelPreviewOverrideKJ` —— 11/15 个有
- `CreateVideo` —— 10/15 个有
- `SaveVideo` —— 10/15 个有
- `GetNode` —— 9/15 个有
- `H3SigmaRefiner` —— 9/15 个有
- `PrimitiveStringMultiline` —— 9/15 个有
- `SetNode` —— 9/15 个有
- `SplitSigmas` —— 8/15 个有
- `MiniMaxH3SigmaShift` —— 6/15 个有
- `MinimaxH3LatentUpscaler3D` —— 6/15 个有
- `VHS_LoadVideo` —— 6/15 个有
- `VHS_VideoCombine` —— 5/15 个有
- `LoadAudio` —— 4/15 个有
- `MinimaxH3LatentUpscalerNode3D` —— 4/15 个有
- `SolAttnMiniMax` —— 4/15 个有
- `DisableNoise` —— 3/15 个有
- `ExtendIntermediateSigmas` —— 3/15 个有
- `PathchSageAttentionKJ` —— 3/15 个有
- `SplitSigmasDenoise` —— 3/15 个有
- `Text Multiline` —— 3/15 个有
- `easy cleanGpuUsed` —— 3/15 个有
- `Label (rgthree)` —— 2/15 个有
- `Text` —— 2/15 个有
- `AudioCrop` —— 1/15 个有
- `CR Text` —— 1/15 个有
- `PlaySound|pysssss` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
