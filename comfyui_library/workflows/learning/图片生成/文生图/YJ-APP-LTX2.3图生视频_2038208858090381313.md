---
key: 图片生成/文生图/YJ-APP-LTX2.3图生视频_2038208858090381313.json
name: YJ-APP-LTX2.3图生视频_2038208858090381313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/YJ-APP-LTX2.3图生视频_2038208858090381313.json
hash: 6662edabe8f991bf
coverage: 0.933333
learned_at: 2026-10-21 02:55:26
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LatentUpscaleModelLoader, CLIPTextEncode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, PreviewAny, LTXVLatentUpsampler, LTXVConcatAVLatent, LTXVCropGuides, CreateVideo, RandomNoise, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageScaleBy, GetImageSize, KSampler, MarkdownNote, TextGenerateLTX2Prompt, SaveVideo, LTXVImgToVideoInplace, LoadImage, ResizeImageMaskNode, GetImageSize, Int, Int, EmptyImage, Text, DualCLIPLoader, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVConditioning, LTXVImgToVideoInplace, SimpleMath+, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 758931124220998, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/YJ-APP-LTX2.3图生视频_2038208858090381313.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/YJ-APP-LTX2.3图生视频_2038208858090381313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `CreateVideo`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleBy`
- `GetImageSize`
- `KSampler` ★核心
- `MarkdownNote`
- `TextGenerateLTX2Prompt`
- `SaveVideo`
- `LTXVImgToVideoInplace`
- `LoadImage`
- `ResizeImageMaskNode`
- `GetImageSize`
- `Int`
- `Int`
- `EmptyImage`
- `Text`
- `DualCLIPLoader`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `SimpleMath+`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `758931124220998`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **93%**（42/45）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`CreateVideo`、`RandomNoise`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageScaleBy`、`GetImageSize`、`KSampler`、`TextGenerateLTX2Prompt`、`SaveVideo`、`LTXVImgToVideoInplace`、`LoadImage`、`ResizeImageMaskNode`、`Int`、`EmptyImage`、`Text`、`DualCLIPLoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVConditioning`、`SimpleMath+`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
