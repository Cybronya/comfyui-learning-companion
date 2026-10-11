---
key: 视频生成/文生视频/LTX2.3【雄舟天文馆高清直出版】首尾帧+音色克隆_2046116731281739777.json
name: LTX2.3【雄舟天文馆高清直出版】首尾帧+音色克隆_2046116731281739777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3【雄舟天文馆高清直出版】首尾帧+音色克隆_2046116731281739777.json
hash: 541471219683fa4f
coverage: 0.681818
learned_at: 2026-10-11 19:49:38
nodes: [KSamplerSelect, Reroute, LTXVCropGuides, INTConstant, Reroute, CFGGuider, BasicScheduler, LTXVSeparateAVLatent, INTConstant, SetNode, EmptyLTXVLatentVideo, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVConcatAVLatent, SetNode, SimpleMath+, RandomNoise, GetNode, GetNode, LTXAVTextEncoderLoader, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXVImgToVideoInplace, KSampler, PrimitiveBoolean, SetLatentNoiseMask, SetNode, LTXVAudioVAEEncode, GetNode, SolidMask, LTX2SamplingPreviewOverride, GetNode, LTX2_NAG, CLIPTextEncode, INTConstant, SimpleMath+, easy showAnything, SimpleMath+, SaveAudio, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, AudioPad, INTConstant, AudioDuration_wan, CM_FloatToInt, PreviewImage, LTXVConcatAVLatent, Apply Whisper, ShowText|pysssss, PreviewAudio, LoraLoaderModelOnly, ImageResizeKJv2, LoadAudio, LTXVConditioning, CLIPTextEncode, GetImageSize, INTConstant, VAEDecodeTiled, GetNode, VHS_VideoCombine, llama_cpp_parameters, llama_cpp_model_loader, Qwen3TTSVoiceClone, GetImageSizeAndCount, LoadImage, ImageBatchMulti, GetNode, SetNode, llama_cpp_instruct_adv, Qwen3TTSModelLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, Text Concatenate, PrimitiveStringMultiline, InversionDemoLazySwitch, InversionDemoLazySwitch, Text Concatenate, SetNode, LoraLoaderModelOnly, CheckpointLoaderSimple, InversionDemoLazySwitch, GetNode, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveBoolean]
patterns: []
missing: [Apply Whisper, SimpleMath+, SimpleMath+, SimpleMath+, Text Concatenate, Text Concatenate]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 734989926258287, "steps": 4}
discoveries: [次要节点 `Apply Whisper` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/文生视频/LTX2.3【雄舟天文馆高清直出版】首尾帧+音色克隆_2046116731281739777.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3【雄舟天文馆高清直出版】首尾帧+音色克隆_2046116731281739777.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
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
- `PreviewAudio`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `LoadAudio`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `INTConstant`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Qwen3TTSVoiceClone`
- `GetImageSizeAndCount`
- `LoadImage`
- `ImageBatchMulti`
- `GetNode`
- `SetNode`
- `llama_cpp_instruct_adv`
- `Qwen3TTSModelLoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `PrimitiveStringMultiline`
- `InversionDemoLazySwitch`
- `InversionDemoLazySwitch`
- `Text Concatenate`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `InversionDemoLazySwitch`
- `GetNode`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `734989926258287`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **68%**（60/88）

**有卡**：`KSamplerSelect`、`LTXVCropGuides`、`INTConstant`、`CFGGuider`、`BasicScheduler`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`RandomNoise`、`LTXAVTextEncoderLoader`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXVImgToVideoInplace`、`KSampler`、`PrimitiveBoolean`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`SaveAudio`、`LTXVFirstLastFrameControl_TTP`、`AudioPad`、`AudioDuration_wan`、`CM_FloatToInt`、`PreviewAudio`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`LoadAudio`、`LTXVConditioning`、`GetImageSize`、`VAEDecodeTiled`、`VHS_VideoCombine`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`Qwen3TTSVoiceClone`、`GetImageSizeAndCount`、`LoadImage`、`ImageBatchMulti`、`llama_cpp_instruct_adv`、`Qwen3TTSModelLoader`、`InversionDemoLazySwitch`、`CheckpointLoaderSimple`

**缺卡**（6）：`Apply Whisper`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`Text Concatenate`、`Text Concatenate`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- 次要节点 `Apply Whisper` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
