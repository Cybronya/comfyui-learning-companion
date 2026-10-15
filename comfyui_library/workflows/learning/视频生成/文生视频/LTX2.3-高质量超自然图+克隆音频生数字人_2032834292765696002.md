---
key: 视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json
name: LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json
hash: 5338b6d56d79241d
coverage: 0.670455
learned_at: 2026-10-15 22:45:05
nodes: [CFGGuider, RandomNoise, Reroute, Reroute, CheckpointLoaderSimple, Reroute, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, LTXVPreprocess, LoraLoaderModelOnly, ResizeImagesByLongerEdge, KSamplerSelect, Reroute, LTXVAudioVAELoader, LTXVImgToVideoInplace, Reroute, KSamplerSelect, EmptyImage, GetImageSize, EmptyLTXVLatentVideo, RandomNoise, SamplerCustomAdvanced, Reroute, LatentUpscaleModelLoader, Reroute, Reroute, Reroute, CFGGuider, Reroute, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, ImageScaleBy, GetImageSize, LTXVConcatAVLatent, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LTXVConditioning, VAEDecode, ManualSigmas, WhisperSTT, Reroute, INTConstant, LTXVConcatAVLatent, LTXVAudioVAEDecode, easy showAnything, PreviewAudio, Reroute, Reroute, CreateVideo, LTXVSeparateAVLatent, SaveVideo, Reroute, LTXVLatentUpsampler, Reroute, ManualSigmas, SamplerCustomAdvanced, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVImgToVideoInplace, Reroute, LTXVSeparateAVLatent, Reroute, CR Prompt Text, LoadImage, LoadAudio, Bjornulf_ShowInt, easy seed, FB_Qwen3TTSVoiceClone, PreviewAudio, PainterAudioLength, CM_FloatToInt, SimpleMath+, Reroute, Reroute, Reroute, CLIPTextEncode, CLIPTextEncode, CR Text]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
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
- `LTXVAudioVAEDecode` ★核心
- `easy showAnything`
- `PreviewAudio`
- `Reroute`
- `Reroute`
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
- `CR Prompt Text`
- `LoadImage`
- `LoadAudio`
- `Bjornulf_ShowInt`
- `easy seed`
- `FB_Qwen3TTSVoiceClone`
- `PreviewAudio`
- `PainterAudioLength`
- `CM_FloatToInt`
- `SimpleMath+`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **67%**（59/88）

**有卡**：`CFGGuider`、`RandomNoise`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`EmptyImage`、`GetImageSize`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`ImageScaleBy`、`LTXVConcatAVLatent`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVConditioning`、`VAEDecode`、`ManualSigmas`、`WhisperSTT`、`INTConstant`、`LTXVAudioVAEDecode`、`PreviewAudio`、`CreateVideo`、`LTXVSeparateAVLatent`、`SaveVideo`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`CR Prompt Text`、`LoadImage`、`LoadAudio`、`Bjornulf_ShowInt`、`easy seed`、`FB_Qwen3TTSVoiceClone`、`PainterAudioLength`、`CM_FloatToInt`、`SimpleMath+`、`CLIPTextEncode`、`CR Text`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
