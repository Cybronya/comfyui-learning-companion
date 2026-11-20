---
key: 平台全量/视频-视频生视频-wan2.2-SVI 2.0 Pro-smooth-官方_2018179536462024706.json
name: 视频-视频生视频-wan2.2-SVI 2.0 Pro-smooth-官方_2018179536462024706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频生视频-wan2.2-SVI 2.0 Pro-smooth-官方_2018179536462024706.json
hash: 4189c6ca3bfdb250
coverage: 0.675926
learned_at: 2026-11-14 02:34:36
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, GetNode, GetNode, PreviewImage, ImageFromBatch, GetImageSizeAndCount, SetNode, CLIPLoader, SetNode, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, LoraLoaderModelOnly, DiffusionModelLoaderKJ, CLIPTextEncode, CLIPTextEncode, Reroute, VAEEncode, GetImageSizeAndCount, VAELoader, VHS_VideoCombine, INTConstant, INTConstant, WanImageToVideoSVIPro, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, GetImageSizeAndCount, CreateVideo, ImpactInt, ImpactInt, CLIPLoader, SaveImage, ImpactFloat, SetNode, SetNode, MathExpression|pysssss, MemoryCleaner, VAEDecode, PreviewImage, VHS_VideoInfoLoaded, GetNode, SetNode, ImageResizeKJv2, StringFunction|pysssss, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, HunyuanVideoFoley, PreviewAudio, VAEDecodeTiled, GetImageSizeAndCount, SetNode, ImageConcanate, VHS_VideoCombine, VHS_LoadVideo, easy showAnything, GetNode, GetImageSizeAndCount, ShowText|pysssss, GetImageSizeAndCount, AILab_MiniCPM_4_V, MemoryCleaner, MemoryCleaner, ShowText|pysssss, easy saveText, SetNode, ShowText|pysssss, GetNode, easy promptReplace, easy int, easy seed, EmptyLatentImage, VAELoader, DiffusionModelLoaderKJ, AIO_Preprocessor, ImageFromBatch+, ModelPatchLoader, GetImageSizeAndCount, easy positive, ImageFromBatch+, Florence2ModelLoader, Florence2Run, GetNode, ConditioningZeroOut, CLIPTextEncode, KSamplerAdvanced, KSamplerAdvanced, INTConstant, GetNode, ZImageFunControlnet, UNETLoader, INTConstant, RH_Captioner, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveFloat, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1080, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1920}
---

# 平台全量/视频-视频生视频-wan2.2-SVI 2.0 Pro-smooth-官方_2018179536462024706.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频生视频-wan2.2-SVI 2.0 Pro-smooth-官方_2018179536462024706.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（108 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `VAEEncode` ★核心
- `GetImageSizeAndCount`
- `VAELoader`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `WanImageToVideoSVIPro`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `GetImageSizeAndCount`
- `CreateVideo`
- `ImpactInt`
- `ImpactInt`
- `CLIPLoader`
- `SaveImage`
- `ImpactFloat`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `VAEDecode` ★核心
- `PreviewImage`
- `VHS_VideoInfoLoaded`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `StringFunction|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `HunyuanVideoFoley`
- `PreviewAudio`
- `VAEDecodeTiled` ★核心
- `GetImageSizeAndCount`
- `SetNode`
- `ImageConcanate`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `easy showAnything`
- `GetNode`
- `GetImageSizeAndCount`
- `ShowText|pysssss`
- `GetImageSizeAndCount`
- `AILab_MiniCPM_4_V`
- `MemoryCleaner`
- `MemoryCleaner`
- `ShowText|pysssss`
- `easy saveText`
- `SetNode`
- `ShowText|pysssss`
- `GetNode`
- `easy promptReplace`
- `easy int`
- `easy seed`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `DiffusionModelLoaderKJ`
- `AIO_Preprocessor`
- `ImageFromBatch+`
- `ModelPatchLoader`
- `GetImageSizeAndCount`
- `easy positive`
- `ImageFromBatch+`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetNode`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `GetNode`
- `ZImageFunControlnet`
- `UNETLoader` ★核心
- `INTConstant`
- `RH_Captioner`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveFloat`
- `PreviewImage`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **68%**（73/108）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`ImageFromBatch`、`CLIPLoader`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`VAEEncode`、`VAELoader`、`VHS_VideoCombine`、`INTConstant`、`WanImageToVideoSVIPro`、`KSamplerAdvanced`、`CreateVideo`、`ImpactInt`、`SaveImage`、`ImpactFloat`、`MathExpression|pysssss`、`MemoryCleaner`、`VAEDecode`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`StringFunction|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`HunyuanVideoFoley`、`PreviewAudio`、`VAEDecodeTiled`、`ImageConcanate`、`VHS_LoadVideo`、`AILab_MiniCPM_4_V`、`easy saveText`、`easy promptReplace`、`easy int`、`easy seed`、`EmptyLatentImage`、`AIO_Preprocessor`、`ImageFromBatch+`、`ModelPatchLoader`、`easy positive`、`Florence2ModelLoader`、`Florence2Run`、`ConditioningZeroOut`、`ZImageFunControlnet`、`UNETLoader`、`RH_Captioner`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LayerUtility: ImageScaleByAspectRatio V2
