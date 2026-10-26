---
name: text_to_image_video_upscale_latent_upscale_20
type: Text To Image
frequency: 4
level: strong
coverage: 0.9245
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Seed, ComfyMathExpression, EmptyLatentImage, ImpactConditionalBranch, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextSaveLatent, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Yuan_H3MotionContextLoadLatent, easy cleanGpuUsed, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/文武双全双采工作流，图生视频文戏武戏全覆盖高质量创作方案_2106834046570553345.json, 视频生成/图生视频/文武双全双采工作流，图生视频文戏武戏全覆盖高质量创作方案_2110541659804098561.json, 视频生成/文生视频/t8大佬文武双全工作流｜文生视频加图生视频通吃_2106639380873048066.json, 视频生成/文生视频/动态视频生成｜文生图生视频生视频多模直出_2093410305727614978.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_20

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/文武双全双采工作流，图生视频文戏武戏全覆盖高质量创作方案_2106834046570553345.json、视频生成/图生视频/文武双全双采工作流，图生视频文戏武戏全覆盖高质量创作方案_2110541659804098561.json、视频生成/文生视频/t8大佬文武双全工作流｜文生视频加图生视频通吃_2106639380873048066.json、视频生成/文生视频/动态视频生成｜文生图生视频生视频多模直出_2093410305727614978.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Seed`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `ImpactConditionalBranch`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Yuan_H3MotionContextLoadLatent`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `ImageBatchMulti` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `Yuan_MiniMaxH3Video` —— 3/4 个有
- `easy anythingIndexSwitch` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxH3AudioConditioningT8` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `ModelPatchTorchSettings` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
