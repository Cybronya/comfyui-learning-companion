---
name: unknown_workflow_video_sampler_clip_121
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8946
common_nodes: [BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, ModelSamplingSD3, SamplerCustom, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2043889875862163457.json, 视频生成/图生视频/2072161079689572354.json, 视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json, 视频生成/文生视频/LTX2.3图生视频_2071785997519646721.json, 视频生成/文生视频/LTX2.3图生视频_KJ版_参数化_2059632348878163969.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_121

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2043889875862163457.json、视频生成/图生视频/2072161079689572354.json、视频生成/文生视频/LTX2.3图生视频-KJ版-参数化_2069425308750671874.json、视频生成/文生视频/LTX2.3图生视频_2071785997519646721.json、视频生成/文生视频/LTX2.3图生视频_KJ版_参数化_2059632348878163969.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ModelSamplingSD3`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `Int` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `AILab_QwenVL_Advanced` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `StringFunction|pysssss` —— 2/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `LTXVAudioVAEEncode` —— 1/5 个有
- `LoadAudio` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `SolidMask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
