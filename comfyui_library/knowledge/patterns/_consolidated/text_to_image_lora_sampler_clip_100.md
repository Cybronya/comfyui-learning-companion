---
name: text_to_image_lora_sampler_clip_100
type: Text To Image
frequency: 11
level: strong
coverage: 0.692091
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, H3SigmaRefiner, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: [RunningHub Deepcleaner]
members: [视频生成/文生视频/MiniMax H3 SelfLift双采4步Lora6步均衡版视频处理工具_2102182079902609410.json, 视频生成/文生视频/MiniMax H3 SelfLift双采8步Lora12步质量版视频处理工具_2102183788070662146.json, 视频生成/文生视频/MiniMax H3 SelfLift工作流V1，文生视频视频生视频图生视频方案_2103940357879844865.json, 视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2106907557137838082.json, 视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频方案_2107577744304459778.json, 视频生成/文生视频/MiniMax H3极速多参视频制作处理生成工具_2101733080221437954.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103244727301795842.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103523327053750273.json, 视频生成/文生视频/MiniMaxH3极速多参视频制作｜文生视频视频生视频图生视频全能_2105547979712192514.json, 视频生成/文生视频/MiniMaxH3极速多参视频｜文生视频图生视频双模式制作_2101561342628028417.json, 视频生成/视频生视频/MiniMax H3极速多参视频制作_文生视频视频生视频图生视频高效方案_2105732529880920065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_100

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 SelfLift双采4步Lora6步均衡版视频处理工具_2102182079902609410.json、视频生成/文生视频/MiniMax H3 SelfLift双采8步Lora12步质量版视频处理工具_2102183788070662146.json、视频生成/文生视频/MiniMax H3 SelfLift工作流V1，文生视频视频生视频图生视频方案_2103940357879844865.json、视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频_2106907557137838082.json、视频生成/文生视频/MiniMax H3 SelfLift影视级情绪表达Skill工作流，文生视频图生视频方案_2107577744304459778.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `GetNode` —— 9/11 个有
- `MiniMaxChunkFeedForward` —— 9/11 个有
- `MiniMaxLowVRAMAttention` —— 9/11 个有
- `ModelAttentionBackend` —— 9/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `SaveImage` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `VAEDecodeAudio` —— 9/11 个有
- `LoadAudio` —— 8/11 个有
- `MiniMaxH3ReferenceToVideo` —— 8/11 个有
- `PrimitiveFloat` —— 8/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `CreateVideo` —— 6/11 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 6/11 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 6/11 个有
- `ModelPreviewOverrideKJ` —— 6/11 个有
- `SaveVideo` —— 6/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/11 个有
- `VHS_LoadVideo` —— 4/11 个有
- `VHS_VideoInfoLoaded` —— 4/11 个有
- `easy showAnything` —— 4/11 个有
- `Float` —— 3/11 个有
- `LTXVSeparateAVLatent` —— 3/11 个有
- `LayerUtility: PurgeVRAM V2` —— 3/11 个有
- `MiniMaxH3AudioConditioningT8` —— 3/11 个有
- `MiniMaxH3AVDecodeT8` —— 2/11 个有
- `MiniMaxH3VAEDecodeFast` —— 2/11 个有
- `RunningHub Deepcleaner` —— 2/11 个有
- `SolAttnMiniMax` —— 2/11 个有
- `Text` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：RunningHub Deepcleaner
