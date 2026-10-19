---
name: text_to_image_video_lora_sampler_16
type: Text To Image
frequency: 21
level: strong
coverage: 0.695333
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json, 图片生成/反推提示词/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json, 图片生成/文生图/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json, 图片生成/文生图/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json, 视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json, 视频生成/图生视频/H3全能参考短剧工作流 多模态输入视频生成_2109027495902277633.json, 视频生成/图生视频/H3官流最强武戏 视频生成官方最佳方案稳定出片_2109173230555713537.json, 视频生成/图生视频/H3官流终极版工作流，文生视频图生视频全覆盖方案_2109435565342019586.json, 视频生成/图生视频/H3工作流最优解 图生视频高质量稳定直出方案_2110367340926955522.json, 视频生成/图生视频/H3工作流最优解 视频生成最佳方案高效出片_2105350475045498881.json, 视频生成/图生视频/H3无损融合单采V2 官方满血API画布级本地流_2110225226482151425.json, 视频生成/图生视频/H3无损融合单采V2 官方满血API画布级本地流_2110353804985196545.json, 视频生成/图生视频/H3无损融合单采官方满血API画布级本地流 视频生成优化_2109397447813455873.json, 视频生成/图生视频/H3无损融合单采官方满血API画布级本地流 视频生成优化_2109781427771498497.json, 视频生成/图生视频/H3无损融合单采方案，速度俱佳图生视频出片_2111278197022224385.json, 视频生成/图生视频/H3无损融合单采满血API，画布级本地文生视频流_2111200196137934849.json, 视频生成/图生视频/H3最强单采V2雷霆祭祀版，33步战斗特效文生视频_2111228248330952705.json, 视频生成/图生视频/H3画布级本地流无损融合 官方满血API单采方案_2110351795410259970.json, 视频生成/图生视频/Minimax H3完美人物替换 图生视频换人方案_2110363954835976194.json, 视频生成/图生视频/Minimax参考图模式 多模态输入视频生成_2109765711622139905.json, 视频生成/文生视频/短剧助手加速双采 self-lift模式高效视频生成_2098298081249947650.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/反推提示词/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json、图片生成/反推提示词/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json、图片生成/文生图/Minimax H3 Best Fast 极速高质量视频生成_2104680372096294914.json、图片生成/文生图/Minimax_H3_Best_Fast极速版｜文生图反推图生图三合一高效出图_2104522656451219457.json、视频生成/图生视频/H3二采SelfLift急速工作流 图生视频高效生成_2100308360200540161.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ModelPreviewOverrideKJ` —— 20/21 个有
- `孤海注释` —— 20/21 个有
- `PrimitiveStringMultiline` —— 19/21 个有
- `SaveImage` —— 19/21 个有
- `LoadAudio` —— 16/21 个有
- `LoadImage` —— 16/21 个有
- `BasicGuider` —— 15/21 个有
- `RandomNoise` —— 15/21 个有
- `SamplerCustomAdvanced` —— 15/21 个有
- `VHS_LoadVideo` —— 15/21 个有
- `GetNode` —— 14/21 个有
- `SetNode` —— 14/21 个有
- `BlockSparseAttention` —— 13/21 个有
- `ManualSigmas` —— 12/21 个有
- `ConditioningZeroOut` —— 7/21 个有
- `H3SigmaRefiner` —— 7/21 个有
- `MiniMaxChunkFeedForward` —— 7/21 个有
- `MiniMaxLowVRAMAttention` —— 7/21 个有
- `SelfLiftH3Sampler` —— 7/21 个有
- `Anything Everywhere3` —— 5/21 个有
- `MiniMaxH3MediaLoaderFantastic` —— 5/21 个有
- `MiniMaxH3ReferenceSplitter` —— 5/21 个有
- `Prompts Everywhere` —— 5/21 个有
- `CR Prompt Text` —— 4/21 个有
- `ComfySwitchNode` —— 4/21 个有
- `PathchSageAttentionKJ` —— 4/21 个有
- `PreviewAny` —— 3/21 个有
- `RH_LLMAPI_Pro_Node` —— 3/21 个有
- `Fast Groups Bypasser (rgthree)` —— 2/21 个有
- `CR Text` —— 1/21 个有
- `PreviewImage` —— 1/21 个有
- `easy showAnything` —— 1/21 个有

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
