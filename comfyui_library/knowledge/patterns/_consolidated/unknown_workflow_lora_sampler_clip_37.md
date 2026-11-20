---
name: unknown_workflow_lora_sampler_clip_37
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.677
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, easy int, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/74wsspduoren_2052611683218145282.json, 视频生成/图生视频/LTX2.3-图生视频工作流_2067574333664489473.json, 视频生成/图生视频/LTX2.3-多帧图生视频工作流_2067832932571635714.json, 视频生成/图生视频/LTX2.3-多镜头分镜+逻辑+长视频+无字幕版图生视频_2066056896305516545.json, 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2051939042543063041.json, 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2052408126128832514.json, 视频生成/图生视频/LTX2.3-首尾帧图生视频工作流_2067818323794022402.json, 视频生成/图生视频/LTX2.3图生视频三段式采样_2044724693445382146.json, 视频生成/图生视频/【LTX2.3+PromptRelay-V2】-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频_2058353151778058241.json, 视频生成/图生视频/【Supermate】LTX2.3-10Eros首尾帧+分镜控制+无字幕版+PromptRelay_2052381787497738241.json, 视频生成/文生视频/LTX2.3-首中尾多帧生成视频工作流-官方版_2050806435688267777.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/反推提示词/74wsspduoren_2052611683218145282.json、视频生成/图生视频/LTX2.3-图生视频工作流_2067574333664489473.json、视频生成/图生视频/LTX2.3-多帧图生视频工作流_2067832932571635714.json、视频生成/图生视频/LTX2.3-多镜头分镜+逻辑+长视频+无字幕版图生视频_2066056896305516545.json、视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2051939042543063041.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 10/11 个有
- `LTXVImgToVideoInplace` —— 10/11 个有
- `LTXVLatentUpsampler` —— 10/11 个有
- `LTXVPreprocess` —— 10/11 个有
- `LatentUpscaleModelLoader` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `VHS_VideoCombine` —— 10/11 个有
- `LTXVScheduler` —— 8/11 个有
- `LTX2_NAG` —— 5/11 个有
- `PromptRelayEncodeTimeline` —— 5/11 个有
- `VAEDecode` —— 5/11 个有
- `easy float` —— 5/11 个有
- `LTXVAddGuide` —— 4/11 个有
- `GetNode` —— 2/11 个有
- `ImageResize+` —— 2/11 个有
- `ImageResizeKJ` —— 2/11 个有
- `ImpactFloat` —— 2/11 个有
- `ImpactInt` —— 2/11 个有
- `LTX2SamplingPreviewOverride` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `VAELoaderKJ` —— 2/11 个有
- `CreateVideo` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `ImageScaleBy` —— 1/11 个有
- `RTXVideoSuperResolution` —— 1/11 个有
- `SaveVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 24 | 24 - 30 | 11 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 30，11 个样本，取值集中（一致性 91%）
