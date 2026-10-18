---
key: 视频生成/图生视频/LTX2.3首尾帧视频【优化版】_2029932864942383106.json
name: LTX2.3首尾帧视频【优化版】_2029932864942383106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧视频【优化版】_2029932864942383106.json
hash: 69481bc18735dccf
coverage: 0.581633
learned_at: 2026-10-15 22:35:24
nodes: [CR Text, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PrimitiveInt, PIP_IntegerCalculator, Int, PIP_IntegerCalculator, GetNode, EmptyImage, Display Any (rgthree), GetImageSize, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, RandomNoise, GetNode, CFGGuider, easy cleanGpuUsed, LTXVScheduler, KSamplerSelect, SetNode, SetNode, LTXVSeparateAVLatent, GetNode, easy cleanGpuUsed, SetNode, SetNode, RandomNoise, GetNode, LTXVPreprocess, CR Text, CR Text, CR Text, CR Text, CR Text, CR Text, VAEDecodeTiled, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, SetNode, CR String To Combo, GetNode, GetNode, LTXVLatentUpsampler, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, SetNode, LTXVPreprocess, SetNode, SetNode, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, CFGGuider, CR Text, CR Prompt Text, CR Text, CR Text, CR Text, CR Text, MuyeTextEditOutput, CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, SetNode, ImageResizeKJv2, ResizeImagesByLongerEdge, GetNode, easy imageConcat, SetNode, VAEDecodeTiled, SetNode, SetNode, SetNode, Int, CR Text, CR Text, CR Text, SamplerCustomAdvanced, easy cleanGpuUsed, easy cleanGpuUsed, KSamplerSelect, LTXVCropGuides, SamplerCustomAdvanced, GetNode, GetNode, LTXVAudioVAEDecode, CheckpointLoaderSimple, easy int, CR Text, Display Any (rgthree), easy cleanGpuUsed, GetNode, easy convertAnything, GetNode, ttN concat, CR Text Concatenate, SetNode, ImpactSwitch, SetNode, easy cleanGpuUsed, LTXVConcatAVLatent, LTXVSeparateAVLatent, DualCLIPLoader, VAELoaderKJ, SetNode, SetNode, VAELoaderKJ, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, SetNode, SetNode, LTXVFirstLastFrameControl_TTP, LatentUpscaleModelLoader, ManualSigmas, LTXVAudioVAEDecode, CheckpointLoaderSimple, GetNode, GetNode, GetNode, LTX2_NAG, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, VRAMReserver, ImageResizeKJv2, Any To String (mtb), GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RH_LLMAPI_Pro_Node, ShowText|pysssss, GetNode, GetNode, Any To String (mtb), SetNode, ShowText|pysssss, llama_cpp_model_loader, LoadImage, LoadImage, CR Text, SetNode, llama_cpp_instruct_adv, CR Text, easy convertAnything, CR Text, CR Text, CR Text, easy convertAnything, CR Text, ImpactSwitch, easy convertAnything, GetNode, CreateVideo, SaveVideo, CR Text, CR Text, CR Text, ImpactSwitch, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, LTXVImgToVideoInplaceKJ, Int, LTXVFirstLastFrameControl_TTP, GetNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧视频【优化版】_2029932864942383106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2029932864942383106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（196 个）：
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
- `RandomNoise`
- `GetNode`
- `CFGGuider`
- `easy cleanGpuUsed`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR String To Combo`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `CR Text`
- `CR Prompt Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `MuyeTextEditOutput`
- `CR Text`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `easy imageConcat`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `CR Text`
- `CR Text`
- `CR Text`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `easy int`
- `CR Text`
- `Display Any (rgthree)`
- `easy cleanGpuUsed`
- `GetNode`
- `easy convertAnything`
- `GetNode`
- `ttN concat`
- `CR Text Concatenate`
- `SetNode`
- `ImpactSwitch`
- `SetNode`
- `easy cleanGpuUsed`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVFirstLastFrameControl_TTP`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VRAMReserver`
- `ImageResizeKJv2`
- `Any To String (mtb)`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `Any To String (mtb)`
- `SetNode`
- `ShowText|pysssss`
- `llama_cpp_model_loader`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `SetNode`
- `llama_cpp_instruct_adv`
- `CR Text`
- `easy convertAnything`
- `CR Text`
- `CR Text`
- `CR Text`
- `easy convertAnything`
- `CR Text`
- `ImpactSwitch`
- `easy convertAnything`
- `GetNode`
- `CreateVideo`
- `SaveVideo`
- `CR Text`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXVImgToVideoInplaceKJ`
- `Int`
- `LTXVFirstLastFrameControl_TTP`
- `GetNode`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **58%**（114/196）

**有卡**：`CR Text`、`PIP_IntegerCalculator`、`Int`、`EmptyImage`、`Display Any (rgthree)`、`GetImageSize`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`LTXVConditioning`、`RandomNoise`、`CFGGuider`、`easy cleanGpuUsed`、`LTXVScheduler`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`VAEDecodeTiled`、`VHS_VideoCombine`、`ImageScaleBy`、`CR String To Combo`、`LTXVLatentUpsampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`CR Prompt Text`、`MuyeTextEditOutput`、`ImageResizeKJv2`、`easy imageConcat`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CheckpointLoaderSimple`、`easy int`、`easy convertAnything`、`ttN concat`、`CR Text Concatenate`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LTXVFirstLastFrameControl_TTP`、`LatentUpscaleModelLoader`、`ManualSigmas`、`LTX2_NAG`、`CLIPTextEncode`、`VRAMReserver`、`Any To String (mtb)`、`EmptyLTXVLatentVideo`、`RH_LLMAPI_Pro_Node`、`llama_cpp_model_loader`、`LoadImage`、`llama_cpp_instruct_adv`、`CreateVideo`、`SaveVideo`、`LoraLoaderModelOnly`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
