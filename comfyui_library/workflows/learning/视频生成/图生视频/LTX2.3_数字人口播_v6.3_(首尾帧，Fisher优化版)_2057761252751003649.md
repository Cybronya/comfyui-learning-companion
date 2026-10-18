---
key: 视频生成/图生视频/LTX2.3_数字人口播_v6.3_(首尾帧，Fisher优化版)_2057761252751003649.json
name: LTX2.3_数字人口播_v6.3_(首尾帧，Fisher优化版)_2057761252751003649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3_数字人口播_v6.3_(首尾帧，Fisher优化版)_2057761252751003649.json
hash: 4d9f8d68411e1f83
coverage: 0.865672
learned_at: 2026-10-15 22:38:15
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, KSamplerSelect, CLIPTextEncode, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, CLIPTextEncode, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXVConcatAVLatent, FloatConstant, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, ManualSigmas, LTXVConditioning, VAEDecodeTiled, MarkdownNote, LTXVPreprocess, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, LTXVLatentUpsampler, LTXVImgToVideoInplace, MarkdownNote, ImageResizeKJv2, LoraLoaderModelOnly, LoraLoaderModelOnly, easy showAnything, TextCombinerTwo, VHS_VideoCombine, LoadImage, LoadImage, ImageResizeKJv2, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, RunningHub_VoxCPM_LoadModel, SoundFlow_GetLength, PrimitiveFloat, PrimitiveInt, SimpleMath+, LTXVAudioVAEDecode, CR Text, LoadAudio, LTXVImgToVideoInplaceKJ, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, PrimitiveInt, PrimitiveInt, LTXVAudioVAELoader, LTXVEmptyLatentAudio, RunningHub_VoxCPM_Generate, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, TrimAudioDuration]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v6.3_(首尾帧，Fisher优化版)_2057761252751003649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057761252751003649.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（67 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `RandomNoise`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `FloatConstant`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `ManualSigmas`
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `MarkdownNote`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `TextCombinerTwo`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `RunningHub_VoxCPM_LoadModel`
- `SoundFlow_GetLength`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SimpleMath+`
- `LTXVAudioVAEDecode` ★核心
- `CR Text`
- `LoadAudio`
- `LTXVImgToVideoInplaceKJ`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVAudioVAELoader`
- `LTXVEmptyLatentAudio` ★核心
- `RunningHub_VoxCPM_Generate`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（58/67）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`FloatConstant`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVConditioning`、`VAEDecodeTiled`、`LTXVPreprocess`、`ComfyMathExpression`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`TextCombinerTwo`、`VHS_VideoCombine`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`RunningHub_VoxCPM_LoadModel`、`SoundFlow_GetLength`、`SimpleMath+`、`LTXVAudioVAEDecode`、`CR Text`、`LoadAudio`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`LTXVAudioVAELoader`、`LTXVEmptyLatentAudio`、`RunningHub_VoxCPM_Generate`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`TrimAudioDuration`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
