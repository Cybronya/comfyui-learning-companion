---
name: unknown_workflow_video_upscale_latent_upscale_16
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.58
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-10Eros单图_2057366686122209281.json, 视频生成/图生视频/LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json, 视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2041533297020375042.json, 视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2062063025334603778.json, 视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版首尾帧+PromptRelay_2052004144654893058.json, 视频生成/图生视频/LTX2.3-无字幕版首尾帧-官方工作流-V2_2051899668497477634.json, 视频生成/图生视频/LTX2.3-首中尾三帧生成视频工作流-官方版_2042449515587833857.json, 视频生成/图生视频/LTX2.3-首中尾多帧生成视频工作流-官方版_2041478864202895362.json, 视频生成/图生视频/LTX2.3-首中尾多帧生成视频工作流-官方版_2062080764627472386.json, 视频生成/图生视频/LTX2.3-首中尾帧生成视频工作流-官方版_2051539757435506689.json, 视频生成/图生视频/LTX2.3-首尾帧生成视频工作流-KJ版-V2_2051562392156426242.json, 视频生成/图生视频/LTX2.3-首尾帧生成视频工作流-官方版_2042433612146024450.json, 视频生成/图生视频/ltx2.3电商 首尾帧  服装行业  服装展示_2082418673716912130.json, 视频生成/图生视频/ltx图生视频工作流-官方-自用_2057367378488553473.json, 视频生成/图生视频/【Supermate】LTX2.3-10Eros单图+分镜控制+无字幕版+PromptRelay_2052409270473371649.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_16

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-10Eros单图_2057366686122209281.json、视频生成/图生视频/LTX2.3-PromptRelay-首尾帧-多镜头分镜控制+逻辑控制+长视频+无字幕版_2052407231588646913.json、视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2041533297020375042.json、视频生成/图生视频/LTX2.3-图生视频工作流-官方版_2062063025334603778.json、视频生成/图生视频/LTX2.3-多镜头分镜控制+逻辑控制+长视频+无字幕版首尾帧+PromptRelay_2052004144654893058.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 15 个 workflow 都包含：
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
- `LoadImage` —— 14/15 个有
- `VAEDecodeTiled` —— 14/15 个有
- `GetNode` —— 13/15 个有
- `ImpactFloat` —— 13/15 个有
- `ImpactInt` —— 13/15 个有
- `LTXVAddGuide` —— 13/15 个有
- `SetNode` —— 13/15 个有
- `LTXVPreprocess` —— 12/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/15 个有
- `ImageResizeKJ` —— 10/15 个有
- `LTX2_NAG` —— 10/15 个有
- `LTXVScheduler` —— 10/15 个有
- `VAEDecode` —— 8/15 个有
- `LTXVImgToVideoInplaceKJ` —— 6/15 个有
- `Int` —— 4/15 个有
- `ImageResizeKJv2` —— 3/15 个有
- `PromptRelayEncodeTimeline` —— 3/15 个有
- `Bool` —— 2/15 个有
- `TTResolutionSelector` —— 2/15 个有
- `BatchImagesNode` —— 1/15 个有
- `BerniniPromptEnhancer` —— 1/15 个有
- `DualCLIPLoader` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `PrimitiveStringMultiline` —— 1/15 个有
- `PurgeVRAM_UTK` —— 1/15 个有
- `SDVN Load Image Url` —— 1/15 个有
- `Text` —— 1/15 个有
- `Text Multiline` —— 1/15 个有
- `UNETLoader` —— 1/15 个有
- `VAELoaderKJ` —— 1/15 个有
- `llama_cpp_instruct_adv` —— 1/15 个有
- `llama_cpp_model_loader` —— 1/15 个有
- `llama_cpp_parameters` —— 1/15 个有
- `string_util_StrConcat` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 15 | 100% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，15 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
