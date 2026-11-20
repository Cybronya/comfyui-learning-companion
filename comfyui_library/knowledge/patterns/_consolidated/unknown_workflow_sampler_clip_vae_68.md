---
name: unknown_workflow_sampler_clip_vae_68
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.78225
common_nodes: [BasicScheduler, CLIPTextEncode, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, PathchSageAttentionKJ, SamplerCustom, SimpleMath+, VAEDecodeTiled, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/文生图/（黑鹤UP主的）▶▶LTX23-文生视频流_2051306835285692417.json, 视频生成/图生视频/(黑鹤UP）LTX23-单多图分段控制(任意图数)2_2055789826540097537.json, 视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2056272692512387073.json, 视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2058414222178086914.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_68

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/（黑鹤UP主的）▶▶LTX23-文生视频流_2051306835285692417.json、视频生成/图生视频/(黑鹤UP）LTX23-单多图分段控制(任意图数)2_2055789826540097537.json、视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2056272692512387073.json、视频生成/图生视频/LTX2.3最强漫剧工作流包含音频参考_2058414222178086914.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 3/4 个有
- `CreateVideo` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `ImageFromBatch` —— 3/4 个有
- `LTXSequencer` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `MultiImageLoader` —— 3/4 个有
- `PromptRelayEncodeTimeline` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ComfySwitchNode` —— 2/4 个有
- `DualCLIPLoaderGGUF` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `LTXVAudioVAEEncode` —— 2/4 个有
- `LoadAudioUI` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `MelBandRoFormerModelLoader` —— 2/4 个有
- `MelBandRoFormerSampler` —— 2/4 个有
- `Power Lora Loader (rgthree)` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `SolidMask` —— 2/4 个有
- `UnetLoaderGGUF` —— 2/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 361 | 361 - 361 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 361，观测区间 361 - 361，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
