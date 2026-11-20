---
name: text_to_image_lora_sampler_clip_430
type: Text To Image
frequency: 5
level: strong
coverage: 0.6126
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ModelPreviewOverrideKJ, ResolutionSelector, SelfLiftH3Sampler, SetNode, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 SelfLift全能流V3 VOSR速度质量兼顾工具_2113402636207742978.json, 视频生成/图生视频/Minimax H3 Ref2V最佳动作 文生视频图生视频处理工具_2113335034068422657.json, 视频生成/图生视频/Minimax H3最佳动作视频生成Ref2V参考图驱动，动作流畅自然高清直出_2114410428527894530.json, 视频生成/图生视频/YZ金鱼改MiniMax H3终极篇文武双全｜无限画布漫剧利器_2111305187406209025.json, 视频生成/图生视频/口播转动画30秒专用 说教情感知识搞笑段子图生视频工具_2113068364288585730.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_430

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 SelfLift全能流V3 VOSR速度质量兼顾工具_2113402636207742978.json、视频生成/图生视频/Minimax H3 Ref2V最佳动作 文生视频图生视频处理工具_2113335034068422657.json、视频生成/图生视频/Minimax H3最佳动作视频生成Ref2V参考图驱动，动作流畅自然高清直出_2114410428527894530.json、视频生成/图生视频/YZ金鱼改MiniMax H3终极篇文武双全｜无限画布漫剧利器_2111305187406209025.json、视频生成/图生视频/口播转动画30秒专用 说教情感知识搞笑段子图生视频工具_2113068364288585730.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `SetNode`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `CreateVideo` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `H3SigmaRefiner` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `ComfySwitchNode` —— 1/5 个有
- `ExtendIntermediateSigmas` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Float` —— 1/5 个有
- `JWImageResizeByLongerSide` —— 1/5 个有
- `LTXVSeparateAVLatent` —— 1/5 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/5 个有
- `QwenH3PromptLocal` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `RTXVideoSuperResolution` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VOSR2ModelLoader` —— 1/5 个有
- `VOSR2Upscale` —— 1/5 个有
- `easy imageSize` —— 1/5 个有
- `easy loraStack` —— 1/5 个有
- `easy loraStackApply` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
