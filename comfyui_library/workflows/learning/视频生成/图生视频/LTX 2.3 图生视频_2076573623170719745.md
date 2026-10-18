---
key: 视频生成/图生视频/LTX 2.3 图生视频_2076573623170719745.json
name: LTX 2.3 图生视频_2076573623170719745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3 图生视频_2076573623170719745.json
hash: bf82513d9143ec6a
coverage: 0.945946
learned_at: 2026-10-15 22:41:31
nodes: [CLIPTextEncode, LTXAVTextEncoderLoader, LTXVAudioVAELoader, TextGenerateLTX2Prompt, DualCLIPLoader, EmptyImage, ImageScaleBy, GetImageSize, LTXVEmptyLatentAudio, CLIPTextEncode, LTXVConditioning, CFGGuider, LTXVScheduler, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, SaveVideo, GetImageSize, PrimitiveInt, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, LoadImage, CheckpointLoaderSimple, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVLatentUpsampler, KSampler, LTXVImgToVideoInplace, JjkText]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4000000000000001, "height": 24, "sampler_name": "euler", "scheduler": "simple", "seed": 848183743434997, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX 2.3 图生视频_2076573623170719745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2076573623170719745.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPTextEncode` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `TextGenerateLTX2Prompt`
- `DualCLIPLoader`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `GetImageSize`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `KSampler` ★核心
- `LTXVImgToVideoInplace`
- `JjkText`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `848183743434997`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`CLIPTextEncode`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`TextGenerateLTX2Prompt`、`DualCLIPLoader`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`CFGGuider`、`LTXVScheduler`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LoadImage`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`KSampler`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
