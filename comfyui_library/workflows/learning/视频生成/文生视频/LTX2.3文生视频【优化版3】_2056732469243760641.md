---
key: 视频生成/文生视频/LTX2.3文生视频【优化版3】_2056732469243760641.json
name: LTX2.3文生视频【优化版3】_2056732469243760641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【优化版3】_2056732469243760641.json
hash: cb7e523e9dbdd30d
coverage: 0.662338
learned_at: 2026-10-11 19:49:39
nodes: [CFGGuider, KSamplerSelect, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, EmptyImage, PrimitiveInt, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, RandomNoise, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVAudioVAEDecode, RandomNoise, ttN concat, easy convertAnything, SamplerCustomAdvanced, ManualSigmas, VideoSizePresetNode, Int, Int, SamplerCustomAdvanced, LTX2_NAG, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, BasicScheduler, LatentUpscaleModelLoader, CLIPTextEncode, KSamplerSelect, CFGGuider, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVLatentUpsampler, BasicScheduler, VAEDecodeTiled, LTXVScheduler, easy cleanGpuUsed, UNETLoader, GetImageSize, ImageScaleBy, EmptyLTXVLatentVideo, easy convertAnything, LTXVSeparateAVLatent, TextNode, CR Text, VRAMReserver, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, LTXVConditioning, easy cleanGpuUsed, DualCLIPLoader, CLIPTextEncode, easy cleanGpuUsed, VHS_VideoCombine, CR Text Concatenate, LoraLoaderModelOnly, Int, Fast Groups Muter (rgthree), CR Text, CR Text, CR Text Concatenate, CR Text, CR Text, RH_LLMAPI_NODE, CR Text, CR Text, Display Any (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), TextNode, ModelscopeApiTextGenerationNode, Display Any (rgthree), ImpactSwitch]
patterns: []
missing: [CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, Display Any (rgthree), Display Any (rgthree), easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy convertAnything, easy convertAnything, ttN concat]
parameters: {"batch_size": 1, "height": 25, "width": 121}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3文生视频【优化版3】_2056732469243760641.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频【优化版3】_2056732469243760641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（77 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `PIP_IntegerCalculator`
- `Int`
- `PIP_IntegerCalculator`
- `EmptyImage`
- `PrimitiveInt`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `LTXVAudioVAEDecode` ★核心
- `RandomNoise`
- `ttN concat`
- `easy convertAnything`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `VideoSizePresetNode`
- `Int`
- `Int`
- `SamplerCustomAdvanced` ★核心
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `BasicScheduler`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `BasicScheduler`
- `VAEDecodeTiled` ★核心
- `LTXVScheduler`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `GetImageSize`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `easy convertAnything`
- `LTXVSeparateAVLatent`
- `TextNode`
- `CR Text`
- `VRAMReserver`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Fast Groups Muter (rgthree)`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
- `RH_LLMAPI_NODE`
- `CR Text`
- `CR Text`
- `Display Any (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `TextNode`
- `ModelscopeApiTextGenerationNode`
- `Display Any (rgthree)`
- `ImpactSwitch`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **66%**（51/77）

**有卡**：`CFGGuider`、`KSamplerSelect`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`ManualSigmas`、`VideoSizePresetNode`、`LTX2_NAG`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`BasicScheduler`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`LTXVScheduler`、`UNETLoader`、`GetImageSize`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`TextNode`、`VRAMReserver`、`LTXICLoRALoaderModelOnly`、`LTXVConditioning`、`DualCLIPLoader`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`ModelscopeApiTextGenerationNode`

**缺卡**（19）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`Display Any (rgthree)`、`Display Any (rgthree)`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy convertAnything`、`easy convertAnything`、`ttN concat`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
