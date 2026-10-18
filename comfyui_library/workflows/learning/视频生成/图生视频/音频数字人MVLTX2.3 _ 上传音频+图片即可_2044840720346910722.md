---
key: 视频生成/图生视频/音频数字人MVLTX2.3 _ 上传音频+图片即可_2044840720346910722.json
name: 音频数字人MVLTX2.3 _ 上传音频+图片即可_2044840720346910722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/音频数字人MVLTX2.3 _ 上传音频+图片即可_2044840720346910722.json
hash: 7142eb41ff3b0b43
coverage: 0.935484
learned_at: 2026-10-15 22:36:42
nodes: [KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, LTXVPreprocess, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, GetImageSize, EmptyImage, INTConstant, GetImageSize, CLIPTextEncode, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, SolidMask, SetLatentNoiseMask, LTXVAudioVAEEncode, LTXVConcatAVLatent, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVCropGuides, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVLatentUpsampler, LTXVImgToVideoInplace, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, CFGGuider, CreateVideo, VAEDecode, LTXVAudioVAEDecode, SimpleMath+, easy showAnything, SetNode, PainterAudioLength, CM_FloatToInt, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, SamplerCustomAdvanced, ImageScaleBy, CLIPTextEncode, RH_LLMAPI_Pro_Node, CR Prompt Text, PreviewAudio, ResizeImagesByLongerEdge, LTXVConditioning, LayerUtility: ImageScaleByAspectRatio V2, ShowAnything|Mie, Note, SaveVideo, ImpactInt, LoadAudio, CR Text, AudioCrop, LoadImage, Bjornulf_ShowInt, Note]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors"}
---

# 视频生成/图生视频/音频数字人MVLTX2.3 _ 上传音频+图片即可_2044840720346910722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044840720346910722.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVPreprocess`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `GetImageSize`
- `EmptyImage`
- `INTConstant`
- `GetImageSize`
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
- `SamplerCustomAdvanced` ★核心
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `PreviewAudio`
- `ResizeImagesByLongerEdge`
- `LTXVConditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowAnything|Mie`
- `Note`
- `SaveVideo`
- `ImpactInt`
- `LoadAudio`
- `CR Text`
- `AudioCrop`
- `LoadImage`
- `Bjornulf_ShowInt`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **94%**（58/62）

**有卡**：`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`GetImageSize`、`EmptyImage`、`INTConstant`、`CLIPTextEncode`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`SolidMask`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`LTXVConcatAVLatent`、`CFGGuider`、`ManualSigmas`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`CreateVideo`、`VAEDecode`、`LTXVAudioVAEDecode`、`SimpleMath+`、`PainterAudioLength`、`CM_FloatToInt`、`SamplerCustomAdvanced`、`ImageScaleBy`、`RH_LLMAPI_Pro_Node`、`CR Prompt Text`、`PreviewAudio`、`ResizeImagesByLongerEdge`、`LTXVConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`ShowAnything|Mie`、`SaveVideo`、`ImpactInt`、`LoadAudio`、`CR Text`、`AudioCrop`、`LoadImage`、`Bjornulf_ShowInt`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
