---
key: 视频生成/图生视频/LTX2.5首尾帧生视频_2095746297683857409.json
name: LTX2.5首尾帧生视频_2095746297683857409
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频_2095746297683857409.json
hash: 4ff77f65def98d01
coverage: 0.865979
learned_at: 2026-10-17 01:09:31
nodes: [LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVCropGuides, SamplerCustomAdvanced, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, GetImageSize, LTXVPreprocess, LTXVPreprocess, UNETLoader, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, PrimitiveInt, LTXVAudioVAEDecode, ResizeImageMaskNode, ResizeImageMaskNode, VAEDecodeTiled, CLIPLoader, PrimitiveBoolean, PrimitiveInt, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, PrimitiveInt, PrimitiveInt, LoadImage, EmptyLTXVLatentVideo, LoadImage, PrimitiveStringMultiline, TextGenerateLTX2Prompt, LTXVEmptyLatentAudio, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, Int, GetVideoComponents, ComfyNumberConvert, ResizeImageMaskNode, VAELoader, UNETLoader, SeedVR2Preprocess, VAEEncodeTiled, SeedVR2TemporalChunk, SeedVR2Conditioning, ComfySwitchNode, KSampler, SeedVR2TemporalMerge, SeedVR2PostProcessing, ComfySwitchNode, SaveVideo, CreateVideo, VAEDecodeTiled, InspyrenetRembg, PreviewImage, JoinImageWithAlpha, UpscaleModelLoader, ImageUpscaleWithModel, PreviewAny, ComfySwitchNode, VHS_VideoCombine, FlashVSRNode, ComfyMathExpression, VHS_VideoCombine, ComfySwitchNode, VideoUtilitiesGetVHSFilePath, Video Slice]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 512738925392953, "steps": 1, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.5首尾帧生视频_2095746297683857409.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧生视频_2095746297683857409.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `PrimitiveInt`
- `LTXVAudioVAEDecode` ★核心
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `VAEDecodeTiled` ★核心
- `CLIPLoader`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `LTXVEmptyLatentAudio` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `Int`
- `GetVideoComponents`
- `ComfyNumberConvert`
- `ResizeImageMaskNode`
- `VAELoader`
- `UNETLoader` ★核心
- `SeedVR2Preprocess`
- `VAEEncodeTiled` ★核心
- `SeedVR2TemporalChunk`
- `SeedVR2Conditioning`
- `ComfySwitchNode`
- `KSampler` ★核心
- `SeedVR2TemporalMerge`
- `SeedVR2PostProcessing`
- `ComfySwitchNode`
- `SaveVideo`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `InspyrenetRembg`
- `PreviewImage`
- `JoinImageWithAlpha`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `PreviewAny`
- `ComfySwitchNode`
- `VHS_VideoCombine`
- `FlashVSRNode`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `ComfySwitchNode`
- `VideoUtilitiesGetVHSFilePath`
- `Video Slice`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `512738925392953`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（84/97）

**有卡**：`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAddGuide`、`ManualSigmas`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`GetImageSize`、`LTXVPreprocess`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`ResizeImageMaskNode`、`VAEDecodeTiled`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`LoadImage`、`EmptyLTXVLatentVideo`、`TextGenerateLTX2Prompt`、`LTXVEmptyLatentAudio`、`Int`、`GetVideoComponents`、`ComfyNumberConvert`、`SeedVR2Preprocess`、`VAEEncodeTiled`、`SeedVR2TemporalChunk`、`SeedVR2Conditioning`、`SeedVR2TemporalMerge`、`SeedVR2PostProcessing`、`SaveVideo`、`CreateVideo`、`InspyrenetRembg`、`JoinImageWithAlpha`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VHS_VideoCombine`、`FlashVSRNode`、`VideoUtilitiesGetVHSFilePath`、`Video Slice`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
