---
key: 视频生成/图生视频/LTX2.3_数字人口播_v2.1_（融合音频生成，效果未必比1.1好）_2054780723667718145.json
name: LTX2.3_数字人口播_v2.1_（融合音频生成，效果未必比1.1好）_2054780723667718145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3_数字人口播_v2.1_（融合音频生成，效果未必比1.1好）_2054780723667718145.json
hash: 38442d9db696f025
coverage: 0.84375
learned_at: 2026-10-15 22:37:51
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVImgToVideoInplace, SolidMask, LTXVConcatAVLatent, SetLatentNoiseMask, LatentUpscaleModelLoader, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, CheckpointLoaderSimple, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LTXVPreprocess, SaveVideo, EmptyLTXVLatentVideo, ComfyMathExpression, LTXVAudioVAEEncode, Qwen3ASRLoader_DFT, CLIPTextEncode, TrimAudioDuration, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, PrimitiveFloat, ComfyMathExpression, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PreviewAny, Qwen3ASRTranscribe_DFT, PrimitiveStringMultiline, PreviewAny, LoadImage, PreviewAny, StringConcatenate, StringConcatenate, CLIPTextEncode, PrimitiveStringMultiline, CR Text, CR Text, RunningHub_VoxCPM_LoadModel, LoadAudio, SoundFlow_GetLength, RunningHub_VoxCPM_Generate]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v2.1_（融合音频生成，效果未必比1.1好）_2054780723667718145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054780723667718145.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
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
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`
- `CR Text`
- `CR Text`
- `RunningHub_VoxCPM_LoadModel`
- `LoadAudio`
- `SoundFlow_GetLength`
- `RunningHub_VoxCPM_Generate`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **84%**（54/64）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`CheckpointLoaderSimple`、`ComfyMathExpression`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`SaveVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`Qwen3ASRLoader_DFT`、`CLIPTextEncode`、`TrimAudioDuration`、`PrimitiveBoolean`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`Qwen3ASRTranscribe_DFT`、`LoadImage`、`StringConcatenate`、`CR Text`、`RunningHub_VoxCPM_LoadModel`、`LoadAudio`、`SoundFlow_GetLength`、`RunningHub_VoxCPM_Generate`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
