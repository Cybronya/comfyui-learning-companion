---
key: 图片生成/图生图/adigital_combination.json_2072223926792581121.json
name: adigital_combination.json_2072223926792581121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/adigital_combination.json_2072223926792581121.json
hash: 955db1833c27f35f
coverage: 0.814433
learned_at: 2026-10-23 11:33:31
nodes: [MMAudioFeatureUtilsLoader, CLIPTextEncode, CheckpointLoaderSimple, CLIPLoader, EmptyLatentAudio, VAEDecodeAudio, KSampler, PreviewAudio, RH_Translator, AudioCombine, CLIPTextEncode, Int, Int, Evaluate Integers, MMAudioSampler, MathExpression|pysssss, easy showAnything, easy showAnything, JWInteger, RH_Translator, MMAudioModelLoader, RH_Captioner, easy showAnything, SaveAudio, easy showAnything, PreviewAudio, RH_Captioner, easy showAnything, RandomNoise, CFGGuider, PrimitiveBoolean, PrimitiveInt, easy showAnything, SolidMask, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoader, UNETLoader, SoundFlow_GetLength, LoraLoaderModelOnly, KSamplerSelect, LoraLoaderModelOnly, PrimitiveInt, BasicScheduler, ModelSamplingSD3, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ComfyMathExpression, LTXVImgToVideoInplace, PrimitiveFloat, PrimitiveFloat, LTXVConditioning, LoraLoaderModelOnly, LTX2_NAG, SetNode, LTXVConcatAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, TrimAudioDuration, LTXVTiledVAEDecode, ComfyMathExpression, EmptyLTXVLatentVideo, easy showAnything, RH_Translator, easy showAnything, WooshLoadFlow, SimpleMath+, SamplerCustomAdvanced, RunningHub Deepcleaner, LayerUtility: TextJoin, JoinStrings, PrimitiveStringMultiline, AudioMerge, GoogleTranslateTextNode, CLIPTextEncode, CLIPTextEncode, ComfyMathExpression, WooshTextEncode, ShowAnything|Mie, easy showAnything, ImageScaleToTotalPixels, GetImageSize, SimpleMath+, WooshSample, VHS_VideoCombine, PrimitiveInt, AudioAdjustVolume, AudioAdjustVolume, JjkText, CR Prompt Text, JjkText, LoadImage, LoadAudio, ImageResizeKJv2, Qwen3_VQA]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 7, "checkpoint": "stable-audio-open-1.0.safetensors", "denoise": 1, "height": 1, "sampler_name": "dpmpp_3m_sde_gpu", "scheduler": "exponential", "seed": 100192689457270, "steps": 60, "width": 40}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/图生图/adigital_combination.json_2072223926792581121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/adigital_combination.json_2072223926792581121.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `MMAudioFeatureUtilsLoader`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `EmptyLatentAudio` ★核心
- `VAEDecodeAudio` ★核心
- `KSampler` ★核心
- `PreviewAudio`
- `RH_Translator`
- `AudioCombine`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `Evaluate Integers`
- `MMAudioSampler` ★核心
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `JWInteger`
- `RH_Translator`
- `MMAudioModelLoader`
- `RH_Captioner`
- `easy showAnything`
- `SaveAudio`
- `easy showAnything`
- `PreviewAudio`
- `RH_Captioner`
- `easy showAnything`
- `RandomNoise`
- `CFGGuider`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `easy showAnything`
- `SolidMask`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `UNETLoader` ★核心
- `SoundFlow_GetLength`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `BasicScheduler`
- `ModelSamplingSD3`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVConditioning`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `SetNode`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `TrimAudioDuration`
- `LTXVTiledVAEDecode` ★核心
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `easy showAnything`
- `RH_Translator`
- `easy showAnything`
- `WooshLoadFlow`
- `SimpleMath+`
- `SamplerCustomAdvanced` ★核心
- `RunningHub Deepcleaner`
- `LayerUtility: TextJoin`
- `JoinStrings`
- `PrimitiveStringMultiline`
- `AudioMerge`
- `GoogleTranslateTextNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `WooshTextEncode`
- `ShowAnything|Mie`
- `easy showAnything`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `SimpleMath+`
- `WooshSample`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `AudioAdjustVolume`
- `AudioAdjustVolume`
- `JjkText`
- `CR Prompt Text`
- `JjkText`
- `LoadImage`
- `LoadAudio`
- `ImageResizeKJv2`
- `Qwen3_VQA`

## 关键参数

- `checkpoint` = `stable-audio-open-1.0.safetensors`
- `width` = `40`
- `height` = `1`
- `seed` = `100192689457270`
- `steps` = `60`
- `cfg` = `7`
- `sampler_name` = `dpmpp_3m_sde_gpu`
- `scheduler` = `exponential`
- `denoise` = `1`

## 知识

覆盖率 **81%**（79/97）

**有卡**：`MMAudioFeatureUtilsLoader`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`CLIPLoader`、`EmptyLatentAudio`、`VAEDecodeAudio`、`KSampler`、`PreviewAudio`、`RH_Translator`、`AudioCombine`、`Int`、`Evaluate Integers`、`MMAudioSampler`、`MathExpression|pysssss`、`JWInteger`、`MMAudioModelLoader`、`RH_Captioner`、`SaveAudio`、`RandomNoise`、`CFGGuider`、`PrimitiveBoolean`、`SolidMask`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`VAELoader`、`UNETLoader`、`SoundFlow_GetLength`、`LoraLoaderModelOnly`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingSD3`、`LTXVSeparateAVLatent`、`LayerUtility: PurgeVRAM V2`、`ComfyMathExpression`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTX2_NAG`、`LTXVConcatAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`TrimAudioDuration`、`LTXVTiledVAEDecode`、`EmptyLTXVLatentVideo`、`WooshLoadFlow`、`SimpleMath+`、`SamplerCustomAdvanced`、`RunningHub Deepcleaner`、`LayerUtility: TextJoin`、`JoinStrings`、`AudioMerge`、`GoogleTranslateTextNode`、`WooshTextEncode`、`ShowAnything|Mie`、`ImageScaleToTotalPixels`、`GetImageSize`、`WooshSample`、`VHS_VideoCombine`、`AudioAdjustVolume`、`CR Prompt Text`、`LoadImage`、`LoadAudio`、`ImageResizeKJv2`、`Qwen3_VQA`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
