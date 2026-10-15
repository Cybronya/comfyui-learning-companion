---
key: 视频生成/文生视频/LTX2.3图生视频+音视同步【双版本优化】_2059047320699891713.json
name: LTX2.3图生视频+音视同步【双版本优化】_2059047320699891713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频+音视同步【双版本优化】_2059047320699891713.json
hash: 0c2ee5bb2cd96bbe
coverage: 0.565476
learned_at: 2026-10-15 22:45:07
nodes: [CR Text, SetNode, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, GetNode, CR Text, CR Text, SetNode, CR Text, CR Text, SetNode, GetNode, easy convertAnything, easy cleanGpuUsed, GetNode, Int, SetNode, easy int, SetNode, SetNode, SetNode, SetNode, llama_cpp_model_loader, GetNode, CR Text, CR Text, CR Text, SetNode, CR String To Combo, LTXVChunkFeedForward, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, easy cleanGpuUsed, SetNode, Any To String (mtb), ImpactSwitch, ResizeImagesByLongerEdge, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, easy convertAnything, ttN concat, CR Text Concatenate, GetNode, GetNode, SetNode, CR Text, Any To String (mtb), Any To String (mtb), Any To String (mtb), CR Text, Any To String (mtb), CR Text, ImpactSwitch, GetNode, GetNode, SetNode, llama_cpp_instruct_adv, ShowText|pysssss, MathExpression|pysssss, GetNode, GetNode, GetNode, PrimitiveInt, GetNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, GetNode, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetNode, easy cleanGpuUsed, GetNode, easy cleanGpuUsed, GetNode, LTXVConditioning, SetNode, SetNode, easy cleanGpuUsed, CLIPTextEncode, GetNode, RandomNoise, KSamplerSelect, GetNode, SamplerCustomAdvanced, CFGGuider, LTXVCropGuides, GetNode, GetNode, LTXVLatentUpsampler, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, CreateVideo, GetNode, CR Value, SetNode, GetNode, GetNode, LTXVScheduler, easy cleanGpuUsed, LTXVSeparateAVLatent, SetNode, SetNode, SetNode, GetImageSize, ImageScaleBy, EmptyImage, SetNode, GetNode, GetNode, ImpactSwitch, GetNode, Int, SetNode, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, CFGGuider, RandomNoise, SamplerCustomAdvanced, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, CheckpointLoaderSimple, CheckpointLoaderSimple, SetNode, SetNode, SetNode, SetNode, SetNode, AnySwitch, AnySwitch, AnySwitch, AnySwitch, AnySwitch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, VRAMReserver, LatentUpscaleModelLoader, LoraLoaderModelOnly, Int, easy cleanGpuUsed, PlaySound|pysssss, PlaySound|pysssss, PlaySound|pysssss, Fast Groups Bypasser (rgthree), Int, SaveVideo, CLIPTextEncode, LoadImage, CR Text, Display Any (rgthree), MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/文生视频/LTX2.3图生视频+音视同步【双版本优化】_2059047320699891713.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频+音视同步【双版本优化】_2059047320699891713.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（168 个）：
- `CR Text`
- `SetNode`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `CR Text`
- `CR Text`
- `SetNode`
- `CR Text`
- `CR Text`
- `SetNode`
- `GetNode`
- `easy convertAnything`
- `easy cleanGpuUsed`
- `GetNode`
- `Int`
- `SetNode`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `llama_cpp_model_loader`
- `GetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `SetNode`
- `CR String To Combo`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `Any To String (mtb)`
- `ImpactSwitch`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `easy convertAnything`
- `ttN concat`
- `CR Text Concatenate`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Text`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `CR Text`
- `Any To String (mtb)`
- `CR Text`
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `SetNode`
- `llama_cpp_instruct_adv`
- `ShowText|pysssss`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `SetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `GetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `CreateVideo`
- `GetNode`
- `CR Value`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVScheduler`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `ImageScaleBy`
- `EmptyImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImpactSwitch`
- `GetNode`
- `Int`
- `SetNode`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `AnySwitch`
- `AnySwitch`
- `AnySwitch`
- `AnySwitch`
- `AnySwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `VRAMReserver`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `easy cleanGpuUsed`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `PlaySound|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `Int`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CR Text`
- `Display Any (rgthree)`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **57%**（95/168）

**有卡**：`CR Text`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy convertAnything`、`easy cleanGpuUsed`、`Int`、`easy int`、`llama_cpp_model_loader`、`CR String To Combo`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`、`Any To String (mtb)`、`ResizeImagesByLongerEdge`、`ttN concat`、`CR Text Concatenate`、`llama_cpp_instruct_adv`、`MathExpression|pysssss`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`CLIPTextEncode`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`CR Value`、`LTXVScheduler`、`GetImageSize`、`ImageScaleBy`、`EmptyImage`、`LTXVAudioVAELoader`、`ManualSigmas`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`AnySwitch`、`VRAMReserver`、`PlaySound|pysssss`、`SaveVideo`、`LoadImage`、`Display Any (rgthree)`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
