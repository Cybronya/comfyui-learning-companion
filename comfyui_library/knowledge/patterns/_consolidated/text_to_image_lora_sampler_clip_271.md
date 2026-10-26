---
name: text_to_image_lora_sampler_clip_271
type: Text To Image
frequency: 8
level: strong
coverage: 0.7655
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3极简全能工作流 SelfLift双采快速处理工具_2114045314729603074.json, 视频生成/图生视频/MiniMax H3极简全能工作流｜文生视频图生视频一网打尽_2113895094708432898.json, 视频生成/图生视频/Minimax H3多参Singularity V2 图生视频处理工具_2114144480856203265.json, 视频生成/图生视频/Minimax H3最佳动作视频生成Ref2V参考图驱动，动作流畅自然高清直出_2114410428527894530.json, 视频生成/图生视频/Minimax-H3多参Singularity-V2版｜多参考一致性生视频_2114060307990663169.json, 视频生成/图生视频/YZ金鱼改MiniMax H3终极篇文武双全｜无限画布漫剧利器_2111305187406209025.json, 视频生成/图生视频/口播转动画30秒专用 说教情感知识搞笑段子图生视频工具_2113068364288585730.json, 视频生成/文生视频/Self Lift双采工作流文生图生视频，文生视频图生视频高效创作方案_2105780339426816001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_271

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3极简全能工作流 SelfLift双采快速处理工具_2114045314729603074.json、视频生成/图生视频/MiniMax H3极简全能工作流｜文生视频图生视频一网打尽_2113895094708432898.json、视频生成/图生视频/Minimax H3多参Singularity V2 图生视频处理工具_2114144480856203265.json、视频生成/图生视频/Minimax H3最佳动作视频生成Ref2V参考图驱动，动作流畅自然高清直出_2114410428527894530.json、视频生成/图生视频/Minimax-H3多参Singularity-V2版｜多参考一致性生视频_2114060307990663169.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 7/8 个有
- `ComfyMathExpression` —— 6/8 个有
- `MiniMaxH3SigmaShift` —— 6/8 个有
- `PrimitiveFloat` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `MiniMaxH3ReferenceToVideo` —— 5/8 个有
- `VHS_VideoCombine` —— 5/8 个有
- `GetNode` —— 4/8 个有
- `H3SigmaRefiner` —— 4/8 个有
- `SetNode` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `ComfySwitchNode` —— 3/8 个有
- `CreateVideo` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `Text` —— 3/8 个有
- `LoraLoaderBypassModelOnly` —— 2/8 个有
- `MiniMaxH3IntegrationAdapterGH` —— 2/8 个有
- `MiniMaxH3IntegrationGH` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `PrimitiveInt` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `MiniMaxChunkFeedForward` —— 1/8 个有
- `MiniMaxH3ImageToVideo` —— 1/8 个有
- `MiniMaxLowVRAMAttention` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `easy loraStack` —— 1/8 个有
- `easy loraStackApply` —— 1/8 个有

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
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
