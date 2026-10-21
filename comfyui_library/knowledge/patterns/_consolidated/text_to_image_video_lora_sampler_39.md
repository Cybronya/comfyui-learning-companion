---
name: text_to_image_video_lora_sampler_39
type: Text To Image
frequency: 15
level: strong
coverage: 0.6472
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [PlaySound|pysssss]
members: [视频生成/图生视频/H3文戏SelfLift融合版｜24G显存720p 九参考图文戏更细腻_2105544997541072897.json, 视频生成/图生视频/MINIMAX-H3八月最强文戏低配版，单采2省显存出片_2110864933956177921.json, 视频生成/图生视频/MINIMAX-H3开源最强文戏低配版｜角色一致性图生视频_2094855880356491266.json, 视频生成/图生视频/MINIMAX-H3最强文戏5参考图版，低配单采轻松跑_2110866429514960898.json, 视频生成/图生视频/MiniMAX H3导演台｜图生视频一键直出生成_2092357167356669954.json, 视频生成/图生视频/MiniMax H3 SelfLift加二采加音频参考工作流，文生视频视频生视频图生视频_2106518365966786562.json, 视频生成/图生视频/minimaxh3selflift二采音频参考_三重加持稳定出片_2106239244355325953.json, 视频生成/图生视频/minimaxh3音频参考加持，selflift二采流程一键出片_2110442485200809985.json, 视频生成/图生视频/最强打斗武戏双采工作流｜MINIMAX-H3自动提示词图生视频_2096734559260995586.json, 视频生成/文生视频/MiniMax H3 SelfLift加二采加音频参考工作流，文生视频视频生视频图生视频_2106518365966786562.json, 视频生成/文生视频/MiniMax H3打斗版二采视频生视频处理生成工具_2101749624259309569.json, 视频生成/文生视频/MiniMax-H3全能参考工作流｜文生图生视频多模式生成_2097418439563505665.json, 视频生成/文生视频/MiniMax-H3全能参考｜多素材视频高质量生成_2095575150086414338.json, 视频生成/文生视频/全能参考生成视频｜MiniMax-H3文生图生视频_2095818212331048962.json, 视频生成/文生视频/武戏专用参考｜MiniMax H3提示词手输自动可选_2096598519665750017.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/H3文戏SelfLift融合版｜24G显存720p 九参考图文戏更细腻_2105544997541072897.json、视频生成/图生视频/MINIMAX-H3八月最强文戏低配版，单采2省显存出片_2110864933956177921.json、视频生成/图生视频/MINIMAX-H3开源最强文戏低配版｜角色一致性图生视频_2094855880356491266.json、视频生成/图生视频/MINIMAX-H3最强文戏5参考图版，低配单采轻松跑_2110866429514960898.json、视频生成/图生视频/MiniMAX H3导演台｜图生视频一键直出生成_2092357167356669954.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 14/15 个有
- `LTXVSeparateAVLatent` —— 14/15 个有
- `LoadAudio` —— 14/15 个有
- `MinimaxH3LatentUpscaler3D` —— 14/15 个有
- `ModelAttentionBackend` —— 14/15 个有
- `H3SigmaRefiner` —— 12/15 个有
- `ExtendIntermediateSigmas` —— 11/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/15 个有
- `PrimitiveStringMultiline` —— 9/15 个有
- `CR Prompt Text` —— 7/15 个有
- `INTConstant` —— 7/15 个有
- `ModelPreviewOverrideKJ` —— 7/15 个有
- `SaveImage` —— 7/15 个有
- `PreviewImage` —— 6/15 个有
- `ConditioningZeroOut` —— 5/15 个有
- `MiniMaxChunkFeedForward` —— 5/15 个有
- `MiniMaxLowVRAMAttention` —— 5/15 个有
- `SelfLiftAvatarH3Sampler` —— 5/15 个有
- `CreateVideo` —— 4/15 个有
- `Fast Groups Bypasser (rgthree)` —— 4/15 个有
- `MiniMaxH3ImageToVideo` —— 4/15 个有
- `Mute / Bypass Repeater (rgthree)` —— 4/15 个有
- `PlaySound|pysssss` —— 4/15 个有
- `Seed (rgthree)` —— 4/15 个有
- `SolAttnMiniMax` —— 4/15 个有
- `VHS_LoadVideo` —— 4/15 个有
- `Any Switch (rgthree)` —— 3/15 个有
- `MiniMaxH3SigmaShift` —— 3/15 个有
- `RH_LLMAPI_Pro_Node` —— 3/15 个有
- `PreviewAny` —— 2/15 个有
- `忽略多组孤海` —— 2/15 个有
- `BlockSparseAttention` —— 1/15 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/15 个有
- `MiniMaxH3LowVRAMAttentionT8Advanced` —— 1/15 个有
- `MuyeTextEditOutput` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：PlaySound|pysssss
