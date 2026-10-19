---
key: 数字人/数字人/ltx2.3文本驱动｜数字人视频声音设计搭配_2101235056969863169.json
name: ltx2.3文本驱动｜数字人视频声音设计搭配_2101235056969863169
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ltx2.3文本驱动｜数字人视频声音设计搭配_2101235056969863169.json
hash: 942d65728eaa5e96
coverage: 0.622642
learned_at: 2026-10-19 00:19:15
nodes: [SimpleMath+, SimpleMath+, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, LatentUpscaleModelLoader, GetNode, UNETLoader, LTXVImgToVideoInplace, LTXVLatentUpsampler, SetNode, SetNode, SetNode, StringSubstring, GetNode, SetNode, InversionDemoLazySwitch, PrimitiveBoolean, SetNode, StringSubstring, SetNode, SetNode, GetNode, AudioInfo, SimpleMath+, GetNode, GetNode, GetNode, PrimitiveInt, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SolidMask, GetNode, LTXVAudioVAEEncode, LTXVPreprocess, LTXVImgToVideoInplace, ShowText, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, VHS_VideoCombine, SetNode, PathchSageAttentionKJ, SetNode, SetNode, SetNode, VAELoaderKJ, VAELoader, DualCLIPLoader, LoraLoaderModelOnly, llama_cpp_model_loader, llama_cpp_parameters, GetNode, GetNode, SetNode, llama_cpp_instruct_adv, GetNode, GetNode, PreviewAudio, Qwen3TTSModelLoader, SetNode, Qwen3TTSVoiceDesign, GetNode, Apply Whisper, SetNode, easy showAnything, GetNode, Qwen3TTSModelLoader, PreviewAudio, Qwen3TTSVoiceClone, AudioCrop, SetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, BasicScheduler, KSamplerSelect, easy cleanGpuUsed, GetNode, SetNode, SamplerCustom, LTXVSeparateAVLatent, GetNode, KSamplerSelect, BasicScheduler, SamplerCustom, SetNode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LoadImage, LoadAudio, Text, Text, Int, Float, Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/ltx2.3文本驱动｜数字人视频声音设计搭配_2101235056969863169.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ltx2.3文本驱动｜数字人视频声音设计搭配_2101235056969863169.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（159 个）：
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `LatentUpscaleModelLoader`
- `GetNode`
- `UNETLoader` ★核心
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `StringSubstring`
- `GetNode`
- `SetNode`
- `InversionDemoLazySwitch`
- `PrimitiveBoolean`
- `SetNode`
- `StringSubstring`
- `SetNode`
- `SetNode`
- `GetNode`
- `AudioInfo`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `SolidMask`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `ShowText`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoader`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `GetNode`
- `GetNode`
- `SetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `GetNode`
- `PreviewAudio`
- `Qwen3TTSModelLoader`
- `SetNode`
- `Qwen3TTSVoiceDesign`
- `GetNode`
- `Apply Whisper`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `Qwen3TTSModelLoader`
- `PreviewAudio`
- `Qwen3TTSVoiceClone`
- `AudioCrop`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustom` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `LoadAudio`
- `Text`
- `Text`
- `Int`
- `Float`
- `Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

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

覆盖率 **62%**（99/159）

**有卡**：`SimpleMath+`、`easy cleanGpuUsed`、`LatentUpscaleModelLoader`、`UNETLoader`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`StringSubstring`、`InversionDemoLazySwitch`、`PrimitiveBoolean`、`AudioInfo`、`LayerUtility: ImageScaleByAspectRatio V2`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVPreprocess`、`ShowText`、`VAEDecodeTiled`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`VAELoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`PreviewAudio`、`Qwen3TTSModelLoader`、`Qwen3TTSVoiceDesign`、`Apply Whisper`、`Qwen3TTSVoiceClone`、`AudioCrop`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`SamplerCustom`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`SetLatentNoiseMask`、`EmptyLTXVLatentVideo`、`LoadImage`、`LoadAudio`、`Text`、`Int`、`Float`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
