---
key: 视频生成/图生视频/音画同步+图生视频 LTX2.3（随机动作提示词）_2073938374595010562.json
name: 音画同步+图生视频 LTX2.3（随机动作提示词）_2073938374595010562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2073938374595010562.json
hash: de71cfcd2afba9b0
coverage: 0.826923
learned_at: 2026-10-15 22:41:10
nodes: [LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVCropGuides, GetImageSize, EmptyImage, ImageScaleBy, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, CheckpointLoaderSimple, LatentUpscaleModelLoader, RandomNoise, DF_Int_to_Float, GetNode, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, PrimitiveInt, SimpleMath+, LTXVScheduler, SetNode, LTXVEmptyLatentAudio, SetNode, KSampler, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVPreprocess, GetImageSize, GetNode, GetNode, ImageResizeKJv2, DF_Int_to_Float, Int, SamplerCustomAdvanced, LTXVAudioVAELoader, DualCLIPLoader, LTXAVTextEncoderLoader, VHS_VideoCombine, ResizeImagesByLongerEdge, TextGenerateLTX2Prompt, PreviewAny, LoraLoaderModelOnly, Text, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 1123381419965192, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/音画同步+图生视频 LTX2.3（随机动作提示词）_2073938374595010562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2073938374595010562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（52 个）：
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `GetImageSize`
- `EmptyImage`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `DF_Int_to_Float`
- `GetNode`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `SimpleMath+`
- `LTXVScheduler`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVPreprocess`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `DF_Int_to_Float`
- `Int`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAELoader`
- `DualCLIPLoader`
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `ResizeImagesByLongerEdge`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `LoraLoaderModelOnly` ★核心
- `Text`
- `LoadImage`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `1123381419965192`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`GetImageSize`、`EmptyImage`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`CFGGuider`、`KSamplerSelect`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`RandomNoise`、`DF_Int_to_Float`、`ResizeImageMaskNode`、`VAEDecode`、`LTXVAudioVAEDecode`、`SimpleMath+`、`LTXVScheduler`、`LTXVEmptyLatentAudio`、`KSampler`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVPreprocess`、`ImageResizeKJv2`、`Int`、`SamplerCustomAdvanced`、`LTXVAudioVAELoader`、`DualCLIPLoader`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`ResizeImagesByLongerEdge`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
