---
key: 视频生成/文生视频/ltx2.3 图生视频【蒸馏版】+反推提示词_2037473491712221185.json
name: ltx2.3 图生视频【蒸馏版】+反推提示词_2037473491712221185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 图生视频【蒸馏版】+反推提示词_2037473491712221185.json
hash: 65b2ae682fe1c603
coverage: 0.307263
learned_at: 2026-10-11 03:48:38
nodes: [LTXVPreprocess, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, Any To String (mtb), ResizeImagesByLongerEdge, Int, CR Text, SetNode, SetNode, Any To String (mtb), SetNode, GetNode, ImpactSwitch, SetNode, GetNode, SetNode, SetNode, ShowText|pysssss, SetNode, SetNode, RTXVideoSuperResolution, CR Text, GetNode, GetNode, GetNode, easy convertAnything, ttN concat, CR Text Concatenate, SetNode, SetNode, Any To String (mtb), Any To String (mtb), Any To String (mtb), Any To String (mtb), easy int, Any To String (mtb), CR Value, easy boolean, LoadImage, SetNode, llama_cpp_instruct_adv, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyImage, LTXVConcatAVLatent, easy cleanGpuUsed, SetNode, easy cleanGpuUsed, SetNode, ImageScaleBy, SetNode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, CFGGuider, RandomNoise, easy cleanGpuUsed, GetNode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, GetNode, LTXVChunkFeedForward, GetImageSize, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, CR Text, CR Text, easy boolean, GetNode, GetNode, GetNode, GetNode, VRAMReserver, ManualSigmas, LTXVLatentUpsampler, LTX2_NAG, LTXVImgToVideoInplace, Switch any [Crystools], LoraLoaderModelOnly, SetNode, KSamplerSelect, LTXVImgToVideoInplace, LTXVConcatAVLatent, RTXVideoSuperResolution, VAELoaderKJ, VAELoaderKJ, ManualSigmas, LoraLoaderModelOnly, LoraLoaderModelOnly, ManualSigmas, CR Text, CR Text, CR Text, CR String To Combo, CR Text, CR Text, CR Text, CR Text, CR Text, ImpactSwitch, CR Text, Fast Groups Muter (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, SetNode, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, ImpactSwitch, Display Any (rgthree), CR Text, Int, CR Text, CR Text, easy convertAnything, GetNode, GetNode, llama_cpp_model_loader, LatentUpscaleModelLoader, UNETLoader, DualCLIPLoader, SetNode, GetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, PrimitiveInt, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, SetNode, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, SetNode, GetNode, RandomNoise, CFGGuider, LTXVScheduler, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, ManualSigmas, SetNode, GetNode, GetNode, SamplerCustomAdvanced, easy cleanGpuUsed, LTXVSeparateAVLatent, ManualSigmas, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, CreateVideo, VAEDecodeTiled, SaveVideo]
patterns: []
missing: [Any To String (mtb), Any To String (mtb), Any To String (mtb), Any To String (mtb), Any To String (mtb), Any To String (mtb), Any To String (mtb), CR String To Combo, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, CR Value, Display Any (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, Switch any [Crystools], easy boolean, easy boolean, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy convertAnything, easy convertAnything, easy int, ttN concat]
parameters: {"batch_size": 1, "height": 24, "width": 97}
discoveries: [次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR String To Combo` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Value` 知识库中没有该节点类型的任何知识, 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/ltx2.3 图生视频【蒸馏版】+反推提示词_2037473491712221185.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 图生视频【蒸馏版】+反推提示词_2037473491712221185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（179 个）：
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `ResizeImagesByLongerEdge`
- `Int`
- `CR Text`
- `SetNode`
- `SetNode`
- `Any To String (mtb)`
- `SetNode`
- `GetNode`
- `ImpactSwitch`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `RTXVideoSuperResolution`
- `CR Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `ttN concat`
- `CR Text Concatenate`
- `SetNode`
- `SetNode`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `easy int`
- `Any To String (mtb)`
- `CR Value`
- `easy boolean`
- `LoadImage`
- `SetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CFGGuider`
- `RandomNoise`
- `easy cleanGpuUsed`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVChunkFeedForward`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `CR Text`
- `CR Text`
- `easy boolean`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VRAMReserver`
- `ManualSigmas`
- `LTXVLatentUpsampler` ★核心
- `LTX2_NAG`
- `LTXVImgToVideoInplace`
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `RTXVideoSuperResolution`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR String To Combo`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `CR Text`
- `Fast Groups Muter (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `SetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `Display Any (rgthree)`
- `CR Text`
- `Int`
- `CR Text`
- `CR Text`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `llama_cpp_model_loader`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `SetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `SaveVideo`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **31%**（55/179）

**有卡**：`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`Int`、`RTXVideoSuperResolution`、`LoadImage`、`llama_cpp_instruct_adv`、`EmptyImage`、`LTXVConcatAVLatent`、`ImageScaleBy`、`CFGGuider`、`RandomNoise`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVChunkFeedForward`、`GetImageSize`、`LTXVCropGuides`、`VRAMReserver`、`ManualSigmas`、`LTXVLatentUpsampler`、`LTX2_NAG`、`LTXVImgToVideoInplace`、`LoraLoaderModelOnly`、`KSamplerSelect`、`VAELoaderKJ`、`llama_cpp_model_loader`、`LatentUpscaleModelLoader`、`UNETLoader`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`SaveVideo`

**缺卡**（51）：`Any To String (mtb)`、`Any To String (mtb)`、`Any To String (mtb)`、`Any To String (mtb)`、`Any To String (mtb)`、`Any To String (mtb)`、`Any To String (mtb)`、`CR String To Combo`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Value`、`Display Any (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`Switch any [Crystools]`、`easy boolean`、`easy boolean`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy convertAnything`、`easy convertAnything`、`easy int`、`ttN concat`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Any To String (mtb)` 知识库中没有该节点类型的任何知识
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
- 次要节点 `CR Value` 知识库中没有该节点类型的任何知识
- 次要节点 `Display Any (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Switch any [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `ttN concat` 知识库中没有该节点类型的任何知识
