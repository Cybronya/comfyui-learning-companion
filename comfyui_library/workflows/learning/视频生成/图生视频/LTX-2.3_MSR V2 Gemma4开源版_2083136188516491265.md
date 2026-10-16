---
key: 视频生成/图生视频/LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265.json
name: LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265.json
hash: 75a058c9303dd04a
coverage: 0.847059
learned_at: 2026-10-16 19:17:08
nodes: [VAELoader, CLIPLoader, LayerUtility: PurgeVRAM V2, easy indexAnything, easy indexAnything, PreviewImage, PreviewImage, RH_Captioner, RH_Captioner, Reroute, PreviewImage, easy forLoopEnd, Split String by Commas, TextEncodeQwenImageEditPlus, KSampler, FluxKontextMultiReferenceLatentMethod, ConditioningZeroOut, VAEDecode, easy batchAnything, ImageConcatenate_UTK, easy forLoopStart, easy showAnything, TextConcatenate_UTK, EmptyLatentImage, EnhancedLoadDiffusionModel, easy showAnything, RandomInt, ImageConcatenate_UTK, Text, Text, LTXAddVideoICLoRAGuide, LTXVEmptyLatentAudio, LTXVConditioning, PromptRelayEncode, LTXAVTextEncoderLoader, LTX2_NAG, LTXVConcatAVLatent, RandomNoise, CFGGuider, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, KSamplerSelect, LTXVSeparateAVLatent, CR Prompt Text, CLIPTextEncode, CR Prompt Text, LiconMSR, VAEDecode, LTXVAudioVAEDecode, TextConcatenate_UTK, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, FloatConstant, SimpleMath+, INTConstant, LTXVAudioVAELoader, CR Float To Integer, EmptyLTXVLatentVideo, PreviewImage, VHS_VideoCombine, PreviewImage, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Text, Int, easy indexAnything, easy showAnything, Text, PreviewImage, LoadImage, llama_cpp_parameters, StringReplace, easy showAnything, llama_cpp_model_loader, llama_cpp_instruct_adv, easy showAnything, LayerUtility: PurgeVRAM V2, INTConstant, LTXICLoRALoaderModelOnly, LowVRAMCheckpointLoader, LoraLoaderModelOnly, Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "denoise": 1, "height": 50, "sampler_name": "euler", "scheduler": "simple", "seed": 65233245443591, "steps": 8, "width": 241}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.3_MSR V2 Gemma4开源版_2083136188516491265.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: PurgeVRAM V2`
- `easy indexAnything`
- `easy indexAnything`
- `PreviewImage`
- `PreviewImage`
- `RH_Captioner`
- `RH_Captioner`
- `Reroute`
- `PreviewImage`
- `easy forLoopEnd`
- `Split String by Commas`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `easy batchAnything`
- `ImageConcatenate_UTK`
- `easy forLoopStart`
- `easy showAnything`
- `TextConcatenate_UTK`
- `EmptyLatentImage` ★核心
- `EnhancedLoadDiffusionModel`
- `easy showAnything`
- `RandomInt`
- `ImageConcatenate_UTK`
- `Text`
- `Text`
- `LTXAddVideoICLoRAGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `PromptRelayEncode`
- `LTXAVTextEncoderLoader`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `CFGGuider`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `LiconMSR`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `TextConcatenate_UTK`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FloatConstant`
- `SimpleMath+`
- `INTConstant`
- `LTXVAudioVAELoader`
- `CR Float To Integer`
- `EmptyLTXVLatentVideo`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`
- `Int`
- `easy indexAnything`
- `easy showAnything`
- `Text`
- `PreviewImage`
- `LoadImage`
- `llama_cpp_parameters`
- `StringReplace`
- `easy showAnything`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `INTConstant`
- `LTXICLoRALoaderModelOnly` ★核心
- `LowVRAMCheckpointLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `65233245443591`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `241`
- `height` = `50`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **85%**（72/85）

**有卡**：`VAELoader`、`CLIPLoader`、`LayerUtility: PurgeVRAM V2`、`easy indexAnything`、`RH_Captioner`、`easy forLoopEnd`、`Split String by Commas`、`TextEncodeQwenImageEditPlus`、`KSampler`、`FluxKontextMultiReferenceLatentMethod`、`ConditioningZeroOut`、`VAEDecode`、`easy batchAnything`、`ImageConcatenate_UTK`、`easy forLoopStart`、`TextConcatenate_UTK`、`EmptyLatentImage`、`EnhancedLoadDiffusionModel`、`RandomInt`、`Text`、`LTXAddVideoICLoRAGuide`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`PromptRelayEncode`、`LTXAVTextEncoderLoader`、`LTX2_NAG`、`LTXVConcatAVLatent`、`RandomNoise`、`CFGGuider`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`ManualSigmas`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`CR Prompt Text`、`CLIPTextEncode`、`LiconMSR`、`LTXVAudioVAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`FloatConstant`、`SimpleMath+`、`INTConstant`、`LTXVAudioVAELoader`、`CR Float To Integer`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`Int`、`LoadImage`、`llama_cpp_parameters`、`StringReplace`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`LTXICLoRALoaderModelOnly`、`LowVRAMCheckpointLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
