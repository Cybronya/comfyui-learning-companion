---
name: text_to_image_lora_sampler_clip_37
type: Text To Image
frequency: 16
level: strong
coverage: 0.67175
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, GetNode, JjkText, KSampler, LoraLoaderModelOnly, ResolutionSelector, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 AutoContext无限时长视频单采直出处理工具_2101723121383460866.json, 视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大1080P直出工具_2101721113498841089.json, 视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大武戏1080P直出工具_2101719041944674305.json, 视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频图生视频_2092362550968147969.json, 视频生成/图生视频/全能参考二采放大｜MiniMax H3视频生视频图生视频_2092619898299179010.json, 视频生成/图生视频/全能多模态二采放大｜H3加速sigma强化工作流_2092350860545314817.json, 视频生成/图生视频/双模双采小脸不崩｜Minimax H3高动态不崩脸视频_2093486007596437506.json, 视频生成/图生视频/双模双采资源面板短剧助手 MiniMax H3 全能参考生成视频_2094255084355022849.json, 视频生成/图生视频/多参考图生视频｜MiniMax H3一键生成直出_2091663599461814274.json, 视频生成/图生视频/完美解决脸部崩坏｜MiniMax H3电影级人物特效图生视频_2090145072644976641.json, 视频生成/图生视频/小脸不崩动态不糊人物不油｜H3开源双模双采短剧漫剧图生视频_2092028224422371330.json, 视频生成/图生视频/小脸不崩漫剧必备｜Minimax H3双采样sigma强化图生视频_2090216685751066626.json, 视频生成/图生视频/潜空间放大｜H3图生视频高清画质增强老八版_2090166759558045698.json, 视频生成/图生视频/电影级人物视频｜MiniMax H3完美解决脸部崩坏人物特效图生视频_2090066539633528834.json, 视频生成/文生视频/小脸不崩运动不糊｜H3高清优化版文生图生视频_2089773922295304193.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 AutoContext无限时长视频单采直出处理工具_2101723121383460866.json、视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大1080P直出工具_2101721113498841089.json、视频生成/图生视频/MiniMax H3 AutoContext无限时长视频双采放大武戏1080P直出工具_2101719041944674305.json、视频生成/图生视频/二次采样放大文戏工作流｜MiniMax_H3图生视频精修_2096324113731248129.json、视频生成/图生视频/全能参考二采放大｜MiniMax H3视频图生视频_2092362550968147969.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 15/16 个有
- `LTXVConcatAVLatent` —— 15/16 个有
- `LTXVSeparateAVLatent` —— 15/16 个有
- `LoadImage` —— 15/16 个有
- `MiniMaxH3SigmaShift` —— 15/16 个有
- `ModelAttentionBackend` —— 15/16 个有
- `SplitSigmas` —— 15/16 个有
- `CreateVideo` —— 14/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 14/16 个有
- `SaveVideo` —— 14/16 个有
- `BasicGuider` —— 13/16 个有
- `ComfyMathExpression` —— 13/16 个有
- `H3SigmaRefiner` —— 13/16 个有
- `KSamplerSelect` —— 13/16 个有
- `MiniMaxH3ReferenceToVideo` —— 13/16 个有
- `PrimitiveFloat` —— 13/16 个有
- `RandomNoise` —— 13/16 个有
- `SamplerCustomAdvanced` —— 13/16 个有
- `ModelPreviewOverrideKJ` —— 12/16 个有
- `MinimaxH3LatentUpscaler3D` —— 10/16 个有
- `PrimitiveStringMultiline` —— 9/16 个有
- `CR Prompt Text` —— 7/16 个有
- `SolAttnMiniMax` —— 7/16 个有
- `MiniMaxLowVRAMAttention` —— 6/16 个有
- `MinimaxH3LatentUpscalerNode3D` —— 5/16 个有
- `Fast Groups Bypasser (rgthree)` —— 3/16 个有
- `H3AutoContextSampler` —— 3/16 个有
- `H3Parameter` —— 3/16 个有
- `H3SeamCorrection` —— 3/16 个有
- `ImageResizeKJv2` —— 3/16 个有
- `SaveImage` —— 3/16 个有
- `easy cleanGpuUsed` —— 3/16 个有
- `Label (rgthree)` —— 2/16 个有
- `PathchSageAttentionKJ` —— 2/16 个有
- `SolAttnPatch` —— 2/16 个有
- `VHS_VideoCombine` —— 2/16 个有
- `Anything Everywhere` —— 1/16 个有
- `Anything Everywhere3` —— 1/16 个有
- `DF_Integer` —— 1/16 个有
- `GetVideoComponents` —— 1/16 个有
- `LoadAudio` —— 1/16 个有
- `LoadVideo` —— 1/16 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/16 个有
- `MiniMaxH3ReferenceSplitter` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（17/16 个样本）：Steps较低可能导致细节不足
