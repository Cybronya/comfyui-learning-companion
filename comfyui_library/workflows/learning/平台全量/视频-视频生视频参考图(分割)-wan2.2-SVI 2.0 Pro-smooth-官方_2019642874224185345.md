---
key: 平台全量/视频-视频生视频参考图(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019642874224185345.json
name: 视频-视频生视频参考图(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019642874224185345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频生视频参考图(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019642874224185345.json
hash: 97c5ca458d71f927
coverage: 0.640244
learned_at: 2026-11-14 02:34:39
nodes: [PreviewImage, ImageFromBatch, SetNode, GetNode, LoraLoaderModelOnly, CLIPTextEncode, VAEEncode, VAELoader, INTConstant, INTConstant, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, GetImageSizeAndCount, CreateVideo, SetNode, MathExpression|pysssss, VHS_VideoInfoLoaded, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetImageSizeAndCount, ShowText|pysssss, AILab_MiniCPM_4_V, ShowText|pysssss, ShowText|pysssss, GetNode, easy promptReplace, easy seed, DiffusionModelLoaderKJ, easy positive, Florence2ModelLoader, Florence2Run, easy showAnything, Int, GetImageSizeAndCount, Reroute, GetImageSizeAndCount, GetNode, GetNode, KSamplerSelect, CFGGuider, CLIPTextEncode, UNETLoader, CLIPTextEncode, ReferenceLatent, CLIPLoader, Reroute, VAEEncode, EmptyFlux2LatentImage, Reroute, Reroute, ReferenceLatent, RandomNoise, GetNode, ImpactFloat, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, MemoryCleaner, GetNode, SamplerCustomAdvanced, Reroute, Reroute, PreviewImage, SetNode, GetNode, PreviewImage, GetNode, CLIPTextEncode, CLIPLoader, Reroute, easy showAnything, easy imageSize, SetNode, easy mathInt, GetImageSizeAndCount, Reroute, ImageResizeKJv2, Reroute, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, PreviewImage, SetNode, easy showAnything, GetNode, GetNode, VHS_VideoInfoLoaded, CR String To Number, ImageFromBatch+, Text List to Text, AnyBatchSliceNode, easy showAnything, Float, FL_VideoCadence, easy lengthAnything, easy showAnything, GODMT_ListToBatch, TextSplitByDelimiter, easy showAnything, easy showAnything, VHS_LoadVideo, VAEDecode, VHS_VideoCombine, GetNode, VAEDecodeTiled, MemoryCleaner, GetImageSizeAndCount, DiffusionModelLoaderKJ, VHS_VideoCombine, ImageConcanate, easy showAnything, WanImageToVideoSVIPro, RH_Captioner, easy showAnything, MemoryCleaner, CM_IntToBool, easy showAnything, Switch any [Crystools], GetImageSizeAndCount, SegmentFrameAdjuster, GetNode, Flux2Scheduler, CR Float To Integer, easy showAnything, CM_IntUnaryOperation, easy batchAnything, ImageToDevice+, SetNode, easy imageRemBg, PreviewImage, easy forLoopEnd, easy forLoopStart, GetImageSizeAndCount, GetImageSizeAndCount, ImageConcanate, SetNode, AutoCropFaces, StringFunction|pysssss, GetNode, Reroute, VAELoader, StringFunction|pysssss, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, GetNode, ImageFromBatch+, GetNode, ImageFromBatch+, VHS_LoadVideo, LoadImage, easy int, PrimitiveFloat, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, PreviewImage, SaveImage, SetNode, easy saveText]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/视频-视频生视频参考图(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019642874224185345.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频生视频参考图(分割)-wan2.2-SVI 2.0 Pro-smooth-官方_2019642874224185345.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（164 个）：
- `PreviewImage`
- `ImageFromBatch`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `GetImageSizeAndCount`
- `CreateVideo`
- `SetNode`
- `MathExpression|pysssss`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetImageSizeAndCount`
- `ShowText|pysssss`
- `AILab_MiniCPM_4_V`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `GetNode`
- `easy promptReplace`
- `easy seed`
- `DiffusionModelLoaderKJ`
- `easy positive`
- `Florence2ModelLoader`
- `Florence2Run`
- `easy showAnything`
- `Int`
- `GetImageSizeAndCount`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CLIPLoader`
- `Reroute`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `Reroute`
- `Reroute`
- `ReferenceLatent`
- `RandomNoise`
- `GetNode`
- `ImpactFloat`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `MemoryCleaner`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Reroute`
- `easy showAnything`
- `easy imageSize`
- `SetNode`
- `easy mathInt`
- `GetImageSizeAndCount`
- `Reroute`
- `ImageResizeKJv2`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `VHS_VideoInfoLoaded`
- `CR String To Number`
- `ImageFromBatch+`
- `Text List to Text`
- `AnyBatchSliceNode`
- `easy showAnything`
- `Float`
- `FL_VideoCadence`
- `easy lengthAnything`
- `easy showAnything`
- `GODMT_ListToBatch`
- `TextSplitByDelimiter`
- `easy showAnything`
- `easy showAnything`
- `VHS_LoadVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `MemoryCleaner`
- `GetImageSizeAndCount`
- `DiffusionModelLoaderKJ`
- `VHS_VideoCombine`
- `ImageConcanate`
- `easy showAnything`
- `WanImageToVideoSVIPro`
- `RH_Captioner`
- `easy showAnything`
- `MemoryCleaner`
- `CM_IntToBool`
- `easy showAnything`
- `Switch any [Crystools]`
- `GetImageSizeAndCount`
- `SegmentFrameAdjuster`
- `GetNode`
- `Flux2Scheduler`
- `CR Float To Integer`
- `easy showAnything`
- `CM_IntUnaryOperation`
- `easy batchAnything`
- `ImageToDevice+`
- `SetNode`
- `easy imageRemBg`
- `PreviewImage`
- `easy forLoopEnd`
- `easy forLoopStart`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `SetNode`
- `AutoCropFaces`
- `StringFunction|pysssss`
- `GetNode`
- `Reroute`
- `VAELoader`
- `StringFunction|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `ImageFromBatch+`
- `GetNode`
- `ImageFromBatch+`
- `VHS_LoadVideo`
- `LoadImage`
- `easy int`
- `PrimitiveFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `easy saveText`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **64%**（105/164）

**有卡**：`ImageFromBatch`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEEncode`、`VAELoader`、`INTConstant`、`KSamplerAdvanced`、`GetImageSizeAndCount`、`CreateVideo`、`MathExpression|pysssss`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_MiniCPM_4_V`、`easy promptReplace`、`easy seed`、`DiffusionModelLoaderKJ`、`easy positive`、`Florence2ModelLoader`、`Florence2Run`、`Int`、`KSamplerSelect`、`CFGGuider`、`UNETLoader`、`ReferenceLatent`、`CLIPLoader`、`EmptyFlux2LatentImage`、`RandomNoise`、`ImpactFloat`、`MemoryCleaner`、`SamplerCustomAdvanced`、`easy imageSize`、`easy mathInt`、`ImageResizeKJv2`、`CR String To Number`、`ImageFromBatch+`、`Text List to Text`、`AnyBatchSliceNode`、`Float`、`FL_VideoCadence`、`easy lengthAnything`、`GODMT_ListToBatch`、`TextSplitByDelimiter`、`VHS_LoadVideo`、`VAEDecode`、`VHS_VideoCombine`、`VAEDecodeTiled`、`ImageConcanate`、`WanImageToVideoSVIPro`、`RH_Captioner`、`CM_IntToBool`、`Switch any [Crystools]`、`SegmentFrameAdjuster`、`Flux2Scheduler`、`CR Float To Integer`、`CM_IntUnaryOperation`、`easy batchAnything`、`ImageToDevice+`、`easy imageRemBg`、`easy forLoopEnd`、`easy forLoopStart`、`AutoCropFaces`、`StringFunction|pysssss`、`LoadImage`、`easy int`、`SaveImage`、`easy saveText`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage
