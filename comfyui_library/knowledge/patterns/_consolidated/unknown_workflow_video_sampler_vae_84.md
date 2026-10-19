---
name: unknown_workflow_video_sampler_vae_84
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.726833
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, PreviewImage, SamplerCustom, SetNode, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2055227152429273089.json, 视频生成/图生视频/2047475119030800385.json, 视频生成/图生视频/2046925023830614018.json, 视频生成/图生视频/2050454214081556481.json, 视频生成/图生视频/2050514926795538434.json, 视频生成/文生视频/LTX2.3_PromptRelay_VLM 高级工作流_2047601506693685249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_84

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2055227152429273089.json、视频生成/图生视频/2047475119030800385.json、视频生成/图生视频/2046925023830614018.json、视频生成/图生视频/2050454214081556481.json、视频生成/图生视频/2050514926795538434.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `PreviewImage`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `PromptRelayEncode` —— 4/6 个有
- `UNETLoader` —— 4/6 个有
- `CR Float To Integer` —— 2/6 个有
- `CheckpointLoaderSimple` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `PromptRelayEncodeTimeline` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `StringReplace` —— 2/6 个有
- `ttN float` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `AILab_QwenVL_Advanced` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `MultiImageLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 377 | 305 - 505 | 6 | 77% |
| 高度 | 25 | 25 - 50 | 6 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 377，观测区间 305 - 505，6 个样本
- 高度 中位数 25，观测区间 25 - 50，6 个样本
