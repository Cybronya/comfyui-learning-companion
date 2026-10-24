---
name: text_to_image_video_lora_sampler_90
type: Text To Image
frequency: 8
level: strong
coverage: 0.7675
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json, 图片生成/反推提示词/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json, 图片生成/文生图/Minimaxh3视频复刻伪原创，selflift版反推洗图_2110833772068425729.json, 视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json, 视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101042811373178881.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101401984950693889.json, 视频生成/文生视频/短剧助手加速双采 self-lift模式高效视频生成_2098298081249947650.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_90

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json、图片生成/反推提示词/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json、图片生成/文生图/Minimaxh3视频复刻伪原创，selflift版反推洗图_2110833772068425729.json、视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json、视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `H3SigmaRefiner`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 7/8 个有
- `SaveImage` —— 7/8 个有
- `SelfLiftH3Sampler` —— 7/8 个有
- `LoadImage` —— 5/8 个有
- `CreateVideo` —— 4/8 个有
- `GetNode` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `Anything Everywhere3` —— 3/8 个有
- `AudioConcat` —— 3/8 个有
- `MiniMaxH3MediaLoaderFantastic` —— 3/8 个有
- `MiniMaxH3MotionContext` —— 3/8 个有
- `MiniMaxH3MotionContextSaveLatent` —— 3/8 个有
- `MiniMaxH3MotionContextTrim` —— 3/8 个有
- `MiniMaxH3ReferenceSplitter` —— 3/8 个有
- `Prompts Everywhere` —— 3/8 个有
- `VHS_MergeImages` —— 3/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `SelfLiftAvatarH3Sampler` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

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
