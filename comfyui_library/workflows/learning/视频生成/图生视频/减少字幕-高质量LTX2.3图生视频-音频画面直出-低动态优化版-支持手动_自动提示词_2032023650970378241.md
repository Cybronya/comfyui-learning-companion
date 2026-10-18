---
key: 视频生成/图生视频/减少字幕-高质量LTX2.3图生视频-音频画面直出-低动态优化版-支持手动_自动提示词_2032023650970378241.json
name: 减少字幕-高质量LTX2.3图生视频-音频画面直出-低动态优化版-支持手动_自动提示词_2032023650970378241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/减少字幕-高质量LTX2.3图生视频-音频画面直出-低动态优化版-支持手动_自动提示词_2032023650970378241.json
hash: 785cbdd8ee059b97
coverage: 0.559633
learned_at: 2026-10-15 22:35:34
nodes: [CLIPTextEncode, CFGGuider, RandomNoise, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, LTXVConcatAVLatent, Reroute, Reroute, CheckpointLoaderSimple, Reroute, EmptyImage, ImageScaleBy, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, GetImageSize, Reroute, Reroute, Reroute, Reroute, GetImageSize, ModelPatchTorchSettings, Reroute, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, Reroute, Reroute, LTXVAudioVAEDecode, VAEDecode, Reroute, Reroute, Reroute, Reroute, Reroute, DualCLIPLoader, LTXVPreprocess, MarkdownNote, MarkdownNote, Reroute, RH_LLMAPI_Pro_Node, MarkdownNote, MarkdownNote, ImpactConditionalBranch, Switch any [Crystools], easy showAnything, RH_LLMAPI_Pro_Node, PrimitiveNode, PreviewAny, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, CR Text, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LTXVLatentUpsampler, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, Reroute, KSamplerSelect, Reroute, RandomNoise, Reroute, Reroute, Reroute, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, Reroute, CFGGuider, ManualSigmas, LTXVConcatAVLatent, Reroute, Reroute, LTXVImgToVideoInplace, Reroute, MarkdownNote, MarkdownNote, LoadImage, LoadImage, MarkdownNote, TextGenerateLTX2Prompt, ImpactInt, PreviewAny, CR Text, CR Text, CLIPTextEncode, CR Text, CR Text, SimpleMath+, Reroute, Reroute, LTXVConditioning, Reroute, easy convertAnything, Reroute, easy convertAnything, CreateVideo, Reroute, Reroute, Int, SaveVideo, ImpactInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/减少字幕-高质量LTX2.3图生视频-音频画面直出-低动态优化版-支持手动_自动提示词_2032023650970378241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032023650970378241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（109 个）：
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `Reroute`
- `Reroute`
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
- `Reroute`
- `DualCLIPLoader`
- `LTXVPreprocess`
- `MarkdownNote`
- `MarkdownNote`
- `Reroute`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `MarkdownNote`
- `ImpactConditionalBranch`
- `Switch any [Crystools]`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveNode`
- `PreviewAny`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `Reroute`
- `KSamplerSelect` ★核心
- `Reroute`
- `RandomNoise`
- `Reroute`
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
- `LTXVImgToVideoInplace`
- `Reroute`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `TextGenerateLTX2Prompt`
- `ImpactInt`
- `PreviewAny`
- `CR Text`
- `CR Text`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Text`
- `SimpleMath+`
- `Reroute`
- `Reroute`
- `LTXVConditioning`
- `Reroute`
- `easy convertAnything`
- `Reroute`
- `easy convertAnything`
- `CreateVideo`
- `Reroute`
- `Reroute`
- `Int`
- `SaveVideo`
- `ImpactInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（61/109）

**有卡**：`CLIPTextEncode`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`CheckpointLoaderSimple`、`EmptyImage`、`ImageScaleBy`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`GetImageSize`、`ModelPatchTorchSettings`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecode`、`DualCLIPLoader`、`LTXVPreprocess`、`RH_LLMAPI_Pro_Node`、`ImpactConditionalBranch`、`Switch any [Crystools]`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`ManualSigmas`、`LoadImage`、`TextGenerateLTX2Prompt`、`ImpactInt`、`SimpleMath+`、`LTXVConditioning`、`easy convertAnything`、`CreateVideo`、`Int`、`SaveVideo`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
