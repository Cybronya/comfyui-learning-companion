---
key: 视频生成/文生视频/视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513.json
name: 视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513.json
hash: e5a8954c2270b981
coverage: 0.902778
learned_at: 2026-10-15 22:49:00
nodes: [KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, RandomNoise, CM_FloatToInt, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, CFGGuider, CFGGuider, SamplerCustomAdvanced, LTXVAudioVAEDecode, EmptyLTXVLatentVideo, LayerUtility: PurgeVRAM V2, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, DisTorchPurgeVRAMV2, LTXVConditioning, LTX2_NAG, PrimitiveBoolean, CheckpointLoaderSimple, MathExpression|pysssss, JWFloatToString, easy positive, easy showAnything, easy positive, StringFunction|pysssss, LoadImage, PrimitiveInt, Int, LTXVImgToVideoConditionOnly, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveFloat, Int, VRAMReserver, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, Image_Resize_longsize, LTXVLatentUpsampler, LatentUpscaleModelLoader, LTXVSeparateAVLatent, PrimitiveFloat, Seed Everywhere, easy seed, ImageScaleBy, GetImageSizeAndCount, ImageResizeKJv2, CreateVideo, VAEDecodeTiled, GetImageSizeAndCount, RH_LLMAPI_NODE, StringFunction|pysssss, SetNode, MemoryCleaner, Text, PromptRelaySmartEncode, easy int, Text, easy showAnything, easy showAnything, easy anythingIndexSwitch, SaveVideo, easy saveText, RH_LLMAPI_NODE, RH_LLMAPI_NODE, easy saveText]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-LTX2.3-VBVR_2054821471918272513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `RandomNoise`
- `CM_FloatToInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `EmptyLTXVLatentVideo`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DisTorchPurgeVRAMV2`
- `LTXVConditioning`
- `LTX2_NAG`
- `PrimitiveBoolean`
- `CheckpointLoaderSimple` ★核心
- `MathExpression|pysssss`
- `JWFloatToString`
- `easy positive`
- `easy showAnything`
- `easy positive`
- `StringFunction|pysssss`
- `LoadImage`
- `PrimitiveInt`
- `Int`
- `LTXVImgToVideoConditionOnly`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveFloat`
- `Int`
- `VRAMReserver`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `Image_Resize_longsize`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `PrimitiveFloat`
- `Seed Everywhere`
- `easy seed`
- `ImageScaleBy`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `RH_LLMAPI_NODE`
- `StringFunction|pysssss`
- `SetNode`
- `MemoryCleaner`
- `Text`
- `PromptRelaySmartEncode`
- `easy int`
- `Text`
- `easy showAnything`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `SaveVideo`
- `easy saveText`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `easy saveText`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-ties-distilled-1.1.safetensors`

## 知识

覆盖率 **90%**（65/72）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`CM_FloatToInt`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`LTXVImgToVideoConditionOnly`、`LTXVConcatAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`DisTorchPurgeVRAMV2`、`LTXVConditioning`、`LTX2_NAG`、`PrimitiveBoolean`、`CheckpointLoaderSimple`、`MathExpression|pysssss`、`JWFloatToString`、`easy positive`、`StringFunction|pysssss`、`LoadImage`、`Int`、`LTXVSeparateAVLatent`、`VRAMReserver`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`Image_Resize_longsize`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`Seed Everywhere`、`easy seed`、`ImageScaleBy`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`CreateVideo`、`VAEDecodeTiled`、`RH_LLMAPI_NODE`、`MemoryCleaner`、`Text`、`PromptRelaySmartEncode`、`easy int`、`easy anythingIndexSwitch`、`SaveVideo`、`easy saveText`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
