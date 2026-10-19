---
name: unknown_workflow_video_upscale_latent_upscale_105
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.618333
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2050734311749505025.json, 视频生成/图生视频/2044724693445382146.json, 视频生成/图生视频/2082418673716912130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_105

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2050734311749505025.json、视频生成/图生视频/2044724693445382146.json、视频生成/图生视频/2082418673716912130.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
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
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `Text` —— 2/3 个有
- `llama_cpp_instruct_adv` —— 2/3 个有
- `llama_cpp_model_loader` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `BatchImagesNode` —— 1/3 个有
- `BerniniPromptEnhancer` —— 1/3 个有
- `CustomAddLabel` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageResizeKJ` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `ImpactFloat` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LTX2_NAG` —— 1/3 个有
- `LTXVAddGuide` —— 1/3 个有
- `LTXVImgToVideoInplaceKJ` —— 1/3 个有
- `PurgeVRAM_UTK` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `UNETLoader` —— 1/3 个有
- `VAELoaderKJ` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy float` —— 1/3 个有
- `string_util_StrConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
