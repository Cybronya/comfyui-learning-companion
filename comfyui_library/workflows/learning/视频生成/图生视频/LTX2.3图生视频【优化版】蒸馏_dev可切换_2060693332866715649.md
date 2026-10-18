---
key: 视频生成/图生视频/LTX2.3图生视频【优化版】蒸馏_dev可切换_2060693332866715649.json
name: LTX2.3图生视频【优化版】蒸馏_dev可切换_2060693332866715649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频【优化版】蒸馏_dev可切换_2060693332866715649.json
hash: a737b330040877e6
coverage: 0.597315
learned_at: 2026-10-15 22:38:49
nodes: [SetNode, SetNode, SetNode, CR Text, GetNode, GetNode, GetNode, EmptyImage, LTXVConcatAVLatent, GetNode, GetNode, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, SetNode, LayerUtility: ImageScaleByAspectRatio V2, CR Text, CR Text, SetNode, EmptyLTXVLatentVideo, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, SetNode, CR Text, easy cleanGpuUsed, easy cleanGpuUsed, CR Text, CR Text, SetNode, GetNode, RandomNoise, GetNode, CR Text, SetNode, easy cleanGpuUsed, Any To String (mtb), GetNode, GetNode, SetNode, PrimitiveInt, Int, GetNode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, CR Text, Display Any (rgthree), easy convertAnything, SetNode, SetNode, easy cleanGpuUsed, LTXVSeparateAVLatent, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, CR Text, EmptyImage, GetImageSize, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, CR Text, CR Text, GetNode, GetNode, ImageScaleBy, SetNode, GetNode, SetNode, CR Text, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CR Text, CR Text, CLIPTextEncode, GetNode, LTXVCropGuides, easy cleanGpuUsed, LTXVLatentUpsampler, CR Text, CR Text, SetNode, PrimitiveInt, GetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, GetNode, GetNode, RandomNoise, LTXVSeparateAVLatent, CR Text, easy cleanGpuUsed, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any To String (mtb), SetNode, GetNode, CR Text, ImpactSwitch, SetNode, GetNode, CR Text, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, SetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ManualSigmas, GetNode, CFGGuider, GetNode, CLIPTextEncode, GetNode, GetNode, llama_cpp_instruct_adv, ManualSigmas, CR Text, easy boolean, CR Text, ImpactSwitch, CR Text, easy boolean, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, KSamplerSelect, ManualSigmas, SetNode, SetNode, CLIPTextEncode, CR Text, LTX2_NAG, llama_cpp_model_loader, ManualSigmas, GetNode, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, GetNode, easy convertAnything, ttN concat, CR Text Concatenate, SetNode, SetNode, SetNode, CR Text, CR Text, CR Text, Any To String (mtb), Any To String (mtb), Any To String (mtb), Any To String (mtb), CR Text, CR Text, SetNode, SetNode, SetNode, GetNode, LoraLoaderModelOnly, CR String To Combo, Any To String (mtb), VAEDecodeTiled, GetNode, easy boolean, CR Text, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, VRAMReserver, LoraLoaderModelOnly, Switch any [Crystools], LTXVScheduler, CFGGuider, RandomNoise, CR Text, CR Text, LoraLoaderModelOnly, LTX2_NAG, CFGGuider, RTXVideoSuperResolution, CreateVideo, SaveVideo, KSamplerSelect, ManualSigmas, CR String To Combo, easy cleanGpuUsed, CFGGuider, LTXVLatentUpsampler, CR Text, CR Value, LTXVCropGuides, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, SetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, KSamplerSelect, LoraLoaderModelOnly, Int, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVAudioVAEDecode, LTXVPreprocess, ManualSigmas, LTXVImgToVideoInplace, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, UNETLoader, ManualSigmas, LTXVImgToVideoInplace, CheckpointLoaderSimple, KSamplerSelect, MathExpression|pysssss, GetImageSize, GetNode, LTXVConcatAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ResizeImagesByLongerEdge, CR Text, ImpactSwitch, VHS_VideoCombine, LTXVScheduler, Fast Groups Muter (rgthree), SetNode, LoraLoaderModelOnly, Switch any [Crystools], LoraLoaderModelOnly, LTXVChunkFeedForward, GetNode, VRAMReserver, ImpactSwitch, CreateVideo, RTXVideoSuperResolution, CR Text, LTXVChunkFeedForward, easy int, GetNode, VAEDecodeTiled, ShowText|pysssss, VAEDecodeTiled, SaveVideo, LoraLoaderModelOnly, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, ManualSigmas, ManualSigmas, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3图生视频【优化版】蒸馏_dev可切换_2060693332866715649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060693332866715649.json`

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
- `SetNode`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `Int`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `Display Any (rgthree)`
- `easy convertAnything`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `easy cleanGpuUsed`
- `CR Text`
- `CR Text`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `GetNode`
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
- `CR Text`
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
- `easy boolean`
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
- `SetNode`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `CR String To Combo`
- `Any To String (mtb)`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `easy boolean`
- `CR Text`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `Switch any [Crystools]`
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
- `LoraLoaderModelOnly` ★核心
- `Int`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `ManualSigmas`
- `LTXVImgToVideoInplace`
- `LoraLoaderModelOnly` ★核心
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
- `Fast Groups Muter (rgthree)`
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
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-fp8.safetensors`

## 知识

覆盖率 **60%**（178/298）

**有卡**：`CR Text`、`EmptyImage`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`LTXVConditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`RandomNoise`、`Any To String (mtb)`、`Int`、`LTXVEmptyLatentAudio`、`Display Any (rgthree)`、`easy convertAnything`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`GetImageSize`、`CLIPTextEncode`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`MathExpression|pysssss`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`ManualSigmas`、`CFGGuider`、`llama_cpp_instruct_adv`、`easy boolean`、`KSamplerSelect`、`LTX2_NAG`、`llama_cpp_model_loader`、`LTXVImgToVideoInplace`、`ttN concat`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`CR String To Combo`、`VAEDecodeTiled`、`VAELoaderKJ`、`DualCLIPLoader`、`VRAMReserver`、`Switch any [Crystools]`、`LTXVScheduler`、`RTXVideoSuperResolution`、`CreateVideo`、`SaveVideo`、`CR Value`、`LTXVPreprocess`、`UNETLoader`、`ResizeImagesByLongerEdge`、`VHS_VideoCombine`、`LTXVChunkFeedForward`、`easy int`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
