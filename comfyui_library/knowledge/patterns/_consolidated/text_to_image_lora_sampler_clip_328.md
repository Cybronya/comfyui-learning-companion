---
name: text_to_image_lora_sampler_clip_328
type: Text To Image
frequency: 3
level: strong
coverage: 0.913333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, GetVideoComponents, ImpactConditionalBranch, ImpactExecutionOrderController, ImpactQueueTrigger, ImpactSetWidgetValue, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3MotionContext, MiniMaxH3MotionContextLoadLatent, MiniMaxH3MotionContextSaveLatent, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxH3TurboLoRA, MiniMaxH3TurboSampler, MiniMaxLowVRAMAttention, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, RTXVideoSuperResolution, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImageKJ, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAELoader, easy indexAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/H3分段参考生视频Impact V6双采｜打破15秒限制整合提示词文生视频_2090437822875529218.json, 视频生成/文生视频/分段参考生视频导播台｜H3三模切换一键生成_2094022419370569729.json, 视频生成/文生视频/分段参考生视频导播台｜H3图生视频剪辑合成_2093800802619052033.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_328

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/H3分段参考生视频Impact V6双采｜打破15秒限制整合提示词文生视频_2090437822875529218.json、视频生成/文生视频/分段参考生视频导播台｜H3三模切换一键生成_2094022419370569729.json、视频生成/文生视频/分段参考生视频导播台｜H3图生视频剪辑合成_2093800802619052033.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `GetVideoComponents`
- `ImpactConditionalBranch`
- `ImpactExecutionOrderController`
- `ImpactQueueTrigger`
- `ImpactSetWidgetValue`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextLoadLatent`
- `MiniMaxH3MotionContextSaveLatent`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3TurboSampler`
- `MiniMaxLowVRAMAttention`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `RTXVideoSuperResolution`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImageKJ`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAELoader`
- `easy indexAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `TheodoreDirector_CommitResult` —— 2/3 个有
- `TheodoreDirector_H3Adapter` —— 2/3 个有
- `TheodoreDirector_OutputPaths` —— 2/3 个有
- `TheodoreDirector_PostprocessSecondPassSource` —— 2/3 个有
- `TheodoreDirector_Project` —— 2/3 个有
- `TheodoreDirector_SaveSecondPass` —— 2/3 个有
- `TheodoreDirector_SelectShot` —— 2/3 个有
- `VAEEncodeAudio` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `ImagePass` —— 1/3 个有
- `JoinStrings` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SomethingToString` —— 1/3 个有
- `TextSplitByDelimiter` —— 1/3 个有
- `easy blocker` —— 1/3 个有
- `easy compare` —— 1/3 个有
- `easy convertAnything` —— 1/3 个有
- `easy isFileExist` —— 1/3 个有
- `easy mathInt` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
