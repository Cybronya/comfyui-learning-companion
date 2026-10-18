---
key: 视频生成/图生视频/LTX2.3 _音频数字人MV_2037904151203549186.json
name: LTX2.3 _音频数字人MV_2037904151203549186.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 _音频数字人MV_2037904151203549186.json
hash: d05c00b2b8893432
coverage: 0.964286
learned_at: 2026-10-15 22:35:59
nodes: [KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, Bjornulf_ShowInt, ImpactInt, PreviewAudio, LoadImage, AudioCrop, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LTXVPreprocess, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, GetImageSize, EmptyImage, INTConstant, GetImageSize, CLIPTextEncode, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, SolidMask, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVConcatAVLatent, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVCropGuides, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVLatentUpsampler, LTXVImgToVideoInplace, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, CFGGuider, CreateVideo, VAEDecode, LTXVAudioVAEDecode, SimpleMath+, easy showAnything, SetNode, PainterAudioLength, CM_FloatToInt, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LoadAudio, SaveVideo, LTXVConditioning, SamplerCustomAdvanced, ImageScaleBy]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/LTX2.3 _音频数字人MV_2037904151203549186.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037904151203549186.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `Bjornulf_ShowInt`
- `ImpactInt`
- `PreviewAudio`
- `LoadImage`
- `AudioCrop`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `GetImageSize`
- `EmptyImage`
- `INTConstant`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `CFGGuider`
- `CreateVideo`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `PainterAudioLength`
- `CM_FloatToInt`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LoadAudio`
- `SaveVideo`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleBy`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **96%**（54/56）

**有卡**：`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`Bjornulf_ShowInt`、`ImpactInt`、`PreviewAudio`、`LoadImage`、`AudioCrop`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`GetImageSize`、`EmptyImage`、`INTConstant`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVConcatAVLatent`、`CFGGuider`、`ManualSigmas`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`CreateVideo`、`VAEDecode`、`LTXVAudioVAEDecode`、`SimpleMath+`、`PainterAudioLength`、`CM_FloatToInt`、`SamplerCustomAdvanced`、`LoadAudio`、`SaveVideo`、`LTXVConditioning`、`ImageScaleBy`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
