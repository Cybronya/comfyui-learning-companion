---
name: text_to_image_lora_sampler_clip_24
type: Text To Image
frequency: 23
level: strong
coverage: 0.820739
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax H3带货视频生成 数字人模特产品展示处理工具_2112980337470042114.json, 数字人/数字人/MiniMaxH3带货视频生成｜模特产品展示商业片直出_2112840776400072706.json, 数字人/数字人/MiniMax超写实颜值赛道数字人 起号图生视频处理工具_2113018540012957697.json, 视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json, 视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101042811373178881.json, 视频生成/图生视频/MiniMax H3急速双采无限时长视频生成处理工作流_2101401984950693889.json, 视频生成/图生视频/MiniMax H3超写实颜值赛道 人物特效图生视频工具_2114054895513980930.json, 视频生成/图生视频/MiniMax H3颜值赛道起号 超写实人物图生视频工具_2114093051516907522.json, 视频生成/图生视频/minimax-H3超写实颜值赛道起号神器｜角色设计特效流_2113976547051921410.json, 视频生成/图生视频/minimax-H3超写实颜值起号神器｜人物特效角色设计_2113995369376997377.json, 视频生成/图生视频/绘影MiniMax H3参考生视频self-lift双采1080P，混合25-49模型加速方案_2103171255007531010.json, 视频生成/图生视频/绘影出品｜Minimax H3参考生视频self-lift双采1080P高清V1版_2103018117453672449.json, 视频生成/图生视频/黑科技加速双采SelfLift Heng图生视频处理工作流_2101779733385146370.json, 视频生成/图生视频/黑科技加速双采self-lift图生视频｜Minimax-H3开源战斗特效版_2097956772765069313.json, 视频生成/文生视频/Aiden黑科技加速双采self-lift工作流｜文图视频三模生视频_2097969163804438530.json, 视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json, 视频生成/文生视频/MiniMax H3极速多参视频制作处理生成工具_2101733080221437954.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103244727301795842.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103523327053750273.json, 视频生成/文生视频/MiniMaxH3极速多参视频制作｜文生视频视频生视频图生视频全能_2105547979712192514.json, 视频生成/文生视频/MiniMaxH3极速多参视频｜文生视频图生视频双模式制作_2101561342628028417.json, 视频生成/视频生视频/MiniMax H3极速多参视频制作，文生视频视频生视频图生视频高效方案_2105732529880920065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（数字人/数字人/MiniMax H3带货视频生成 数字人模特产品展示处理工具_2112980337470042114.json、数字人/数字人/MiniMaxH3带货视频生成｜模特产品展示商业片直出_2112840776400072706.json、数字人/数字人/MiniMax超写实颜值赛道数字人 起号图生视频处理工具_2113018540012957697.json、视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json、视频生成/图生视频/H3急速双采加无限时长长视频续写工作流工具_2100314628738871297.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 23 个 workflow 都包含：
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 21/23 个有
- `H3SigmaRefiner` —— 18/23 个有
- `MiniMaxLowVRAMAttention` —— 18/23 个有
- `VHS_VideoCombine` —— 18/23 个有
- `ModelPreviewOverrideKJ` —— 15/23 个有
- `SaveImage` —— 15/23 个有
- `CreateVideo` —— 13/23 个有
- `LoadAudio` —— 10/23 个有
- `Fast Groups Bypasser (rgthree)` —— 7/23 个有
- `MiniMaxH3SigmaShift` —— 7/23 个有
- `SaveVideo` —— 7/23 个有
- `GetNode` —— 6/23 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 6/23 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 6/23 个有
- `SetNode` —— 6/23 个有
- `AudioConcat` —— 5/23 个有
- `BlockSparseAttention` —— 5/23 个有
- `StringFormat` —— 5/23 个有
- `VHS_LoadVideo` —— 5/23 个有
- `VHS_VideoInfoLoaded` —— 4/23 个有
- `easy showAnything` —— 4/23 个有
- `MiniMaxH3MotionContext` —— 3/23 个有
- `MiniMaxH3MotionContextSaveLatent` —— 3/23 个有
- `MiniMaxH3MotionContextTrim` —— 3/23 个有
- `VHS_MergeImages` —— 3/23 个有
- `ImageBatch` —— 2/23 个有
- `ImageFromBatch` —— 2/23 个有
- `LTXVSeparateAVLatent` —— 2/23 个有
- `MiniMaxH3AddGuide` —— 2/23 个有
- `MiniMaxH3VAEDecodeFast` —— 2/23 个有
- `RunningHub Deepcleaner` —— 2/23 个有
- `TrimAudioDuration` —— 2/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（25/23 个样本）：Steps较低可能导致细节不足
