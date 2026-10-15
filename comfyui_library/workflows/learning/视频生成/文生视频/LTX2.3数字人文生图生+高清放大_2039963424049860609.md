---
key: 视频生成/文生视频/LTX2.3数字人文生图生+高清放大_2039963424049860609.json
name: LTX2.3数字人文生图生+高清放大_2039963424049860609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人文生图生+高清放大_2039963424049860609.json
hash: f2b29c7c1d1825e1
coverage: 0.789474
learned_at: 2026-10-15 22:45:09
nodes: [KSamplerSelect, Reroute, INTConstant, INTConstant, Reroute, CFGGuider, RandomNoise, INTConstant, INTConstant, SetNode, PreviewAudio, LTXVAudioVAEEncode, GetNode, SolidMask, SamplerCustomAdvanced, LTXVCropGuides, PrimitiveBoolean, LoadImage, CR Text, SetNode, CheckpointLoaderSimple, LTXVAudioVAELoader, SetNode, SetLatentNoiseMask, LTX2SamplingPreviewOverride, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, LTXVConditioning, PathchSageAttentionKJ, CLIPTextEncode, LTXVConcatAVLatent, GetNode, LTXVImgToVideoInplace, LTXVPreprocess, LTX2_NAG, LTXVSeparateAVLatent, LTXVLatentUpsampler, GetNode, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSampler, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, ImageSharpen, GetNode, SimpleMath+, SimpleMath+, easy showAnything, INTConstant, SimpleMath+, ResizeImageMaskNode, ResizeImagesByLongerEdge, VHS_VideoCombine, EmptyLTXVLatentVideo, SetNode, SeedVR2LoadVAEModel, VHS_VideoInfo, INTConstant, ImageScaleToTotalPixels, Note, Note, SeedVR2LoadDiTModel, VHS_VideoCombine, VHS_LoadVideo, Note, SeedVR2VideoUpscaler, MemoryCleaner, CM_FloatToInt, VHS_LoadAudioUpload, LTXAVTextEncoderLoader, easy cleanGpuUsed, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 868703346938759, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3数字人文生图生+高清放大_2039963424049860609.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3数字人文生图生+高清放大_2039963424049860609.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（76 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `RandomNoise`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `PreviewAudio`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `PrimitiveBoolean`
- `LoadImage`
- `CR Text`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `SetNode`
- `SetLatentNoiseMask`
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTX2_NAG`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ImageSharpen`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `easy showAnything`
- `INTConstant`
- `SimpleMath+`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SeedVR2LoadVAEModel`
- `VHS_VideoInfo`
- `INTConstant`
- `ImageScaleToTotalPixels`
- `Note`
- `Note`
- `SeedVR2LoadDiTModel`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Note`
- `SeedVR2VideoUpscaler`
- `MemoryCleaner`
- `CM_FloatToInt`
- `VHS_LoadAudioUpload`
- `LTXAVTextEncoderLoader`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `868703346938759`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **79%**（60/76）

**有卡**：`KSamplerSelect`、`INTConstant`、`CFGGuider`、`RandomNoise`、`PreviewAudio`、`LTXVAudioVAEEncode`、`SolidMask`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`PrimitiveBoolean`、`LoadImage`、`CR Text`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`BasicScheduler`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LTX2_NAG`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`KSampler`、`VAEDecodeTiled`、`ImageSharpen`、`SimpleMath+`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`SeedVR2LoadVAEModel`、`VHS_VideoInfo`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`VHS_LoadVideo`、`SeedVR2VideoUpscaler`、`MemoryCleaner`、`CM_FloatToInt`、`VHS_LoadAudioUpload`、`LTXAVTextEncoderLoader`、`easy cleanGpuUsed`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
