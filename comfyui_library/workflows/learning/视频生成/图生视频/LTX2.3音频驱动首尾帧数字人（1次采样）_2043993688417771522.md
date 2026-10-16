---
key: 视频生成/图生视频/LTX2.3音频驱动首尾帧数字人（1次采样）_2043993688417771522.json
name: LTX2.3音频驱动首尾帧数字人（1次采样）_2043993688417771522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043993688417771522.json
hash: 8ee21897b13d3ce6
coverage: 0.785714
learned_at: 2026-10-15 22:36:35
nodes: [LoraLoaderModelOnly, EmptyImage, GetImageSize, CM_FloatToInt, LTXAVTextEncoderLoader, LTXVPreprocess, CheckpointLoaderSimple, SimpleMath+, KSamplerSelect, GetImageSize, LTXVAudioVAELoader, LoadImage, EmptyLTXVLatentVideo, SolidMask, INTConstant, VAEDecodeTiled, LTXVAudioVAEDecode, LayerUtility: ImageScaleByAspectRatio V2, ComfyMathExpression, SetNode, Int, SetNode, Int, easy showAnything, CFGGuider, RandomNoise, GetNode, Bjornulf_ShowInt, PainterAudioLength, LTXVAudioVAEEncode, GetNode, SetLatentNoiseMask, GetNode, LTXVImgToVideoInplaceKJ, GetNode, SetNode, SetNode, GetNode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVSeparateAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVConcatAVLatent, GetNode, CreateVideo, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ttN concat, SaveVideo, LTXVPreprocess, LoadImage, LoadAudio, AudioCrop, PreviewAudio]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3音频驱动首尾帧数字人（1次采样）_2043993688417771522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043993688417771522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `LoraLoaderModelOnly` ★核心
- `EmptyImage`
- `GetImageSize`
- `CM_FloatToInt`
- `LTXAVTextEncoderLoader`
- `LTXVPreprocess`
- `CheckpointLoaderSimple` ★核心
- `SimpleMath+`
- `KSamplerSelect` ★核心
- `GetImageSize`
- `LTXVAudioVAELoader`
- `LoadImage`
- `EmptyLTXVLatentVideo`
- `SolidMask`
- `INTConstant`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ComfyMathExpression`
- `SetNode`
- `Int`
- `SetNode`
- `Int`
- `easy showAnything`
- `CFGGuider`
- `RandomNoise`
- `GetNode`
- `Bjornulf_ShowInt`
- `PainterAudioLength`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ttN concat`
- `SaveVideo`
- `LTXVPreprocess`
- `LoadImage`
- `LoadAudio`
- `AudioCrop`
- `PreviewAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **79%**（44/56）

**有卡**：`LoraLoaderModelOnly`、`EmptyImage`、`GetImageSize`、`CM_FloatToInt`、`LTXAVTextEncoderLoader`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`SimpleMath+`、`KSamplerSelect`、`LTXVAudioVAELoader`、`LoadImage`、`EmptyLTXVLatentVideo`、`SolidMask`、`INTConstant`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ComfyMathExpression`、`Int`、`CFGGuider`、`RandomNoise`、`Bjornulf_ShowInt`、`PainterAudioLength`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVImgToVideoInplaceKJ`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`CreateVideo`、`ttN concat`、`SaveVideo`、`LoadAudio`、`AudioCrop`、`PreviewAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
