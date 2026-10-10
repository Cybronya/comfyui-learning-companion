---
key: 视频生成/文生视频/LTX2.0文生视频_2008728323093962754.json
name: LTX2.0文生视频_2008728323093962754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频_2008728323093962754.json
hash: 41e8a16122e18ddc
coverage: 0.573333
learned_at: 2026-10-11 03:07:10
nodes: [CFGGuider, LTXVSeparateAVLatent, ImageScaleBy, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXVSeparateAVLatent, CFGGuider, SamplerCustomAdvanced, easy cleanGpuUsed, KSamplerSelect, KSamplerSelect, CR Text, CR Text, ImpactSwitch, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, LTXVConditioning, RandomNoise, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, ManualSigmas, LTXVConcatAVLatent, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, LTXVAudioVAELoader, ManualSigmas, easy cleanGpuUsed, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, Int, Int, CR Text Concatenate, RandomNoise, LTXVLatentUpsampler, SaveAudio, GetImageSize, CR Text Concatenate, ttN concat, easy convertAnything, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, RH_LLMAPI_NODE, LTXVChunkFeedForward, ImpactSwitch, VRAMReserver, CR String To Combo, LoraLoaderModelOnly, LoraLoaderModelOnly, Display Any (rgthree), CR Text Concatenate, CR Text, CR Text Concatenate, CR Text, CR Text, Int, ManualSigmas]
patterns: []
missing: [CR String To Combo, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, Display Any (rgthree), easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy convertAnything, ttN concat]
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-distilled-fp8.safetensors", "height": 25, "width": 121}
discoveries: [次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.0文生视频_2008728323093962754.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.0文生视频_2008728323093962754.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `ImageScaleBy`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `PIP_IntegerCalculator`
- `Int`
- `PIP_IntegerCalculator`
- `EmptyImage`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `RandomNoise`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `ManualSigmas`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Int`
- `Int`
- `CR Text Concatenate`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `SaveAudio`
- `GetImageSize`
- `CR Text Concatenate`
- `ttN concat`
- `easy convertAnything`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_NODE`
- `LTXVChunkFeedForward`
- `ImpactSwitch`
- `VRAMReserver`
- `CR String To Combo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Display Any (rgthree)`
- `CR Text Concatenate`
- `CR Text`
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
- `Int`
- `ManualSigmas`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-distilled-fp8.safetensors`

## 知识

覆盖率 **57%**（43/75）

**有卡**：`CFGGuider`、`LTXVSeparateAVLatent`、`ImageScaleBy`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`KSamplerSelect`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`RandomNoise`、`ManualSigmas`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`SaveAudio`、`GetImageSize`、`RH_LLMAPI_NODE`、`LTXVChunkFeedForward`、`VRAMReserver`、`LoraLoaderModelOnly`

**缺卡**（27）：`CR String To Combo`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`Display Any (rgthree)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy convertAnything`、`ttN concat`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
