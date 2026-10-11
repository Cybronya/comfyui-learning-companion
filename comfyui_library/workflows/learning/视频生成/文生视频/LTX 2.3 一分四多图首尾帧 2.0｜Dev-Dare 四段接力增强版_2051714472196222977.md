---
key: 视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json
name: LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json
hash: 12bf67da3275ecb7
coverage: 0.859729
learned_at: 2026-10-11 19:49:34
nodes: [PrimitiveInt, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, PrimitiveBoolean, RandomNoise, CM_FloatToInt, LTXVPreprocess, GetImageSize+, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAEDecodeTiled, LTXVImgToVideoConditionOnly, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, JWImageSequenceExtractFromBatch, CreateVideo, Int, Int, PrimitiveFloat, VHS_VideoCombine, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, LTXVAddGuideMulti, LTX2_NAG, LTXVConditioning, EmptyLTXVLatentVideo, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, ResizeLongestToNode, easy showAnything, LTXVLatentUpsampler, PromptRelayEncode, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, Int, Seed Everywhere, easy showAnything, easy showAnything, GetImageSize+, SaveImage, SaveImage, SaveImage, MathExpression|pysssss, MathExpression|pysssss, LoadImage, SaveImage, ImageCrop+, ImageCrop+, ImageCrop+, ImageCrop+, image_scale_pixel_v2, Int, PrimitiveFloat, LTXVAddGuideMulti, LTXVAddGuideMulti, VRAMReserver, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, PrimitiveBoolean, RandomNoise, CM_FloatToInt, LTXVPreprocess, GetImageSize+, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAEDecodeTiled, LTXVImgToVideoConditionOnly, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, JWImageSequenceExtractFromBatch, CreateVideo, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, LTXVAddGuideMulti, LTX2_NAG, LTXVConditioning, EmptyLTXVLatentVideo, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, CLIPTextEncode, ResizeLongestToNode, easy showAnything, LTXVLatentUpsampler, PromptRelayEncode, LTXVAddGuideMulti, LTXVAddGuideMulti, VRAMReserver, KSamplerSelect, ManualSigmas, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, RandomNoise, PrimitiveBoolean, RandomNoise, CM_FloatToInt, LTXVPreprocess, GetImageSize+, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, ImageResizeKJv2, LTXVPreprocess, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVLatentUpsampler, VAEDecodeTiled, LTXVImgToVideoConditionOnly, PreviewImage, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, JWImageSequenceExtractFromBatch, CreateVideo, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVConcatAVLatent, LTXVAddGuideMulti, LTX2_NAG, LTXVConditioning, EmptyLTXVLatentVideo, LayerUtility: PurgeVRAM V2, CLIPTextEncode, ResizeLongestToNode, easy showAnything, LTXVLatentUpsampler, PromptRelayEncode, LTXVAddGuideMulti, LTXVAddGuideMulti, VHS_VideoCombine, VHS_VideoCombine, CheckpointLoaderSimple, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTXVAudioVAELoader, LatentUpscaleModelLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, VRAMReserver, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXAVTextEncoderLoader, Text, Text, Text]
patterns: []
missing: [ImageCrop+, ImageCrop+, ImageCrop+, ImageCrop+, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, MathExpression|pysssss, GetImageSize+, GetImageSize+, GetImageSize+, GetImageSize+, Seed Everywhere]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 一分四多图首尾帧 2.0｜Dev-Dare 四段接力增强版_2051714472196222977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（221 个）：
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `PrimitiveBoolean`
- `RandomNoise`
- `CM_FloatToInt`
- `LTXVPreprocess`
- `GetImageSize+`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `JWImageSequenceExtractFromBatch`
- `CreateVideo`
- `Int`
- `Int`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `LTXVAddGuideMulti`
- `LTX2_NAG`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ResizeLongestToNode`
- `easy showAnything`
- `LTXVLatentUpsampler` ★核心
- `PromptRelayEncode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Int`
- `Seed Everywhere`
- `easy showAnything`
- `easy showAnything`
- `GetImageSize+`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `LoadImage`
- `SaveImage`
- `ImageCrop+`
- `ImageCrop+`
- `ImageCrop+`
- `ImageCrop+`
- `image_scale_pixel_v2`
- `Int`
- `PrimitiveFloat`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `VRAMReserver`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `PrimitiveBoolean`
- `RandomNoise`
- `CM_FloatToInt`
- `LTXVPreprocess`
- `GetImageSize+`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `JWImageSequenceExtractFromBatch`
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `LTXVAddGuideMulti`
- `LTX2_NAG`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ResizeLongestToNode`
- `easy showAnything`
- `LTXVLatentUpsampler` ★核心
- `PromptRelayEncode`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `VRAMReserver`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `PrimitiveBoolean`
- `RandomNoise`
- `CM_FloatToInt`
- `LTXVPreprocess`
- `GetImageSize+`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoConditionOnly`
- `PreviewImage`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `JWImageSequenceExtractFromBatch`
- `CreateVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `LTXVConcatAVLatent`
- `LTXVAddGuideMulti`
- `LTX2_NAG`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LayerUtility: PurgeVRAM V2`
- `CLIPTextEncode` ★核心
- `ResizeLongestToNode`
- `easy showAnything`
- `LTXVLatentUpsampler` ★核心
- `PromptRelayEncode`
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `Text`
- `Text`
- `Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-dare-merged-distilled-1.1.safetensors`

## 知识

覆盖率 **86%**（190/221）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`PrimitiveBoolean`、`CM_FloatToInt`、`LTXVPreprocess`、`ImageResizeKJv2`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoConditionOnly`、`LTXVAudioVAEDecode`、`JWImageSequenceExtractFromBatch`、`CreateVideo`、`Int`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`LTXVAddGuideMulti`、`LTX2_NAG`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ResizeLongestToNode`、`PromptRelayEncode`、`SaveImage`、`LoadImage`、`image_scale_pixel_v2`、`VRAMReserver`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`Text`

**缺卡**（14）：`ImageCrop+`、`ImageCrop+`、`ImageCrop+`、`ImageCrop+`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`GetImageSize+`、`GetImageSize+`、`GetImageSize+`、`GetImageSize+`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCrop+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
