---
name: unknown_workflow_upscale_latent_upscale_sampler_15
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.843714
common_nodes: [CLIPLoader, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVDualCFGGuider, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json, 数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json, 数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json, 数字人/数字人/LTX25-音频驱动口播数字人_2114293983605252098.json, 视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json, 视频生成/图生视频/LTX2.5数字+Prompt+Relay提示词分段控制_2088161703614832642.json, 视频生成/图生视频/LTX2.5数字人+提示词反推_2089579904223498242.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_15

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json、数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json、数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json、数字人/数字人/LTX25-音频驱动口播数字人_2114293983605252098.json、视频生成/图生视频/LTX-2.5 音频驱动数字人口播视频｜自然口型｜微表情｜动作同步_2095839296384229377.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVDualCFGGuider`
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
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TrimAudioDuration` —— 6/7 个有
- `AudioInfo` —— 4/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `CreateVideo` —— 4/7 个有
- `PrimitiveStringMultiline` —— 4/7 个有
- `PromptRelaySmartEncode` —— 4/7 个有
- `ResizeImagesByLongerEdge` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `CLIPTextEncode` —— 3/7 个有
- `CR Text` —— 3/7 个有
- `ResolutionSelector` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `AudioCrop` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `llama_cpp_instruct_adv` —— 1/7 个有
- `llama_cpp_model_loader` —— 1/7 个有
- `llama_cpp_parameters` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
