---
key: 视频生成/图生视频/LTX2.3_数字人口播_v2.0_（融合音频生成，效果未必比1.0好）_2054789125802340354.json
name: LTX2.3_数字人口播_v2.0_（融合音频生成，效果未必比1.0好）_2054789125802340354.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2054789125802340354.json
hash: e8411b5cc14e008b
coverage: 0.898305
learned_at: 2026-10-15 22:37:51
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, CFGGuider, SolidMask, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, SetLatentNoiseMask, PrimitiveInt, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, ComfyMathExpression, PrimitiveBoolean, ComfyMathExpression, LatentUpscaleModelLoader, LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, CheckpointLoaderSimple, CLIPTextEncode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CreateVideo, PrimitiveInt, TrimAudioDuration, PrimitiveFloat, LoadImage, SaveVideo, PrimitiveStringMultiline, RunningHub_VoxCPM_LoadModel, CR Text, CR Text, SoundFlow_GetLength, RunningHub_VoxCPM_Generate, LoadAudio, LoadAudio, ResizeImageMaskNode]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v2.0_（融合音频生成，效果未必比1.0好）_2054789125802340354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054789125802340354.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
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
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `SolidMask`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `PrimitiveBoolean`
- `ComfyMathExpression`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `PrimitiveInt`
- `TrimAudioDuration`
- `PrimitiveFloat`
- `LoadImage`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `RunningHub_VoxCPM_LoadModel`
- `CR Text`
- `CR Text`
- `SoundFlow_GetLength`
- `RunningHub_VoxCPM_Generate`
- `LoadAudio`
- `LoadAudio`
- `ResizeImageMaskNode`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **90%**（53/59）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`LTXVPreprocess`、`ComfyMathExpression`、`SetLatentNoiseMask`、`ResizeImagesByLongerEdge`、`PrimitiveBoolean`、`LatentUpscaleModelLoader`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`CreateVideo`、`TrimAudioDuration`、`LoadImage`、`SaveVideo`、`RunningHub_VoxCPM_LoadModel`、`CR Text`、`SoundFlow_GetLength`、`RunningHub_VoxCPM_Generate`、`LoadAudio`、`ResizeImageMaskNode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
