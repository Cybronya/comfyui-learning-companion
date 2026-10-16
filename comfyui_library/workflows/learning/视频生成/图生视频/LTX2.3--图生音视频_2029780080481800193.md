---
key: 视频生成/图生视频/LTX2.3--图生音视频_2029780080481800193.json
name: LTX2.3--图生音视频_2029780080481800193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2029780080481800193.json
hash: b3bde3de23664bf6
coverage: 0.911111
learned_at: 2026-10-15 22:35:23
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetImageSize, LTXVPreprocess, CFGGuider, LatentUpscaleModelLoader, EmptyImage, CLIPTextEncode, LTXVImgToVideoInplace, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, MarkdownNote, MarkdownNote, VAEDecode, ResizeImagesByLongerEdge, LTXVSeparateAVLatent, LTXVAudioVAEDecode, PreviewAny, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVCropGuides, CreateVideo, LTXVConditioning, RandomNoise, DualCLIPLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageScaleBy, GetImageSize, PrimitiveInt, SaveVideo, KSampler, LoadImage, Text, CLIPTextEncode, TextGenerateLTX2Prompt, ResizeImageMaskNode, Int, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 590262634552718, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3--图生音视频_2029780080481800193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029780080481800193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetImageSize`
- `LTXVPreprocess`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `EmptyImage`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `VAEDecode` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `PreviewAny`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `CreateVideo`
- `LTXVConditioning`
- `RandomNoise`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `PrimitiveInt`
- `SaveVideo`
- `KSampler` ★核心
- `LoadImage`
- `Text`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `ResizeImageMaskNode`
- `Int`
- `Int`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `590262634552718`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **91%**（41/45）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`GetImageSize`、`LTXVPreprocess`、`CFGGuider`、`LatentUpscaleModelLoader`、`EmptyImage`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAEDecode`、`ResizeImagesByLongerEdge`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`CreateVideo`、`LTXVConditioning`、`RandomNoise`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageScaleBy`、`SaveVideo`、`KSampler`、`LoadImage`、`Text`、`TextGenerateLTX2Prompt`、`ResizeImageMaskNode`、`Int`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
