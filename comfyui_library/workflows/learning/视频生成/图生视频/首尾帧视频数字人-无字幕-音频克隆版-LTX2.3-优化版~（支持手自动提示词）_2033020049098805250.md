---
key: 视频生成/图生视频/首尾帧视频数字人-无字幕-音频克隆版-LTX2.3-优化版~（支持手自动提示词）_2033020049098805250.json
name: 首尾帧视频数字人-无字幕-音频克隆版-LTX2.3-优化版~（支持手自动提示词）_2033020049098805250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033020049098805250.json
hash: b3a9c1da52879d19
coverage: 0.609756
learned_at: 2026-10-15 22:35:37
nodes: [CreateVideo, CLIPTextEncode, CFGGuider, RandomNoise, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVConditioning, CheckpointLoaderSimple, Reroute, EmptyImage, ImageScaleBy, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, Reroute, Reroute, Reroute, Reroute, ModelPatchTorchSettings, Reroute, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVAudioVAEDecode, VAEDecode, Reroute, Reroute, Reroute, Reroute, RH_LLMAPI_Pro_Node, MarkdownNote, MarkdownNote, ImpactConditionalBranch, Switch any [Crystools], easy showAnything, RH_LLMAPI_Pro_Node, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LTXVLatentUpsampler, Reroute, KSamplerSelect, Reroute, RandomNoise, Reroute, Reroute, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, Reroute, CFGGuider, ManualSigmas, LTXVConcatAVLatent, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LoadImage, LTXVPreprocess, Reroute, Reroute, LTXVConcatAVLatent, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, LTXVPreprocess, Reroute, Reroute, LoadImage, MarkdownNote, CR Text, PrimitiveNode, CR Text, PreviewAny, PreviewImage, Reroute, Reroute, DualCLIPLoader, TextGenerateLTX2Prompt, PreviewAny, Reroute, Reroute, Reroute, Reroute, MarkdownNote, CR Text, CR Text, CLIPTextEncode, easy imageConcat, ImpactInt, ImpactInt, SimpleMath+, easy showAnything, PainterAudioLength, PreviewAudio, CM_FloatToInt, FB_Qwen3TTSVoiceClone, WhisperSTT, easy seed, EmptyLTXVLatentVideo, INTConstant, Bjornulf_ShowInt, LTXVAudioVAEEncode, SetLatentNoiseMask, GetImageSize, GetImageSize, SolidMask, Reroute, LoadAudio, LTXVEmptyLatentAudio, CR Text, SaveVideo, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/首尾帧视频数字人-无字幕-音频克隆版-LTX2.3-优化版~（支持手自动提示词）_2033020049098805250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033020049098805250.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（123 个）：
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `EmptyImage`
- `ImageScaleBy`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelPatchTorchSettings`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `MarkdownNote`
- `ImpactConditionalBranch`
- `Switch any [Crystools]`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `Reroute`
- `KSamplerSelect` ★核心
- `Reroute`
- `RandomNoise`
- `Reroute`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `Reroute`
- `CFGGuider`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `LoadImage`
- `MarkdownNote`
- `CR Text`
- `PrimitiveNode`
- `CR Text`
- `PreviewAny`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `DualCLIPLoader`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `CR Text`
- `CR Text`
- `CLIPTextEncode` ★核心
- `easy imageConcat`
- `ImpactInt`
- `ImpactInt`
- `SimpleMath+`
- `easy showAnything`
- `PainterAudioLength`
- `PreviewAudio`
- `CM_FloatToInt`
- `FB_Qwen3TTSVoiceClone`
- `WhisperSTT`
- `easy seed`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `Bjornulf_ShowInt`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `GetImageSize`
- `GetImageSize`
- `SolidMask`
- `Reroute`
- `LoadAudio`
- `LTXVEmptyLatentAudio` ★核心
- `CR Text`
- `SaveVideo`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（75/123）

**有卡**：`CreateVideo`、`CLIPTextEncode`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVConditioning`、`CheckpointLoaderSimple`、`EmptyImage`、`ImageScaleBy`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecode`、`RH_LLMAPI_Pro_Node`、`ImpactConditionalBranch`、`Switch any [Crystools]`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LoadImage`、`LTXVPreprocess`、`LTXVFirstLastFrameControl_TTP`、`LTXVImgToVideoInplace`、`CR Text`、`DualCLIPLoader`、`TextGenerateLTX2Prompt`、`easy imageConcat`、`ImpactInt`、`SimpleMath+`、`PainterAudioLength`、`PreviewAudio`、`CM_FloatToInt`、`FB_Qwen3TTSVoiceClone`、`WhisperSTT`、`easy seed`、`EmptyLTXVLatentVideo`、`INTConstant`、`Bjornulf_ShowInt`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`GetImageSize`、`SolidMask`、`LoadAudio`、`LTXVEmptyLatentAudio`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
