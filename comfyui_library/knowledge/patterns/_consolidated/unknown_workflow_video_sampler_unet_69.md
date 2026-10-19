---
name: unknown_workflow_video_sampler_unet_69
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.716333
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, PathchSageAttentionKJ, PreviewImage, PromptRelayEncode, SamplerCustom, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2045841411437760514.json, 视频生成/图生视频/2046880656696807426.json, 视频生成/文生视频/prompt_relay_ltx23_2046846063507677186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_69

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2045841411437760514.json、视频生成/图生视频/2046880656696807426.json、视频生成/文生视频/prompt_relay_ltx23_2046846063507677186.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PromptRelayEncode`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ResizeImagesByLongerEdge` —— 1/3 个有
- `SimpleCalculatorKJ` —— 1/3 个有
- `StringReplace` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 241 - 489 | 3 | 64% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 241 - 489，3 个样本
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
