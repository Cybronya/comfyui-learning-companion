---
key: 数字人/数字人/灵感岛GEOLTX2.3图生视频_2036313104744718337.json
name: 灵感岛GEOLTX2.3图生视频_2036313104744718337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/灵感岛GEOLTX2.3图生视频_2036313104744718337.json
hash: 56965a25f174d8b0
coverage: 0.904762
learned_at: 2026-10-26 02:03:49
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetImageSize, LTXVPreprocess, CFGGuider, EmptyImage, LTXVImgToVideoInplace, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, MarkdownNote, MarkdownNote, ResizeImagesByLongerEdge, PreviewAny, LTXVConcatAVLatent, LTXVCropGuides, LTXVConditioning, RandomNoise, DualCLIPLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ImageScaleBy, GetImageSize, KSampler, LoadImage, TextGenerateLTX2Prompt, SaveVideo, VAEDecode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, CreateVideo, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVLatentUpsampler, ResizeImageMaskNode, CLIPTextEncode, CLIPTextEncode, PrimitiveInt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 837214377136081, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/灵感岛GEOLTX2.3图生视频_2036313104744718337.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/灵感岛GEOLTX2.3图生视频_2036313104744718337.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetImageSize`
- `LTXVPreprocess`
- `CFGGuider`
- `EmptyImage`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ResizeImagesByLongerEdge`
- `PreviewAny`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVConditioning`
- `RandomNoise`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ImageScaleBy`
- `GetImageSize`
- `KSampler` ★核心
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `SaveVideo`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `837214377136081`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`GetImageSize`、`LTXVPreprocess`、`CFGGuider`、`EmptyImage`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVCropGuides`、`LTXVConditioning`、`RandomNoise`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`ImageScaleBy`、`KSampler`、`LoadImage`、`TextGenerateLTX2Prompt`、`SaveVideo`、`VAEDecode`、`LTXVAudioVAEDecode`、`CreateVideo`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`ResizeImageMaskNode`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
