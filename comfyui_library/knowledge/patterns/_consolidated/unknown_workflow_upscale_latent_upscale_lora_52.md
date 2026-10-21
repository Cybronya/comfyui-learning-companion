---
name: unknown_workflow_upscale_latent_upscale_lora_52
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.896167
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2039914785319424002.json, 视频生成/图生视频/2013531899406323713.json, 视频生成/图生视频/2021998636346904578.json, 视频生成/图生视频/2015590078243938306.json, 视频生成/图生视频/2008822192066269185.json, 视频生成/文生视频/LTX2.0 图生视频工作流（48G）_2008873261282627585.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_52

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2039914785319424002.json、视频生成/图生视频/2013531899406323713.json、视频生成/图生视频/2021998636346904578.json、视频生成/图生视频/2015590078243938306.json、视频生成/图生视频/2008822192066269185.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ImageResizeKJv2` —— 5/6 个有
- `LTXVImgToVideoInplace` —— 5/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `CreateVideo` —— 2/6 个有
- `ImpactInt` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `BetaSamplingScheduler` —— 1/6 个有
- `CLIPLoader` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `KSampler` —— 1/6 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `VAELoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
