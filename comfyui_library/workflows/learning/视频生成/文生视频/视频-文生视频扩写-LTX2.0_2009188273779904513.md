---
key: 视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json
name: 视频-文生视频扩写-LTX2.0_2009188273779904513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json
hash: 08a0519cf198c56a
coverage: 0.709302
learned_at: 2026-10-15 22:49:00
nodes: [GetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, EmptyImage, SetNode, MathExpression|pysssss, GetImageSizeAndCount, SetNode, SetNode, SetNode, easy seed, StringFunction|pysssss, JWFloatToString, easy positive, GetNode, easy showAnything, StringFunction|pysssss, RH_LLMAPI_NODE, StringFunction|pysssss, SetNode, easy saveText, ManualSigmas, VAEDecode, CFGGuider, MarkdownNote, KSamplerSelect, KSamplerSelect, MarkdownNote, RandomNoise, LTXVConcatAVLatent, LoraLoaderModelOnly, Reroute, LTXVLatentUpsampler, GetImageSize, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ImageScaleBy, LTXVConditioning, CLIPTextEncode, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVConcatAVLatent, LTXVAudioVAEDecode, LTXVAudioVAELoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveInt, LTXAVTextEncoderLoader, RH_Translator, CFGGuider, LoraLoaderModelOnly, LTXVScheduler, RandomNoise, LoraLoaderModelOnly, CLIPTextEncode, EmptyImage, LTXVSeparateAVLatent, VAEDecode, LTXVAudioVAEDecode, LoraLoaderModelOnly, VAEDecodeTiled, MarkdownNote, GetNode, Reroute, GetNode, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, easy anythingIndexSwitch, PrimitiveInt, PrimitiveFloat, GetNode, GetNode, GetNode, CM_FloatToInt, LatentUpscaleModelLoader, LTXVCropGuides, easy positive, PrimitiveFloat, easy positive, easy int, ImpactFloat, easy int, easy int]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-LTX2.0_2009188273779904513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `EmptyImage`
- `SetNode`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy seed`
- `StringFunction|pysssss`
- `JWFloatToString`
- `easy positive`
- `GetNode`
- `easy showAnything`
- `StringFunction|pysssss`
- `RH_LLMAPI_NODE`
- `StringFunction|pysssss`
- `SetNode`
- `easy saveText`
- `ManualSigmas`
- `VAEDecode` ★核心
- `CFGGuider`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ImageScaleBy`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVAudioVAELoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `RH_Translator`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyImage`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `MarkdownNote`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `PrimitiveInt`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `easy positive`
- `PrimitiveFloat`
- `easy positive`
- `easy int`
- `ImpactFloat`
- `easy int`
- `easy int`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **71%**（61/86）

**有卡**：`GetImageSizeAndCount`、`EmptyImage`、`MathExpression|pysssss`、`easy seed`、`StringFunction|pysssss`、`JWFloatToString`、`easy positive`、`RH_LLMAPI_NODE`、`easy saveText`、`ManualSigmas`、`VAEDecode`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ImageScaleBy`、`LTXVConditioning`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVAudioVAEDecode`、`LTXVAudioVAELoader`、`LTXVSeparateAVLatent`、`LTXAVTextEncoderLoader`、`RH_Translator`、`LTXVScheduler`、`VAEDecodeTiled`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`CM_FloatToInt`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`easy int`、`ImpactFloat`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
