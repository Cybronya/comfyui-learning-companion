---
name: unknown_workflow_video_lora_sampler_852
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5715
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LTXVSpatioTemporalTiledVAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SigmasPreview, SimpleCalculatorKJ, SolidMask, UNETLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json, 视频生成/图生视频/LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_852

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-数字人-自定义音频图像(抖音复现)_2044784831422275586.json、视频生成/图生视频/LTX2.3-音频数字人(双采样高清版)_2050231422836846593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SigmasPreview`
- `SimpleCalculatorKJ`
- `SolidMask`
- `UNETLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `LTXVImgToVideoConditionOnly` —— 1/2 个有
- `LTXVLatentUpsampler` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LatentUpscaleModelLoader` —— 1/2 个有
- `Mute / Bypass Relay (rgthree)` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `PreviewTextNode` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TrimAudioDuration` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
