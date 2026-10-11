---
key: 视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json
name: 视频-文生视频扩写-LTX2.3_2037067149814013954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json
hash: 168d203ed86389bf
coverage: 0.604938
learned_at: 2026-10-11 03:48:40
nodes: [GetNode, SetNode, SetNode, GetNode, GetImageSizeAndCount, EmptyImage, SetNode, MathExpression|pysssss, GetImageSizeAndCount, SetNode, SetNode, SetNode, StringFunction|pysssss, JWFloatToString, easy positive, GetNode, easy showAnything, StringFunction|pysssss, RH_LLMAPI_NODE, StringFunction|pysssss, SetNode, easy saveText, easy positive, ImpactFloat, LTXVEmptyLatentAudio, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, LTXVPreprocess, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, CLIPTextEncode, PathchSageAttentionKJ, ModelPatchTorchSettings, EmptyLTXVLatentVideo, LTXVLatentUpsampler, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CheckpointLoaderSimple, RandomNoise, ManualSigmas, GetNode, GetNode, PrimitiveInt, CM_FloatToInt, PrimitiveFloat, VHS_VideoCombine, GetNode, easy anythingIndexSwitch, LTXVChunkFeedForward, RandomNoise, GetNode, GetNode, ImageScaleBy, GetImageSizeAndCount, INTConstant, INTConstant, INTConstant, MemoryCleaner, GetImageSizeAndCount, LTXVImgToVideoConditionOnly, PrimitiveBoolean, easy int, PrimitiveFloat, easy int, easy positive, easy int, easy seed]
patterns: []
missing: [MathExpression|pysssss, StringFunction|pysssss, StringFunction|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy int, easy int, easy positive, easy positive, easy positive, easy saveText, easy seed]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/视频-文生视频扩写-LTX2.3_2037067149814013954.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
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
- `easy positive`
- `ImpactFloat`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVPreprocess`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoConditionOnly`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `CM_FloatToInt`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `GetNode`
- `easy anythingIndexSwitch`
- `LTXVChunkFeedForward`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `GetImageSizeAndCount`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `MemoryCleaner`
- `GetImageSizeAndCount`
- `LTXVImgToVideoConditionOnly`
- `PrimitiveBoolean`
- `easy int`
- `PrimitiveFloat`
- `easy int`
- `easy positive`
- `easy int`
- `easy seed`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **60%**（49/81）

**有卡**：`GetImageSizeAndCount`、`EmptyImage`、`JWFloatToString`、`RH_LLMAPI_NODE`、`ImpactFloat`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`LTXVPreprocess`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVImgToVideoConditionOnly`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`RandomNoise`、`CM_FloatToInt`、`VHS_VideoCombine`、`LTXVChunkFeedForward`、`ImageScaleBy`、`INTConstant`、`MemoryCleaner`、`PrimitiveBoolean`

**缺卡**（13）：`MathExpression|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`StringFunction|pysssss`、`easy anythingIndexSwitch`、`easy int`、`easy int`、`easy int`、`easy positive`、`easy positive`、`easy positive`、`easy saveText`、`easy seed`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
