---
name: text_to_image_lora_sampler_clip_184
type: Text To Image
frequency: 10
level: strong
coverage: 0.7365
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/多参考latent二采｜minimaxh3反推提示词图生图_2091177125763174402.json, 图片生成/文生图/多参考latent二采｜minimaxh3图生图反推提示词生成_2091246455515336706.json, 图片生成/文生图/真人一致性｜人物一致、细节升级_2098733105417908225.json, 数字人/数字人/7度工作流改版1号｜数字人生成效果升级更自然_2106257948442972161.json, 数字人/数字人/7度工作流改版1数字人生成方案，数字人图像处理工具_2107527180271050754.json, 数字人/数字人/7度工作流改版1，数字人生成图像编辑多场景覆盖处理方案_2106524485028499458.json, 数字人/数字人/7度工作流改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107284908405248002.json, 数字人/数字人/MiniMax H3数字人与MV视频制作工作流，虚拟形象演唱表演一键生成_2114421903237668865.json, 数字人/数字人/MinimaxH3数字人&MV工作流｜数字人唱歌表演一站搞定_2114251983816314882.json, 视频生成/图生视频/h3最优基础工作流汇总，文生视频图生视频全能_2111282762715062273.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_184

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/多参考latent二采｜minimaxh3反推提示词图生图_2091177125763174402.json、图片生成/文生图/多参考latent二采｜minimaxh3图生图反推提示词生成_2091246455515336706.json、图片生成/文生图/真人一致性｜人物一致、细节升级_2098733105417908225.json、数字人/数字人/7度工作流改版1号｜数字人生成效果升级更自然_2106257948442972161.json、数字人/数字人/7度工作流改版1数字人生成方案，数字人图像处理工具_2107527180271050754.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 9/10 个有
- `孤海注释` —— 9/10 个有
- `MiniMaxH3SigmaShift` —— 8/10 个有
- `GetNode` —— 7/10 个有
- `LoadAudio` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `CreateVideo` —— 6/10 个有
- `LTXVConcatAVLatent` —— 6/10 个有
- `LTXVSeparateAVLatent` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/10 个有
- `SaveVideo` —— 6/10 个有
- `PreviewImage` —— 5/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/10 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 4/10 个有
- `MinimaxH3LatentUpscaler3D` —— 4/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `SaveImage` —— 4/10 个有
- `SplitSigmas` —— 4/10 个有
- `VHS_VideoCombine` —— 4/10 个有
- `Any Switch (rgthree)` —— 3/10 个有
- `BlockSparseAttention` —— 3/10 个有
- `ExtendIntermediateSigmas` —— 3/10 个有
- `H3SigmaRefiner` —— 3/10 个有
- `LTXVAudioVAEEncode` —— 3/10 个有
- `SetLatentNoiseMask` —— 3/10 个有
- `SolidMask` —— 3/10 个有
- `SoundFlow_GetLength` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/10 个有
- `PT_H3ConcatAVLatent` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `easy int` —— 2/10 个有
- `ComfyNumberConvert` —— 1/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `CustomSigmas` —— 1/10 个有
- `H3KitSemanticBridge` —— 1/10 个有
- `MiniMaxChunkFeedForward` —— 1/10 个有
- `MiniMaxLowVRAMAttention` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `SelfLiftAvatarH3Sampler` —— 1/10 个有
- `SelfLiftAvatarH3TST` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有
- `ZML_MergeText` —— 1/10 个有
- `ZML_TextInput` —— 1/10 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 1/10 个有

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
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
