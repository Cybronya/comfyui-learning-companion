---
key: 视频生成/图生视频/fl2va首尾帧4K高清V2｜Minimaxh3-ltx2.5高效率图生视频_2089491006780698626.json
name: fl2va首尾帧4K高清V2｜Minimaxh3-ltx2.5高效率图生视频_2089491006780698626
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/fl2va首尾帧4K高清V2｜Minimaxh3-ltx2.5高效率图生视频_2089491006780698626.json
hash: 5cb925565a32a91d
coverage: 0.839416
learned_at: 2026-10-16 22:02:18
nodes: [RandomNoise, KSamplerSelect, CFGGuider, KSamplerSelect, MiniMaxH3MemoryEfficientSageAttentionPatch, easy cleanGpuUsed, SamplerCustomAdvanced, KSamplerSelect, CLIPLoader, VAELoader, easy cleanGpuUsed, VAEEncode, SetNode, VAEDecodeAudio, VAEDecodeAudio, VAELoader, VAELoader, LoraLoaderModelOnly, CLIPLoader, MiniMaxH3ReferenceToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, VAELoader, UNETLoader, RandomNoise, BasicGuider, SamplerCustomAdvanced, easy showAnything, BasicGuider, VAEEncodeAudio, PT_H3ConcatAVLatent, RandomNoise, GetImageSize, ImageScaleBy, PreviewImage, easy cleanGpuUsed, CLIPTextEncode, GetNode, SetNode, GetNode, LTXVConditioning, LatentUpscaleModelLoader, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVCropGuides, Float, PrimitiveFloat, BasicScheduler, GetNode, GetNode, SetNode, LTXVLatentUpsampler, GetNode, VAELoader, SetNode, easy showAnything, VAEDecode, LTXVAddGuideMulti, ComfyMathExpression, LTXVEmptyLatentAudio, GetNode, VAEDecode, LoraLoaderModelOnly, SamplerCustomAdvanced, CLIPTextEncode, ImageResize+, UNETLoader, BasicScheduler, VHS_VideoCombine, VHS_VideoCombine, SetNode, Float, GetNode, VHS_VideoCombine, GetNode, CR Text, LoadImage, VAEEncode, ImageResize+, MiniMaxH3ImageToVideo, GetImageSize, ComfyMathExpression, ComfyMathExpression, ImageResizeKJv2, ImageResize+, LTXVPreprocess, LTXVPreprocess, LoadImage, ComfyMathExpression, ResolutionSelector, ImageResize+, ComfyMathExpression, UNETLoader, CLIPLoader, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, LTX2MemoryEfficientSageAttentionPatch, LTX2_NAG, ManualSigmas, JoinStrings, SomethingToString, SetNode, CR Prompt Text, TextInput_, Comfly_LLm_API, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/fl2va首尾帧4K高清V2｜Minimaxh3-ltx2.5高效率图生视频_2089491006780698626.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/fl2va首尾帧4K高清V2｜Minimaxh3-ltx2.5高效率图生视频_2089491006780698626.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（137 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `SetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `easy showAnything`
- `BasicGuider`
- `VAEEncodeAudio` ★核心
- `PT_H3ConcatAVLatent`
- `RandomNoise`
- `GetImageSize`
- `ImageScaleBy`
- `PreviewImage`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `Float`
- `PrimitiveFloat`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `VAELoader`
- `SetNode`
- `easy showAnything`
- `VAEDecode` ★核心
- `LTXVAddGuideMulti`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `UNETLoader` ★核心
- `BasicScheduler`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `Float`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `CR Text`
- `LoadImage`
- `VAEEncode` ★核心
- `ImageResize+`
- `MiniMaxH3ImageToVideo`
- `GetImageSize`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `ImageResize+`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LoadImage`
- `ComfyMathExpression`
- `ResolutionSelector`
- `ImageResize+`
- `ComfyMathExpression`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTX2_NAG`
- `ManualSigmas`
- `JoinStrings`
- `SomethingToString`
- `SetNode`
- `CR Prompt Text`
- `TextInput_`
- `Comfly_LLm_API`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **84%**（115/137）

**有卡**：`RandomNoise`、`KSamplerSelect`、`CFGGuider`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`VAEDecodeAudio`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`、`BasicGuider`、`VAEEncodeAudio`、`PT_H3ConcatAVLatent`、`GetImageSize`、`ImageScaleBy`、`CLIPTextEncode`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXVCropGuides`、`Float`、`BasicScheduler`、`LTXVLatentUpsampler`、`VAEDecode`、`LTXVAddGuideMulti`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`ImageResize+`、`VHS_VideoCombine`、`CR Text`、`LoadImage`、`MiniMaxH3ImageToVideo`、`ImageResizeKJv2`、`LTXVPreprocess`、`ResolutionSelector`、`LTX2MemoryEfficientSageAttentionPatch`、`LTX2_NAG`、`ManualSigmas`、`JoinStrings`、`SomethingToString`、`CR Prompt Text`、`TextInput_`、`Comfly_LLm_API`、`KSampler`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
