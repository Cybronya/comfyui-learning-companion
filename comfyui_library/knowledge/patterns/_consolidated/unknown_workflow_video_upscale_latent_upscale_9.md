---
name: unknown_workflow_video_upscale_latent_upscale_9
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.598955
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-10Eros单图_2057366686122209281.json, 视频生成/图生视频/LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json, 视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2041533297020375042.json, 视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2062063025334603778.json, 视频生成/图生视频/LTX2.3-图生视频工作流_2067574333664489473.json, 视频生成/图生视频/LTX2.3-多帧图生视频工作流_2067832932571635714.json, 视频生成/图生视频/LTX2.3-多镜头分镜+逻辑+长视频+无字幕版图生视频_2066056896305516545.json, 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2051939042543063041.json, 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版图生视频PromptRelay_2052408126128832514.json, 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版首尾帧+PromptRelay_2052004144654893058.json, 视频生成/图生视频/LTX2.3-无字幕版首尾帧-官方工作流-V2_2051899668497477634.json, 视频生成/图生视频/LTX2.3-首中尾三帧生成视频工作流-官方版_2042449515587833857.json, 视频生成/图生视频/LTX2.3-首中尾多帧生成视频工作流-官方版_2041478864202895362.json, 视频生成/图生视频/LTX2.3-首中尾多帧生成视频工作流-官方版_2062080764627472386.json, 视频生成/图生视频/LTX2.3-首中尾帧生成视频工作流-官方版_2051539757435506689.json, 视频生成/图生视频/LTX2.3-首尾帧图生视频工作流_2067818323794022402.json, 视频生成/图生视频/LTX2.3-首尾帧生成视频工作流-KJ版-V2_2051562392156426242.json, 视频生成/图生视频/LTX2.3-首尾帧生成视频工作流-官方版_2042433612146024450.json, 视频生成/图生视频/ltx图生视频工作流-官方-自用_2057367378488553473.json, 视频生成/图生视频/【Supermate】LTX2.3-10Eros单图+分镜控制+无字幕版+PromptRelay_2052409270473371649.json, 视频生成/图生视频/【Supermate】LTX2.3-10Eros首尾帧+分镜控制+无字幕版+PromptRelay_2052381787497738241.json, 视频生成/文生视频/LTX2.3-首中尾多帧生成视频工作流-官方版_2050806435688267777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_9

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-10Eros单图_2057366686122209281.json、视频生成/图生视频/LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json、视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2041533297020375042.json、视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2062063025334603778.json、视频生成/图生视频/LTX2.3-图生视频工作流_2067574333664489473.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 22 个 workflow 都包含：
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
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VHS_VideoCombine`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 21/22 个有
- `VAEDecodeTiled` —— 21/22 个有
- `LTXVPreprocess` —— 19/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 19/22 个有
- `LTXVAddGuide` —— 16/22 个有
- `GetNode` —— 14/22 个有
- `ImpactFloat` —— 14/22 个有
- `ImpactInt` —— 14/22 个有
- `LTX2_NAG` —— 14/22 个有
- `LTXVScheduler` —— 14/22 个有
- `SetNode` —— 14/22 个有
- `VAEDecode` —— 12/22 个有
- `ImageResizeKJ` —— 11/22 个有
- `PromptRelayEncodeTimeline` —— 7/22 个有
- `LTXVImgToVideoInplaceKJ` —— 5/22 个有
- `Int` —— 4/22 个有
- `ImageResizeKJv2` —— 3/22 个有
- `easy float` —— 3/22 个有
- `Bool` —— 2/22 个有
- `Fast Groups Bypasser (rgthree)` —— 2/22 个有
- `ImageResize+` —— 2/22 个有
- `TTResolutionSelector` —— 2/22 个有
- `VAELoaderKJ` —— 2/22 个有
- `DualCLIPLoader` —— 1/22 个有
- `LTX2SamplingPreviewOverride` —— 1/22 个有
- `PrimitiveStringMultiline` —— 1/22 个有
- `SDVN Load Image Url` —— 1/22 个有
- `UNETLoader` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 22 | 100% |
| 高度 | 25 | 24 - 30 | 22 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，22 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 30，22 个样本，取值集中（一致性 94%）
