---
key: 视频生成/图生视频/LTX2.3 多帧参考-参考音色-AddGuide-V2_2061644573146968066.json
name: LTX2.3 多帧参考-参考音色-AddGuide-V2_2061644573146968066.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 多帧参考-参考音色-AddGuide-V2_2061644573146968066.json
hash: 9cddd00d2e9338ab
coverage: 0.387324
learned_at: 2026-10-15 22:38:55
nodes: [ManualSigmas, KSamplerSelect, KSamplerSelect, SetNode, SetNode, LTXVConditioning, SamplerCustomAdvanced, LTXVConcatAVLatent, GetNode, ManualSigmas, JjkText, JjkText, PreviewAny, GetNode, LTXVScheduler, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, PrimitiveInt, SetNode, SetNode, PrimitiveFloat, SetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, PrimitiveInt, LoadImage, CFGGuider, GetNode, GetNode, SolidMask, GetNode, MathExpression|pysssss, MelBandRoFormerModelLoader, SetLatentNoiseMask, Any Switch (rgthree), AudioInfoNode, GetNode, SetNode, Display Any (rgthree), SetNode, MelBandRoFormerSampler, GetNode, LTXVAudioVAEEncode, SetNode, LTXVEmptyLatentAudio, GetNode, GetNode, SetNode, LTXVConcatAVLatent, GetNode, PreviewAudio, GetNode, ImageResizeKJv2, Reroute, ImageResizeKJv2, Reroute, ImageResizeKJv2, GetNode, Reroute, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), Float, Float, Float, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetNode, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVCropGuides, VAEDecode, CR Text Concatenate, CR Text Concatenate, ProcessString, ExtractLinesByIndex, SetNode, SetNode, SetNode, LTXVCropGuides, CFGGuider, LTXVAddGuideMulti, PathchSageAttentionKJ, PurgeVRAM_UTK, GetNode, GetNode, IntToString, IntegerComparison, Reroute, MathExpression|pysssss, JoinStrings, ComfySwitchNode, IntToString, JoinStrings, IntToString, ComfySwitchNode, ComfySwitchNode, GetNode, MathExpression|pysssss, JoinStrings, IntegerComparison, IntegerComparison, Any Switch (rgthree), easy mathFloat, MathExpression|pysssss, easy mathFloat, easy mathFloat, SetNode, VHS_VideoCombine, SomethingToString, GetNode, PreviewAny, GetNode, GetNode, GetNode, GetNode, PreviewAny, Dapao_LlamaChat, RandomNoise, GetNode, GetNode, SimpleMath+, SetNode, GetNode, GetNode, SetNode, ModelPatchTorchSettings, LoadImage, LoadImage, LoadImage, GetNode, Reroute, Reroute, PreviewAny, LTX2SamplingPreviewOverride, LTXVAddGuideMulti, VAELoaderKJ, ConvertAny2Int, LoadAudio, SetNode, Any Switch (rgthree), GetNode, SetNode, Any Switch (rgthree), CR Text Concatenate, GetNode, Any Switch (rgthree), SetNode, GetNode, ComfyMathExpression, SetNode, Int, SetNode, IntToString, Float, Any Switch (rgthree), SetNode, GetNode, Any Switch (rgthree), GetNode, Any Switch (rgthree), SetNode, JoinStringMulti, easy showAnything, SetNode, SetNode, easy showAnything, easy showAnything, Reroute, SetNode, ImageResizeKJv2, GetImageSize, ImageScaleBy, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, Reroute, Fast Groups Bypasser (rgthree), LTXVAudioVAEDecode, SetNode, SaveAudioMP3, MelBandRoFormerSampler, SeedVCRun, AudioMerge, MelBandRoFormerSampler, MelBandRoFormerModelLoader, GetNode, Any Switch (rgthree), GetNode, GetNode, LoadAudio, PrimitiveStringMultiline, MarkdownNote, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, CLIPTextEncode, PreviewAny, CheckpointLoaderSimple, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, MarkdownNote, SetNode, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, SetNode, SetNode, SetNode, CheckpointLoaderSimple, SetNode, LTXAVTextEncoderLoader, SetNode, LTXVAudioVAELoader, Note, PromptRelayAdvancedOptions, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, PrimitiveStringMultiline, PromptRelayEncode, Note, MarkdownNote, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), LatentUpscaleModelLoader, Fast Groups Bypasser (rgthree), MarkdownNote, SetNode, GetNode, SimpleMath+, SimpleMath+, GetNode, GetNode, SimpleMath+, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX2.3 多帧参考-参考音色-AddGuide-V2_2061644573146968066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061644573146968066.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（284 个）：
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `ManualSigmas`
- `JjkText`
- `JjkText`
- `PreviewAny`
- `GetNode`
- `LTXVScheduler`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `PrimitiveInt`
- `LoadImage`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `SetLatentNoiseMask`
- `Any Switch (rgthree)`
- `AudioInfoNode`
- `GetNode`
- `SetNode`
- `Display Any (rgthree)`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `PreviewAudio`
- `GetNode`
- `ImageResizeKJv2`
- `Reroute`
- `ImageResizeKJv2`
- `Reroute`
- `ImageResizeKJv2`
- `GetNode`
- `Reroute`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Float`
- `Float`
- `Float`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `CR Text Concatenate`
- `CR Text Concatenate`
- `ProcessString`
- `ExtractLinesByIndex`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVAddGuideMulti`
- `PathchSageAttentionKJ`
- `PurgeVRAM_UTK`
- `GetNode`
- `GetNode`
- `IntToString`
- `IntegerComparison`
- `Reroute`
- `MathExpression|pysssss`
- `JoinStrings`
- `ComfySwitchNode`
- `IntToString`
- `JoinStrings`
- `IntToString`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `GetNode`
- `MathExpression|pysssss`
- `JoinStrings`
- `IntegerComparison`
- `IntegerComparison`
- `Any Switch (rgthree)`
- `easy mathFloat`
- `MathExpression|pysssss`
- `easy mathFloat`
- `easy mathFloat`
- `SetNode`
- `VHS_VideoCombine`
- `SomethingToString`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `Dapao_LlamaChat`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `Reroute`
- `Reroute`
- `PreviewAny`
- `LTX2SamplingPreviewOverride`
- `LTXVAddGuideMulti`
- `VAELoaderKJ`
- `ConvertAny2Int`
- `LoadAudio`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `SetNode`
- `Any Switch (rgthree)`
- `CR Text Concatenate`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `Int`
- `SetNode`
- `IntToString`
- `Float`
- `Any Switch (rgthree)`
- `SetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `SetNode`
- `JoinStringMulti`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `Reroute`
- `SetNode`
- `ImageResizeKJv2`
- `GetImageSize`
- `ImageScaleBy`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SaveAudioMP3`
- `MelBandRoFormerSampler` ★核心
- `SeedVCRun`
- `AudioMerge`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `MarkdownNote`
- `SetNode`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `LTXVAudioVAELoader`
- `Note`
- `PromptRelayAdvancedOptions`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PromptRelayEncode`
- `Note`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `LatentUpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `JjkText`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **39%**（110/284）

**有卡**：`ManualSigmas`、`KSamplerSelect`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`LTXVScheduler`、`EmptyLTXVLatentVideo`、`LoadImage`、`CFGGuider`、`SolidMask`、`MathExpression|pysssss`、`MelBandRoFormerModelLoader`、`SetLatentNoiseMask`、`AudioInfoNode`、`Display Any (rgthree)`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`LTXVEmptyLatentAudio`、`PreviewAudio`、`ImageResizeKJv2`、`Float`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVCropGuides`、`VAEDecode`、`CR Text Concatenate`、`ProcessString`、`ExtractLinesByIndex`、`LTXVAddGuideMulti`、`PathchSageAttentionKJ`、`PurgeVRAM_UTK`、`IntToString`、`IntegerComparison`、`JoinStrings`、`easy mathFloat`、`VHS_VideoCombine`、`SomethingToString`、`Dapao_LlamaChat`、`RandomNoise`、`SimpleMath+`、`ModelPatchTorchSettings`、`LTX2SamplingPreviewOverride`、`VAELoaderKJ`、`ConvertAny2Int`、`LoadAudio`、`ComfyMathExpression`、`Int`、`JoinStringMulti`、`GetImageSize`、`ImageScaleBy`、`LTXVAudioVAEDecode`、`SaveAudioMP3`、`SeedVCRun`、`AudioMerge`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`PromptRelayAdvancedOptions`、`PromptRelayEncode`、`LatentUpscaleModelLoader`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
