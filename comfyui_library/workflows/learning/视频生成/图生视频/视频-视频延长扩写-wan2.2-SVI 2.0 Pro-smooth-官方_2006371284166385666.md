---
key: 视频生成/图生视频/视频-视频延长扩写-wan2.2-SVI 2.0 Pro-smooth-官方_2006371284166385666.json
name: 视频-视频延长扩写-wan2.2-SVI 2.0 Pro-smooth-官方_2006371284166385666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2006371284166385666.json
hash: 8f9abeacb9a2f768
coverage: 0.678571
learned_at: 2026-10-15 22:34:01
nodes: [easy showAnything, easy imageSize, GetNode, GetNode, GetNode, SetNode, PreviewImage, ImageFromBatch, GetImageSizeAndCount, PreviewImage, SetNode, easy seed, CLIPLoader, SetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, SetNode, SetNode, easy int, GetImageSizeAndCount, SetNode, MathExpression|pysssss, MemoryCleaner, LoraLoaderModelOnly, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, CLIPTextEncode, CLIPTextEncode, Reroute, VHS_VideoCombine, INTConstant, INTConstant, LoraLoaderModelOnly, GetNode, KSamplerAdvanced, LoraLoaderModelOnly, WanImageToVideoSVIPro, LoadImage, VAEEncode, Reroute, VAELoader, GetImageSizeAndCount, VAEEncode, GetImageSizeAndCount, VAEDecodeTiled, SaveLatent, ShowText|pysssss, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, ImageResizeKJv2, GetImageSizeAndCount, GetImageSizeAndCount, GetImageSizeAndCount, ImageBatchExtendWithOverlap, VHS_LoadVideo, ImpactFloat, ImageFromBatch, GetImageSizeAndCount, PreviewImage, PrimitiveFloat, easy showAnything, JWFloatToString, easy positive, easy anythingIndexSwitch, ImageConcanate, StringFunction|pysssss, ImageFromBatch+, KSamplerAdvanced, Qwen3_VQA, GetNode, easy showAnything, RH_LLMAPI_NODE, easy positive, easy positive, easy positive, VHS_VideoCombine, SetNode, StringFunction|pysssss, easy saveText, easy int]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 2, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/视频-视频延长扩写-wan2.2-SVI 2.0 Pro-smooth-官方_2006371284166385666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006371284166385666.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `easy showAnything`
- `easy imageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SetNode`
- `easy seed`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `easy int`
- `GetImageSizeAndCount`
- `SetNode`
- `MathExpression|pysssss`
- `MemoryCleaner`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanImageToVideoSVIPro`
- `LoadImage`
- `VAEEncode` ★核心
- `Reroute`
- `VAELoader`
- `GetImageSizeAndCount`
- `VAEEncode` ★核心
- `GetImageSizeAndCount`
- `VAEDecodeTiled` ★核心
- `SaveLatent`
- `ShowText|pysssss`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageBatchExtendWithOverlap`
- `VHS_LoadVideo`
- `ImpactFloat`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `PreviewImage`
- `PrimitiveFloat`
- `easy showAnything`
- `JWFloatToString`
- `easy positive`
- `easy anythingIndexSwitch`
- `ImageConcanate`
- `StringFunction|pysssss`
- `ImageFromBatch+`
- `KSamplerAdvanced` ★核心
- `Qwen3_VQA`
- `GetNode`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `easy positive`
- `easy positive`
- `easy positive`
- `VHS_VideoCombine`
- `SetNode`
- `StringFunction|pysssss`
- `easy saveText`
- `easy int`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `2`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **68%**（57/84）

**有卡**：`easy imageSize`、`ImageFromBatch`、`GetImageSizeAndCount`、`easy seed`、`CLIPLoader`、`easy int`、`MathExpression|pysssss`、`MemoryCleaner`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`CLIPTextEncode`、`VHS_VideoCombine`、`INTConstant`、`KSamplerAdvanced`、`WanImageToVideoSVIPro`、`LoadImage`、`VAEEncode`、`VAELoader`、`VAEDecodeTiled`、`SaveLatent`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`ImageBatchExtendWithOverlap`、`VHS_LoadVideo`、`ImpactFloat`、`JWFloatToString`、`easy positive`、`easy anythingIndexSwitch`、`ImageConcanate`、`StringFunction|pysssss`、`ImageFromBatch+`、`Qwen3_VQA`、`RH_LLMAPI_NODE`、`easy saveText`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced、easy seed
