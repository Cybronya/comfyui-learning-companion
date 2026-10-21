---
name: unknown_workflow_video_upscale_latent_upscale_144
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.513
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, Float, GetNode, ImageScaleBy, Int, Int to String, InversionDemoLazySwitch, KSamplerSelect, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, Seed (rgthree), SetNode, StringFunction|pysssss, Text, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/2054885295354589185.json, 视频生成/图生视频/2054112708936650753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_144

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2054885295354589185.json、视频生成/图生视频/2054112708936650753.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `Float`
- `GetNode`
- `ImageScaleBy`
- `Int`
- `Int to String`
- `InversionDemoLazySwitch`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SetNode`
- `StringFunction|pysssss`
- `Text`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `AudioInfo` —— 1/2 个有
- `CM_FloatToInt` —— 1/2 个有
- `LTXFloatToInt` —— 1/2 个有
- `LTXVAudioVAEDecode` —— 1/2 个有
- `LTXVAudioVAEEncode` —— 1/2 个有
- `LTXVEmptyLatentAudio` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `MathExpression_UTK` —— 1/2 个有
- `MelBandRoFormerModelLoader` —— 1/2 个有
- `MelBandRoFormerSampler` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `SolidMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
