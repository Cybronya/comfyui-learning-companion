---
name: text_to_image_lora_sampler_clip_28
type: Text To Image
frequency: 23
level: strong
coverage: 0.694
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多图参考带货视频｜MiniMax-H3数字人倾情出镜_2096572891126124546.json, 视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频多素材融合_2088699208495882241.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2092760928600285186.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2093795328280584193.json, 视频生成/图生视频/多图参考生视频｜MiniMax R2V 768分辨率8步极速出片_2103022962520707074.json, 视频生成/图生视频/我自用的H3-w1_2094228023120846849.json, 视频生成/图生视频/数字人视频带货｜MiniMax-H3多图参考生视频制作_2096314183389372417.json, 视频生成/图生视频/最佳动态战斗版V2｜Minimax H3图生视频高质量生成_2096318583386230785.json, 视频生成/文生视频/H3开源数字人口播带货 多图生视频电商内容制作_2098851175243280386.json, 视频生成/文生视频/H3突破15秒长视频不劣化工作流拆解系列_2100272112148766722.json, 视频生成/文生视频/H3突破15秒长视频不劣化｜工作流拆解系列生成_2095301463194034178.json, 视频生成/文生视频/MiniMax H3全能参考长视频生成 多模态参考创作工具_2098814553525153793.json, 视频生成/文生视频/MiniMax H3全能参考长视频视频生成处理工具_2101735315026305026.json, 视频生成/文生视频/MiniMax-H3全能参考工作流｜文生图生视频多模式生成_2097418439563505665.json, 视频生成/文生视频/MiniMax-H3全能参考长视频生成｜文生视频图生视频双模支持_2099094223952900097.json, 视频生成/文生视频/MiniMax-H3全能参考｜多素材视频高质量生成_2095575150086414338.json, 视频生成/文生视频/MiniMax-H3全能参考｜长视频文生图生视频通吃出片_2101564544643592193.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频生成_2093477174438354945.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频直出_2090658700645191681.json, 视频生成/文生视频/全能参考生视频｜MiniMax H3图生文生二合一_2090839391815159809.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/多图参考带货视频｜MiniMax-H3数字人倾情出镜_2096572891126124546.json、视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频多素材融合_2088699208495882241.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 23 个 workflow 都包含：
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
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 22/23 个有
- `孤海注释` —— 22/23 个有
- `VAEDecodeAudio` —— 21/23 个有
- `PrimitiveStringMultiline` —— 20/23 个有
- `LoadAudio` —— 18/23 个有
- `GetNode` —— 15/23 个有
- `SetNode` —— 15/23 个有
- `ExtendIntermediateSigmas` —— 14/23 个有
- `LTXVConcatAVLatent` —— 13/23 个有
- `ModelAttentionBackend` —— 13/23 个有
- `VHS_VideoCombine` —— 13/23 个有
- `Fast Groups Bypasser (rgthree)` —— 12/23 个有
- `LTXVSeparateAVLatent` —— 12/23 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/23 个有
- `VHS_LoadVideo` —— 12/23 个有
- `CreateVideo` —— 10/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/23 个有
- `MiniMaxH3SigmaShift` —— 10/23 个有
- `MinimaxH3LatentUpscaler3D` —— 10/23 个有
- `ModelPreviewOverrideKJ` —— 10/23 个有
- `SaveVideo` —— 10/23 个有
- `Seed (rgthree)` —— 10/23 个有
- `SolAttnMiniMax` —— 9/23 个有
- `Any Switch (rgthree)` —— 8/23 个有
- `MiniMaxH3ImageToVideo` —— 7/23 个有
- `Mute / Bypass Repeater (rgthree)` —— 7/23 个有
- `GetImageRangeFromBatch` —— 6/23 个有
- `MiniMaxH3AddGuide` —— 6/23 个有
- `SaveImage` —— 6/23 个有
- `H3SigmaRefiner` —— 5/23 个有
- `ImageAddNoise` —— 4/23 个有
- `SplitSigmas` —— 4/23 个有
- `TrimAudioDuration` —— 4/23 个有
- `easy cleanGpuUsed` —— 4/23 个有
- `INTConstant` —— 3/23 个有
- `ImageResizeKJv2` —— 3/23 个有
- `ManualSigmas` —— 3/23 个有
- `VAEEncode` —— 3/23 个有
- `VAEEncodeAudio` —— 3/23 个有
- `ConditioningZeroOut` —— 2/23 个有
- `DisableNoise` —— 2/23 个有
- `MiniMaxH3AVDecodeT8` —— 2/23 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/23 个有
- `PT_H3ConcatAVLatent` —— 2/23 个有
- `SplitSigmasDenoise` —— 2/23 个有
- `easy showAnything` —— 2/23 个有
- `CM_IntToFloat` —— 1/23 个有
- `Int` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 高发问题（25/23 个样本）：Steps较低可能导致细节不足
