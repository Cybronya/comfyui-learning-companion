---
key: 视频生成/图生视频/LTX2.3图生视频【优化版】切镜头产品口播_2058353502581252098.json
name: LTX2.3图生视频【优化版】切镜头产品口播_2058353502581252098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058353502581252098.json
hash: c4d267a22b56b12f
coverage: 0.557576
learned_at: 2026-10-15 22:38:21
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyImage, LTXVConcatAVLatent, GetNode, GetNode, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, easy cleanGpuUsed, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, GetNode, RandomNoise, SetNode, easy cleanGpuUsed, Any To String (mtb), GetNode, GetNode, SetNode, PrimitiveInt, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, easy convertAnything, easy cleanGpuUsed, LTXVSeparateAVLatent, CR Text, SetNode, SetNode, GetNode, CFGGuider, GetNode, llama_cpp_instruct_adv, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ManualSigmas, SetNode, SetNode, llama_cpp_model_loader, GetNode, GetNode, GetNode, GetNode, easy convertAnything, ttN concat, CR Text Concatenate, SetNode, SetNode, easy boolean, CR Text, easy cleanGpuUsed, CFGGuider, LTXVLatentUpsampler, CR Text, CR Value, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, KSamplerSelect, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVAudioVAEDecode, LTXVPreprocess, ManualSigmas, LTXVImgToVideoInplace, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ManualSigmas, KSamplerSelect, MathExpression|pysssss, GetImageSize, GetNode, ResizeImagesByLongerEdge, Fast Groups Muter (rgthree), VRAMReserver, CreateVideo, RTXVideoSuperResolution, GetNode, VAEDecodeTiled, VAEDecodeTiled, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, ManualSigmas, VAELoaderKJ, VAELoaderKJ, LTX2_NAG, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, BasicScheduler, ManualSigmas, ManualSigmas, LTXVScheduler, UNETLoader, CheckpointLoaderSimple, DualCLIPLoader, Any To String (mtb), SetNode, LoraLoaderModelOnly, SetNode, BasicScheduler, LoraLoaderModelOnly, SetNode, LTXICLoRALoaderModelOnly, GetNode, LTXVChunkFeedForward, CR Text, SetNode, CR Text, SetNode, SaveVideo, SetNode, easy int, VHS_VideoCombine, CR Text, GetNode, Display Any (rgthree), SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LatentUpscaleModelLoader, LoraLoaderModelOnly, Int, SetNode, ShowText|pysssss, ImpactSwitch, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, GetNode, CR Text, Int, CR Text, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3图生视频【优化版】切镜头产品口播_2058353502581252098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058353502581252098.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（165 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `RandomNoise`
- `SetNode`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `CR Text`
- `SetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `llama_cpp_model_loader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `ttN concat`
- `CR Text Concatenate`
- `SetNode`
- `SetNode`
- `easy boolean`
- `CR Text`
- `easy cleanGpuUsed`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `CR Text`
- `CR Value`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `MathExpression|pysssss`
- `GetImageSize`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `Fast Groups Muter (rgthree)`
- `VRAMReserver`
- `CreateVideo`
- `RTXVideoSuperResolution`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `BasicScheduler`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVScheduler`
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `DualCLIPLoader`
- `Any To String (mtb)`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `GetNode`
- `LTXVChunkFeedForward`
- `CR Text`
- `SetNode`
- `CR Text`
- `SetNode`
- `SaveVideo`
- `SetNode`
- `easy int`
- `VHS_VideoCombine`
- `CR Text`
- `GetNode`
- `Display Any (rgthree)`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `SetNode`
- `ShowText|pysssss`
- `ImpactSwitch`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `CR Text`
- `Int`
- `CR Text`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **56%**（92/165）

**有卡**：`EmptyImage`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`RandomNoise`、`Any To String (mtb)`、`LTXVEmptyLatentAudio`、`easy convertAnything`、`LTXVSeparateAVLatent`、`CR Text`、`CFGGuider`、`llama_cpp_instruct_adv`、`ManualSigmas`、`llama_cpp_model_loader`、`ttN concat`、`CR Text Concatenate`、`easy boolean`、`LTXVLatentUpsampler`、`CR Value`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`MathExpression|pysssss`、`GetImageSize`、`ResizeImagesByLongerEdge`、`VRAMReserver`、`CreateVideo`、`RTXVideoSuperResolution`、`VAEDecodeTiled`、`VAELoaderKJ`、`LTX2_NAG`、`BasicScheduler`、`LTXVScheduler`、`UNETLoader`、`CheckpointLoaderSimple`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`LTXVChunkFeedForward`、`SaveVideo`、`easy int`、`VHS_VideoCombine`、`Display Any (rgthree)`、`LatentUpscaleModelLoader`、`Int`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
