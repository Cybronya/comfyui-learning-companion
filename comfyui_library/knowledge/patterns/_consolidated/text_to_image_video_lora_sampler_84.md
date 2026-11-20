---
name: text_to_image_video_lora_sampler_84
type: Text To Image
frequency: 10
level: strong
coverage: 0.8595
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3带货视频生成 数字人模特产品展示处理工具_2112980337470042114.json, 数字人/数字人/MiniMaxH3带货视频生成｜模特产品展示商业片直出_2112840776400072706.json, 数字人/数字人/MiniMax超写实颜值赛道数字人 起号图生视频处理工具_2113018540012957697.json, 视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json, 视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101042811373178881.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101401984950693889.json, 视频生成/图生视频/MiniMax H3超写实颜值赛道 人物特效图生视频工具_2114054895513980930.json, 视频生成/图生视频/MiniMax H3颜值赛道起号 超写实人物图生视频工具_2114093051516907522.json, 视频生成/文生视频/Minimax H3满血版黑科技加速 Self-lift双采工作流_2098704152372277249.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/MiniMax H3带货视频生成 数字人模特产品展示处理工具_2112980337470042114.json、数字人/数字人/MiniMaxH3带货视频生成｜模特产品展示商业片直出_2112840776400072706.json、数字人/数字人/MiniMax超写实颜值赛道数字人 起号图生视频处理工具_2113018540012957697.json、视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json、视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
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
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `H3SigmaRefiner` —— 7/10 个有
- `MiniMaxLowVRAMAttention` —— 7/10 个有
- `AudioConcat` —— 5/10 个有
- `CreateVideo` —— 4/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `BlockSparseAttention` —— 3/10 个有
- `MiniMaxH3MotionContext` —— 3/10 个有
- `MiniMaxH3MotionContextSaveLatent` —— 3/10 个有
- `MiniMaxH3MotionContextTrim` —— 3/10 个有
- `MiniMaxH3SigmaShift` —— 3/10 个有
- `StringFormat` —— 3/10 个有
- `VHS_MergeImages` —— 3/10 个有
- `ImageBatch` —— 2/10 个有
- `ImageFromBatch` —— 2/10 个有
- `LoadAudio` —— 2/10 个有
- `MiniMaxH3AddGuide` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `AudioCrop` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
