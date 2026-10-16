---
key: 视频生成/图生视频/LTX2.3_数字人口播_v6.0_（首尾帧，抖动问题未解决）_2058106663583969282.json
name: LTX2.3_数字人口播_v6.0_（首尾帧，抖动问题未解决）_2058106663583969282.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058106663583969282.json
hash: 1c42f0fc6fc4ef6c
coverage: 0.909091
learned_at: 2026-10-15 22:38:18
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, SolidMask, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, SetLatentNoiseMask, PrimitiveInt, PrimitiveInt, RandomNoise, ComfyMathExpression, PrimitiveBoolean, ComfyMathExpression, LatentUpscaleModelLoader, LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, LTXVAudioVAEEncode, CLIPTextEncode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CreateVideo, SaveVideo, RunningHub_VoxCPM_LoadModel, CR Text, CR Text, SoundFlow_GetLength, RunningHub_VoxCPM_Generate, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, CheckpointLoaderSimple, CLIPTextEncode, ResizeImageMaskNode, LoadImage, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImageMaskNode, TrimAudioDuration, LoadAudio, LoadImage, PrimitiveStringMultiline, ComfyMathExpression, SimpleMath+, FloatConstant, PrimitiveInt, PrimitiveFloat, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v6.0_（首尾帧，抖动问题未解决）_2058106663583969282.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058106663583969282.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
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
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `SolidMask`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `ComfyMathExpression`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `SaveVideo`
- `RunningHub_VoxCPM_LoadModel`
- `CR Text`
- `CR Text`
- `SoundFlow_GetLength`
- `RunningHub_VoxCPM_Generate`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `ResizeImageMaskNode`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `TrimAudioDuration`
- `LoadAudio`
- `LoadImage`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `SimpleMath+`
- `FloatConstant`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **91%**（60/66）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`ComfyMathExpression`、`SetLatentNoiseMask`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVAudioVAEEncode`、`CLIPTextEncode`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`CreateVideo`、`SaveVideo`、`RunningHub_VoxCPM_LoadModel`、`CR Text`、`SoundFlow_GetLength`、`RunningHub_VoxCPM_Generate`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`ResizeImageMaskNode`、`LoadImage`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`TrimAudioDuration`、`LoadAudio`、`SimpleMath+`、`FloatConstant`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
