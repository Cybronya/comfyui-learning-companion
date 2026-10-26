---
key: 数字人/数字人/LTX2.3 3.5套件｜头像开口·单人数字人口播唱歌音频驱动_2068714653911445505.json
name: LTX2.3 3.5套件｜头像开口·单人数字人口播唱歌音频驱动_2068714653911445505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 3.5套件｜头像开口·单人数字人口播唱歌音频驱动_2068714653911445505.json
hash: 00340183056d4113
coverage: 0.975207
learned_at: 2026-10-26 01:55:48
nodes: [KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LatentUpscaleModelLoader, SolidMask, CFGGuider, CFGGuider, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SetLatentNoiseMask, LTXVConcatAVLatent, SolidMask, SamplerCustomAdvanced, Audio Duration (mtb), GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, PathchSageAttentionKJ, LoraLoaderModelOnly, LTXVConditioning, LTXVPreprocess, EmptyLTXVLatentVideo, PrimitiveInt, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, MelBandRoFormerModelLoader, LoraLoaderModelOnly, PrimitiveBoolean, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SolidMask, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, Sigmas Easing, STGGuiderAdvanced, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVAudioVAEEncode, LoraLoaderModelOnly, LoadAudio, Float, TrimAudioDuration, PromptRelayEncode, LTXFaceDetector, PrimitiveFloat, JWImageResizeByLongerSide, SimpleMath+, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, image_scale_pixel_v2, VAEDecodeTiled, LoraLoaderModelOnly, SetLatentNoiseMask, SaveVideo, LoadImage, JjkText, Text, CLIPTextEncode, Text, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2_NAG, Text, VHS_VideoCombine, ImageFromBatch, LTXICLoRALoaderModelOnly, MelBandRoFormerSampler, Float]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors"}
---

# 数字人/数字人/LTX2.3 3.5套件｜头像开口·单人数字人口播唱歌音频驱动_2068714653911445505.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 3.5套件｜头像开口·单人数字人口播唱歌音频驱动_2068714653911445505.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（121 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `SolidMask`
- `CFGGuider`
- `CFGGuider`
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `GetLatentSizeAndCount`
- `LTXVImgToVideoConditionOnly`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `SolidMask`
- `SamplerCustomAdvanced` ★核心
- `Audio Duration (mtb)`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `MelBandRoFormerModelLoader`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SolidMask`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `Sigmas Easing`
- `STGGuiderAdvanced`
- `LTXLikenessGuide`
- `LTXLatentAnchorAware`
- `LTXLikenessAnchor`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `LTXVAudioVAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `Float`
- `TrimAudioDuration`
- `PromptRelayEncode`
- `LTXFaceDetector`
- `PrimitiveFloat`
- `JWImageResizeByLongerSide`
- `SimpleMath+`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `image_scale_pixel_v2`
- `VAEDecodeTiled` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetLatentNoiseMask`
- `SaveVideo`
- `LoadImage`
- `JjkText`
- `Text`
- `CLIPTextEncode` ★核心
- `Text`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `Text`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `LTXICLoRALoaderModelOnly` ★核心
- `MelBandRoFormerSampler` ★核心
- `Float`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **98%**（118/121）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LatentUpscaleModelLoader`、`SolidMask`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`Audio Duration (mtb)`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXICLoRALoaderModelOnly`、`MelBandRoFormerModelLoader`、`PrimitiveBoolean`、`LTX2_NAG`、`LTXLikenessGuide`、`LTXLatentAnchorAware`、`LTXLikenessAnchor`、`Sigmas Easing`、`STGGuiderAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LTXVAudioVAEEncode`、`LoadAudio`、`Float`、`TrimAudioDuration`、`PromptRelayEncode`、`LTXFaceDetector`、`JWImageResizeByLongerSide`、`SimpleMath+`、`image_scale_pixel_v2`、`LoadImage`、`Text`、`CLIPTextEncode`、`VHS_VideoCombine`、`ImageFromBatch`、`MelBandRoFormerSampler`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
