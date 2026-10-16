---
key: 视频生成/图生视频/无字幕高质量首尾帧视频数字人LTX2.3-音频画面直出-优化版-支持手动_自动提示词_2032091629703663617.json
name: 无字幕高质量首尾帧视频数字人LTX2.3-音频画面直出-优化版-支持手动_自动提示词_2032091629703663617.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032091629703663617.json
hash: 9adff7d6b3ad79dd
coverage: 0.5625
learned_at: 2026-10-15 22:35:34
nodes: [CreateVideo, CLIPTextEncode, CFGGuider, RandomNoise, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVConditioning, CheckpointLoaderSimple, Reroute, EmptyImage, ImageScaleBy, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, GetImageSize, Reroute, Reroute, Reroute, Reroute, GetImageSize, ModelPatchTorchSettings, SimpleMath+, Reroute, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVAudioVAEDecode, VAEDecode, Reroute, Reroute, Reroute, Reroute, RH_LLMAPI_Pro_Node, MarkdownNote, MarkdownNote, ImpactConditionalBranch, Switch any [Crystools], easy showAnything, RH_LLMAPI_Pro_Node, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LTXVLatentUpsampler, Reroute, KSamplerSelect, Reroute, RandomNoise, Reroute, Reroute, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, Reroute, CFGGuider, ManualSigmas, LTXVConcatAVLatent, Reroute, Reroute, Reroute, MarkdownNote, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LoadImage, LTXVPreprocess, Reroute, Reroute, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, LTXVPreprocess, Reroute, Reroute, EmptyLTXVLatentVideo, LoadImage, MarkdownNote, CR Text, PrimitiveNode, CR Text, PreviewAny, PreviewImage, Reroute, Reroute, DualCLIPLoader, TextGenerateLTX2Prompt, PreviewAny, Reroute, Reroute, Reroute, Reroute, MarkdownNote, MarkdownNote, CR Text, CR Text, CLIPTextEncode, CR Text, ImpactInt, SaveVideo, easy imageConcat, LoadImage, ImpactInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/无字幕高质量首尾帧视频数字人LTX2.3-音频画面直出-优化版-支持手动_自动提示词_2032091629703663617.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032091629703663617.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
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
- `GetImageSize`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetImageSize`
- `ModelPatchTorchSettings`
- `SimpleMath+`
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
- `MarkdownNote`
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVFirstLastFrameControl_TTP`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `EmptyLTXVLatentVideo`
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
- `MarkdownNote`
- `CR Text`
- `CR Text`
- `CLIPTextEncode` ★核心
- `CR Text`
- `ImpactInt`
- `SaveVideo`
- `easy imageConcat`
- `LoadImage`
- `ImpactInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（63/112）

**有卡**：`CreateVideo`、`CLIPTextEncode`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVConditioning`、`CheckpointLoaderSimple`、`EmptyImage`、`ImageScaleBy`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`GetImageSize`、`ModelPatchTorchSettings`、`SimpleMath+`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecode`、`RH_LLMAPI_Pro_Node`、`ImpactConditionalBranch`、`Switch any [Crystools]`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`LoadImage`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`LTXVFirstLastFrameControl_TTP`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`CR Text`、`DualCLIPLoader`、`TextGenerateLTX2Prompt`、`ImpactInt`、`SaveVideo`、`easy imageConcat`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
