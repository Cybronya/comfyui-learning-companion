---
key: 视频生成/图生视频/LTX2.3 数字人唱歌 图生视频 智能对口型 极速版  图片音频双驱动_2035160184418471938.json
name: LTX2.3 数字人唱歌 图生视频 智能对口型 极速版  图片音频双驱动_2035160184418471938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2035160184418471938.json
hash: 006cd553f2c08ac4
coverage: 0.877193
learned_at: 2026-10-15 22:35:47
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, KSamplerSelect, Reroute, LTXVSeparateAVLatent, CFGGuider, LTXVAudioVAELoader, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, PrimitiveInt, LTXVConditioning, LTXVImgToVideoInplace, LTXVSeparateAVLatent, SamplerCustomAdvanced, ManualSigmas, Int, SamplerCustomAdvanced, LTXVAudioVAEEncode, MelBandRoFormerSampler, PrimitiveBoolean, CLIPTextEncode, ResizeImageMaskNode, SetNode, SetNode, GetNode, ImageResizeKJv2, LTXVConcatAVLatent, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, ComfyMathExpression, TrimAudioDuration, SoundFlow_GetLength, EmptyLTXVLatentVideo, CM_FloatToInt, SetLatentNoiseMask, SolidMask, DF_Int_to_Float, DF_Int_to_Float, PrimitiveInt, LTXAVTextEncoderLoader, MelBandRoFormerModelLoader, SimpleMath+, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVImgToVideoInplace, LoraLoaderModelOnly, LoadImage, LoadAudio, PrimitiveStringMultiline, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3 数字人唱歌 图生视频 智能对口型 极速版  图片音频双驱动_2035160184418471938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2035160184418471938.json`

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
