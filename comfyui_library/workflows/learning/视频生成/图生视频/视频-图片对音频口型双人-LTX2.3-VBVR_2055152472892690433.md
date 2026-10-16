---
key: 视频生成/图生视频/视频-图片对音频口型双人-LTX2.3-VBVR_2055152472892690433.json
name: 视频-图片对音频口型双人-LTX2.3-VBVR_2055152472892690433.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055152472892690433.json
hash: 00a8647ff89d1953
coverage: 0.866667
learned_at: 2026-10-15 22:37:55
nodes: [LayerUtility: PurgeVRAM V2, PrimitiveBoolean, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, LatentUpscaleModelLoader, CM_FloatToInt, JWImageResizeByLongerSide, SolidMask, CFGGuider, CFGGuider, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXVImgToVideoConditionOnly, SolidMask, LTXVConcatAVLatent, SamplerCustomAdvanced, SimpleMath+, easy showAnything, GetLatentSizeAndCount, LTXVConcatAVLatent, PathchSageAttentionKJ, LTXVPreprocess, EmptyLTXVLatentVideo, PrimitiveInt, LTX2_NAG, LTXVAudioVAELoader, LTXAVTextEncoderLoader, SetLatentNoiseMask, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVSeparateAVLatent, SetLatentNoiseMask, JWFloatToString, easy int, Int, StringFunction|pysssss, SetNode, Seed Everywhere, Qwen3ASRLoader_DFT, Text, easy showAnything, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, easy showAnything, easy showAnything, LTXVConditioning, PromptRelaySmartEncode, ImageScaleBy, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, CreateVideo, VAEDecodeTiled, GetImageSizeAndCount, LoadAudio, MelBandRoFormerSampler, MelBandRoFormerModelLoader, TrimAudioDuration, Float, Float, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, MemoryCleaner, easy seed, CLIPTextEncode, Qwen3ASRTranscribe_DFT, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy showAnything, StringFunction|pysssss, easy anythingIndexSwitch, easy positive, Audio Duration (mtb), SimpleMath+, SetNode, GetNode, Qwen3_VQA_Plus, RH_LLMAPI_NODE, LoadImage, SaveVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/视频-图片对音频口型双人-LTX2.3-VBVR_2055152472892690433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055152472892690433.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `LayerUtility: PurgeVRAM V2`
- `PrimitiveBoolean`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `CM_FloatToInt`
- `JWImageResizeByLongerSide`
- `SolidMask`
- `CFGGuider`
- `CFGGuider`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoConditionOnly`
- `SolidMask`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SimpleMath+`
- `easy showAnything`
- `GetLatentSizeAndCount`
- `LTXVConcatAVLatent`
- `PathchSageAttentionKJ`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `PrimitiveInt`
- `LTX2_NAG`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `SetLatentNoiseMask`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `JWFloatToString`
- `easy int`
- `Int`
- `StringFunction|pysssss`
- `SetNode`
- `Seed Everywhere`
- `Qwen3ASRLoader_DFT`
- `Text`
- `easy showAnything`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `easy showAnything`
- `easy showAnything`
- `LTXVConditioning`
- `PromptRelaySmartEncode`
- `ImageScaleBy`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `LoadAudio`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `TrimAudioDuration`
- `Float`
- `Float`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `MemoryCleaner`
- `easy seed`
- `CLIPTextEncode` ★核心
- `Qwen3ASRTranscribe_DFT`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `StringFunction|pysssss`
- `easy anythingIndexSwitch`
- `easy positive`
- `Audio Duration (mtb)`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `Qwen3_VQA_Plus`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **87%**（78/90）

**有卡**：`LayerUtility: PurgeVRAM V2`、`PrimitiveBoolean`、`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LatentUpscaleModelLoader`、`CM_FloatToInt`、`JWImageResizeByLongerSide`、`SolidMask`、`CFGGuider`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`SimpleMath+`、`GetLatentSizeAndCount`、`PathchSageAttentionKJ`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTX2_NAG`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`SetLatentNoiseMask`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVAudioVAEEncode`、`JWFloatToString`、`easy int`、`Int`、`StringFunction|pysssss`、`Seed Everywhere`、`Qwen3ASRLoader_DFT`、`Text`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXVConditioning`、`PromptRelaySmartEncode`、`ImageScaleBy`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`CreateVideo`、`VAEDecodeTiled`、`LoadAudio`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`TrimAudioDuration`、`Float`、`MemoryCleaner`、`easy seed`、`CLIPTextEncode`、`Qwen3ASRTranscribe_DFT`、`RH_LLMAPI_NODE`、`easy anythingIndexSwitch`、`easy positive`、`Audio Duration (mtb)`、`Qwen3_VQA_Plus`、`LoadImage`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
