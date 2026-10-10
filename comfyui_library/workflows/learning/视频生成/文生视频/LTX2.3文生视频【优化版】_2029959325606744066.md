---
key: 视频生成/文生视频/LTX2.3文生视频【优化版】_2029959325606744066.json
name: LTX2.3文生视频【优化版】_2029959325606744066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【优化版】_2029959325606744066.json
hash: 482376986867a0de
coverage: 0.614458
learned_at: 2026-10-11 03:16:47
nodes: [CFGGuider, LTXVSeparateAVLatent, ImageScaleBy, CFGGuider, easy cleanGpuUsed, KSamplerSelect, KSamplerSelect, CR Text, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, easy cleanGpuUsed, easy cleanGpuUsed, RandomNoise, easy cleanGpuUsed, easy cleanGpuUsed, LTXVConcatAVLatent, easy cleanGpuUsed, VHS_VideoCombine, VAEDecodeTiled, LTXVAudioVAEDecode, RandomNoise, SaveAudio, GetImageSize, ttN concat, easy convertAnything, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, Display Any (rgthree), CR Text, CR Text, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, CR Text, TextNode, ManualSigmas, ImpactSwitch, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, UNETLoader, LTXVConditioning, SamplerCustomAdvanced, CR String To Combo, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, ManualSigmas, ManualSigmas, SamplerCustomAdvanced, VRAMReserver, LTX2_NAG, VideoSizePresetNode, Int, Int, Int, LTXVScheduler, LoraLoaderModelOnly, CR Text Concatenate, RH_LLMAPI_NODE, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, LTXICLoRALoaderModelOnly, CR Text, ImpactSwitch]
patterns: []
missing: [CR String To Combo, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, Display Any (rgthree), easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy convertAnything, ttN concat]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled.safetensors", "height": 25, "width": 121}
discoveries: [次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3文生视频【优化版】_2029959325606744066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【优化版】_2029959325606744066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `ImageScaleBy`
- `CFGGuider`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `CR Text`
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
- `easy cleanGpuUsed`
- `RandomNoise`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `SaveAudio`
- `GetImageSize`
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
- `Display Any (rgthree)`
- `CR Text`
- `CR Text`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CR Text`
- `TextNode`
- `ManualSigmas`
- `ImpactSwitch`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `UNETLoader` ★核心
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `CR String To Combo`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VRAMReserver`
- `LTX2_NAG`
- `VideoSizePresetNode`
- `Int`
- `Int`
- `Int`
- `LTXVScheduler`
- `LoraLoaderModelOnly` ★核心
- `CR Text Concatenate`
- `RH_LLMAPI_NODE`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `LTXICLoRALoaderModelOnly` ★核心
- `CR Text`
- `ImpactSwitch`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **61%**（51/83）

**有卡**：`CFGGuider`、`LTXVSeparateAVLatent`、`ImageScaleBy`、`KSamplerSelect`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`RandomNoise`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`SaveAudio`、`GetImageSize`、`LTXVLatentUpsampler`、`TextNode`、`ManualSigmas`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`LTXVConditioning`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VRAMReserver`、`LTX2_NAG`、`VideoSizePresetNode`、`LTXVScheduler`、`RH_LLMAPI_NODE`、`LTXICLoRALoaderModelOnly`

**缺卡**（27）：`CR String To Combo`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`Display Any (rgthree)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy convertAnything`、`ttN concat`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

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
