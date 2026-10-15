---
key: 视频生成/文生视频/LTX2.3 单人数字人工作流｜新增10S相似度保持，口播、唱歌、角色一致性一套跑通_2061362758670708737.json
name: LTX2.3 单人数字人工作流｜新增10S相似度保持，口播、唱歌、角色一致性一套跑通_2061362758670708737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 单人数字人工作流｜新增10S相似度保持，口播、唱歌、角色一致性一套跑通_2061362758670708737.json
hash: 5fd3e00b722279d9
coverage: 0.969388
learned_at: 2026-10-15 22:44:59
nodes: [KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LatentUpscaleModelLoader, SolidMask, CFGGuider, CFGGuider, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, GetLatentSizeAndCount, LTXVImgToVideoConditionOnly, SetLatentNoiseMask, LTXVConcatAVLatent, SolidMask, SamplerCustomAdvanced, Audio Duration (mtb), GetLatentSizeAndCount, LTXVConcatAVLatent, LTXVSeparateAVLatent, PathchSageAttentionKJ, LoraLoaderModelOnly, LTXVConditioning, LTXVPreprocess, EmptyLTXVLatentVideo, PrimitiveInt, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, MelBandRoFormerModelLoader, LoraLoaderModelOnly, PrimitiveBoolean, LoraLoaderModelOnly, LTX2_NAG, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SolidMask, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, Sigmas Easing, STGGuiderAdvanced, LTXLikenessGuide, LTXLatentAnchorAware, LTXLikenessAnchor, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVAudioVAEDecode, CreateVideo, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, LTXVAudioVAEEncode, LoraLoaderModelOnly, LoadAudio, Float, Float, TrimAudioDuration, PromptRelayEncode, LTXFaceDetector, PrimitiveFloat, MelBandRoFormerSampler, JWImageResizeByLongerSide, SimpleMath+, LoadImage, CLIPTextEncode, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, image_scale_pixel_v2, VAEDecodeTiled, LoraLoaderModelOnly, SetLatentNoiseMask, JjkText, Text, SaveVideo]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors"}
---

# 视频生成/文生视频/LTX2.3 单人数字人工作流｜新增10S相似度保持，口播、唱歌、角色一致性一套跑通_2061362758670708737.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 单人数字人工作流｜新增10S相似度保持，口播、唱歌、角色一致性一套跑通_2061362758670708737.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
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
- `Float`
- `TrimAudioDuration`
- `PromptRelayEncode`
- `LTXFaceDetector`
- `PrimitiveFloat`
- `MelBandRoFormerSampler` ★核心
- `JWImageResizeByLongerSide`
- `SimpleMath+`
- `LoadImage`
- `CLIPTextEncode` ★核心
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
- `JjkText`
- `Text`
- `SaveVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **97%**（95/98）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LatentUpscaleModelLoader`、`SolidMask`、`CFGGuider`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`GetLatentSizeAndCount`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`Audio Duration (mtb)`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`LTXVConditioning`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXICLoRALoaderModelOnly`、`MelBandRoFormerModelLoader`、`PrimitiveBoolean`、`LTX2_NAG`、`LTXLikenessGuide`、`LTXLatentAnchorAware`、`LTXLikenessAnchor`、`Sigmas Easing`、`STGGuiderAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LTXVAudioVAEEncode`、`LoadAudio`、`Float`、`TrimAudioDuration`、`PromptRelayEncode`、`LTXFaceDetector`、`MelBandRoFormerSampler`、`JWImageResizeByLongerSide`、`SimpleMath+`、`LoadImage`、`CLIPTextEncode`、`image_scale_pixel_v2`、`Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
