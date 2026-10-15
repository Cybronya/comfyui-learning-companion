---
key: 视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json
name: LTX2.3  图生视频  超强开源视频模型_2044752658199744513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json
hash: 6c796d1f1d4d5afb
coverage: 0.926829
learned_at: 2026-10-15 22:44:55
nodes: [LTXVSeparateAVLatent, VAEDecode, CreateVideo, LTXVAudioVAEDecode, SaveVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, CFGGuider, LTXVScheduler, KSampler, LatentUpscaleModelLoader, PreviewAny, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVConcatAVLatent, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, ImageScaleBy, LoadImage, PrimitiveInt, PreviewImage, LTXVPreprocess, ResizeImagesByLongerEdge, ResizeImageMaskNode, EmptyLTXVLatentVideo, GetImageSize, EmptyImage, GetImageSize, LTXVAudioVAELoader, LTXAVTextEncoderLoader, DualCLIPLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, TextGenerateLTX2Prompt]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 948093177563792, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3  图生视频  超强开源视频模型_2044752658199744513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVScheduler`
- `KSampler` ★核心
- `LatentUpscaleModelLoader`
- `PreviewAny`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `LoadImage`
- `PrimitiveInt`
- `PreviewImage`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `EmptyImage`
- `GetImageSize`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `TextGenerateLTX2Prompt`

## 关键参数

- `seed` = `948093177563792`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **93%**（38/41）

**有卡**：`LTXVSeparateAVLatent`、`VAEDecode`、`CreateVideo`、`LTXVAudioVAEDecode`、`SaveVideo`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`LTXVScheduler`、`KSampler`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CLIPTextEncode`、`ImageScaleBy`、`LoadImage`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`GetImageSize`、`EmptyImage`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
