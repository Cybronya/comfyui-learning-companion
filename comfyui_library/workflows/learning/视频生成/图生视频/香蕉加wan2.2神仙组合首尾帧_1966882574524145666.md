---
key: 视频生成/图生视频/香蕉加wan2.2神仙组合首尾帧_1966882574524145666.json
name: 香蕉加wan2.2神仙组合首尾帧_1966882574524145666.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/香蕉加wan2.2神仙组合首尾帧_1966882574524145666.json
hash: cdbc79faaaccfcbd
coverage: 0.528736
learned_at: 2026-10-15 22:31:39
nodes: [ModelSamplingSD3, GetNode, GetNode, GetNode, SetNode, easy showAnything, ImpactSwitch, VHS_VideoInfo, Int, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, CLIPVisionLoader, CLIPVisionEncode, GetNode, UNETLoader, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, PathchSageAttentionKJ, CFGNorm, SetNode, GetImageSize, SetNode, GetNode, ImpactSwitch, Reroute, Reroute, Reroute, Reroute, MathExpression|pysssss, easy batchAnything, GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, GetNode, VAEDecode, GetNode, ImageResizeKJv2, LoraLoaderModelOnly, Int, SetNode, SetNode, VAELoader, CLIPVisionEncode, WanMoeKSampler, SeedVR2, SeedVR2BlockSwap, SetNode, SetNode, CLIPTextEncode, VHS_VideoCombine, VHS_LoadVideo, GetImageRangeFromBatch, GetImageRangeFromBatch, Image Comparer (rgthree), GetNode, GetNode, SetNode, CLIPLoader, GetNode, SetNode, GetNode, SetNode, VHS_VideoCombine, SetNode, SetNode, WanFirstLastFrameToVideo, SetNode, ImageResizeKJ, easy forLoopEnd, MathExpression|pysssss, GetNode, SetNode, easy forLoopStart, LoadImage, PreviewImage, RH_Nano_Banana_Image2Image, SetNode, SaveImage, INTConstant, INTConstant, INTConstant, Note, CLIPTextEncode, CR Text]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "euler", "sampler_name": 3.5, "scheduler": 1, "seed": 0.875, "steps": "randomize"}
---

# 视频生成/图生视频/香蕉加wan2.2神仙组合首尾帧_1966882574524145666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966882574524145666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（87 个）：
- `ModelSamplingSD3`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `ImpactSwitch`
- `VHS_VideoInfo`
- `Int`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `GetNode`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CFGNorm`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `ImpactSwitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `MathExpression|pysssss`
- `easy batchAnything`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `SetNode`
- `SetNode`
- `VAELoader`
- `CLIPVisionEncode`
- `WanMoeKSampler` ★核心
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanFirstLastFrameToVideo`
- `SetNode`
- `ImageResizeKJ`
- `easy forLoopEnd`
- `MathExpression|pysssss`
- `GetNode`
- `SetNode`
- `easy forLoopStart`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `SetNode`
- `SaveImage`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Note`
- `CLIPTextEncode` ★核心
- `CR Text`

## 关键参数

- `seed` = `0.875`
- `steps` = `randomize`
- `cfg` = `14`
- `sampler_name` = `3.5`
- `scheduler` = `1`
- `denoise` = `euler`

## 知识

覆盖率 **53%**（46/87）

**有卡**：`ModelSamplingSD3`、`VHS_VideoInfo`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`CLIPVisionEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`CFGNorm`、`GetImageSize`、`MathExpression|pysssss`、`easy batchAnything`、`GetImageRangeFromBatch`、`VAEDecode`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`VAELoader`、`WanMoeKSampler`、`SeedVR2`、`SeedVR2BlockSwap`、`CLIPTextEncode`、`VHS_VideoCombine`、`VHS_LoadVideo`、`CLIPLoader`、`WanFirstLastFrameToVideo`、`ImageResizeKJ`、`easy forLoopEnd`、`easy forLoopStart`、`LoadImage`、`RH_Nano_Banana_Image2Image`、`SaveImage`、`INTConstant`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
