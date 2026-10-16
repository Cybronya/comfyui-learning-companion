---
key: 视频生成/图生视频/LTX2.3 多图参考生视频_2061938954978553858.json
name: LTX2.3 多图参考生视频_2061938954978553858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061938954978553858.json
hash: cdc496c674f6920e
coverage: 0.942308
learned_at: 2026-10-15 22:38:58
nodes: [KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVLatentUpsampler, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LatentUpscaleModelLoader, PrimitiveFloat, PrimitiveFloat, LTXVAddGuideMulti, GetImageSize+, PrimitiveFloat, Int, Int, Int, PrimitiveFloat, LTXVPreprocess, PrimitiveInt, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAddGuideMulti, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, image_scale_pixel_v2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LTXVPreprocess, LTXVPreprocess, PromptRelaySmartEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ManualSigmas, LTXFaceDetector, LTXLikenessGuide, Sigmas Easing, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, LTXLikenessGuide, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LoadImage, LoadImage, Int, LTXVAddGuideMulti, LoadImage, LoadImage, Text, Text, LTXVSeparateAVLatent, VAEDecodeTiled, JWImageSequenceExtractFromBatch, CLIPTextEncode, LoraLoaderModelOnly, Seed Everywhere, PrimitiveFloat, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXVPreprocess, VRAMReserver, image_scale_pixel_v2, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LTXVConditioning, STGGuiderAdvanced, RandomNoise, LTX2_NAG, LTXLatentAnchorAware, LTXLikenessAnchor, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVAudioVAEEncode, CM_FloatToInt, LoadAudio, LTXVAudioVAELoader, LTXVAudioVAELoader, CreateVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 多图参考生视频_2061938954978553858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061938954978553858.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVAddGuideMulti`
- `GetImageSize+`
- `PrimitiveFloat`
- `Int`
- `Int`
- `Int`
- `PrimitiveFloat`
- `LTXVPreprocess`
- `PrimitiveInt`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAddGuideMulti`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `PromptRelaySmartEncode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `LTXFaceDetector`
- `LTXLikenessGuide`
- `Sigmas Easing`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `LTXLikenessGuide`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `Int`
- `LTXVAddGuideMulti`
- `LoadImage`
- `LoadImage`
- `Text`
- `Text`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `JWImageSequenceExtractFromBatch`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Seed Everywhere`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVPreprocess`
- `VRAMReserver`
- `image_scale_pixel_v2`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConditioning`
- `STGGuiderAdvanced`
- `RandomNoise`
- `LTX2_NAG`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEEncode` ★核心
- `CM_FloatToInt`
- `LoadAudio`
- `LTXVAudioVAELoader`
- `LTXVAudioVAELoader`
- `CreateVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（98/104）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVAddGuideMulti`、`GetImageSize+`、`Int`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`Text`、`LoraLoaderModelOnly`、`image_scale_pixel_v2`、`ImageResizeKJv2`、`PromptRelaySmartEncode`、`LTXFaceDetector`、`LTXLikenessGuide`、`Sigmas Easing`、`LTXLatentAnchorAware`、`LTXLikenessAnchor`、`CreateVideo`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SaveVideo`、`LoadImage`、`JWImageSequenceExtractFromBatch`、`CLIPTextEncode`、`Seed Everywhere`、`LTXICLoRALoaderModelOnly`、`VRAMReserver`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`STGGuiderAdvanced`、`LTX2_NAG`、`LTXVAudioVAEEncode`、`CM_FloatToInt`、`LoadAudio`、`LTXVAudioVAELoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
