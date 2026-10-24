---
name: text_to_image_lora_sampler_clip_667
type: Text To Image
frequency: 2
level: weak
coverage: 0.62
common_nodes: [AudioConcat, AudioCrop, BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, ConditioningZeroOut, CountOccurrences, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), FloatConstant, GetImageRangeFromBatch, GetNode, H3SigmaRefiner, ImageResizeKJv2, Int, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SaveVideo, SelfLiftH3Sampler, SetNode, SynVowTextSplitter, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoInfo, easy cleanGpuUsed, easy compare, easy forLoopEnd, easy forLoopStart, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/多参H3长视频FOR内循环SelfLift二采加速 视频生成优化方案_2105366086060429313.json, 视频生成/文生视频/多参H3长视频二采加速｜FOR内循环SelfLift提效版_2105247019764899841.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_667

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/多参H3长视频FOR内循环SelfLift二采加速 视频生成优化方案_2105366086060429313.json、视频生成/文生视频/多参H3长视频二采加速｜FOR内循环SelfLift提效版_2105247019764899841.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioConcat`
- `AudioCrop`
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `CountOccurrences`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FloatConstant`
- `GetImageRangeFromBatch`
- `GetNode`
- `H3SigmaRefiner`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SaveVideo`
- `SelfLiftH3Sampler`
- `SetNode`
- `SynVowTextSplitter`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `easy cleanGpuUsed`
- `easy compare`
- `easy forLoopEnd`
- `easy forLoopStart`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
