---
key: 图片生成/文生图/🈚️Flux.1 反推+文_图生图+redux_cn参考+局部修脸+ttp放大_1934392733874479105.json
name: 🈚️Flux.1 反推+文_图生图+redux_cn参考+局部修脸+ttp放大_1934392733874479105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/🈚️Flux.1 反推+文_图生图+redux_cn参考+局部修脸+ttp放大_1934392733874479105.json
hash: b6a84278d4eb9bca
coverage: 0.440329
learned_at: 2026-10-15 22:29:11
nodes: [BasicGuider, BasicGuider, SetNode, SetNode, KSamplerSelect, BasicGuider, RandomNoise, VAEEncode, BasicScheduler, SetNode, GetNode, GetNode, ModelSamplingFlux, GetNode, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, VAELoader, Anything Everywhere, FluxGuidance, ConditioningZeroOut, FaceSegmentation, MaskToSEGS, VAEDecodeTiled, easy imageListToImageBatch, PreviewImage, AIO_Preprocessor, AIO_Preprocessor, SetNode, PreviewImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, SamplerCustomAdvanced, VAEDecode, Fast Groups Bypasser (rgthree), VAEEncode, GetNode, GetNode, SetNode, RebatchLatents, RepeatLatentBatch, InjectLatentNoise+, GetNode, SetNode, SetNode, SetNode, NunchakuFluxDiTLoader, Reroute, ControlNetLoader, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Any Switch (rgthree), GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), Reroute, ImageUpscaleWithModel, TTP_Tile_image_size, ImageScaleToTotalPixels, SamplerCustomAdvanced, FaceAnalysisModels, SetNode, Any Switch (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy cleanGpuUsed, SetNode, GetNode, LayerUtility: TextJoin, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, Int, SimpleMathSlider+, FluxGuidance, PreviewImage, PreviewImage, GetNode, SetNode, UpscaleModelLoader, ImageResizeKJ, GetNode, SetNode, ImageFromBatch+, easy imageCount, Text, Display Any (rgthree), GetNode, Any Switch (rgthree), TTP_Image_Assy, TTP_Image_Tile_Batch, PreviewImage, easy imageBatchToImageList, easy forLoopEnd, ImageListToBatch+, easy forLoopStart, ImageFromBatch, Text, RH_Translator, ApplySageAttention, easy batchAnything, DualCLIPLoader, SetNode, GetNode, GetNode, CLIPTextEncode, BasicScheduler, BasicScheduler, FluxGuidance, FluxGuidance, PreviewImage, PreviewImage, SaveImage, Fast Groups Bypasser (rgthree), SetNode, CLIPVisionLoader, StyleModelLoader, SetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ControlNetApplySD3, SetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SetUnionControlNetType, Reroute, SetNode, CLIPTextEncode, ConditioningZeroOut, SetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy int, PreviewImage, GetNode, PreviewImage, LoadImage, SetNode, LoadImage, SetNode, Fast Groups Bypasser (rgthree), Reroute, Anything Everywhere, ModelSamplingFlux, GetNode, GetNode, SetNode, ModelSamplingFlux, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, GetNode, GetNode, GetNode, EasyCache, RandomNoise, GetNode, SetNode, GetNode, GetNode, RandomNoise, DetailerForEachDebug, InjectLatentNoise+, SetNode, ControlNetApplySD3, Fast Groups Bypasser (rgthree), easy seed, LoraLoaderModelOnly, GetNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Any Switch (rgthree), SaveImage, SamplerCustomAdvanced, VAEDecode, GetNode, GetNode, ImageSmartSharpen+, GetNode, LatentPixelScale, GetNode, UpscaleModelLoader, Any Switch (rgthree), GetNode, Reroute, Any Switch (rgthree), GetNode, Float, SimpleMathSlider+, Bjornulf_ShowStringText, PreviewAny, AILab_QwenVL, GetNode, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, Fast Groups Bypasser (rgthree), ImpactSwitch, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ReduxAdvanced, ReduxAdvanced, SaveImage, SaveImage, Note, KSamplerSelect, DetailDaemonSamplerNode, KSamplerSelect, DetailDaemonSamplerNode, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.8000000000000002}
---

# 图片生成/文生图/🈚️Flux.1 反推+文_图生图+redux_cn参考+局部修脸+ttp放大_1934392733874479105.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/🈚️Flux.1 反推+文_图生图+redux_cn参考+局部修脸+ttp放大_1934392733874479105.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（243 个）：
- `BasicGuider`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `VAEEncode` ★核心
- `BasicScheduler`
- `SetNode`
- `GetNode`
- `GetNode`
- `ModelSamplingFlux`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `Anything Everywhere`
- `FluxGuidance`
- `ConditioningZeroOut`
- `FaceSegmentation`
- `MaskToSEGS`
- `VAEDecodeTiled` ★核心
- `easy imageListToImageBatch`
- `PreviewImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `RebatchLatents`
- `RepeatLatentBatch`
- `InjectLatentNoise+`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `NunchakuFluxDiTLoader`
- `Reroute`
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Reroute`
- `ImageUpscaleWithModel`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `SamplerCustomAdvanced` ★核心
- `FaceAnalysisModels`
- `SetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `LayerUtility: TextJoin`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Int`
- `SimpleMathSlider+`
- `FluxGuidance`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `UpscaleModelLoader`
- `ImageResizeKJ`
- `GetNode`
- `SetNode`
- `ImageFromBatch+`
- `easy imageCount`
- `Text`
- `Display Any (rgthree)`
- `GetNode`
- `Any Switch (rgthree)`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `PreviewImage`
- `easy imageBatchToImageList`
- `easy forLoopEnd`
- `ImageListToBatch+`
- `easy forLoopStart`
- `ImageFromBatch`
- `Text`
- `RH_Translator`
- `ApplySageAttention`
- `easy batchAnything`
- `DualCLIPLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `BasicScheduler`
- `FluxGuidance`
- `FluxGuidance`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ControlNetApplySD3` ★核心
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SetUnionControlNetType`
- `Reroute`
- `SetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `easy int`
- `PreviewImage`
- `GetNode`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `Anything Everywhere`
- `ModelSamplingFlux`
- `GetNode`
- `GetNode`
- `SetNode`
- `ModelSamplingFlux`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `EasyCache`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `DetailerForEachDebug`
- `InjectLatentNoise+`
- `SetNode`
- `ControlNetApplySD3` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy seed`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ImageSmartSharpen+`
- `GetNode`
- `LatentPixelScale`
- `GetNode`
- `UpscaleModelLoader`
- `Any Switch (rgthree)`
- `GetNode`
- `Reroute`
- `Any Switch (rgthree)`
- `GetNode`
- `Float`
- `SimpleMathSlider+`
- `Bjornulf_ShowStringText`
- `PreviewAny`
- `AILab_QwenVL`
- `GetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ReduxAdvanced`
- `ReduxAdvanced`
- `SaveImage`
- `SaveImage`
- `Note`
- `KSamplerSelect` ★核心
- `DetailDaemonSamplerNode` ★核心
- `KSamplerSelect` ★核心
- `DetailDaemonSamplerNode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **44%**（107/243）

**有卡**：`BasicGuider`、`KSamplerSelect`、`RandomNoise`、`VAEEncode`、`BasicScheduler`、`ModelSamplingFlux`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`FluxGuidance`、`ConditioningZeroOut`、`FaceSegmentation`、`MaskToSEGS`、`VAEDecodeTiled`、`easy imageListToImageBatch`、`AIO_Preprocessor`、`SamplerCustomAdvanced`、`VAEDecode`、`RebatchLatents`、`RepeatLatentBatch`、`InjectLatentNoise+`、`NunchakuFluxDiTLoader`、`ControlNetLoader`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`FaceAnalysisModels`、`LayerUtility: TextJoin`、`Int`、`SimpleMathSlider+`、`UpscaleModelLoader`、`ImageResizeKJ`、`ImageFromBatch+`、`easy imageCount`、`Text`、`Display Any (rgthree)`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`easy forLoopEnd`、`ImageListToBatch+`、`easy forLoopStart`、`ImageFromBatch`、`RH_Translator`、`ApplySageAttention`、`easy batchAnything`、`DualCLIPLoader`、`CLIPTextEncode`、`SaveImage`、`CLIPVisionLoader`、`StyleModelLoader`、`ControlNetApplySD3`、`SetUnionControlNetType`、`easy int`、`LoadImage`、`UNETLoader`、`EasyCache`、`DetailerForEachDebug`、`easy seed`、`ImageSmartSharpen+`、`LatentPixelScale`、`Float`、`Bjornulf_ShowStringText`、`AILab_QwenVL`、`ReduxAdvanced`、`DetailDaemonSamplerNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
