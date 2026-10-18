---
key: 视频生成/图生视频/LTX2.3图生视频【优化版】蒸馏_dev可切换_2057424859017334786.json
name: LTX2.3图生视频【优化版】蒸馏_dev可切换_2057424859017334786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频【优化版】蒸馏_dev可切换_2057424859017334786.json
hash: 100af177678d8cbb
coverage: 0.597315
learned_at: 2026-10-15 22:38:12
nodes: [SetNode, SetNode, SetNode, CR Text, GetNode, GetNode, GetNode, EmptyImage, LTXVConcatAVLatent, GetNode, GetNode, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, SetNode, LayerUtility: ImageScaleByAspectRatio V2, CR Text, CR Text, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, SetNode, CR Text, easy cleanGpuUsed, easy cleanGpuUsed, CR Text, CR Text, SetNode, GetNode, RandomNoise, GetNode, CR Text, easy cleanGpuUsed, Any To String (mtb), GetNode, GetNode, SetNode, PrimitiveInt, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, easy convertAnything, easy cleanGpuUsed, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, CR Text, EmptyImage, GetImageSize, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, easy cleanGpuUsed, CR Text, CR Text, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, CR Text, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CR Text, CR Text, CLIPTextEncode, GetNode, LTXVCropGuides, easy cleanGpuUsed, LTXVLatentUpsampler, CR Text, CR Text, SetNode, PrimitiveInt, GetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, GetNode, GetNode, RandomNoise, LTXVSeparateAVLatent, CR Text, easy cleanGpuUsed, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any To String (mtb), SetNode, GetNode, ImpactSwitch, SetNode, GetNode, CR Text, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ManualSigmas, GetNode, CFGGuider, GetNode, CLIPTextEncode, GetNode, GetNode, llama_cpp_instruct_adv, ManualSigmas, CR Text, CR Text, ImpactSwitch, CR Text, easy boolean, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, KSamplerSelect, ManualSigmas, SetNode, SetNode, CLIPTextEncode, CR Text, LTX2_NAG, llama_cpp_model_loader, ManualSigmas, GetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, easy convertAnything, ttN concat, CR Text Concatenate, SetNode, SetNode, CR Text, CR Text, CR Text, Any To String (mtb), Any To String (mtb), Any To String (mtb), Any To String (mtb), CR Text, CR Text, SetNode, GetNode, LoraLoaderModelOnly, CR String To Combo, Any To String (mtb), VAEDecodeTiled, GetNode, easy boolean, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, VRAMReserver, LoraLoaderModelOnly, LTXVScheduler, CFGGuider, RandomNoise, CR Text, CR Text, LoraLoaderModelOnly, LTX2_NAG, CFGGuider, RTXVideoSuperResolution, CreateVideo, SaveVideo, KSamplerSelect, ManualSigmas, CR String To Combo, easy cleanGpuUsed, CFGGuider, LTXVLatentUpsampler, CR Value, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, KSamplerSelect, Int, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVAudioVAEDecode, LTXVPreprocess, ManualSigmas, LTXVImgToVideoInplace, LTXVAudioVAELoader, LTXAVTextEncoderLoader, UNETLoader, ManualSigmas, LTXVImgToVideoInplace, CheckpointLoaderSimple, KSamplerSelect, MathExpression|pysssss, GetImageSize, GetNode, LTXVConcatAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ResizeImagesByLongerEdge, CR Text, ImpactSwitch, VHS_VideoCombine, LTXVScheduler, LoadImage, SetNode, LoraLoaderModelOnly, Switch any [Crystools], LoraLoaderModelOnly, LTXVChunkFeedForward, GetNode, VRAMReserver, ImpactSwitch, CreateVideo, RTXVideoSuperResolution, CR Text, LTXVChunkFeedForward, easy int, GetNode, VAEDecodeTiled, ShowText|pysssss, VAEDecodeTiled, SaveVideo, LoraLoaderModelOnly, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, ManualSigmas, ManualSigmas, CR Text, CR Text, SetNode, LoadImage, CR Text, GetNode, GetNode, easy boolean, Switch any [Crystools], LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SetNode, Fast Groups Muter (rgthree), SetNode, Int, SetNode, SetNode, Display Any (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3图生视频【优化版】蒸馏_dev可切换_2057424859017334786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057424859017334786.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（298 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
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
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `CR Text`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CR Text`
- `CR Text`
- `SetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `CR Text`
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
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `EmptyImage`
- `GetImageSize`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `CR Text`
- `CR Text`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `CR Text`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Text`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVCropGuides`
- `easy cleanGpuUsed`
- `LTXVLatentUpsampler` ★核心
- `CR Text`
- `CR Text`
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `CR Text`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any To String (mtb)`
- `SetNode`
- `GetNode`
- `ImpactSwitch`
- `SetNode`
- `GetNode`
- `CR Text`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `llama_cpp_instruct_adv`
- `ManualSigmas`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `CR Text`
- `easy boolean`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CR Text`
- `LTX2_NAG`
- `llama_cpp_model_loader`
- `ManualSigmas`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy convertAnything`
- `ttN concat`
- `CR Text Concatenate`
- `SetNode`
- `SetNode`
- `CR Text`
- `CR Text`
- `CR Text`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `CR Text`
- `CR Text`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `CR String To Combo`
- `Any To String (mtb)`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `easy boolean`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `CFGGuider`
- `RandomNoise`
- `CR Text`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `CFGGuider`
- `RTXVideoSuperResolution`
- `CreateVideo`
- `SaveVideo`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CR String To Combo`
- `easy cleanGpuUsed`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
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
- `Int`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `UNETLoader` ★核心
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `CheckpointLoaderSimple` ★核心
- `KSamplerSelect` ★核心
- `MathExpression|pysssss`
- `GetImageSize`
- `GetNode`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `CR Text`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `LTXVScheduler`
- `LoadImage`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `LTXVChunkFeedForward`
- `GetNode`
- `VRAMReserver`
- `ImpactSwitch`
- `CreateVideo`
- `RTXVideoSuperResolution`
- `CR Text`
- `LTXVChunkFeedForward`
- `easy int`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ShowText|pysssss`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `ManualSigmas`
- `CR Text`
- `CR Text`
- `SetNode`
- `LoadImage`
- `CR Text`
- `GetNode`
- `GetNode`
- `easy boolean`
- `Switch any [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `Display Any (rgthree)`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **60%**（178/298）

**有卡**：`CR Text`、`EmptyImage`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`LTXVConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`RandomNoise`、`Any To String (mtb)`、`LTXVEmptyLatentAudio`、`easy convertAnything`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`GetImageSize`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`MathExpression|pysssss`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`CFGGuider`、`llama_cpp_instruct_adv`、`easy boolean`、`KSamplerSelect`、`LTX2_NAG`、`llama_cpp_model_loader`、`LTXVImgToVideoInplace`、`ttN concat`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`CR String To Combo`、`VAEDecodeTiled`、`VAELoaderKJ`、`DualCLIPLoader`、`VRAMReserver`、`LTXVScheduler`、`RTXVideoSuperResolution`、`CreateVideo`、`SaveVideo`、`CR Value`、`Int`、`LTXVPreprocess`、`UNETLoader`、`ResizeImagesByLongerEdge`、`VHS_VideoCombine`、`LoadImage`、`Switch any [Crystools]`、`LTXVChunkFeedForward`、`easy int`、`Display Any (rgthree)`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
