---
key: 视频生成/图生视频/LTX2.3高质量-8分镜图生视频-剧情漫剧_2039687730661167105.json
name: LTX2.3高质量-8分镜图生视频-剧情漫剧_2039687730661167105.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039687730661167105.json
hash: 386137a504dcb207
coverage: 0.590406
learned_at: 2026-10-15 22:36:10
nodes: [SetNode, GetNode, SetNode, CR Value, GetNode, LayerUtility: ImageScaleByAspectRatio V2, easy int, LTXAVTextEncoderLoader, SetNode, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, SetNode, SetNode, CR Text, GetNode, GetNode, GetNode, EmptyImage, GetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, GetNode, LTXVConcatAVLatent, easy cleanGpuUsed, GetNode, GetNode, CLIPTextEncode, GetNode, SetNode, SetNode, GetNode, GetNode, CFGGuider, GetNode, SetNode, RandomNoise, SamplerCustomAdvanced, easy cleanGpuUsed, LTXVSeparateAVLatent, GetNode, GetNode, ManualSigmas, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, LTXVCropGuides, LTXVLatentUpsampler, GetNode, SetNode, GetNode, LTXVImgToVideoInplace, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVConcatAVLatent, GetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, GetNode, easy cleanGpuUsed, Any To String (mtb), GetNode, CR Text Concatenate, SetNode, SetNode, GetNode, ResizeImagesByLongerEdge, LTXVPreprocess, SetNode, llama_cpp_model_loader, ShowText|pysssss, SetNode, llama_cpp_instruct_adv, SetNode, SetNode, SetNode, SetNode, SetNode, CR Text, ImpactSwitch, GetNode, CR Text, Int, LoraLoaderModelOnly, easy showAnything, GetNode, GetNode, EmptyLTXVLatentVideo, GetNode, PrimitiveInt, SetNode, CR Text, CR Text, CR String To Combo, Switch any [Crystools], GetNode, GetNode, ManualSigmas, GetNode, GetNode, easy cleanGpuUsed, LTXVCropGuides, LTXVLatentUpsampler, GetNode, GetNode, KSamplerSelect, LTXVImgToVideoInplace, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, ManualSigmas, ManualSigmas, easy showAnything, CR Text, CR Text, ManualSigmas, ManualSigmas, VRAMReserver, LoraLoaderModelOnly, ManualSigmas, GetImageSize, ImageScaleBy, KSamplerSelect, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LoraLoaderModelOnly, CR Text, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy convertAnything, ttN concat, SetNode, SetNode, GetNode, SetNode, GetNode, CR Text, Int, UNETLoader, LoraLoaderModelOnly, LTXVChunkFeedForward, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, easy boolean, VAELoader, ManualSigmas, ManualSigmas, LTXVImgToVideoInplace, ManualSigmas, ManualSigmas, GetNode, GetNode, VAEDecodeTiled, LTXVAudioVAEDecode, easy isNone, AudioConcat, LTXVAudioVAEDecode, VAEDecodeTiled, CLIPTextEncode, LTX2_NAG, LTXVConditioning, easy cleanGpuUsed, easy cleanGpuUsed, easy anythingIndexSwitch, easy forLoopStart, ManualSigmas, SaveVideo, SaveVideo, If ANY execute A else B, easy isNone, GetNode, easy batchAnything, easy forLoopEnd, GetNode, EmptyAudio, AudioConcat, CreateVideo, GetNode, easy batchAnything, GetNode, If ANY execute A else B, EmptyAudio, LTX2AttentionTunerPatch, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXVAudioVAELoader, UNETLoader, SetNode, SetNode, GetNode, easy forLoopEnd, SetNode, SetNode, easy indexAnything, SetNode, SetNode, PreviewImage, easy indexAnything, SetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageResizeKJv2, easy promptLine, ProcessString, SetNode, SDVM Image List Repeat, SetNode, PreviewImage, Display Any (rgthree), GetNode, GetNode, SetNode, CR Text, MarkdownNote, Text, SetNode, CR Text, Int, CR Text, CR Text, CR Text, VHS_VideoCombine, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, ImpactSwitch, SetNode, Fast Groups Bypasser (rgthree), TTResolutionSelector, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3高质量-8分镜图生视频-剧情漫剧_2039687730661167105.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039687730661167105.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（271 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `CR Value`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `SetNode`
- `SetNode`
- `CR Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `GetNode`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `SetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `GetNode`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `GetNode`
- `CR Text Concatenate`
- `SetNode`
- `SetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SetNode`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `SetNode`
- `llama_cpp_instruct_adv`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `ImpactSwitch`
- `GetNode`
- `CR Text`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `CR Text`
- `CR Text`
- `CR String To Combo`
- `Switch any [Crystools]`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `ManualSigmas`
- `easy showAnything`
- `CR Text`
- `CR Text`
- `ManualSigmas`
- `ManualSigmas`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `ttN concat`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `CR Text`
- `Int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `easy boolean`
- `VAELoader`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `easy isNone`
- `AudioConcat`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVConditioning`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy anythingIndexSwitch`
- `easy forLoopStart`
- `ManualSigmas`
- `SaveVideo`
- `SaveVideo`
- `If ANY execute A else B`
- `easy isNone`
- `GetNode`
- `easy batchAnything`
- `easy forLoopEnd`
- `GetNode`
- `EmptyAudio`
- `AudioConcat`
- `CreateVideo`
- `GetNode`
- `easy batchAnything`
- `GetNode`
- `If ANY execute A else B`
- `EmptyAudio`
- `LTX2AttentionTunerPatch`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `LTXVAudioVAELoader`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `easy forLoopEnd`
- `SetNode`
- `SetNode`
- `easy indexAnything`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `easy indexAnything`
- `SetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `easy promptLine`
- `ProcessString`
- `SetNode`
- `SDVM Image List Repeat`
- `SetNode`
- `PreviewImage`
- `Display Any (rgthree)`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Text`
- `MarkdownNote`
- `Text`
- `SetNode`
- `CR Text`
- `Int`
- `CR Text`
- `CR Text`
- `CR Text`
- `VHS_VideoCombine`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ImpactSwitch`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `TTResolutionSelector`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **59%**（160/271）

**有卡**：`CR Value`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`LTXAVTextEncoderLoader`、`CR Text`、`EmptyImage`、`MathExpression|pysssss`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`CLIPTextEncode`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`Any To String (mtb)`、`CR Text Concatenate`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`Int`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`CR String To Combo`、`Switch any [Crystools]`、`KSamplerSelect`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`VRAMReserver`、`GetImageSize`、`ImageScaleBy`、`VAELoaderKJ`、`DualCLIPLoader`、`easy convertAnything`、`ttN concat`、`UNETLoader`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`easy boolean`、`VAELoader`、`easy isNone`、`AudioConcat`、`LTX2_NAG`、`LTXVConditioning`、`easy anythingIndexSwitch`、`easy forLoopStart`、`SaveVideo`、`If ANY execute A else B`、`easy batchAnything`、`easy forLoopEnd`、`EmptyAudio`、`LTX2AttentionTunerPatch`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXVAudioVAELoader`、`easy indexAnything`、`LoadImage`、`ImageResizeKJv2`、`easy promptLine`、`ProcessString`、`SDVM Image List Repeat`、`Display Any (rgthree)`、`Text`、`VHS_VideoCombine`、`TTResolutionSelector`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider
