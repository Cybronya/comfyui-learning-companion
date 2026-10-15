---
key: 视频生成/文生视频/LTX2.3 数字人唱歌说话 对口型 图生视频 智能极速版  图片音频双驱动_2035153850771968001.json
name: LTX2.3 数字人唱歌说话 对口型 图生视频 智能极速版  图片音频双驱动_2035153850771968001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 数字人唱歌说话 对口型 图生视频 智能极速版  图片音频双驱动_2035153850771968001.json
hash: c3787539b67eb824
coverage: 0.877193
learned_at: 2026-10-15 22:45:00
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, KSamplerSelect, Reroute, LTXVSeparateAVLatent, CFGGuider, LTXVAudioVAELoader, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, PrimitiveInt, LTXVConditioning, LTXVImgToVideoInplace, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, Int, SamplerCustomAdvanced, LTXVAudioVAEEncode, MelBandRoFormerSampler, PrimitiveBoolean, CLIPTextEncode, ResizeImageMaskNode, SetNode, SetNode, GetNode, ImageResizeKJv2, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, TrimAudioDuration, SoundFlow_GetLength, EmptyLTXVLatentVideo, CM_FloatToInt, SetLatentNoiseMask, SolidMask, DF_Int_to_Float, DF_Int_to_Float, PrimitiveInt, LTXAVTextEncoderLoader, MelBandRoFormerModelLoader, SimpleMath+, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVImgToVideoInplace, LoraLoaderModelOnly, LoadImage, LoadAudio, PrimitiveStringMultiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/文生视频/LTX2.3 数字人唱歌说话 对口型 图生视频 智能极速版  图片音频双驱动_2035153850771968001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 数字人唱歌说话 对口型 图生视频 智能极速版  图片音频双驱动_2035153850771968001.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（57 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `Int`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `TrimAudioDuration`
- `SoundFlow_GetLength`
- `EmptyLTXVLatentVideo`
- `CM_FloatToInt`
- `SetLatentNoiseMask`
- `SolidMask`
- `DF_Int_to_Float`
- `DF_Int_to_Float`
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `MelBandRoFormerModelLoader`
- `SimpleMath+`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoInplace`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **88%**（50/57）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`Int`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`PrimitiveBoolean`、`CLIPTextEncode`、`ResizeImageMaskNode`、`ImageResizeKJv2`、`ComfyMathExpression`、`TrimAudioDuration`、`SoundFlow_GetLength`、`EmptyLTXVLatentVideo`、`CM_FloatToInt`、`SetLatentNoiseMask`、`SolidMask`、`DF_Int_to_Float`、`LTXAVTextEncoderLoader`、`MelBandRoFormerModelLoader`、`SimpleMath+`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LoraLoaderModelOnly`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
