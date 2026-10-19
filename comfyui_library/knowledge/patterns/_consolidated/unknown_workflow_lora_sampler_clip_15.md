---
name: unknown_workflow_lora_sampler_clip_15
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8359
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, RunningHub_VoxCPM_Generate, RunningHub_VoxCPM_LoadModel, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, SoundFlow_GetLength, TrimAudioDuration, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2058101725361430530.json, 视频生成/图生视频/2054789125802340354.json, 视频生成/图生视频/2054780723667718145.json, 视频生成/图生视频/2058082401418563586.json, 视频生成/图生视频/2058097242602557441.json, 视频生成/图生视频/2058053097523601410.json, 视频生成/图生视频/2058106663583969282.json, 视频生成/图生视频/2058106651525345282.json, 视频生成/图生视频/2057761252751003649.json, 视频生成/图生视频/2058134319910187009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2058101725361430530.json、视频生成/图生视频/2054789125802340354.json、视频生成/图生视频/2054780723667718145.json、视频生成/图生视频/2058082401418563586.json、视频生成/图生视频/2058097242602557441.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
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
- `RunningHub_VoxCPM_Generate`
- `RunningHub_VoxCPM_LoadModel`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `SoundFlow_GetLength`
- `TrimAudioDuration`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 9/10 个有
- `LTXVAudioVAEDecode` —— 9/10 个有
- `LTXVLatentUpsampler` —— 9/10 个有
- `LatentUpscaleModelLoader` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `LTXVImgToVideoInplace` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `LTXVImgToVideoInplaceKJ` —— 7/10 个有
- `PrimitiveBoolean` —— 7/10 个有
- `ResizeImagesByLongerEdge` —— 7/10 个有
- `FloatConstant` —— 4/10 个有
- `LTXVEmptyLatentAudio` —— 4/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/10 个有
- `PreviewAny` —— 4/10 个有
- `Qwen3ASRLoader_DFT` —— 4/10 个有
- `Qwen3ASRTranscribe_DFT` —— 4/10 个有
- `ResizeImageMaskNode` —— 4/10 个有
- `SimpleMath+` —— 4/10 个有
- `StringConcatenate` —— 4/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `LTXVChunkFeedForward` —— 2/10 个有
- `ModelPatchTorchSettings` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `TextCombinerTwo` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `GetImageSize` —— 1/10 个有
- `LTXVAddGuide` —— 1/10 个有
- `SamplerEulerAncestral` —— 1/10 个有

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
