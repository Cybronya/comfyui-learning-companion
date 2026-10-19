---
key: 数字人/数字人/ltx2.3文本驱动-声音设计_2100950016872505346.json
name: ltx2.3文本驱动-声音设计_2100950016872505346
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/ltx2.3文本驱动-声音设计_2100950016872505346.json
hash: 77960856e4bafdde
coverage: 0.487805
learned_at: 2026-10-19 00:19:15
nodes: [SimpleMath+, SimpleMath+, GetNode, GetNode, Note, GetNode, Note, easy cleanGpuUsed, GetNode, LatentUpscaleModelLoader, GetNode, UNETLoader, LTXVImgToVideoInplace, LTXVLatentUpsampler, SetNode, SetNode, SetNode, StringSubstring, GetNode, SetNode, InversionDemoLazySwitch, PrimitiveBoolean, SetNode, StringSubstring, SetNode, SetNode, GetNode, AudioInfo, SimpleMath+, GetNode, GetNode, GetNode, PrimitiveInt, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SolidMask, GetNode, LTXVAudioVAEEncode, LTXVPreprocess, LTXVImgToVideoInplace, ShowText, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, VHS_VideoCombine, SetNode, PathchSageAttentionKJ, SetNode, SetNode, SetNode, VAELoaderKJ, VAELoader, DualCLIPLoader, LoraLoaderModelOnly, llama_cpp_model_loader, llama_cpp_parameters, GetNode, GetNode, SetNode, llama_cpp_instruct_adv, GetNode, GetNode, PreviewAudio, Qwen3TTSModelLoader, SetNode, Qwen3TTSVoiceDesign, GetNode, Apply Whisper, SetNode, easy showAnything, GetNode, Qwen3TTSModelLoader, PreviewAudio, Qwen3TTSVoiceClone, AudioCrop, SetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, BasicScheduler, KSamplerSelect, easy cleanGpuUsed, GetNode, SetNode, SamplerCustom, LTXVSeparateAVLatent, GetNode, KSamplerSelect, BasicScheduler, Note, SamplerCustom, SetNode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVConcatAVLatent, EmptyLTXVLatentVideo, Note, Note, Note, LoadImage, LoadAudio, Text, Note, Text, Int, Float, Text]
patterns: []
missing: []
---

# 数字人/数字人/ltx2.3文本驱动-声音设计_2100950016872505346.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/ltx2.3文本驱动-声音设计_2100950016872505346.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（123 个）：
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `Note`
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
- `Note`
- `SamplerCustom` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadAudio`
- `Text`
- `Note`
- `Text`
- `Int`
- `Float`
- `Text`

## 知识

覆盖率 **49%**（60/123）

**有卡**：`SimpleMath+`、`easy cleanGpuUsed`、`LatentUpscaleModelLoader`、`UNETLoader`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`StringSubstring`、`InversionDemoLazySwitch`、`PrimitiveBoolean`、`AudioInfo`、`LayerUtility: ImageScaleByAspectRatio V2`、`SolidMask`、`LTXVAudioVAEEncode`、`LTXVPreprocess`、`ShowText`、`VAEDecodeTiled`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`VAELoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`PreviewAudio`、`Qwen3TTSModelLoader`、`Qwen3TTSVoiceDesign`、`Apply Whisper`、`Qwen3TTSVoiceClone`、`AudioCrop`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`SamplerCustom`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`SetLatentNoiseMask`、`EmptyLTXVLatentVideo`、`LoadImage`、`LoadAudio`、`Text`、`Int`、`Float`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVLatentUpsampler
