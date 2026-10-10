---
key: 视频生成/文生视频/LTX2.0音视频同步-文生视频_2009172721598472194.json
name: LTX2.0音视频同步-文生视频_2009172721598472194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0音视频同步-文生视频_2009172721598472194.json
hash: 44d1a8836e5214bd
coverage: 0.672131
learned_at: 2026-10-11 03:07:10
nodes: [RandomNoise, CFGGuider, LTXVScheduler, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, KSamplerSelect, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVCropGuides, LatentUpscaleModelLoader, Reroute, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVLatentUpsampler, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, Reroute, LTXVAudioVAEDecode, Note, PrimitiveStringMultiline, ToFloat, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXAVTextEncoderLoader, LTXVAudioVAELoader, ImpactSwitch, Note, ImpactSwitch, Note, PrimitiveStringMultiline, PrimitiveStringMultiline, RH_LLMAPI_NODE, IntConditions, easy ifElse, PrimitiveInt, PrimitiveInt, ShowText|pysssss, ImageScaleBy, GetImageSize, Int, MathExpression|pysssss, EmptyImage, VHS_VideoCombine, Reroute, VHS_VideoCombine, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CheckpointLoaderSimple, Reroute, Int, Note, VAEDecode, LayerUtility: PurgeVRAM V2]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, MathExpression|pysssss]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.0音视频同步-文生视频_2009172721598472194.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0音视频同步-文生视频_2009172721598472194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（61 个）：
- `RandomNoise`
- `CFGGuider`
- `LTXVScheduler`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `Reroute`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `Note`
- `PrimitiveStringMultiline`
- `ToFloat`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `ImpactSwitch`
- `Note`
- `ImpactSwitch`
- `Note`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `IntConditions`
- `easy ifElse`
- `PrimitiveInt`
- `PrimitiveInt`
- `ShowText|pysssss`
- `ImageScaleBy`
- `GetImageSize`
- `Int`
- `MathExpression|pysssss`
- `EmptyImage`
- `VHS_VideoCombine`
- `Reroute`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `Int`
- `Note`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **67%**（41/61）

**有卡**：`RandomNoise`、`CFGGuider`、`LTXVScheduler`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`KSamplerSelect`、`LoraLoaderModelOnly`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`ManualSigmas`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ToFloat`、`CLIPTextEncode`、`LTXVConditioning`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`RH_LLMAPI_NODE`、`IntConditions`、`ImageScaleBy`、`GetImageSize`、`Int`、`EmptyImage`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`VAEDecode`

**缺卡**（2）：`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
