---
key: 视频生成/图生视频/LTX2.3图生视频-音频画面同步直出_2031324375839940609.json
name: LTX2.3图生视频-音频画面同步直出_2031324375839940609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031324375839940609.json
hash: 5cede6e2cc64aca8
coverage: 0.590909
learned_at: 2026-10-15 22:35:30
nodes: [CreateVideo, CLIPTextEncode, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, RandomNoise, SamplerCustomAdvanced, Reroute, Reroute, Reroute, Reroute, LTXVConcatAVLatent, Reroute, Reroute, LTXVConditioning, CheckpointLoaderSimple, Reroute, LTXVScheduler, EmptyImage, ImageScaleBy, PathchSageAttentionKJ, LTXVChunkFeedForward, Reroute, GetImageSize, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVLatentUpsampler, GetImageSize, ModelPatchTorchSettings, SimpleMath+, ResizeImagesByLongerEdge, Reroute, KSampler, Reroute, LTXVSeparateAVLatent, Reroute, LTXVCropGuides, Reroute, Reroute, Reroute, Reroute, LTXVAudioVAEDecode, VAEDecode, Reroute, Reroute, LTXVImgToVideoInplace, Reroute, Reroute, Reroute, Reroute, DualCLIPLoader, CLIPTextEncode, LTXVPreprocess, MarkdownNote, MarkdownNote, Reroute, RH_LLMAPI_Pro_Node, MarkdownNote, MarkdownNote, ImpactInt, LoadImage, ResizeImageMaskNode, ImpactConditionalBranch, Switch any [Crystools], PreviewAny, TextGenerateLTX2Prompt, CR Text, ImpactInt, LTXVImgToVideoInplace, easy showAnything, RH_LLMAPI_Pro_Node, ImpactInt, PrimitiveNode, CR Text, PreviewAny, LTXAVTextEncoderLoader, LTXVAudioVAELoader, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, SaveVideo, MarkdownNote, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 673974685906517, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频-音频画面同步直出_2031324375839940609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031324375839940609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
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
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `LTXVScheduler`
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
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `GetImageSize`
- `ModelPatchTorchSettings`
- `SimpleMath+`
- `ResizeImagesByLongerEdge`
- `Reroute`
- `KSampler` ★核心
- `Reroute`
- `LTXVSeparateAVLatent`
- `Reroute`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplace`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `MarkdownNote`
- `MarkdownNote`
- `Reroute`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `MarkdownNote`
- `ImpactInt`
- `LoadImage`
- `ResizeImageMaskNode`
- `ImpactConditionalBranch`
- `Switch any [Crystools]`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `CR Text`
- `ImpactInt`
- `LTXVImgToVideoInplace`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `ImpactInt`
- `PrimitiveNode`
- `CR Text`
- `PreviewAny`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `SaveVideo`
- `MarkdownNote`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `673974685906517`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **59%**（52/88）

**有卡**：`CreateVideo`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVConditioning`、`CheckpointLoaderSimple`、`LTXVScheduler`、`EmptyImage`、`ImageScaleBy`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`GetImageSize`、`LTXVLatentUpsampler`、`ModelPatchTorchSettings`、`SimpleMath+`、`ResizeImagesByLongerEdge`、`KSampler`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVImgToVideoInplace`、`DualCLIPLoader`、`LTXVPreprocess`、`RH_LLMAPI_Pro_Node`、`ImpactInt`、`LoadImage`、`ResizeImageMaskNode`、`ImpactConditionalBranch`、`Switch any [Crystools]`、`TextGenerateLTX2Prompt`、`CR Text`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`SaveVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
