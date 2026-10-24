---
name: unknown_workflow_upscale_latent_upscale_lora_56
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8958
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/电商内衣换装+视频生成_2039914785319424002.json, 视频生成/图生视频/短剧对白视频LTX2.0 图生视频LTX2.0 图生视频_2013531899406323713.json, 视频生成/图生视频/短剧对白视频LTX2.0 图生视频LTX2.0 图生视频_2021998636346904578.json, 视频生成/图生视频/音画同处LTX2.0！【又快又好】_2015590078243938306.json, 视频生成/图生视频/🥗开源视频新秀LTX2.0！【图生视频】工作流🥗_2008822192066269185.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_56

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/电商内衣换装+视频生成_2039914785319424002.json、视频生成/图生视频/短剧对白视频LTX2.0 图生视频LTX2.0 图生视频_2013531899406323713.json、视频生成/图生视频/短剧对白视频LTX2.0 图生视频LTX2.0 图生视频_2021998636346904578.json、视频生成/图生视频/音画同处LTX2.0！【又快又好】_2015590078243938306.json、视频生成/图生视频/🥗开源视频新秀LTX2.0！【图生视频】工作流🥗_2008822192066269185.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 4/5 个有
- `LTXVImgToVideoInplace` —— 4/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `CreateVideo` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `BetaSamplingScheduler` —— 1/5 个有
- `CLIPLoader` —— 1/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `KSampler` —— 1/5 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/5 个有
- `UNETLoader` —— 1/5 个有
- `VAELoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
