---
key: 视频生成/图生视频/LTX2.3 Eros 锚点视频生成 （MV, 数字人，脱口秀）_2075060521405083649.json
name: LTX2.3 Eros 锚点视频生成 （MV, 数字人，脱口秀）_2075060521405083649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2075060521405083649.json
hash: 81071122e82fbd5c
coverage: 0.583333
learned_at: 2026-10-15 22:41:21
nodes: [GetNode, Sigmas Easing, ManualSigmas, LTXVConcatAVLatent, GetNode, LTXVConditioning, LTXVLatentUpsamplerTiled, KSamplerSelect, LatentUpscaleModelLoader, SetNode, JWStringToFloat, JWStringToFloat, JWStringToFloat, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, SetNode, VAELoaderKJ, Note, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, GetNode, RTXVideoSuperResolution, ComfyMathExpression, SetNode, SetNode, VAEDecode, LTXVAudioVAEDecode, SetNode, SetNode, GetNode, GetNode, PreviewImage, EmptyLTXVLatentVideo, GetNode, ImageResizeKJv2, GetNode, SetNode, SetNode, easy float, LTXVCropGuides, Fast Groups Bypasser (rgthree), CLIPTextEncode, JWStringToFloat, Note, GetImageSize, ImageScaleBy, Fast Groups Bypasser (rgthree), LTXVAudioVAEEncode, GetNode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SolidMask, LTXVAddGuide, LTXLatentAnchorAware, AudioAdjustVolume, SamplerCustomAdvanced, LTXVSeparateAVLatent, STGGuiderAdvanced, KSamplerSelect, LTXVEmptyLatentAudio, LTXTextAttentionAmplifier, CFGGuider, SetLatentNoiseMask, LTX2SamplingPreviewOverride, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, GetNode, GetNode, LTXVImgToVideoInplaceKJ, LTXVImgToVideoInplaceKJ, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, PreviewAudio, PainterAudioLength, SetNode, SetNode, easy showAnything, ComfyMathExpression, LTXVAudioVAELoader, LTXAVTextEncoderLoader, Label (rgthree), GetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, SamplerCustomAdvanced, CheckpointLoaderSimple, PrimitiveFloat, GetNode, PrimitiveInt, PrimitiveInt, LoadImage, LoadAudio, AudioCrop, PrimitiveStringMultiline, LoraLoaderModelOnly, VHS_VideoCombine, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "10Eros_v1-fp8mixed_learned.safetensors", "height": 24, "lora_name": "ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors", "strength_clip": 0, "strength_model": 1, "width": 1}
---

# 视频生成/图生视频/LTX2.3 Eros 锚点视频生成 （MV, 数字人，脱口秀）_2075060521405083649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075060521405083649.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（120 个）：
- `GetNode`
- `Sigmas Easing`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVConditioning`
- `LTXVLatentUpsamplerTiled` ★核心
- `KSamplerSelect` ★核心
- `LatentUpscaleModelLoader`
- `SetNode`
- `JWStringToFloat`
- `JWStringToFloat`
- `JWStringToFloat`
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `RTXVideoSuperResolution`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy float`
- `LTXVCropGuides`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `JWStringToFloat`
- `Note`
- `GetImageSize`
- `ImageScaleBy`
- `Fast Groups Bypasser (rgthree)`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SolidMask`
- `LTXVAddGuide`
- `LTXLatentAnchorAware`
- `AudioAdjustVolume`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `STGGuiderAdvanced`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXTextAttentionAmplifier`
- `CFGGuider`
- `SetLatentNoiseMask`
- `LTX2SamplingPreviewOverride`
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVImgToVideoInplaceKJ`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `PreviewAudio`
- `PainterAudioLength`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `ComfyMathExpression`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `Label (rgthree)`
- `GetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `PrimitiveFloat`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1`
- `height` = `24`
- `batch_size` = `1`
- `lora_name` = `ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors`
- `strength_model` = `1`
- `strength_clip` = `0`
- `checkpoint` = `10Eros_v1-fp8mixed_learned.safetensors`

## 知识

覆盖率 **58%**（70/120）

**有卡**：`Sigmas Easing`、`ManualSigmas`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXVLatentUpsamplerTiled`、`KSamplerSelect`、`LatentUpscaleModelLoader`、`JWStringToFloat`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`RTXVideoSuperResolution`、`ComfyMathExpression`、`VAEDecode`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`easy float`、`LTXVCropGuides`、`CLIPTextEncode`、`GetImageSize`、`ImageScaleBy`、`LTXVAudioVAEEncode`、`Label (rgthree)`、`SolidMask`、`LTXVAddGuide`、`LTXLatentAnchorAware`、`AudioAdjustVolume`、`SamplerCustomAdvanced`、`STGGuiderAdvanced`、`LTXVEmptyLatentAudio`、`LTXTextAttentionAmplifier`、`CFGGuider`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`LTX2LoraLoaderAdvanced`、`LTXVImgToVideoInplaceKJ`、`RandomNoise`、`PreviewAudio`、`PainterAudioLength`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LoadImage`、`LoadAudio`、`AudioCrop`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`SaveImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
