---
key: 视频生成/文生视频/迄今超强高质量画音同步LTX2.3 KJ版低显存提速版文+音频生MV视频分镜支持横竖屏自定义分镜时间_1955807480933597185.json
name: 迄今超强高质量画音同步LTX2.3 KJ版低显存提速版文+音频生MV视频分镜支持横竖屏自定义分镜时间_1955807480933597185
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/迄今超强高质量画音同步LTX2.3 KJ版低显存提速版文+音频生MV视频分镜支持横竖屏自定义分镜时间_1955807480933597185.json
hash: f866e06710f9a5da
coverage: 0.517857
learned_at: 2026-10-10 23:14:06
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MathExpression|pysssss, SetNode, GetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, KSamplerSelect, GetNode, SimpleMath+, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, KSamplerSelect, SeedVR2ExtraArgs, PreviewImage, SimpleCalculatorKJ, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, LTXVPreprocess, SamplerCustomAdvanced, LoadImage, SetNode, SetNode, PrimitiveFloat, SetNode, SetNode, SetNode, VAELoaderKJ, LTXVConditioning, ManualSigmas, LatentUpscaleModelLoader, MarkdownNote, LTXVImgToVideoInplace, SetNode, SetNode, ImageScaleBy, GetImageSize, easy int, easy int, CFGGuider, LTXVScheduler, Qwen3_VQA_Plus, ImpactMinMax, GetNode, GetNode, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, PathchSageAttentionKJ, ModelPatchTorchSettings, DualCLIPLoader, VAELoaderKJ, MelBandRoFormerModelLoader, GetNode, MelBandRoFormerSampler, SetNode, LTXVAudioVAEEncode, SolidMask, GetNode, TrimAudioDuration, MarkdownNote, GetNode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecodeTiled, easy showAnything, SetNode, CLIPTextEncode, CLIPTextEncode, GetNode, AudioCrop, UnetLoaderGGUF, MarkdownNote, LoadDiffusionModelShared //Inspire, LTXAVTextEncoderLoader, GetNode, GetNode, RandomNoise, CFGGuider, RandomNoise, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVEmptyLatentAudio, SetNode, SetNode, SetLatentNoiseMask, PreviewAudio, LoadAudio, ImpactSwitch, Fast Groups Bypasser (rgthree), ComfySwitchNode, VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes, Text Concatenate, RHHiddenNodes, CR Text, LoraLoaderModelOnly, SeedVR2BlockSwap, SeedVR2GGUF, easy int]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, LoadDiffusionModelShared //Inspire, MathExpression|pysssss, SimpleMath+, Text Concatenate, easy int, easy int, easy int]
parameters: {"batch_size": 1, "height": 25, "width": 121}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LoadDiffusionModelShared //Inspire` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/迄今超强高质量画音同步LTX2.3 KJ版低显存提速版文+音频生MV视频分镜支持横竖屏自定义分镜时间_1955807480933597185.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/迄今超强高质量画音同步LTX2.3 KJ版低显存提速版文+音频生MV视频分镜支持横竖屏自定义分镜时间_1955807480933597185.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `SeedVR2ExtraArgs`
- `PreviewImage`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `LTXVConditioning`
- `ManualSigmas`
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `LTXVImgToVideoInplace`
- `SetNode`
- `SetNode`
- `ImageScaleBy`
- `GetImageSize`
- `easy int`
- `easy int`
- `CFGGuider`
- `LTXVScheduler`
- `Qwen3_VQA_Plus`
- `ImpactMinMax`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `MelBandRoFormerModelLoader`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `GetNode`
- `TrimAudioDuration`
- `MarkdownNote`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `easy showAnything`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `AudioCrop`
- `UnetLoaderGGUF` ★核心
- `MarkdownNote`
- `LoadDiffusionModelShared //Inspire`
- `LTXAVTextEncoderLoader`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `RandomNoise`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `PreviewAudio`
- `LoadAudio`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `Text Concatenate`
- `RHHiddenNodes`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2BlockSwap`
- `SeedVR2GGUF`
- `easy int`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **52%**（58/112）

**有卡**：`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`SeedVR2ExtraArgs`、`SimpleCalculatorKJ`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`LoadImage`、`VAELoaderKJ`、`LTXVConditioning`、`ManualSigmas`、`LatentUpscaleModelLoader`、`ImageScaleBy`、`GetImageSize`、`CFGGuider`、`LTXVScheduler`、`Qwen3_VQA_Plus`、`ImpactMinMax`、`EmptyImage`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`DualCLIPLoader`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`TrimAudioDuration`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CLIPTextEncode`、`AudioCrop`、`UnetLoaderGGUF`、`LTXAVTextEncoderLoader`、`RandomNoise`、`LTXVChunkFeedForward`、`LTXVEmptyLatentAudio`、`SetLatentNoiseMask`、`PreviewAudio`、`LoadAudio`、`VHS_VideoCombine`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`SeedVR2BlockSwap`、`SeedVR2GGUF`

**缺卡**（9）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadDiffusionModelShared //Inspire`、`MathExpression|pysssss`、`SimpleMath+`、`Text Concatenate`、`easy int`、`easy int`、`easy int`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、SeedVR2BlockSwap、SeedVR2ExtraArgs

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LoadDiffusionModelShared //Inspire` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
