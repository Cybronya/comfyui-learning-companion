---
key: 视频生成/图生视频/LTX2.3_数字人口播_v3.1_（首尾帧）_2058082401418563586.json
name: LTX2.3_数字人口播_v3.1_（首尾帧）_2058082401418563586.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058082401418563586.json
hash: ad3793256ad745e9
coverage: 0.842857
learned_at: 2026-10-15 22:38:18
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVLatentUpsampler, KSamplerSelect, Reroute, LTXVConditioning, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, SolidMask, LatentUpscaleModelLoader, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAEEncode, Qwen3ASRLoader_DFT, CLIPTextEncode, PrimitiveInt, LTXAVTextEncoderLoader, Qwen3ASRTranscribe_DFT, PreviewAny, PreviewAny, StringConcatenate, StringConcatenate, CLIPTextEncode, CR Text, CR Text, RunningHub_VoxCPM_LoadModel, LoadAudio, SoundFlow_GetLength, RunningHub_VoxCPM_Generate, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, CheckpointLoaderSimple, PreviewAny, LTXVAudioVAELoader, PrimitiveInt, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SetLatentNoiseMask, PrimitiveFloat, TrimAudioDuration, SaveVideo, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveInt, LTXVCropGuides, LTXVPreprocess, PrimitiveBoolean, ComfyMathExpression, LoadImage, LTXVPreprocess, Reroute, LTXVImgToVideoInplaceKJ, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v3.1_（首尾帧）_2058082401418563586.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058082401418563586.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVConditioning`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `SolidMask`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVAEEncode` ★核心
- `Qwen3ASRLoader_DFT`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `Qwen3ASRTranscribe_DFT`
- `PreviewAny`
- `PreviewAny`
- `StringConcatenate`
- `StringConcatenate`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Text`
- `RunningHub_VoxCPM_LoadModel`
- `LoadAudio`
- `SoundFlow_GetLength`
- `RunningHub_VoxCPM_Generate`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `CheckpointLoaderSimple` ★核心
- `PreviewAny`
- `LTXVAudioVAELoader`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `PrimitiveFloat`
- `TrimAudioDuration`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `LTXVCropGuides`
- `LTXVPreprocess`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `LoadImage`
- `LTXVPreprocess`
- `Reroute`
- `LTXVImgToVideoInplaceKJ`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（59/70）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`ComfyMathExpression`、`LTXVAudioVAEEncode`、`Qwen3ASRLoader_DFT`、`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`Qwen3ASRTranscribe_DFT`、`StringConcatenate`、`CR Text`、`RunningHub_VoxCPM_LoadModel`、`LoadAudio`、`SoundFlow_GetLength`、`RunningHub_VoxCPM_Generate`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`TrimAudioDuration`、`SaveVideo`、`LTXVCropGuides`、`LTXVPreprocess`、`PrimitiveBoolean`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
