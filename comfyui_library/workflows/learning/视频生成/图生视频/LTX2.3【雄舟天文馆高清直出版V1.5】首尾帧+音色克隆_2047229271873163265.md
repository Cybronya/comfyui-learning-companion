---
key: 视频生成/图生视频/LTX2.3【雄舟天文馆高清直出版V1.5】首尾帧+音色克隆_2047229271873163265.json
name: LTX2.3【雄舟天文馆高清直出版V1.5】首尾帧+音色克隆_2047229271873163265.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3【雄舟天文馆高清直出版V1.5】首尾帧+音色克隆_2047229271873163265.json
hash: 8445a0661cf2fd4f
coverage: 0.758242
learned_at: 2026-10-15 22:37:04
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, Reroute, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, INTConstant, SetNode, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, RandomNoise, GetNode, GetNode, LTXAVTextEncoderLoader, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXVImgToVideoInplace, KSampler, PrimitiveBoolean, SetLatentNoiseMask, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, LTX2SamplingPreviewOverride, GetNode, LTX2_NAG, CLIPTextEncode, INTConstant, SimpleMath+, easy showAnything, SimpleMath+, SaveAudio, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, AudioPad, INTConstant, AudioDuration_wan, CM_FloatToInt, PreviewImage, LTXVConcatAVLatent, Apply Whisper, ShowText|pysssss, LoraLoaderModelOnly, ImageResizeKJv2, GetImageSize, INTConstant, VAEDecodeTiled, GetNode, VHS_VideoCombine, llama_cpp_parameters, Qwen3TTSVoiceClone, GetImageSizeAndCount, LoadImage, ImageBatchMulti, GetNode, SetNode, llama_cpp_instruct_adv, Qwen3TTSModelLoader, PrimitiveStringMultiline, Text Concatenate, PrimitiveStringMultiline, InversionDemoLazySwitch, Text Concatenate, SetNode, LoraLoaderModelOnly, CheckpointLoaderSimple, InversionDemoLazySwitch, GetNode, LoadImage, PrimitiveStringMultiline, llama_cpp_model_loader, PrimitiveBoolean, Text Concatenate, InversionDemoLazySwitch, InversionDemoLazySwitch, PrimitiveBoolean, LTXVConditioning, CLIPTextEncode, PreviewAudio, LoadAudio, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 126722408111018, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3【雄舟天文馆高清直出版V1.5】首尾帧+音色克隆_2047229271873163265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047229271873163265.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVCropGuides`
- `INTConstant`
- `Reroute`
- `CFGGuider`
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `INTConstant`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `SimpleMath+`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXAVTextEncoderLoader`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `LTXVImgToVideoInplace`
- `KSampler` ★核心
- `PrimitiveBoolean`
- `SetLatentNoiseMask`
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SolidMask`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `SimpleMath+`
- `easy showAnything`
- `SimpleMath+`
- `SaveAudio`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVImgToVideoInplace`
- `AudioPad`
- `INTConstant`
- `AudioDuration_wan`
- `CM_FloatToInt`
- `PreviewImage`
- `LTXVConcatAVLatent`
- `Apply Whisper`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `GetImageSize`
- `INTConstant`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `llama_cpp_parameters`
- `Qwen3TTSVoiceClone`
- `GetImageSizeAndCount`
- `LoadImage`
- `ImageBatchMulti`
- `GetNode`
- `SetNode`
- `llama_cpp_instruct_adv`
- `Qwen3TTSModelLoader`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `PrimitiveStringMultiline`
- `InversionDemoLazySwitch`
- `Text Concatenate`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `InversionDemoLazySwitch`
- `GetNode`
- `LoadImage`
- `PrimitiveStringMultiline`
- `llama_cpp_model_loader`
- `PrimitiveBoolean`
- `Text Concatenate`
- `InversionDemoLazySwitch`
- `InversionDemoLazySwitch`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `PreviewAudio`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `126722408111018`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **76%**（69/91）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`SimpleMath+`、`RandomNoise`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`KSampler`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`SaveAudio`、`LTXVFirstLastFrameControl_TTP`、`AudioPad`、`AudioDuration_wan`、`CM_FloatToInt`、`Apply Whisper`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`GetImageSize`、`VAEDecodeTiled`、`VHS_VideoCombine`、`llama_cpp_parameters`、`Qwen3TTSVoiceClone`、`GetImageSizeAndCount`、`LoadImage`、`ImageBatchMulti`、`llama_cpp_instruct_adv`、`Qwen3TTSModelLoader`、`Text Concatenate`、`InversionDemoLazySwitch`、`CheckpointLoaderSimple`、`llama_cpp_model_loader`、`LTXVConditioning`、`PreviewAudio`、`LoadAudio`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
