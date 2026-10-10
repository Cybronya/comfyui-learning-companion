---
key: 视频生成/文生视频/Wan2.2_S2V-数字人极速长视频_1965020962519437313.json
name: Wan2.2_S2V-数字人极速长视频_1965020962519437313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_S2V-数字人极速长视频_1965020962519437313.json
hash: ced285028030fa91
coverage: 0.405941
learned_at: 2026-10-10 23:07:19
nodes: [LoraLoaderModelOnly, LayerUtility: PurgeVRAM, AudioEncoderLoader, CLIPTextEncode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, ImageSmartSharpen+, AudioConcatenate, AudioSeparation, Audio Duration (mtb), easy showAnything, GetNode, GetNode, GetNode, easy showAnything, easy forLoopStart, AudioEncoderEncode, easy showAnything, Audio Duration (mtb), easy convertAnything, ConditionalTextOutput, easy convertAnything, easy mathInt, LatentConcat, MathExpression|pysssss, easy showAnything, easy forLoopEnd, Reroute, LatentConcat, LatentCut, GetImageSizeAndCount, SetNode, MathExpression|pysssss, easy cleanGpuUsed, GetNode, ImageFromBatch, SimpleMath+, VAEDecode, GetNode, SetNode, LoadAudio, AudioCrop, PreviewAudio, AudioCrop, GetImageRangeFromBatch, PrimitiveString, MathExpression|pysssss, easy showAnything, easy convertAnything, PreviewAudio, VHS_VideoCombine, UNETLoader, GetNode, CR Text, GetNode, LoraLoaderModelOnly, VAELoader, SetNode, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, easy cleanGpuUsed, KSampler, KSampler, CLIPTextEncode, GetNode, WanSoundImageToVideoExtend, Reroute, CLIPLoader, CR Text, LoadAudio, PrimitiveString, Reroute, SetNode, easy showAnything, GetNode, GetNode, GetNode, WanSoundImageToVideo, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, MathExpression|pysssss, LoadImage, Note, VHS_VideoCombine, AIO_Preprocessor, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, Fast Bypasser (rgthree), CR Image Input Switch, Int, easy convertAnything, VHS_LoadVideo, Int, Reroute, Reroute, Reroute, ImageResizeKJv2, Int]
patterns: []
missing: [Audio Duration (mtb), Audio Duration (mtb), CR Image Input Switch, CR Text, CR Text, Fast Bypasser (rgthree), ImageSmartSharpen+, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy convertAnything, easy convertAnything, easy convertAnything, easy convertAnything, easy forLoopEnd, easy forLoopStart, easy mathInt]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 594466356251814, "steps": 8}
discoveries: [次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Image Input Switch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2_S2V-数字人极速长视频_1965020962519437313.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_S2V-数字人极速长视频_1965020962519437313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（101 个）：
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `AudioEncoderLoader`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `ImageSmartSharpen+`
- `AudioConcatenate`
- `AudioSeparation`
- `Audio Duration (mtb)`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy forLoopStart`
- `AudioEncoderEncode`
- `easy showAnything`
- `Audio Duration (mtb)`
- `easy convertAnything`
- `ConditionalTextOutput`
- `easy convertAnything`
- `easy mathInt`
- `LatentConcat`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy forLoopEnd`
- `Reroute`
- `LatentConcat`
- `LatentCut`
- `GetImageSizeAndCount`
- `SetNode`
- `MathExpression|pysssss`
- `easy cleanGpuUsed`
- `GetNode`
- `ImageFromBatch`
- `SimpleMath+`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `LoadAudio`
- `AudioCrop`
- `PreviewAudio`
- `AudioCrop`
- `GetImageRangeFromBatch`
- `PrimitiveString`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy convertAnything`
- `PreviewAudio`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `GetNode`
- `CR Text`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `SetNode`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `WanSoundImageToVideoExtend`
- `Reroute`
- `CLIPLoader`
- `CR Text`
- `LoadAudio`
- `PrimitiveString`
- `Reroute`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanSoundImageToVideo`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `MathExpression|pysssss`
- `LoadImage`
- `Note`
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `Fast Bypasser (rgthree)`
- `CR Image Input Switch`
- `Int`
- `easy convertAnything`
- `VHS_LoadVideo`
- `Int`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `Int`

## 关键参数

- `seed` = `594466356251814`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **41%**（41/101）

**有卡**：`LoraLoaderModelOnly`、`AudioEncoderLoader`、`CLIPTextEncode`、`AudioConcatenate`、`AudioSeparation`、`AudioEncoderEncode`、`ConditionalTextOutput`、`LatentConcat`、`LatentCut`、`GetImageSizeAndCount`、`ImageFromBatch`、`VAEDecode`、`LoadAudio`、`AudioCrop`、`PreviewAudio`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`UNETLoader`、`VAELoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`KSampler`、`WanSoundImageToVideoExtend`、`CLIPLoader`、`WanSoundImageToVideo`、`LoadImage`、`AIO_Preprocessor`、`Int`、`VHS_LoadVideo`、`ImageResizeKJv2`

**缺卡**（28）：`Audio Duration (mtb)`、`Audio Duration (mtb)`、`CR Image Input Switch`、`CR Text`、`CR Text`、`Fast Bypasser (rgthree)`、`ImageSmartSharpen+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy convertAnything`、`easy convertAnything`、`easy convertAnything`、`easy convertAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy mathInt`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Audio Duration (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Image Input Switch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy convertAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
