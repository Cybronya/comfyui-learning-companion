---
name: unknown_workflow_video_lora_sampler_487
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.85925
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoaderGGUF, EmptyLTXVLatentVideo, ImpactConditionalBranch, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PlaySound|pysssss, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, UnetLoaderGGUF, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2056632746793070593.json, 视频生成/图生视频/2053296155462782978.json, 视频生成/文生视频/LTX2.3 PromptRelay 四合一全能音视频工作流_2054463722072092674.json, 视频生成/文生视频/LTX2.3 四合一全能音视频工作流_2047235485235417089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_487

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2056632746793070593.json、视频生成/图生视频/2053296155462782978.json、视频生成/文生视频/LTX2.3 PromptRelay 四合一全能音视频工作流_2054463722072092674.json、视频生成/文生视频/LTX2.3 四合一全能音视频工作流_2047235485235417089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoaderGGUF`
- `EmptyLTXVLatentVideo`
- `ImpactConditionalBranch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `UnetLoaderGGUF`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVEnhanceAVideoKJ` —— 3/4 个有
- `PreviewAudio` —— 3/4 个有
- `GetImageSize` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `LTXVAddGuide` —— 2/4 个有
- `LTXVImgToVideoInplace` —— 2/4 个有
- `LTXVLatentUpsampler` —— 2/4 个有
- `LTXVReferenceAudio` —— 2/4 个有
- `LatentUpscaleModelLoader` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `PromptRelayEncodeTimeline` —— 2/4 个有
- `ResizeImagesByLongerEdge` —— 2/4 个有
- `SamplerEulerAncestral` —— 2/4 个有
- `VHS_LoadAudioUpload` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `TrimAudioDuration` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
