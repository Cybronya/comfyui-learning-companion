---
key: 视频生成/图生视频/LTX2.3图生视频mv文生视频长视频制作文本生成视频mv制作口播视频生成两个模式切换_2037757708098609154.json
name: LTX2.3图生视频mv文生视频长视频制作文本生成视频mv制作口播视频生成两个模式切换_2037757708098609154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2037757708098609154.json
hash: 9731626308adc4c2
coverage: 0.819672
learned_at: 2026-10-15 22:35:58
nodes: [KSamplerSelect, Reroute, CLIPTextEncode, LTXVCropGuides, INTConstant, INTConstant, Reroute, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, easy cleanGpuUsed, VAEDecodeTiled, INTConstant, SetNode, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, SimpleMath+, LTXVConditioning, RandomNoise, GetNode, GetNode, LTXVPreprocess, ResizeImageMaskNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoaderModelOnly, ImageSharpen, GetNode, PathchSageAttentionKJ, LTXVAudioVAELoader, ResizeImagesByLongerEdge, LTXVImgToVideoInplace, KSampler, PrimitiveBoolean, SetLatentNoiseMask, CM_FloatToInt, SimpleMath+, easy showAnything, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, CLIPTextEncode, VHS_VideoCombine, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LTXVImgToVideoInplace, GetNode, LTX2_NAG, LoadImage, INTConstant, INTConstant, VHS_LoadAudioUpload, PreviewAudio]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 572195242730155, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3图生视频mv文生视频长视频制作文本生成视频mv制作口播视频生成两个模式切换_2037757708098609154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2037757708098609154.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（61 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `VAEDecodeTiled` ★核心
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVConditioning`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageSharpen`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `ResizeImagesByLongerEdge`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `CM_FloatToInt`
- `SimpleMath+`
- `easy showAnything`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTX2_NAG`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `VHS_LoadAudioUpload`
- `PreviewAudio`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `572195242730155`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **82%**（50/61）

**有卡**：`KSamplerSelect`、`CLIPTextEncode`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`easy cleanGpuUsed`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`SimpleMath+`、`LTXVConditioning`、`RandomNoise`、`LTXVPreprocess`、`ResizeImageMaskNode`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`ImageSharpen`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`ResizeImagesByLongerEdge`、`LTXVImgToVideoInplace`、`KSampler`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`CM_FloatToInt`、`LTXVAudioVAEEncode`、`SolidMask`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`LoadImage`、`VHS_LoadAudioUpload`、`PreviewAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
