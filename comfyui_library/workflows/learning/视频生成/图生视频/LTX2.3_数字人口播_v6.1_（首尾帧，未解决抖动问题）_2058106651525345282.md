---
key: 视频生成/图生视频/LTX2.3_数字人口播_v6.1_（首尾帧，未解决抖动问题）_2058106651525345282.json
name: LTX2.3_数字人口播_v6.1_（首尾帧，未解决抖动问题）_2058106651525345282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058106651525345282.json
hash: e8db99c7287425b1
coverage: 0.861111
learned_at: 2026-10-15 22:38:18
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, SolidMask, LTXVConcatAVLatent, SetLatentNoiseMask, LatentUpscaleModelLoader, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, SaveVideo, ComfyMathExpression, LTXVAudioVAEEncode, Qwen3ASRLoader_DFT, CLIPTextEncode, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PreviewAny, Qwen3ASRTranscribe_DFT, PreviewAny, StringConcatenate, StringConcatenate, CLIPTextEncode, CR Text, CR Text, RunningHub_VoxCPM_LoadModel, SoundFlow_GetLength, RunningHub_VoxCPM_Generate, ComfyMathExpression, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, CheckpointLoaderSimple, EmptyLTXVLatentVideo, LTXVPreprocess, LTXVPreprocess, LTXVImgToVideoInplace, LoadImage, PreviewAny, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, TrimAudioDuration, LoadAudio, PrimitiveFloat, ComfyMathExpression, SimpleMath+, FloatConstant, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v6.1_（首尾帧，未解决抖动问题）_2058106651525345282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058106651525345282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
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
- `SolidMask`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SaveVideo`
- `ComfyMathExpression`
- `LTXVAudioVAEEncode` ★核心
- `Qwen3ASRLoader_DFT`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `PreviewAny`
- `Qwen3ASRTranscribe_DFT`
- `PreviewAny`
- `StringConcatenate`
- `StringConcatenate`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Text`
- `RunningHub_VoxCPM_LoadModel`
- `SoundFlow_GetLength`
- `RunningHub_VoxCPM_Generate`
- `ComfyMathExpression`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `CheckpointLoaderSimple` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `LoadImage`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `TrimAudioDuration`
- `LoadAudio`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SimpleMath+`
- `FloatConstant`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **86%**（62/72）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`ComfyMathExpression`、`SaveVideo`、`LTXVAudioVAEEncode`、`Qwen3ASRLoader_DFT`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`Qwen3ASRTranscribe_DFT`、`StringConcatenate`、`CR Text`、`RunningHub_VoxCPM_LoadModel`、`SoundFlow_GetLength`、`RunningHub_VoxCPM_Generate`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`CheckpointLoaderSimple`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`LoadImage`、`TrimAudioDuration`、`LoadAudio`、`SimpleMath+`、`FloatConstant`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
