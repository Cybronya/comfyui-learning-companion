---
name: text_to_image_lora_sampler_clip_47
type: Text To Image
frequency: 18
level: strong
coverage: 0.709833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/五分钟1080p高清 MiniMax H3 可视化全模态输出_2094229426480439297.json, 视频生成/图生视频/五分钟1080p高清生成｜MiniMax H3全模态可视化视频_2094576638112657410.json, 视频生成/图生视频/五分钟出1080p高清｜MiniMax H3全模态可视化视频_2094351180242710529.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频图生视频_2092362550968147969.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频生视频图生视频_2092619898299179010.json, 视频生成/图生视频/全能多模态二采放大｜H3加速sigma强化工作流_2092350860545314817.json, 视频生成/图生视频/单模型二采无编解码放大｜MiniMax-H3 ref2va超分_2093849774721167362.json, 视频生成/图生视频/多参图生视频双采Latent放大｜Minimax-H3一键直出_2091672749377941505.json, 视频生成/图生视频/多参考图生视频｜MiniMax H3一键生成直出_2091663599461814274.json, 视频生成/图生视频/完美解决脸部崩坏｜MiniMax H3电影级人物特效图生视频_2090145072644976641.json, 视频生成/图生视频/小脸不崩动态不糊人物不油｜H3开源双模双采短剧漫剧图生视频_2092028224422371330.json, 视频生成/图生视频/小脸不崩漫剧必备｜Minimax H3双采样sigma强化图生视频_2090216685751066626.json, 视频生成/图生视频/强化二采放大工作流｜MiniMax H3自然去油画质提升_2096318365974491138.json, 视频生成/图生视频/显存终极优化｜MINIMAX-H3视频图生视频工作流_2090556860897259521.json, 视频生成/图生视频/武打戏特化制作｜MINIMAX-H3视频生视频图生视频_2092210437902393346.json, 视频生成/图生视频/潜空间放大｜H3图生视频高清画质增强老八版_2090166759558045698.json, 视频生成/图生视频/电影级人物视频｜MiniMax H3完美解决脸部崩坏人物特效图生视频_2090066539633528834.json, 视频生成/文生视频/全能参考v2｜MiniMax H3文生图生视频直出_2091027600822071297.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/五分钟1080p高清 MiniMax H3 可视化全模态输出_2094229426480439297.json、视频生成/图生视频/五分钟1080p高清生成｜MiniMax H3全模态可视化视频_2094576638112657410.json、视频生成/图生视频/五分钟出1080p高清｜MiniMax H3全模态可视化视频_2094351180242710529.json、视频生成/图生视频/全能参考二采放大｜MiniMax H3视频图生视频_2092362550968147969.json、视频生成/图生视频/全能参考二采放大｜MiniMax H3视频生视频图生视频_2092619898299179010.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3SigmaShift` —— 17/18 个有
- `ModelPreviewOverrideKJ` —— 17/18 个有
- `ResolutionSelector` —— 17/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 16/18 个有
- `ModelAttentionBackend` —— 16/18 个有
- `PrimitiveStringMultiline` —— 16/18 个有
- `ComfyMathExpression` —— 15/18 个有
- `LoadImage` —— 15/18 个有
- `MiniMaxH3ReferenceToVideo` —— 15/18 个有
- `H3SigmaRefiner` —— 14/18 个有
- `GetNode` —— 13/18 个有
- `SetNode` —— 13/18 个有
- `MinimaxH3LatentUpscaler3D` —— 12/18 个有
- `CreateVideo` —— 11/18 个有
- `SaveVideo` —— 11/18 个有
- `VHS_VideoCombine` —— 9/18 个有
- `Fast Groups Bypasser (rgthree)` —— 6/18 个有
- `SolAttnMiniMax` —— 6/18 个有
- `MinimaxH3LatentUpscalerNode3D` —— 5/18 个有
- `ExtendIntermediateSigmas` —— 4/18 个有
- `LoadAudio` —— 4/18 个有
- `MiniMaxH3Unified` —— 3/18 个有
- `MiniMaxLowVRAMAttention` —— 3/18 个有
- `PreviewImage` —— 3/18 个有
- `CR Prompt Text` —— 2/18 个有
- `GetVideoComponents` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `LoadVideo` —— 2/18 个有
- `ManualSigmas` —— 2/18 个有
- `MiniMaxChunkFeedForward` —— 2/18 个有
- `VHS_LoadVideo` —— 2/18 个有
- `ImageFromBatch` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `MathExpression|pysssss` —— 1/18 个有
- `PixaromaDuration` —— 1/18 个有
- `PixaromaSizes` —— 1/18 个有
- `PlaySound|pysssss` —— 1/18 个有
- `PrimitiveInt` —— 1/18 个有
- `RIFE VFI` —— 1/18 个有
- `SigmasToFloat` —— 1/18 个有
- `VHS_LoadVideoFFmpeg` —— 1/18 个有
- `VHS_VideoInfo` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（20/18 个样本）：Steps较低可能导致细节不足
