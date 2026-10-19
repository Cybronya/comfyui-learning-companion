---
name: unknown_workflow_video_upscale_latent_upscale_104
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.389667
common_nodes: [Any Switch (rgthree), AudioInfoNode, AudioMerge, CFGGuider, CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, ComfyMathExpression, ComfySwitchNode, ConvertAny2Int, Dapao_LlamaChat, Display Any (rgthree), DualCLIPLoader, EmptyLTXVLatentVideo, ExtractLinesByIndex, Fast Groups Bypasser (rgthree), Float, GetImageSize, GetNode, ImageResizeKJv2, ImageScaleBy, Int, IntToString, IntegerComparison, JjkText, JoinStringMulti, JoinStrings, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAny, PreviewAudio, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, ProcessString, PromptRelayAdvancedOptions, PromptRelayEncode, PurgeVRAM_UTK, RandomNoise, SamplerCustomAdvanced, SaveAudioMP3, SeedVCRun, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, SomethingToString, VAEDecode, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy mathFloat, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2061644573146968066.json, 视频生成/图生视频/2066854552296579074.json, 视频生成/图生视频/2069621183007510529.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_104

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2061644573146968066.json、视频生成/图生视频/2066854552296579074.json、视频生成/图生视频/2069621183007510529.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：39%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AudioInfoNode`
- `AudioMerge`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ConvertAny2Int`
- `Dapao_LlamaChat`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ExtractLinesByIndex`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `GetImageSize`
- `GetNode`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `Int`
- `IntToString`
- `IntegerComparison`
- `JjkText`
- `JoinStringMulti`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PreviewAudio`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ProcessString`
- `PromptRelayAdvancedOptions`
- `PromptRelayEncode`
- `PurgeVRAM_UTK`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveAudioMP3`
- `SeedVCRun`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `SomethingToString`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy mathFloat`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 3 | 100% |
| 高度 | 24 | 24 - 24 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，3 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）
