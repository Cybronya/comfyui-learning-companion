---
name: unknown_workflow_lora_sampler_clip_36
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.840083
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, SoundFlow_GetLength, TrimAudioDuration, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3_数字人口播_6.2_(首尾帧，Style Transition)_2058101725361430530.json, 视频生成/图生视频/LTX2.3_数字人口播_v1.0_（mv数字人）_2054790441681342465.json, 视频生成/图生视频/LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json, 视频生成/图生视频/LTX2.3_数字人口播_v2.0_（融合音频生成，效果未必比1.0好）_2054789125802340354.json, 视频生成/图生视频/LTX2.3_数字人口播_v2.1_（融合音频生成，效果未必比1.1好）_2054780723667718145.json, 视频生成/图生视频/LTX2.3_数字人口播_v3.1_（首尾帧）_2058082401418563586.json, 视频生成/图生视频/LTX2.3_数字人口播_v5.0_（首尾帧）_2058097242602557441.json, 视频生成/图生视频/LTX2.3_数字人口播_v5.1_（首尾帧）_2058053097523601410.json, 视频生成/图生视频/LTX2.3_数字人口播_v6.0_（首尾帧，抖动问题未解决）_2058106663583969282.json, 视频生成/图生视频/LTX2.3_数字人口播_v6.1_（首尾帧，未解决抖动问题）_2058106651525345282.json, 视频生成/图生视频/LTX2.3_数字人口播_v6.3_(首尾帧，Fisher优化版)_2057761252751003649.json, 视频生成/图生视频/LTX2.3_数字人口播_v6.3_(首尾帧，Fisher优化版)_2058134319910187009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_36

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/LTX2.3_数字人口播_6.2_(首尾帧，Style Transition)_2058101725361430530.json、视频生成/图生视频/LTX2.3_数字人口播_v1.0_（mv数字人）_2054790441681342465.json、视频生成/图生视频/LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json、视频生成/图生视频/LTX2.3_数字人口播_v2.0_（融合音频生成，效果未必比1.0好）_2054789125802340354.json、视频生成/图生视频/LTX2.3_数字人口播_v2.1_（融合音频生成，效果未必比1.1好）_2054780723667718145.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 11/12 个有
- `LTXVAudioVAEDecode` —— 11/12 个有
- `LTXVLatentUpsampler` —— 11/12 个有
- `LatentUpscaleModelLoader` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `CR Text` —— 10/12 个有
- `CreateVideo` —— 10/12 个有
- `LTXVImgToVideoInplace` —— 10/12 个有
- `RunningHub_VoxCPM_Generate` —— 10/12 个有
- `RunningHub_VoxCPM_LoadModel` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `PrimitiveBoolean` —— 9/12 个有
- `ResizeImagesByLongerEdge` —— 9/12 个有
- `LTXVImgToVideoInplaceKJ` —— 7/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/12 个有
- `PreviewAny` —— 5/12 个有
- `Qwen3ASRLoader_DFT` —— 5/12 个有
- `Qwen3ASRTranscribe_DFT` —— 5/12 个有
- `ResizeImageMaskNode` —— 5/12 个有
- `StringConcatenate` —— 5/12 个有
- `FloatConstant` —— 4/12 个有
- `LTXVEmptyLatentAudio` —— 4/12 个有
- `SimpleMath+` —— 4/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `ImageResizeKJv2` —— 2/12 个有
- `LTXVChunkFeedForward` —— 2/12 个有
- `ModelPatchTorchSettings` —— 2/12 个有
- `PathchSageAttentionKJ` —— 2/12 个有
- `RH_LLMAPI_Pro_Node` —— 2/12 个有
- `TextCombinerTwo` —— 2/12 个有
- `VHS_VideoCombine` —— 2/12 个有
- `easy showAnything` —— 2/12 个有
- `GetImageSize` —— 1/12 个有
- `LTXVAddGuide` —— 1/12 个有
- `SamplerEulerAncestral` —— 1/12 个有

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
