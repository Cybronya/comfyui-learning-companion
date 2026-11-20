---
name: text_to_image_lora_sampler_clip_26
type: Text To Image
frequency: 22
level: strong
coverage: 0.852045
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MMH3 Selflift短剧制作 直出1080P高质量工具_2114125666512887809.json, 图片生成/图生图/MiniMax H3 舞蹈短片｜首帧驱动音画同生律动成片_2112438123752939521.json, 图片生成/图生图/Minimax H3二采提速版｜self_lift多参考生成更快更稳_2101522960317243393.json, 图片生成/图生图/全能参考加速双采self-lift工作流｜图生图加速双采样，参考一致性更强_2100442926517149698.json, 视频生成/图生视频/H3加速双采SelfLift图生视频高效处理工作流_2101041401202036738.json, 视频生成/图生视频/H3加速双采SelfLift工作流_图生视频高效生成_2100427115794624514.json, 视频生成/图生视频/MMH3 Selflift常规万能流 15分钟直出1080P处理工具_2113682479256268801.json, 视频生成/图生视频/MMH3 Selflift常规万能流，直出1080p最高质量版_2110447282897383425.json, 视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110255149494132737.json, 视频生成/图生视频/MMH3 Selflift短剧直出1080p 高质量视频制作_2110369401181655042.json, 视频生成/图生视频/MMH3_Selflift常规万能流，直出1080p最高质量版_2113812542706511873.json, 视频生成/图生视频/MiniMax H3图生视频长视频加速版，B站爆款素材高效批量产出_2114471857700294658.json, 视频生成/图生视频/短剧制作直出1080P最高质量版MMH3 Selflift工作流，图生视频方案_2106889115852689410.json, 视频生成/图生视频/短剧制作直出1080P最高质量版MMH3_Selflift工作流，图生视频方案_2109094089965789186.json, 视频生成/图生视频/短剧制作直出1080p最高质量版 MMH3 Selflift 视频生成优化_2109336160928616450.json, 视频生成/图生视频/短剧制作直出1080p最高质量版MMH3 Selflift 视频生成优化_2109762427930890242.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099191168692219906.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099573312807591938.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099189481143365633.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099571650248400898.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099192888298139649.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099574994182434818.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/MMH3 Selflift短剧制作 直出1080P高质量工具_2114125666512887809.json、图片生成/图生图/MiniMax H3 舞蹈短片｜首帧驱动音画同生律动成片_2112438123752939521.json、图片生成/图生图/Minimax H3二采提速版｜self_lift多参考生成更快更稳_2101522960317243393.json、图片生成/图生图/全能参考加速双采self-lift工作流｜图生图加速双采样，参考一致性更强_2100442926517149698.json、视频生成/图生视频/H3加速双采SelfLift图生视频高效处理工作流_2101041401202036738.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 20/22 个有
- `VHS_VideoCombine` —— 20/22 个有
- `SaveImage` —— 19/22 个有
- `孤海注释` —— 19/22 个有
- `LoadAudio` —— 17/22 个有
- `ModelAttentionBackend` —— 15/22 个有
- `ModelPreviewOverrideKJ` —— 15/22 个有
- `VAEDecodeAudio` —— 15/22 个有
- `MiniMaxH3ReferenceToVideo` —— 14/22 个有
- `LTXVSeparateAVLatent` —— 12/22 个有
- `SelfLiftH3Sampler` —— 12/22 个有
- `SelfLiftAvatarH3Sampler` —— 11/22 个有
- `H3SigmaRefiner` —— 10/22 个有
- `PreviewAny` —— 10/22 个有
- `PrimitiveFloat` —— 10/22 个有
- `LayerUtility: PurgeVRAM V2` —— 9/22 个有
- `EmptyImage` —— 8/22 个有
- `PreviewImage` —— 8/22 个有
- `MiniMaxH3AVDecodeT8` —— 7/22 个有
- `MiniMaxH3AudioConditioningT8` —— 7/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/22 个有
- `Int` —— 5/22 个有
- `JWStringToFloat` —— 5/22 个有
- `CreateVideo` —— 3/22 个有
- `PrimitiveInt` —— 2/22 个有
- `RTXVideoFrameGeneration` —— 2/22 个有
- `SaveVideo` —— 2/22 个有
- `DF_Int_to_Float` —— 1/22 个有
- `GetNode` —— 1/22 个有
- `MiniMaxH3ImageToVideo` —— 1/22 个有
- `SetNode` —— 1/22 个有

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
| Steps较低可能导致细节不足 | 28/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（28/22 个样本）：Steps较低可能导致细节不足
