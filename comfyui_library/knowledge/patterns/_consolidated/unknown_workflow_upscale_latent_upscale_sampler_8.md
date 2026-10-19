---
name: unknown_workflow_upscale_latent_upscale_sampler_8
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6928
common_nodes: [ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, UNETLoader, VAEDecodeTiled, VAELoader]
problems: []
missing: []
members: [数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json, 数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json, 数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json, 视频生成/图生视频/2045851201853464578.json, 视频生成/图生视频/2042456955284889601.json, 视频生成/图生视频/2045890888169164802.json, 视频生成/图生视频/2050462775322923010.json, 视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2035972657669214210.json, 视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2050177856264785921.json, 视频生成/文生视频/图生视频，上传图像＋音频，即可做出你想要的短视频，短剧，_2043763255142785026.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_8

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/LTX2.5数字+Prompt+Relay提示词分段控制_2087942580880367617.json、数字人/数字人/LTX2.5数字-agent调用版_2100471648406294530.json、数字人/数字人/LTX2.5，音频驱动口播数字人_2089890373689757697.json、视频生成/图生视频/2045851201853464578.json、视频生成/图生视频/2042456955284889601.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 10 个 workflow 都包含：
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
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioInfo` —— 9/10 个有
- `CreateVideo` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `ResizeImagesByLongerEdge` —— 9/10 个有
- `SaveVideo` —— 9/10 个有
- `CLIPTextEncode` —— 8/10 个有
- `AudioCrop` —— 7/10 个有
- `CFGGuider` —— 7/10 个有
- `Display Any (rgthree)` —— 7/10 个有
- `DualCLIPLoader` —— 7/10 个有
- `LTXVChunkFeedForward` —— 7/10 个有
- `LTXVCropGuides` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `PathchSageAttentionKJ` —— 7/10 个有
- `PrimitiveFloat` —— 7/10 个有
- `ShowText|pysssss` —— 7/10 个有
- `SimpleMath+` —— 7/10 个有
- `TextInput_` —— 7/10 个有
- `VAELoaderKJ` —— 7/10 个有
- `RH_LLMAPI_NODE` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `CLIPLoader` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `JoinStrings` —— 3/10 个有
- `LTXVDualCFGGuider` —— 3/10 个有
- `Label (rgthree)` —— 3/10 个有
- `MelBandRoFormerModelLoader` —— 3/10 个有
- `MelBandRoFormerSampler` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `PreviewAudio` —— 3/10 个有
- `SimpleCalculatorKJ` —— 3/10 个有
- `llama_cpp_instruct_adv` —— 3/10 个有
- `llama_cpp_model_loader` —— 3/10 个有
- `llama_cpp_parameters` —— 3/10 个有
- `llama_cpp_unload_model` —— 3/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `PromptRelaySmartEncode` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `ResolutionSelector` —— 1/10 个有
- `VHS_VideoCombine` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
