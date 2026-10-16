---
key: 视频生成/图生视频/LTX2.3 I2V First Last Frame首尾帧（无限中间帧）_2075069452714078209.json
name: LTX2.3 I2V First Last Frame首尾帧（无限中间帧）_2075069452714078209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2075069452714078209.json
hash: 44a04722a9352b40
coverage: 0.591667
learned_at: 2026-10-15 22:41:21
nodes: [GetNode, ModelPatchTorchSettings, GetNode, GetNode, SetNode, PathchSageAttentionKJ, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, GetNode, SetNode, SetNode, Text Concatenate, SimpleMath+, SetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SetNode, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, SetNode, SetNode, SetNode, SetNode, LTXVAudioVAEDecode, SetNode, GetNode, SetNode, Fast Groups Bypasser (rgthree), SimpleMath+, GetNode, ImageScaleBy, KSamplerSelect, GetNode, LTX2_NAG, LTX2SamplingPreviewOverride, BasicScheduler, LTXVLatentUpsampler, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, Fast Groups Bypasser (rgthree), Note, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, GetNode, BasicScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, GetNode, GetNode, ManualSigmas, CFGGuider, SetNode, SetNode, PreviewAudio, AudioCrop, GetNode, LTXVCropGuides, CFGGuider, LTXVConcatAVLatent, LTXVSeparateAVLatent, MelBandRoFormerSampler, ComfySwitchNode, Note, VAELoaderKJ, GetNode, GetNode, Note, GetNode, GetNode, CFGGuider, CFGGuider, ManualSigmas, GetNode, easy ifElse, PrimitiveStringMultiline, LTXVReferenceAudio, PrimitiveFloat, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, LoadAudio, MelBandRoFormerModelLoader, GetImageSize, SetNode, LTXAVTextEncoderLoader, easy ifElse, ImageScaleBy, VHS_VideoCombine, LoraLoaderModelOnly, RandomNoise, VHS_VideoCombine, LTXVReferenceAudio, PrimitiveBoolean, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, ImageBatchMulti, CheckpointLoaderSimple, ImageResizeKJv2, PrimitiveInt, LTXSequencer, PreviewImage, Note, LoadImage, SaveImage, LTXSequencer, LTXVCropGuides]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8mixed.safetensors", "height": 24, "width": 1}
---

# 视频生成/图生视频/LTX2.3 I2V First Last Frame首尾帧（无限中间帧）_2075069452714078209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075069452714078209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（120 个）：
- `GetNode`
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `Text Concatenate`
- `SimpleMath+`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `SimpleMath+`
- `GetNode`
- `ImageScaleBy`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `BasicScheduler`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `CFGGuider`
- `SetNode`
- `SetNode`
- `PreviewAudio`
- `AudioCrop`
- `GetNode`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `MelBandRoFormerSampler` ★核心
- `ComfySwitchNode`
- `Note`
- `VAELoaderKJ`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CFGGuider`
- `ManualSigmas`
- `GetNode`
- `easy ifElse`
- `PrimitiveStringMultiline`
- `LTXVReferenceAudio`
- `PrimitiveFloat`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `GetImageSize`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `easy ifElse`
- `ImageScaleBy`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `VHS_VideoCombine`
- `LTXVReferenceAudio`
- `PrimitiveBoolean`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ImageBatchMulti`
- `CheckpointLoaderSimple` ★核心
- `ImageResizeKJv2`
- `PrimitiveInt`
- `LTXSequencer`
- `PreviewImage`
- `Note`
- `LoadImage`
- `SaveImage`
- `LTXSequencer`
- `LTXVCropGuides`

## 关键参数

- `width` = `1`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8mixed.safetensors`

## 知识

覆盖率 **59%**（71/120）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`Text Concatenate`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`ImageScaleBy`、`KSamplerSelect`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVConditioning`、`CLIPTextEncode`、`VAEDecodeTiled`、`ManualSigmas`、`CFGGuider`、`PreviewAudio`、`AudioCrop`、`LTXVCropGuides`、`MelBandRoFormerSampler`、`LTXVReferenceAudio`、`LoraLoaderModelOnly`、`LoadAudio`、`MelBandRoFormerModelLoader`、`GetImageSize`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`RandomNoise`、`PrimitiveBoolean`、`LoadImage`、`ImageBatchMulti`、`CheckpointLoaderSimple`、`ImageResizeKJv2`、`LTXSequencer`、`SaveImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
