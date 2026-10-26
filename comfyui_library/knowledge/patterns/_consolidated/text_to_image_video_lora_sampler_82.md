---
name: text_to_image_video_lora_sampler_82
type: Text To Image
frequency: 10
level: strong
coverage: 0.7118
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 SelfLift双采4步Lora6步均衡版视频处理工具_2102182079902609410.json, 视频生成/文生视频/MiniMax H3 SelfLift双采8步Lora12步质量版视频处理工具_2102183788070662146.json, 视频生成/文生视频/MiniMax H3 SelfLift工作流V1，文生视频视频生视频图生视频方案_2103940357879844865.json, 视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2106907557137838082.json, 视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频方案_2107577744304459778.json, 视频生成/文生视频/MiniMax H3导演Skill加双采2K直出工作流，文生视频视频生视频图生视频_2106862808569827330.json, 视频生成/文生视频/MiniMax H3导演skill加持｜双采样2K直出高质感视频_2104492093019353089.json, 视频生成/文生视频/MiniMax H3文生首尾图参多合一二采高清放大视频工具_2101039738512822274.json, 视频生成/文生视频/Minimax H3多合一生视频V6.0｜文生首尾图参二采放大_2098765941927665665.json, 视频生成/文生视频/Minimax H3文生首尾图参多合一 二采高清放大工作流V6.0自用版_2098645500403736577.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_82

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 SelfLift双采4步Lora6步均衡版视频处理工具_2102182079902609410.json、视频生成/文生视频/MiniMax H3 SelfLift双采8步Lora12步质量版视频处理工具_2102183788070662146.json、视频生成/文生视频/MiniMax H3 SelfLift工作流V1，文生视频视频生视频图生视频方案_2103940357879844865.json、视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2106907557137838082.json、视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频方案_2107577744304459778.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：71%

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
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `H3SigmaRefiner` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `SaveImage` —— 8/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 7/10 个有
- `ModelAttentionBackend` —— 7/10 个有
- `PrimitiveFloat` —— 7/10 个有
- `GetNode` —— 6/10 个有
- `MiniMaxChunkFeedForward` —— 6/10 个有
- `MiniMaxLowVRAMAttention` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `LoadAudio` —— 5/10 个有
- `MiniMaxH3SigmaShift` —— 5/10 个有
- `ModelPreviewOverrideKJ` —— 5/10 个有
- `Any Switch (rgthree)` —— 3/10 个有
- `Float` —— 3/10 个有
- `ImageResizeKJv2` —— 3/10 个有
- `ImpactConditionalBranch` —— 3/10 个有
- `Int` —— 3/10 个有
- `LayerUtility: PurgeVRAM V2` —— 3/10 个有
- `MathExpression|pysssss` —— 3/10 个有
- `MiniMaxH3AudioConditioningT8` —— 3/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 3/10 个有
- `布尔孤海` —— 3/10 个有
- `MiniMaxH3AVDecodeT8` —— 2/10 个有
- `MiniMaxH3Unified` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `RandomNoise` —— 2/10 个有
- `SolAttnMiniMax` —— 2/10 个有
- `SolAttnPatch` —— 2/10 个有
- `Text` —— 2/10 个有
- `LTXVSeparateAVLatent` —— 1/10 个有

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
