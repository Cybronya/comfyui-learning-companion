---
key: 视频生成/图生视频/LTX2.3图生视频竖屏短剧分镜11秒_2030844044808560641.json
name: LTX2.3图生视频竖屏短剧分镜11秒_2030844044808560641.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030844044808560641.json
hash: 2cc093f502c4a423
coverage: 0.913043
learned_at: 2026-10-15 22:35:28
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LatentUpscaleModelLoader, EmptyImage, CLIPTextEncode, LTXVImgToVideoInplace, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, PreviewAny, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, CreateVideo, LTXVConditioning, DualCLIPLoader, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ImageScaleBy, GetImageSize, SaveVideo, CLIPTextEncode, TextGenerateLTX2Prompt, PrimitiveInt, MathExpression|pysssss, JWInteger, RandomNoise, KSampler, LoraLoaderModelOnly, LTX2_NAG, LTXVCropGuides, GetImageSize, JjkText, PreviewImage, ResizeImagesByLongerEdge, LTXVPreprocess, ImageResizeKJv2, String, Load Image From Url (mtb)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 779026745479043, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频竖屏短剧分镜11秒_2030844044808560641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030844044808560641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LatentUpscaleModelLoader`
- `EmptyImage`
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `PreviewAny`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `CreateVideo`
- `LTXVConditioning`
- `DualCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ImageScaleBy`
- `GetImageSize`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `JWInteger`
- `RandomNoise`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LTXVCropGuides`
- `GetImageSize`
- `JjkText`
- `PreviewImage`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `String`
- `Load Image From Url (mtb)`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `779026745479043`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **91%**（42/46）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CFGGuider`、`LatentUpscaleModelLoader`、`EmptyImage`、`CLIPTextEncode`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`CreateVideo`、`LTXVConditioning`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`ImageScaleBy`、`GetImageSize`、`SaveVideo`、`TextGenerateLTX2Prompt`、`MathExpression|pysssss`、`JWInteger`、`RandomNoise`、`KSampler`、`LoraLoaderModelOnly`、`LTX2_NAG`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ImageResizeKJv2`、`String`、`Load Image From Url (mtb)`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
