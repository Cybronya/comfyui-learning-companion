---
key: 视频生成/图生视频/LTX2.3-数字人（支持双人对话）_2031346405217935361.json
name: LTX2.3-数字人（支持双人对话）_2031346405217935361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031346405217935361.json
hash: 4c77097312834a82
coverage: 0.916667
learned_at: 2026-10-15 22:35:31
nodes: [SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, RandomNoise, CFGGuider, SamplerCustomAdvanced, VAEDecodeTiled, LTXVPreprocess, SimpleMath+, RandomNoise, CFGGuider, KSamplerSelect, KSamplerSelect, ResizeImagesByLongerEdge, PrimitiveInt, ManualSigmas, EmptyLTXVLatentVideo, PrimitiveInt, LTXVConditioning, LTXVSeparateAVLatent, SaveVideo, PrimitiveInt, PrimitiveInt, LTXVConcatAVLatent, AudioCrop, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPTextEncode, LTXVAudioVAEEncode, LTXVImgToVideoInplace, LTXVAudioVAEDecode, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, ManualSigmas, LTXVLatentUpsampler, LTXVCropGuides, LTXVImgToVideoInplace, LTXVConcatAVLatent, SetLatentNoiseMask, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, SolidMask, ImageResizeKJv2, LoadAudio, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3-数字人（支持双人对话）_2031346405217935361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031346405217935361.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVPreprocess`
- `SimpleMath+`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `ManualSigmas`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `AudioCrop`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SolidMask`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **92%**（44/48）

**有卡**：`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CreateVideo`、`RandomNoise`、`CFGGuider`、`VAEDecodeTiled`、`LTXVPreprocess`、`SimpleMath+`、`KSamplerSelect`、`ResizeImagesByLongerEdge`、`ManualSigmas`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SaveVideo`、`LTXVConcatAVLatent`、`AudioCrop`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`LTXVAudioVAEEncode`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`SetLatentNoiseMask`、`ComfyMathExpression`、`SolidMask`、`ImageResizeKJv2`、`LoadAudio`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
