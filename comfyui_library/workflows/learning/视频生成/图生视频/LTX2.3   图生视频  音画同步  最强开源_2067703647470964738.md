---
key: 视频生成/图生视频/LTX2.3   图生视频  音画同步  最强开源_2067703647470964738.json
name: LTX2.3   图生视频  音画同步  最强开源_2067703647470964738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067703647470964738.json
hash: 25c8aba0ee922373
coverage: 0.95
learned_at: 2026-10-15 22:40:12
nodes: [LTXAVTextEncoderLoader, LTXVCropGuides, LTXVLatentUpsampler, LTXVAudioVAEDecode, VAEDecode, LTXVConcatAVLatent, CreateVideo, CLIPTextEncode, GetImageSize, EmptyImage, CheckpointLoaderSimple, CLIPTextEncode, LTXVConditioning, CFGGuider, RandomNoise, LatentUpscaleModelLoader, LTXVAudioVAELoader, LoraLoaderModelOnly, KSamplerSelect, LTXVPreprocess, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVImgToVideoInplace, LTXVSeparateAVLatent, KSampler, ResizeImagesByLongerEdge, PreviewAny, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVScheduler, SaveVideo, PrimitiveInt, EmptyLTXVLatentVideo, ResizeImageMaskNode, DualCLIPLoader, TextGenerateLTX2Prompt, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 2704862465239, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3   图生视频  音画同步  最强开源_2067703647470964738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067703647470964738.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LTXAVTextEncoderLoader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `EmptyImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `KSampler` ★核心
- `ResizeImagesByLongerEdge`
- `PreviewAny`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `SaveVideo`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `ResizeImageMaskNode`
- `DualCLIPLoader`
- `TextGenerateLTX2Prompt`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `2704862465239`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（38/40）

**有卡**：`LTXAVTextEncoderLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTXVConcatAVLatent`、`CreateVideo`、`CLIPTextEncode`、`GetImageSize`、`EmptyImage`、`CheckpointLoaderSimple`、`LTXVConditioning`、`CFGGuider`、`RandomNoise`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`KSamplerSelect`、`LTXVPreprocess`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`KSampler`、`ResizeImagesByLongerEdge`、`ImageScaleBy`、`LTXVEmptyLatentAudio`、`LTXVScheduler`、`SaveVideo`、`EmptyLTXVLatentVideo`、`ResizeImageMaskNode`、`DualCLIPLoader`、`TextGenerateLTX2Prompt`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
