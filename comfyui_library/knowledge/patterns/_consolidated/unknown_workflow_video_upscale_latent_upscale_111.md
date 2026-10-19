---
name: unknown_workflow_video_upscale_latent_upscale_111
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.635667
common_nodes: [Audio Duration (mtb), AudioCrop, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfySwitchNode, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoader, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, PreviewAudio, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleMath+, SolidMask, TextGenerateLTX2Prompt, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/2045415102794436609.json, 视频生成/图生视频/2045669408932110338.json, 视频生成/图生视频/2051244321340436482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_111

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2045415102794436609.json、视频生成/图生视频/2045669408932110338.json、视频生成/图生视频/2051244321340436482.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfySwitchNode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `TextGenerateLTX2Prompt`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `SomethingToString` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `llama_cpp_instruct_adv` —— 1/3 个有
- `llama_cpp_model_loader` —— 1/3 个有
- `llama_cpp_parameters` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
