---
name: text_to_image_video_upscale_latent_upscale
type: Text To Image
frequency: 22
level: strong
coverage: 0.484909
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetNode, ImageAddNoise, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3AddGuide, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SetNode, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy forLoopEnd, easy forLoopStart, easy isNone, easy lengthAnything, Seed (rgthree), easy promptConcat, BatchCount+, SimpleMath+]
members: [视频生成/图生视频/MiniMax H3全能参考长视频 多模态输入视频生成_2109383084931108866.json, 视频生成/图生视频/MiniMax H3全能参考长视频 多模态输入视频生成_2109691646983106561.json, 视频生成/图生视频/MiniMax H3全能参考长视频工作流，文生视频图生视频高效创作方案_2106821630193389570.json, 视频生成/图生视频/MiniMax-H3全能参考生视频｜长视频高质量直出_2106587912711270401.json, 视频生成/图生视频/MiniMax-H3全能参考长视频，文生视频图生视频双模式_2110486274929946626.json, 视频生成/图生视频/MiniMax-H3全能参考长视频｜多素材一次喂饱长片直出_2111285734811455490.json, 视频生成/文生视频/H3全能参考长视频 文生视频图生视频创作_2100264124860162049.json, 视频生成/文生视频/MiniMax H3全能参考长视频工作流，文生视频图生视频处理方案_2108296343327436802.json, 视频生成/文生视频/MiniMax H3全能参考长视频工作流，文生视频图生视频高效创作方案_2106821630193389570.json, 视频生成/文生视频/MiniMax H3全能参考长视频生成 多模态参考创作工具_2098814553525153793.json, 视频生成/文生视频/MiniMax H3全能参考长视频生成，文生视频与图生视频双模式支持_2102844494524805121.json, 视频生成/文生视频/MiniMax H3全能参考长视频生成，文生视频与图生视频双模式支持_2103167835215319042.json, 视频生成/文生视频/MiniMax H3全能参考长视频视频生成处理工具_2101735315026305026.json, 视频生成/文生视频/MiniMax H3全能参考长视频｜单图单句直出长片｜出片效率翻倍_2102646336528150530.json, 视频生成/文生视频/MiniMax-H3全能参考长视频生成｜文生视频图生视频双模支持_2099094223952900097.json, 视频生成/文生视频/MiniMax-H3全能参考长视频｜文生视频图生视频 长片创作好帮手_2105502797755146241.json, 视频生成/文生视频/MiniMax-H3全能参考｜长视频文生图生视频通吃出片_2101564544643592193.json, 视频生成/文生视频/全能参考长视频方案 MiniMax H3多段续接稳定生成_2104654658500382721.json, 视频生成/视频生视频/MiniMax H3全能参考长视频工作流_文生视频图生视频一站式创作方案_2105723145415122946.json, 视频生成/视频生视频/MiniMax H3全能参考长视频工作流_角色表演图生视频一站式创作方案_2106088201877286914.json, 视频生成/视频生视频/MiniMax-H3全能参考生视频_长视频高质量直出_2106587912711270401.json, 视频生成/视频生视频/MiniMax_H3全能参考长视频生成_文生视频与图生视频双模式支持_2105858543348961282.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全能参考长视频 多模态输入视频生成_2109383084931108866.json、视频生成/图生视频/MiniMax H3全能参考长视频 多模态输入视频生成_2109691646983106561.json、视频生成/图生视频/MiniMax H3全能参考长视频工作流，文生视频图生视频高效创作方案_2106821630193389570.json、视频生成/图生视频/MiniMax-H3全能参考生视频｜长视频高质量直出_2106587912711270401.json、视频生成/图生视频/MiniMax-H3全能参考长视频，文生视频图生视频双模式_2110486274929946626.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 22 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageAddNoise`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AddGuide`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetNode`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 21/22 个有
- `孤海注释` —— 21/22 个有
- `SplitSigmas` —— 20/22 个有
- `INTConstant` —— 17/22 个有
- `ImageFromBatch` —— 17/22 个有
- `SaveImage` —— 15/22 个有
- `VHS_VideoInfoLoaded` —— 13/22 个有
- `BatchImagesNode` —— 12/22 个有
- `BlockSparseAttention` —— 11/22 个有
- `GetImagesFromBatchIndexed` —— 10/22 个有
- `PreviewAny` —— 10/22 个有
- `easy forLoopEnd` —— 10/22 个有
- `easy forLoopStart` —— 10/22 个有
- `easy ifElse` —— 10/22 个有
- `easy isNone` —— 10/22 个有
- `easy lengthAnything` —— 10/22 个有
- `easy promptConcat` —— 10/22 个有
- `RepeatImageBatch` —— 7/22 个有
- `easy showAnything` —— 6/22 个有
- `PrimitiveBoolean` —— 5/22 个有
- `BatchCount+` —— 4/22 个有
- `SimpleMath+` —— 4/22 个有
- `ConditioningZeroOut` —— 2/22 个有
- `MiniMaxH3ImageToVideo` —— 2/22 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/22 个有
- `SelfLiftH3Sampler` —— 2/22 个有
- `SolAttnMiniMax` —— 2/22 个有
- `ColorTransfer` —— 1/22 个有
- `PreviewImage` —— 1/22 个有
- `VHS_LoadAudioUpload` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（24/22 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy forLoopEnd、easy forLoopStart、easy isNone、easy lengthAnything
