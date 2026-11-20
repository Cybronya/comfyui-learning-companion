---
name: text_to_image_video_lora_sampler_27
type: Text To Image
frequency: 21
level: strong
coverage: 0.770143
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3人物演技提升 文生视频图生视频处理工具_2113333463540658178.json, 视频生成/图生视频/MiniMax H3全能参考正式版 真实电影质感视频处理工具_2113410728010014721.json, 视频生成/图生视频/MiniMax H3全能参考真实电影质感V2，图生视频胶片感运镜直出_2114442449908228097.json, 视频生成/图生视频/MiniMax H3全能参考｜真实电影质感V2文生视频图生视频三合一_2114262759729881089.json, 视频生成/图生视频/MiniMax H3全能插件加音频设计 视频加音效一站式方案_2105420482479742977.json, 视频生成/图生视频/MiniMax H3全能插件升级｜音频设计加持视频创作_2105253049693458433.json, 视频生成/图生视频/MiniMax H3图生视频2K快速版，支持15秒长视频场景特效方案_2103610501115768833.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110250634422341633.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim latent放大增强_2110365841622659073.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110252157650956290.json, 视频生成/图生视频/MiniMax H3图生视频fastH3加速 trim多帧动态优化_2110367355523133442.json, 视频生成/图生视频/MiniMax H3数字人带货视频｜多图直生成模特产品展示_2103033669408608258.json, 视频生成/图生视频/MiniMax H3极速多参视频制作，文生视频图生视频多模式高效出片_2114423427422576642.json, 视频生成/图生视频/MiniMax H3角色替换 指定角色视频编辑换脸处理工具_2113766570131542018.json, 视频生成/图生视频/MiniMax H3角色替换单人指定版｜视频编辑换脸一步完成_2113541615401918466.json, 视频生成/图生视频/MiniMax H3角色替换｜单人指定角色+视频编辑多合一_2110716972131512322.json, 视频生成/图生视频/MiniMaxH3-极速多参视频制作｜文生视频图生视频快到飞起_2114257352080846849.json, 视频生成/图生视频/MiniMaxH3极速多参视频 加速Lora语义强化生成工具_2113350861492678657.json, 视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092084924617674753.json, 视频生成/图生视频/minimax h3 i2v Latent Upscaler｜图生视频潜空间放大_2092377938405707778.json, 视频生成/图生视频/极速图生视频 MinimaxH3 人物场景特效快速生成_2094196531091034114.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3人物演技提升 文生视频图生视频处理工具_2113333463540658178.json、视频生成/图生视频/MiniMax H3全能参考正式版 真实电影质感视频处理工具_2113410728010014721.json、视频生成/图生视频/MiniMax H3全能参考真实电影质感V2，图生视频胶片感运镜直出_2114442449908228097.json、视频生成/图生视频/MiniMax H3全能参考｜真实电影质感V2文生视频图生视频三合一_2114262759729881089.json、视频生成/图生视频/MiniMax H3全能插件加音频设计 视频加音效一站式方案_2105420482479742977.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 21 个 workflow 都包含：
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
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 20/21 个有
- `PrimitiveStringMultiline` —— 17/21 个有
- `MiniMaxH3ReferenceToVideo` —— 15/21 个有
- `BasicScheduler` —— 14/21 个有
- `MiniMaxH3SigmaShift` —— 14/21 个有
- `ModelPreviewOverrideKJ` —— 14/21 个有
- `SaveImage` —— 14/21 个有
- `ManualSigmas` —— 13/21 个有
- `BlockSparseAttention` —— 11/21 个有
- `GetNode` —— 11/21 个有
- `SetNode` —— 11/21 个有
- `Fast Groups Bypasser (rgthree)` —— 9/21 个有
- `LTXVConcatAVLatent` —— 9/21 个有
- `LTXVSeparateAVLatent` —— 9/21 个有
- `MinimaxH3LatentUpscaler3D` —— 9/21 个有
- `VHS_LoadVideo` —— 9/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/21 个有
- `SplitSigmas` —— 7/21 个有
- `H3SigmaRefiner` —— 6/21 个有
- `LoadAudio` —— 6/21 个有
- `MiniMaxH3ImageToVideo` —— 6/21 个有
- `MiniMaxH3Unified` —— 6/21 个有
- `ConditioningZeroOut` —— 4/21 个有
- `CR Text` —— 3/21 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/21 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/21 个有
- `ImageResizeKJv2` —— 2/21 个有
- `MiniMaxH3AddGuide` —— 2/21 个有
- `PreviewAny` —— 2/21 个有
- `Vignette` —— 2/21 个有
- `GetVideoComponents` —— 1/21 个有
- `Label (rgthree)` —— 1/21 个有
- `MiniMaxH3HybridArtifactBuilderT8Advanced` —— 1/21 个有
- `MiniMaxH3HybridModelLoaderT8Advanced` —— 1/21 个有
- `MiniMaxH3HybridPairInspectorT8Advanced` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（22/21 个样本）：Steps较低可能导致细节不足
