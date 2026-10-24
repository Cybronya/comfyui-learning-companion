---
name: text_to_image_lora_sampler_clip_176
type: Text To Image
frequency: 10
level: strong
coverage: 0.738
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json, 视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json, 视频生成/文生视频/MiniMax H3 SelfLift低分辨率采样器加速视频生成工具_2101028313874649090.json, 视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json, 视频生成/文生视频/MiniMax H3极速多参视频制作处理生成工具_2101733080221437954.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103244727301795842.json, 视频生成/文生视频/MiniMax H3极速多参视频制作，文生视频图生视频多参考高效产出方案_2103523327053750273.json, 视频生成/文生视频/MiniMaxH3极速多参视频制作｜文生视频视频生视频图生视频全能_2105547979712192514.json, 视频生成/文生视频/MiniMaxH3极速多参视频｜文生视频图生视频双模式制作_2101561342628028417.json, 视频生成/视频生视频/MiniMax H3极速多参视频制作，文生视频视频生视频图生视频高效方案_2105732529880920065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_176

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/BUNNY_SelfLift混合工作流｜7分钟直出1080P高动态不模糊_2108382144140759042.json、视频生成/文生视频/H3 TaoMate 3步加速Lora 视频生成处理工具_2100654393346576385.json、视频生成/文生视频/MiniMax H3 SelfLift低分辨率采样器加速视频生成工具_2101028313874649090.json、视频生成/文生视频/MiniMax H3加速双采SelfLift图生视频处理工作流_2101739128789487617.json、视频生成/文生视频/MiniMax H3极速多参视频制作处理生成工具_2101733080221437954.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `SelfLiftH3Sampler` —— 9/10 个有
- `VAEDecodeAudio` —— 9/10 个有
- `H3SigmaRefiner` —— 8/10 个有
- `LoadAudio` —— 8/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `MiniMaxChunkFeedForward` —— 7/10 个有
- `MiniMaxLowVRAMAttention` —— 7/10 个有
- `ModelPreviewOverrideKJ` —— 7/10 个有
- `SaveImage` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `GetNode` —— 6/10 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 6/10 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 6/10 个有
- `SetNode` —— 6/10 个有
- `VHS_LoadVideo` —— 4/10 个有
- `VHS_VideoInfoLoaded` —— 4/10 个有
- `easy showAnything` —— 4/10 个有
- `LTXVSeparateAVLatent` —— 3/10 个有
- `MiniMaxH3AudioConditioningT8` —— 2/10 个有
- `MiniMaxH3VAEDecodeFast` —— 2/10 个有
- `RunningHub Deepcleaner` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `LoraLoader` —— 1/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `MiniMaxH3AVDecodeT8` —— 1/10 个有
- `MiniMaxH3SigmaShift` —— 1/10 个有
- `SelfLiftAvatarH3Sampler` —— 1/10 个有
- `SelfLiftAvatarH3TST` —— 1/10 个有
- `SolAttnMiniMax` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 0.75 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
