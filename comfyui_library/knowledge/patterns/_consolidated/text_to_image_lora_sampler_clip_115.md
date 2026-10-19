---
name: text_to_image_lora_sampler_clip_115
type: Text To Image
frequency: 8
level: strong
coverage: 0.90225
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelPreviewOverrideKJ, PrimitiveStringMultiline, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/minimax h3长视频人物替换加动作迁移，内部循环视频生视频_2111516810670600194.json, 视频生成/图生视频/DsiwaV2小脸高动态SelfLift图生视频处理工具_2101035152284676097.json, 视频生成/图生视频/FastH3 V2 SelfLift 1080P｜图生视频数字人快速出片_2100893504040955905.json, 视频生成/图生视频/H3加速双采SelfLift图生视频高效处理工作流_2101041401202036738.json, 视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099213820353933314.json, 视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099567116251910145.json, 视频生成/图生视频/H3加速双采SelfLift工作流_图生视频高效生成_2100427115794624514.json, 视频生成/文生视频/H3 dasiwaV3加高动态支持加特殊运镜工作流，文生视频图生视频处理方案_2108257601246027778.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_115

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/minimax h3长视频人物替换加动作迁移，内部循环视频生视频_2111516810670600194.json、视频生成/图生视频/DsiwaV2小脸高动态SelfLift图生视频处理工具_2101035152284676097.json、视频生成/图生视频/FastH3 V2 SelfLift 1080P｜图生视频数字人快速出片_2100893504040955905.json、视频生成/图生视频/H3加速双采SelfLift图生视频高效处理工作流_2101041401202036738.json、视频生成/图生视频/H3加速双采SelfLift工作流 图生视频高效生成_2099213820353933314.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelPreviewOverrideKJ`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `H3SigmaRefiner` —— 7/8 个有
- `MiniMaxChunkFeedForward` —— 7/8 个有
- `MiniMaxLowVRAMAttention` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `VAEDecodeAudio` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `MiniMaxH3SigmaShift` —— 4/8 个有
- `SelfLiftH3Sampler` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/8 个有
- `SelfLiftAvatarH3Sampler` —— 3/8 个有
- `easy seed` —— 3/8 个有
- `EmptyImage` —— 2/8 个有
- `LoraLoaderBypassModelOnly` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `BlockSparseAttention` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `MiniMaxH3LongVideoSampler-solarL` —— 1/8 个有
- `MiniMaxH3TurboLoRA` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `PrimitiveBoolean` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VHS_VideoCombine` —— 1/8 个有
- `easy float` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
