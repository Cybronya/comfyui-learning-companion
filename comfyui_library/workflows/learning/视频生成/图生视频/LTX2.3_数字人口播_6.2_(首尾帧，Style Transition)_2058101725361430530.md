---
key: 视频生成/图生视频/LTX2.3_数字人口播_6.2_(首尾帧，Style Transition)_2058101725361430530.json
name: LTX2.3_数字人口播_6.2_(首尾帧，Style Transition)_2058101725361430530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058101725361430530.json
hash: 0e67ee4030acfd2f
coverage: 0.5125
learned_at: 2026-10-15 22:38:18
nodes: [RandomNoise, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, LTXVAddGuide, PrimitiveInt, LTXVAddGuide, SamplerEulerAncestral, ManualSigmas, SamplerCustomAdvanced, PrimitiveInt, PrimitiveInt, VAEDecodeTiled, LTXVSeparateAVLatent, CheckpointLoaderSimple, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, CFGGuider, LoraLoaderModelOnly, ResizeImageMaskNode, LoraLoaderModelOnly, LoadImage, SaveVideo, RunningHub_VoxCPM_LoadModel, SetLatentNoiseMask, SoundFlow_GetLength, ComfyMathExpression, SolidMask, LTXVAudioVAEEncode, LTXVAudioVAELoader, RunningHub_VoxCPM_Generate, GetImageSize, CR Text, ComfyMathExpression, LTXVConcatAVLatent, CreateVideo, LoadImage, ResizeImageMaskNode, LTXVPreprocess, LTXAVTextEncoderLoader, LoadAudio, CLIPTextEncode, CLIPTextEncode, PrimitiveFloat, TrimAudioDuration]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3_数字人口播_6.2_(首尾帧，Style Transition)_2058101725361430530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058101725361430530.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `RandomNoise`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `LTXVAddGuide`
- `PrimitiveInt`
- `LTXVAddGuide`
- `SamplerEulerAncestral` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `ResizeImageMaskNode`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `SaveVideo`
- `RunningHub_VoxCPM_LoadModel`
- `SetLatentNoiseMask`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVAudioVAELoader`
- `RunningHub_VoxCPM_Generate`
- `GetImageSize`
- `CR Text`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `CreateVideo`
- `LoadImage`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXAVTextEncoderLoader`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `TrimAudioDuration`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **51%**（41/80）

**有卡**：`RandomNoise`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`LTXVAddGuide`、`SamplerEulerAncestral`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`CheckpointLoaderSimple`、`CFGGuider`、`LoraLoaderModelOnly`、`ResizeImageMaskNode`、`LoadImage`、`SaveVideo`、`RunningHub_VoxCPM_LoadModel`、`SetLatentNoiseMask`、`SoundFlow_GetLength`、`ComfyMathExpression`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVAudioVAELoader`、`RunningHub_VoxCPM_Generate`、`GetImageSize`、`CR Text`、`LTXVConcatAVLatent`、`CreateVideo`、`LTXAVTextEncoderLoader`、`LoadAudio`、`CLIPTextEncode`、`TrimAudioDuration`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVConcatAVLatent
