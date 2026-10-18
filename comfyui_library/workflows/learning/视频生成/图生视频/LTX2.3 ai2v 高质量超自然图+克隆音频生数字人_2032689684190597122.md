---
key: 视频生成/图生视频/LTX2.3 ai2v 高质量超自然图+克隆音频生数字人_2032689684190597122.json
name: LTX2.3 ai2v 高质量超自然图+克隆音频生数字人_2032689684190597122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 ai2v 高质量超自然图+克隆音频生数字人_2032689684190597122.json
hash: 64eb55443b551646
coverage: 0.707865
learned_at: 2026-10-15 22:35:36
nodes: [CFGGuider, RandomNoise, Reroute, Reroute, CheckpointLoaderSimple, Reroute, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, LTXVPreprocess, LoraLoaderModelOnly, ResizeImagesByLongerEdge, KSamplerSelect, Reroute, LTXVAudioVAELoader, LoadImage, LTXVImgToVideoInplace, Reroute, KSamplerSelect, EmptyImage, GetImageSize, EmptyLTXVLatentVideo, RandomNoise, SamplerCustomAdvanced, Reroute, LatentUpscaleModelLoader, Reroute, Reroute, Reroute, CFGGuider, Reroute, Bjornulf_ShowInt, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, ImageScaleBy, GetImageSize, LTXVConcatAVLatent, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LTXVConditioning, VAEDecode, ManualSigmas, WhisperSTT, Reroute, INTConstant, LTXVConcatAVLatent, FB_Qwen3TTSVoiceClone, FB_Qwen3TTSVoiceClone, WhisperSTT, AudioConcatenate, easy seed, PlaySound|pysssss, LTXVAudioVAEDecode, CLIPTextEncode, PainterAudioLength, SimpleMath+, CM_FloatToInt, easy showAnything, PreviewAudio, CLIPTextEncode, Reroute, Reroute, CR Prompt Text, CR Prompt Text, LoadAudio, LoadAudio, CreateVideo, LTXVSeparateAVLatent, SaveVideo, Reroute, LTXVLatentUpsampler, Reroute, ManualSigmas, SamplerCustomAdvanced, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVImgToVideoInplace, Reroute, LTXVSeparateAVLatent, Reroute]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3 ai2v 高质量超自然图+克隆音频生数字人_2032689684190597122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032689684190597122.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `CFGGuider`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAELoader`
- `LoadImage`
- `LTXVImgToVideoInplace`
- `Reroute`
- `KSamplerSelect` ★核心
- `EmptyImage`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LatentUpscaleModelLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `CFGGuider`
- `Reroute`
- `Bjornulf_ShowInt`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVConcatAVLatent`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVConditioning`
- `VAEDecode` ★核心
- `ManualSigmas`
- `WhisperSTT`
- `Reroute`
- `INTConstant`
- `LTXVConcatAVLatent`
- `FB_Qwen3TTSVoiceClone`
- `FB_Qwen3TTSVoiceClone`
- `WhisperSTT`
- `AudioConcatenate`
- `easy seed`
- `PlaySound|pysssss`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PainterAudioLength`
- `SimpleMath+`
- `CM_FloatToInt`
- `easy showAnything`
- `PreviewAudio`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadAudio`
- `LoadAudio`
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `SaveVideo`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplace`
- `Reroute`
- `LTXVSeparateAVLatent`
- `Reroute`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **71%**（63/89）

**有卡**：`CFGGuider`、`RandomNoise`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVAudioVAELoader`、`LoadImage`、`LTXVImgToVideoInplace`、`EmptyImage`、`GetImageSize`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`Bjornulf_ShowInt`、`LTXAVTextEncoderLoader`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`ImageScaleBy`、`LTXVConcatAVLatent`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVConditioning`、`VAEDecode`、`ManualSigmas`、`WhisperSTT`、`INTConstant`、`FB_Qwen3TTSVoiceClone`、`AudioConcatenate`、`easy seed`、`PlaySound|pysssss`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`PainterAudioLength`、`SimpleMath+`、`CM_FloatToInt`、`PreviewAudio`、`CR Prompt Text`、`LoadAudio`、`CreateVideo`、`LTXVSeparateAVLatent`、`SaveVideo`、`LTXVLatentUpsampler`、`LTXVCropGuides`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
