---
name: unknown_workflow_upscale_latent_upscale_sampler_6
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.848818
common_nodes: [ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, VAEDecodeTiled]
problems: []
missing: []
members: [数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json, 数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json, 数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json, 数字人/数字人/LTX25-音频驱动口播数字人_2114293983605252098.json, 视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json, 视频生成/图生视频/LTX2.3数字人V3 Prompt Relay提示词分段控制_2073319876273463297.json, 视频生成/图生视频/LTX2.3数字人—支持双人_2073313777977745410.json, 视频生成/图生视频/LTX2.3音频图片生成视频_2051636070026096642.json, 视频生成/图生视频/LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642.json, 视频生成/图生视频/LTX2.5数字人+提示词反推_2089579904223498242.json, 视频生成/图生视频/Ltx2.3 _mv数字人_2044558768721108993.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json、数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json、数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json、数字人/数字人/LTX25-音频驱动口播数字人_2114293983605252098.json、视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 11 个 workflow 都包含：
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `TrimAudioDuration` —— 10/11 个有
- `CreateVideo` —— 8/11 个有
- `PrimitiveStringMultiline` —— 8/11 个有
- `ResizeImagesByLongerEdge` —— 8/11 个有
- `SaveVideo` —— 8/11 个有
- `CLIPLoader` —— 7/11 个有
- `LTXVDualCFGGuider` —— 7/11 个有
- `UNETLoader` —— 7/11 个有
- `VAELoader` —— 7/11 个有
- `CLIPTextEncode` —— 6/11 个有
- `AudioInfo` —— 5/11 个有
- `ConditioningZeroOut` —— 5/11 个有
- `PromptRelaySmartEncode` —— 5/11 个有
- `CFGGuider` —— 4/11 个有
- `CheckpointLoaderSimple` —— 4/11 个有
- `LTXAVTextEncoderLoader` —— 4/11 个有
- `LTXVAudioVAELoader` —— 4/11 个有
- `LTXVCropGuides` —— 4/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `CR Text` —— 3/11 个有
- `ResolutionSelector` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `PrimitiveFloat` —— 2/11 个有
- `easy cleanGpuUsed` —— 2/11 个有
- `AudioCrop` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `MelBandRoFormerModelLoader` —— 1/11 个有
- `MelBandRoFormerSampler` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `RecordAudio` —— 1/11 个有
- `SoundFlow_GetLength` —— 1/11 个有
- `llama_cpp_instruct_adv` —— 1/11 个有
- `llama_cpp_model_loader` —— 1/11 个有
- `llama_cpp_parameters` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
