---
key: 视频生成/图生视频/LTX2.3 Org版对口型神器｜图片说话唱歌嘴型精准同步_2103702543808425986.json
name: LTX2.3 Org版对口型神器｜图片说话唱歌嘴型精准同步_2103702543808425986
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 Org版对口型神器｜图片说话唱歌嘴型精准同步_2103702543808425986.json
hash: 775ca67ed08109ec
coverage: 0.877193
learned_at: 2026-10-17 02:28:48
nodes: [RandomNoise, CFGGuider, EmptyLTXVLatentVideo, LTXVConcatAVLatent, CM_FloatToInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ImageAndMaskResizeNode, ImageResizeKJv2, LTXVConditioning, LTXVImgToVideoInplace, SamplerCustomAdvanced, CFGGuider, BasicScheduler, RandomNoise, CheckpointLoaderSimple, LTXVAudioVAELoader, PrimitiveInt, CLIPTextEncode, CLIPTextEncode, LTXVPreprocess, SamplerCustomAdvanced, LTX2_NAG, LoraLoaderModelOnly, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVConcatAVLatent, Reroute, LTXVSeparateAVLatent, GetNode, SetNode, PrimitiveBoolean, VAEDecodeTiled, KSamplerSelect, BasicScheduler, ManualSigmas, KSamplerSelect, JoinStrings, PrimitiveInt, SoundFlow_GetLength, LTXVCropGuides, LTXVSeparateAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, TrimAudioDuration, SetNode, KSampler, LTXVAudioVAEDecode, PrimitiveStringMultiline, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, LTX2SamplingPreviewOverride, PreviewAudio, SimpleMath+, Int, PrimitiveFloat, VHS_VideoCombine, TrimAudioDuration, LTXVAudioVAEEncode, MelBandRoFormerSampler, MelBandRoFormerModelLoader, SoundFlow_GetLength, SetLatentNoiseMask, SolidMask, DF_Int_to_Float, DF_Int_to_Float, PrimitiveInt, PrimitiveStringMultiline, LoadImage, LoadAudio, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3 Org版对口型神器｜图片说话唱歌嘴型精准同步_2103702543808425986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3 Org版对口型神器｜图片说话唱歌嘴型精准同步_2103702543808425986.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `RandomNoise`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `CM_FloatToInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageAndMaskResizeNode`
- `ImageResizeKJv2`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `BasicScheduler`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVConcatAVLatent`
- `Reroute`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `PrimitiveBoolean`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `JoinStrings`
- `PrimitiveInt`
- `SoundFlow_GetLength`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `TrimAudioDuration`
- `SetNode`
- `KSampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `LTX2SamplingPreviewOverride`
- `PreviewAudio`
- `SimpleMath+`
- `Int`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `SoundFlow_GetLength`
- `SetLatentNoiseMask`
- `SolidMask`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadAudio`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（100/114）

**有卡**：`RandomNoise`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`CM_FloatToInt`、`ComfyMathExpression`、`ImageAndMaskResizeNode`、`ImageResizeKJv2`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`BasicScheduler`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVPreprocess`、`LTX2_NAG`、`LoraLoaderModelOnly`、`LTXVSeparateAVLatent`、`PrimitiveBoolean`、`VAEDecodeTiled`、`KSamplerSelect`、`ManualSigmas`、`JoinStrings`、`SoundFlow_GetLength`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`TrimAudioDuration`、`KSampler`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`LTX2SamplingPreviewOverride`、`PreviewAudio`、`SimpleMath+`、`Int`、`VHS_VideoCombine`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`SetLatentNoiseMask`、`SolidMask`、`DF_Int_to_Float`、`LoadImage`、`LoadAudio`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
