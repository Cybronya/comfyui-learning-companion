---
key: 视频生成/图生视频/LTX2.3 高质量超自然图+音频数字人MV_2033038433718898690.json
name: LTX2.3 高质量超自然图+音频数字人MV_2033038433718898690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 高质量超自然图+音频数字人MV_2033038433718898690.json
hash: ab928c7db40c771c
coverage: 0.658537
learned_at: 2026-10-15 22:35:38
nodes: [CFGGuider, RandomNoise, Reroute, Reroute, CheckpointLoaderSimple, Reroute, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, Reroute, Reroute, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVPreprocess, LoraLoaderModelOnly, ResizeImagesByLongerEdge, KSamplerSelect, Reroute, LTXVAudioVAELoader, LTXVImgToVideoInplace, Reroute, KSamplerSelect, LTXVConcatAVLatent, EmptyImage, GetImageSize, EmptyLTXVLatentVideo, Reroute, INTConstant, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, Reroute, LatentUpscaleModelLoader, Reroute, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, LTXVCropGuides, CFGGuider, Reroute, Bjornulf_ShowInt, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, ImageScaleBy, LTXVConcatAVLatent, LTXVLatentUpsampler, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LTXVConditioning, CreateVideo, PainterAudioLength, CM_FloatToInt, SetNode, LoadAudio, easy showAnything, SimpleMath+, Reroute, SamplerCustomAdvanced, Reroute, VAEDecode, LTXVAudioVAEDecode, LoadImage, PreviewAudio, SaveVideo, CLIPTextEncode, CLIPTextEncode, ManualSigmas, Reroute, GetImageSize, ManualSigmas, LTXVImgToVideoInplace, Reroute, AudioCrop]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3 高质量超自然图+音频数字人MV_2033038433718898690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033038433718898690.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `CFGGuider`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
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
- `LTXVConcatAVLatent`
- `EmptyImage`
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `Reroute`
- `INTConstant`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LatentUpscaleModelLoader`
- `Reroute`
- `LTXVSeparateAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVCropGuides`
- `CFGGuider`
- `Reroute`
- `Bjornulf_ShowInt`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `ImageScaleBy`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVConditioning`
- `CreateVideo`
- `PainterAudioLength`
- `CM_FloatToInt`
- `SetNode`
- `LoadAudio`
- `easy showAnything`
- `SimpleMath+`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LoadImage`
- `PreviewAudio`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `Reroute`
- `GetImageSize`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `Reroute`
- `AudioCrop`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **66%**（54/82）

**有卡**：`CFGGuider`、`RandomNoise`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`KSamplerSelect`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyImage`、`GetImageSize`、`EmptyLTXVLatentVideo`、`INTConstant`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`Bjornulf_ShowInt`、`LTXAVTextEncoderLoader`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`ImageScaleBy`、`LTXVLatentUpsampler`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVConditioning`、`CreateVideo`、`PainterAudioLength`、`CM_FloatToInt`、`LoadAudio`、`SimpleMath+`、`VAEDecode`、`LTXVAudioVAEDecode`、`LoadImage`、`PreviewAudio`、`SaveVideo`、`CLIPTextEncode`、`ManualSigmas`、`AudioCrop`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
