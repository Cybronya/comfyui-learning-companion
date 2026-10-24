---
name: text_to_image_lora_sampler_clip_16
type: Text To Image
frequency: 28
level: strong
coverage: 0.895179
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Minimax H3二采提速版｜self_lift多参考生成更快更稳_2101522960317243393.json, 图片生成/图生图/全能参考加速双采self-lift工作流｜图生图加速双采样，参考一致性更强_2100442926517149698.json, 视频生成/图生视频/DsiwaV2小脸高动态SelfLift图生视频处理工具_2101035152284676097.json, 视频生成/图生视频/FastH3 V2 SelfLift 1080P｜图生视频数字人快速出片_2100893504040955905.json, 视频生成/图生视频/H3加速双采SelfLift图生视频高效处理工作流_2101041401202036738.json, 视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099213820353933314.json, 视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099567116251910145.json, 视频生成/图生视频/H3加速双采SelfLift工作流_图生视频高效生成_2100427115794624514.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采参考生视频｜武戏动态强_2108458056047742978.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采武戏动态强参考生视频方案_2108644932058697730.json, 视频生成/图生视频/MiniMax H3 SelfLift加速双采｜武戏动态强的参考生视频_2111123791060496385.json, 视频生成/图生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101363088590196738.json, 视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110247054734880770.json, 视频生成/图生视频/Minimax H3全能参考Selflift双采 Sage加速高质量直出_2110372049079324674.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110248726794162177.json, 视频生成/图生视频/Minimax H3高质量高速度全能参考 Selflift双采Sage加速版_2110362722650124289.json, 视频生成/图生视频/低显存12GB直出1080P高分辨率视频，BUNNY_SelfLift混合工作流LoRA不模糊_2105510967852486657.json, 视频生成/文生视频/7分钟直出1080P 12GB可用BUNNY SelfLift高动态加LORA不模糊混合工作流_2108616556530987010.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099191168692219906.json, 视频生成/文生视频/H3 SelfLift五图音频数字人 15秒广告视频生成_2099573312807591938.json, 视频生成/文生视频/H3 dasiwaV3加高动态支持加特殊运镜工作流，文生视频图生视频处理方案_2108257601246027778.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099189481143365633.json, 视频生成/文生视频/H3二采数字人SelfLift单图三人音频参考 多角色口播_2099571650248400898.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099192888298139649.json, 视频生成/文生视频/H3二采数字人SelfLift单图双人音频参考 多人口播_2099574994182434818.json, 视频生成/文生视频/MiniMax H3 SelfLift双采4步Lora6步均衡版视频处理工具_2102182079902609410.json, 视频生成/文生视频/MiniMax H3 SelfLift双采8步Lora12步质量版视频处理工具_2102183788070662146.json, 视频生成/文生视频/Minimax H3 self-lift双采 BF16加sage四步加速lora高质量高速_2098296538933059585.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_16

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Minimax H3二采提速版｜self_lift多参考生成更快更稳_2101522960317243393.json、图片生成/图生图/全能参考加速双采self-lift工作流｜图生图加速双采样，参考一致性更强_2100442926517149698.json、视频生成/图生视频/DsiwaV2小脸高动态SelfLift图生视频处理工具_2101035152284676097.json、视频生成/图生视频/FastH3 V2 SelfLift 1080P｜图生视频数字人快速出片_2100893504040955905.json、视频生成/图生视频/H3加速双采SelfLift图生视频高效处理工作流_2101041401202036738.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 28 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 26/28 个有
- `H3SigmaRefiner` —— 24/28 个有
- `SaveImage` —— 23/28 个有
- `SelfLiftH3Sampler` —— 23/28 个有
- `MiniMaxChunkFeedForward` —— 21/28 个有
- `MiniMaxLowVRAMAttention` —— 21/28 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 19/28 个有
- `MiniMaxH3AVDecodeT8` —— 16/28 个有
- `MiniMaxH3AudioConditioningT8` —— 16/28 个有
- `VHS_VideoCombine` —— 15/28 个有
- `CreateVideo` —— 14/28 个有
- `LayerUtility: PurgeVRAM V2` —— 14/28 个有
- `SaveVideo` —— 13/28 个有
- `MiniMaxH3ReferenceToVideo` —— 12/28 个有
- `ModelPreviewOverrideKJ` —— 12/28 个有
- `VAEDecodeAudio` —— 12/28 个有
- `LoadAudio` —— 11/28 个有
- `ModelAttentionBackend` —— 10/28 个有
- `LoraLoaderBypassModelOnly` —— 7/28 个有
- `EmptyImage` —— 5/28 个有
- `PreviewImage` —— 5/28 个有
- `SelfLiftAvatarH3Sampler` —— 5/28 个有
- `SolAttnMiniMax` —— 5/28 个有
- `ExtendIntermediateSigmas` —— 3/28 个有
- `MiniMaxH3SigmaShift` —— 3/28 个有
- `easy seed` —— 3/28 个有
- `easy showAnything` —— 3/28 个有
- `SelfLiftAvatarH3TST` —— 2/28 个有
- `BlockSparseAttention` —— 1/28 个有
- `MiniMaxH3TurboLoRA` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 28 | 100% |
| 高度 | 80 | 80 - 80 | 28 | 100% |
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 28 | 100% |
| 采样算法 | er_sde | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高发问题（29/28 个样本）：Steps较低可能导致细节不足
