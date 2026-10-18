---
key: 视频生成/图生视频/LTX2.0-【首尾帧】_2009910509788733441.json
name: LTX2.0-【首尾帧】_2009910509788733441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.0-【首尾帧】_2009910509788733441.json
hash: 17ce770f9c71c9d3
coverage: 0.586207
learned_at: 2026-10-15 22:34:15
nodes: [SetNode, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CR Text, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveInt, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, GetNode, EmptyImage, Display Any (rgthree), GetImageSize, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, RandomNoise, GetNode, GetNode, CFGGuider, easy cleanGpuUsed, LTXVScheduler, KSamplerSelect, SetNode, SetNode, LTXVSeparateAVLatent, easy cleanGpuUsed, GetNode, easy cleanGpuUsed, SetNode, SetNode, RandomNoise, GetNode, LTXVPreprocess, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, VAEDecodeTiled, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, ImageScaleBy, CreateVideo, SetNode, SetNode, GetNode, GetNode, GetNode, ProcessString, easy cleanGpuUsed, SetNode, Any To String (mtb), SetNode, RH_LLMAPI_NODE, Display Any (rgthree), SomethingToString, Qwen3_VQA, SetNode, SetNode, Any To String (mtb), GetNode, GetNode, GetNode, GetNode, Any To String (mtb), CR String To Combo, CR Text, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVLatentUpsampler, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, SetNode, LTXVPreprocess, SetNode, SetNode, ResizeImagesByLongerEdge, LTXVFirstLastFrameControl_TTP, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVFirstLastFrameControl_TTP, CFGGuider, LTXVSeparateAVLatent, CR Text, CR Prompt Text, CR Text, CR Text, CR Text, GetNode, CR Text, MuyeTextEditOutput, CR Text, CR Text, ModelScopeVisionPromptInversion_Sevr, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, ImageResizeKJv2, ResizeImagesByLongerEdge, GetNode, ImageResizeKJv2, easy imageConcat, SetNode, SaveVideo, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, SetNode, SetNode, SetNode, Int, CR Text, Any To String (mtb), SetNode, ImpactSwitch, CR Text, Display Any (rgthree), Display Any (rgthree), CR Text, CR Text, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, ShowText|pysssss, LTXVConcatAVLatent, GetNode, SamplerCustomAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, KSamplerSelect, LTXVCropGuides, SamplerCustomAdvanced, CR Text, CR Text, ttN concat, CR Text Concatenate, CR Text, CR Text, CR Text Concatenate, ttN concat, SetNode, CR Text Concatenate, ImpactSwitch, easy convertAnything, GetNode, easy convertAnything, GetNode, GetNode, LTXVAudioVAEDecode, LatentUpscaleModelLoader, CheckpointLoaderSimple, LoadImage, CR Text, ManualSigmas, LoadImage, Int, easy int, CR Text, VRAMReserver, DualCLIPLoader, ImpactSwitch, CheckpointLoaderSimple, CheckpointLoaderSimple, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx2-phr00tmerge-sfw-v5.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.0-【首尾帧】_2009910509788733441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2009910509788733441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（203 个）：
- `SetNode`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CR Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `PIP_IntegerCalculator`
- `Int`
- `PIP_IntegerCalculator`
- `GetNode`
- `EmptyImage`
- `Display Any (rgthree)`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `easy cleanGpuUsed`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `GetNode`
- `LTXVPreprocess`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `CreateVideo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ProcessString`
- `easy cleanGpuUsed`
- `SetNode`
- `Any To String (mtb)`
- `SetNode`
- `RH_LLMAPI_NODE`
- `Display Any (rgthree)`
- `SomethingToString`
- `Qwen3_VQA`
- `SetNode`
- `SetNode`
- `Any To String (mtb)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any To String (mtb)`
- `CR String To Combo`
- `CR Text`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LTXVFirstLastFrameControl_TTP`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVFirstLastFrameControl_TTP`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `CR Text`
- `CR Prompt Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `GetNode`
- `CR Text`
- `MuyeTextEditOutput`
- `CR Text`
- `CR Text`
- `ModelScopeVisionPromptInversion_Sevr`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `ImageResizeKJv2`
- `easy imageConcat`
- `SetNode`
- `SaveVideo`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `CR Text`
- `Any To String (mtb)`
- `SetNode`
- `ImpactSwitch`
- `CR Text`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `CR Text`
- `CR Text`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `ShowText|pysssss`
- `LTXVConcatAVLatent`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `CR Text`
- `CR Text`
- `ttN concat`
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `ttN concat`
- `SetNode`
- `CR Text Concatenate`
- `ImpactSwitch`
- `easy convertAnything`
- `GetNode`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CR Text`
- `ManualSigmas`
- `LoadImage`
- `Int`
- `easy int`
- `CR Text`
- `VRAMReserver`
- `DualCLIPLoader`
- `ImpactSwitch`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `UNETLoader` ★核心

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx2-phr00tmerge-sfw-v5.safetensors`

## 知识

覆盖率 **59%**（119/203）

**有卡**：`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CR Text`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`Display Any (rgthree)`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`easy cleanGpuUsed`、`LTXVScheduler`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`VAEDecodeTiled`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`ImageScaleBy`、`CreateVideo`、`ProcessString`、`Any To String (mtb)`、`RH_LLMAPI_NODE`、`SomethingToString`、`Qwen3_VQA`、`CR String To Combo`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVFirstLastFrameControl_TTP`、`CR Prompt Text`、`MuyeTextEditOutput`、`ModelScopeVisionPromptInversion_Sevr`、`ImageResizeKJv2`、`easy imageConcat`、`SaveVideo`、`LTXVAudioVAEDecode`、`VAELoaderKJ`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`LTXVCropGuides`、`ttN concat`、`CR Text Concatenate`、`easy convertAnything`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LoadImage`、`ManualSigmas`、`easy int`、`VRAMReserver`、`DualCLIPLoader`、`UNETLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
