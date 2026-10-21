---
name: text_to_image_lora_sampler_clip_51
type: Text To Image
frequency: 15
level: strong
coverage: 0.679533
common_nodes: [CLIPLoader, CLIPTextEncode, CM_BoolToInt, CR Prompt Text, ComfyMathExpression, CreateVideo, EmptyLatentImage, ExecutionBlocker, FloatToText, GetCurrentTimeNode, ImpactNeg, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, RHLLMChatNode, RandomNoise, SaveAudioAdvanced, SaveLatent, SaveVideo, StringReplace, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy anythingIndexSwitch, easy mathString, solarL_SaveImagesToZip, ttN concat, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/10Eros-MiniMax V3参考生视频｜反推提示词生成_2095286007716470785.json, 视频生成/图生视频/10Eros-MiniMax V3图生视频｜反推提示词生成_2095282947782959105.json, 视频生成/图生视频/260831版latent放大双采样｜MiniMaxH3反推提示词图生视频_2094712652223307778.json, 视频生成/图生视频/600ema高动态效果｜Dasiwa-MiniMax H3双采样latent放大_2094313583290183681.json, 视频生成/图生视频/Dasiwa MiniMax H3+600ema双采样｜latent放大高动态拉满_2103092445645991938.json, 视频生成/图生视频/Dasiwa MiniMax H3加600ema极佳高动态效果 latent放大双采样_2105056789514510338.json, 视频生成/图生视频/Dasiwa-MiniMax H3+600ema高动态效果｜latent放大双采样_2100798473594560513.json, 视频生成/图生视频/H3加VDN加SelfLift快速参考生视频处理工具_2100650562076368898.json, 视频生成/图生视频/MiniMax H3+600EMA高动态Latent放大双采样图生视频工具_2101013104544018434.json, 视频生成/图生视频/MiniMax+VDN+SelfLift快速参考生视频处理工具_2101409554914435074.json, 视频生成/图生视频/MiniMax+VDN+selflift快速参考生视频｜反推提示词配图生视频，出片速度翻倍_2100472018708819970.json, 视频生成/图生视频/MiniMax+VDN+selflift｜快速参考生视频实战教程_2101160203919126530.json, 视频生成/图生视频/MiniMaxH3双采样latent放大｜反推提示词图生视频_2094489645626249218.json, 视频生成/图生视频/latent放大双采样极佳高动态 MiniMax H3 Dasiwa 600ema图生视频_2094177581091352577.json, 视频生成/图生视频/双采参考生视频｜10Eros-minimax-beta3 latent放大_2092922374697078785.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/10Eros-MiniMax V3参考生视频｜反推提示词生成_2095286007716470785.json、视频生成/图生视频/10Eros-MiniMax V3图生视频｜反推提示词生成_2095282947782959105.json、视频生成/图生视频/260831版latent放大双采样｜MiniMaxH3反推提示词图生视频_2094712652223307778.json、视频生成/图生视频/600ema高动态效果｜Dasiwa-MiniMax H3双采样latent放大_2094313583290183681.json、视频生成/图生视频/Dasiwa MiniMax H3+600ema双采样｜latent放大高动态拉满_2103092445645991938.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_BoolToInt`
- `CR Prompt Text`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `ExecutionBlocker`
- `FloatToText`
- `GetCurrentTimeNode`
- `ImpactNeg`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RHLLMChatNode`
- `RandomNoise`
- `SaveAudioAdvanced`
- `SaveLatent`
- `SaveVideo`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy mathString`
- `solarL_SaveImagesToZip`
- `ttN concat`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 14/15 个有
- `ImageScaleToTotalPixels` —— 14/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/15 个有
- `GetNode` —— 13/15 个有
- `LayerUtility: PurgeVRAM` —— 13/15 个有
- `MiniMaxH3AVDecodeT8` —— 13/15 个有
- `SetNode` —— 13/15 个有
- `Int` —— 12/15 个有
- `IntConditions` —— 12/15 个有
- `MiniMaxH3PromptEnhancerT8` —— 12/15 个有
- `BasicGuider` —— 11/15 个有
- `MiniMaxH3AudioConditioningT8` —— 11/15 个有
- `SamplerCustomAdvanced` —— 11/15 个有
- `PreviewAny` —— 10/15 个有
- `CM_FloatBinaryOperation` —— 9/15 个有
- `LoraLoaderBypassModelOnly` —— 9/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/15 个有
- `ModelAttentionBackend` —— 9/15 个有
- `SolAttnMiniMax` —— 9/15 个有
- `BasicScheduler` —— 8/15 个有
- `KSamplerSelect` —— 8/15 个有
- `MiniMaxH3DualClockSamplerT8` —— 7/15 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 7/15 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 7/15 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 7/15 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 7/15 个有
- `H3SigmaRefiner` —— 6/15 个有
- `1hew_TextToAny` —— 5/15 个有
- `easy showAnything` —— 5/15 个有
- `ConditioningZeroOut` —— 4/15 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 4/15 个有
- `SaveImage` —— 4/15 个有
- `SelfLiftH3Sampler` —— 4/15 个有
- `MiniMaxH3ReferenceToVideo` —— 3/15 个有
- `EmptyImage` —— 2/15 个有
- `LTXVConcatAVLatent` —— 2/15 个有
- `LTXVSeparateAVLatent` —— 2/15 个有
- `MiniMaxH3BlockCacheT8` —— 2/15 个有
- `MinimaxH3LatentUpscaler3D` —— 2/15 个有
- `PathchSageAttentionKJ` —— 2/15 个有
- `PreviewImage` —— 2/15 个有
- `SplitSigmas` —— 2/15 个有
- `VAEDecodeAudio` —— 2/15 个有
- `MiniMaxH3ImageToVideo` —— 1/15 个有
- `ResolutionSelector` —— 1/15 个有
- `VHS_VideoCombine` —— 1/15 个有

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
