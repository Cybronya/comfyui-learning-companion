---
name: unknown_workflow_lora_sampler_clip_85
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.73
common_nodes: [BasicScheduler, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, INTConstant, ImageFromBatch, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXSequencer, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, MultiImageLoader, PathchSageAttentionKJ, PromptRelayEncodeTimeline, SamplerCustom, SimpleMath+, VAEDecodeTiled, VAELoaderKJ, VisualizeSigmasKJ, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2055789826540097537.json, 视频生成/图生视频/2056272692512387073.json, 视频生成/图生视频/2058414222178086914.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2055789826540097537.json、视频生成/图生视频/2056272692512387073.json、视频生成/图生视频/2058414222178086914.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageFromBatch`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXSequencer`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MultiImageLoader`
- `PathchSageAttentionKJ`
- `PromptRelayEncodeTimeline`
- `SamplerCustom`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/3 个有
- `CreateVideo` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `LTXVAudioVAEEncode` —— 2/3 个有
- `LoadAudioUI` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `MelBandRoFormerModelLoader` —— 2/3 个有
- `MelBandRoFormerSampler` —— 2/3 个有
- `PreviewAudio` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `SetLatentNoiseMask` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `SolidMask` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `DualCLIPLoaderGGUF` —— 1/3 个有
- `Power Lora Loader (rgthree)` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 361 - 361 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 361 - 361，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
