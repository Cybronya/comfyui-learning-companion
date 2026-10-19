---
name: text_to_image_video_lora_sampler_35
type: Text To Image
frequency: 16
level: strong
coverage: 0.631437
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [PlaySound|pysssss]
members: [视频生成/图生视频/H3文戏SelfLift融合版｜24G显存720p 九参考图文戏更细腻_2105544997541072897.json, 视频生成/图生视频/MINIMAX-H3八月最强文戏低配版，单采2省显存出片_2110864933956177921.json, 视频生成/图生视频/MINIMAX-H3开源最强文戏低配版｜角色一致性图生视频_2094855880356491266.json, 视频生成/图生视频/MINIMAX-H3最强文戏5参考图版，低配单采轻松跑_2110866429514960898.json, 视频生成/图生视频/MiniMAX H3导演台｜图生视频一键直出生成_2092357167356669954.json, 视频生成/图生视频/MiniMax H3 SelfLift加二采加音频参考工作流，文生视频视频生视频图生视频_2106518365966786562.json, 视频生成/图生视频/minimaxh3selflift二采音频参考_三重加持稳定出片_2106239244355325953.json, 视频生成/图生视频/minimaxh3音频参考加持，selflift二采流程一键出片_2110442485200809985.json, 视频生成/图生视频/最强打斗武戏双采工作流｜MINIMAX-H3自动提示词图生视频_2096734559260995586.json, 视频生成/文生视频/MiniMax H3 SelfLift加二采加音频参考工作流，文生视频视频生视频图生视频_2106518365966786562.json, 视频生成/文生视频/MiniMax H3打斗版二采视频生视频处理生成工具_2101749624259309569.json, 视频生成/文生视频/MiniMax-H3全能参考工作流｜文生图生视频多模式生成_2097418439563505665.json, 视频生成/文生视频/MiniMax-H3全能参考｜多素材视频高质量生成_2095575150086414338.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频生成_2093477174438354945.json, 视频生成/文生视频/全能参考工作流｜MiniMax-H3文生图生视频直出_2090658700645191681.json, 视频生成/文生视频/全能参考生视频｜MiniMax H3图生文生二合一_2090839391815159809.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/H3文戏SelfLift融合版｜24G显存720p 九参考图文戏更细腻_2105544997541072897.json、视频生成/图生视频/MINIMAX-H3八月最强文戏低配版，单采2省显存出片_2110864933956177921.json、视频生成/图生视频/MINIMAX-H3开源最强文戏低配版｜角色一致性图生视频_2094855880356491266.json、视频生成/图生视频/MINIMAX-H3最强文戏5参考图版，低配单采轻松跑_2110866429514960898.json、视频生成/图生视频/MiniMAX H3导演台｜图生视频一键直出生成_2092357167356669954.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 16 个 workflow 都包含：
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
- `LTXVConcatAVLatent` —— 15/16 个有
- `LoadAudio` —— 15/16 个有
- `ModelAttentionBackend` —— 15/16 个有
- `H3SigmaRefiner` —— 14/16 个有
- `LTXVSeparateAVLatent` —— 14/16 个有
- `ExtendIntermediateSigmas` —— 12/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 12/16 个有
- `MinimaxH3LatentUpscaler3D` —— 12/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/16 个有
- `INTConstant` —— 10/16 个有
- `PrimitiveStringMultiline` —— 10/16 个有
- `SaveImage` —— 8/16 个有
- `ConditioningZeroOut` —— 7/16 个有
- `ModelPreviewOverrideKJ` —— 7/16 个有
- `CR Prompt Text` —— 6/16 个有
- `Fast Groups Bypasser (rgthree)` —— 6/16 个有
- `MiniMaxH3ImageToVideo` —— 6/16 个有
- `Mute / Bypass Repeater (rgthree)` —— 6/16 个有
- `Seed (rgthree)` —— 6/16 个有
- `SolAttnMiniMax` —— 6/16 个有
- `VHS_LoadVideo` —— 6/16 个有
- `MiniMaxChunkFeedForward` —— 5/16 个有
- `MiniMaxLowVRAMAttention` —— 5/16 个有
- `PreviewImage` —— 5/16 个有
- `SelfLiftAvatarH3Sampler` —— 5/16 个有
- `Any Switch (rgthree)` —— 4/16 个有
- `CreateVideo` —— 4/16 个有
- `PlaySound|pysssss` —— 4/16 个有
- `ImageResizeKJv2` —— 3/16 个有
- `MiniMaxH3SigmaShift` —— 3/16 个有
- `VAEEncode` —— 3/16 个有
- `VAEEncodeAudio` —— 3/16 个有
- `easy cleanGpuUsed` —— 3/16 个有
- `MinimaxH3LatentUpscalerNode3D` —— 2/16 个有
- `PT_H3ConcatAVLatent` —— 2/16 个有
- `PreviewAny` —— 2/16 个有
- `RH_LLMAPI_Pro_Node` —— 2/16 个有
- `SplitSigmas` —— 2/16 个有
- `忽略多组孤海` —— 2/16 个有
- `BlockSparseAttention` —— 1/16 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/16 个有
- `MiniMaxH3LowVRAMAttentionT8Advanced` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（18/16 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：PlaySound|pysssss
