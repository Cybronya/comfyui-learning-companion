---
key: 视频生成/图生视频/LTX2.3 I2V FLFV MV Lip Sync 首尾帧音乐视频对口形_2075065970321874946.json
name: LTX2.3 I2V FLFV MV Lip Sync 首尾帧音乐视频对口形_2075065970321874946.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2075065970321874946.json
hash: d6898e881d1f5324
coverage: 0.568966
learned_at: 2026-10-15 22:41:21
nodes: [GetNode, ModelPatchTorchSettings, LTX2SamplingPreviewOverride, GetNode, GetNode, LTX2_NAG, SetNode, PathchSageAttentionKJ, SamplerCustomAdvanced, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, GetNode, SetNode, SetNode, KSamplerSelect, BasicScheduler, Text Concatenate, SamplerCustomAdvanced, SimpleMath+, SetNode, LTXVConditioning, EmptyLTXVLatentVideo, CLIPTextEncode, GetNode, CLIPTextEncode, LTXVCropGuides, CFGGuider, GetNode, LTXVLatentUpsampler, GetNode, BasicScheduler, GetNode, CFGGuider, SetNode, LTXVConcatAVLatent, PrimitiveFloat, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, LTXVAudioVAEDecode, GetNode, SetNode, GetNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), GetNode, SimpleMath+, GetNode, MelBandRoFormerSampler, PainterAudioLength, LTXVAudioVAEEncode, SetNode, SetNode, easy showAnything, ComfySwitchNode, SolidMask, GetNode, GetNode, Note, VAEDecodeTiled, GetNode, GetNode, GetNode, Note, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVSeparateAVLatent, VHS_VideoCombine, VAELoaderKJ, Fast Groups Bypasser (rgthree), Note, Note, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, MelBandRoFormerModelLoader, LoadAudio, GetImageSize, ImageScaleBy, LTXAVTextEncoderLoader, PreviewImage, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, PrimitiveStringMultiline, SetLatentNoiseMask, VHS_VideoCombine, ImageBatchMulti, AudioCrop, PreviewAudio, ImageResizeKJv2, GetNode, ImageScaleBy, LTXSequencer, PrimitiveStringMultiline, SetNode, SetNode, Note, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, RandomNoise, LoadImage, SaveImage, LTXSequencer, LTXVCropGuides]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8mixed.safetensors"}
---

# 视频生成/图生视频/LTX2.3 I2V FLFV MV Lip Sync 首尾帧音乐视频对口形_2075065970321874946.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075065970321874946.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（116 个）：
- `GetNode`
- `ModelPatchTorchSettings`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `SetNode`
- `PathchSageAttentionKJ`
- `SamplerCustomAdvanced` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `Text Concatenate`
- `SamplerCustomAdvanced` ★核心
- `SimpleMath+`
- `SetNode`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `CFGGuider`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `CFGGuider`
- `SetNode`
- `LTXVConcatAVLatent`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `PainterAudioLength`
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `SetNode`
- `easy showAnything`
- `ComfySwitchNode`
- `SolidMask`
- `GetNode`
- `GetNode`
- `Note`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `VAELoaderKJ`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `GetImageSize`
- `ImageScaleBy`
- `LTXAVTextEncoderLoader`
- `PreviewImage`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `PrimitiveStringMultiline`
- `SetLatentNoiseMask`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `AudioCrop`
- `PreviewAudio`
- `ImageResizeKJv2`
- `GetNode`
- `ImageScaleBy`
- `LTXSequencer`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RandomNoise`
- `LoadImage`
- `SaveImage`
- `LTXSequencer`
- `LTXVCropGuides`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8mixed.safetensors`

## 知识

覆盖率 **57%**（66/116）

**有卡**：`ModelPatchTorchSettings`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`KSamplerSelect`、`BasicScheduler`、`Text Concatenate`、`SimpleMath+`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVCropGuides`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`MelBandRoFormerSampler`、`PainterAudioLength`、`LTXVAudioVAEEncode`、`SolidMask`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`MelBandRoFormerModelLoader`、`LoadAudio`、`GetImageSize`、`ImageScaleBy`、`LTXAVTextEncoderLoader`、`SetLatentNoiseMask`、`ImageBatchMulti`、`AudioCrop`、`PreviewAudio`、`ImageResizeKJv2`、`LTXSequencer`、`LoadImage`、`RandomNoise`、`SaveImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
