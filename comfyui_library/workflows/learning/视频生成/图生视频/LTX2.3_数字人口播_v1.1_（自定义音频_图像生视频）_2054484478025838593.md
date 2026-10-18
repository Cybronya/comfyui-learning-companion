---
key: 视频生成/图生视频/LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json
name: LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json
hash: 81162f166ba4b7b6
coverage: 0.833333
learned_at: 2026-10-15 22:37:48
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVImgToVideoInplace, SolidMask, LTXVConcatAVLatent, SetLatentNoiseMask, LatentUpscaleModelLoader, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, CheckpointLoaderSimple, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LTXVPreprocess, SaveVideo, EmptyLTXVLatentVideo, ComfyMathExpression, LTXVAudioVAEEncode, Qwen3ASRLoader_DFT, CLIPTextEncode, TrimAudioDuration, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, PrimitiveFloat, ComfyMathExpression, SoundFlow_GetLength, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PreviewAny, Qwen3ASRTranscribe_DFT, PrimitiveStringMultiline, PreviewAny, LoadImage, PreviewAny, StringConcatenate, StringConcatenate, LoadAudio, PrimitiveStringMultiline, CLIPTextEncode]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054484478025838593.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `SolidMask`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SaveVideo`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `LTXVAudioVAEEncode` ★核心
- `Qwen3ASRLoader_DFT`
- `CLIPTextEncode` ★核心
- `TrimAudioDuration`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SoundFlow_GetLength`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `PreviewAny`
- `Qwen3ASRTranscribe_DFT`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `LoadImage`
- `PreviewAny`
- `StringConcatenate`
- `StringConcatenate`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`CheckpointLoaderSimple`、`ComfyMathExpression`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`SaveVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`Qwen3ASRLoader_DFT`、`CLIPTextEncode`、`TrimAudioDuration`、`PrimitiveBoolean`、`SoundFlow_GetLength`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`Qwen3ASRTranscribe_DFT`、`LoadImage`、`StringConcatenate`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
