---
key: 数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json
name: LTX2.3 s2v双人数字人_2031917616582889474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json
hash: 4ce1edb6d3f9dbc1
coverage: 0.896552
learned_at: 2026-10-26 01:55:49
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, PrimitiveInt, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, CreateVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, LTXVPreprocess, LTXVImgToVideoInplace, CFGGuider, CLIPTextEncode, LTXVConditioning, LTXVImgToVideoInplace, ManualSigmas, LTXVAudioVAEEncode, SetLatentNoiseMask, PreviewAny, SimpleMath+, ResizeImagesByLongerEdge, ResizeImageMaskNode, ImageLoader, LoadAudio, LoadAudio, TrimAudioDuration, TrimAudioDuration, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SolidMask, AudioConcat, PreviewAudio, CheckpointLoaderSimple, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, SaveVideo, FloatConstant, CLIPTextEncode, LTX2_NAG]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 s2v双人数字人_2031917616582889474.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `PreviewAny`
- `SimpleMath+`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `ImageLoader`
- `LoadAudio`
- `LoadAudio`
- `TrimAudioDuration`
- `TrimAudioDuration`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `SolidMask`
- `AudioConcat`
- `PreviewAudio`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `FloatConstant`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（52/58）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`ComfyMathExpression`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SimpleMath+`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`ImageLoader`、`LoadAudio`、`TrimAudioDuration`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`SolidMask`、`AudioConcat`、`PreviewAudio`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`SaveVideo`、`FloatConstant`、`LTX2_NAG`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
