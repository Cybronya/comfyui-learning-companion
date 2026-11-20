---
key: 平台全量/【后拉运镜】Wan2.2+FusionX图生视频（基础流）_2018154363864223745.json
name: 【后拉运镜】Wan2.2+FusionX图生视频（基础流）_2018154363864223745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【后拉运镜】Wan2.2+FusionX图生视频（基础流）_2018154363864223745.json
hash: 214b69215a486731
coverage: 0.701299
learned_at: 2026-11-14 01:23:33
nodes: [Anything Everywhere, Note, Note, Note, Int, WanVideoClipVisionEncode, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, GetNode, easy showAnything, ImageResize+, easy showAnything, ImageResize+, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, WanVideoImageToVideoEncode, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, GetNode, Note, Note, CR String To Number, InversionDemoLazyIndexSwitch, JWInteger, LoadWanVideoT5TextEncoder, WanVideoDecode, VHS_VideoCombine, WanVideoTextEncode, easy int, ColorCorrectOfUtils, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSetBlockSwap, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, CR Text Concatenate, WanVideoVAELoader, WanVideoLoraSelect, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, RHHiddenNodes, CR Text, FluxResolutionNode, LoadImage]
patterns: []
missing: []
---

# 平台全量/【后拉运镜】Wan2.2+FusionX图生视频（基础流）_2018154363864223745.json

> 来源文件 `comfyui_library/workflows/平台全量/【后拉运镜】Wan2.2+FusionX图生视频（基础流）_2018154363864223745.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（77 个）：
- `Anything Everywhere`
- `Note`
- `Note`
- `Note`
- `Int`
- `WanVideoClipVisionEncode`
- `Anything Everywhere`
- `InversionDemoLazyIndexSwitch`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `ImageResize+`
- `easy showAnything`
- `ImageResize+`
- `easy showAnything`
- `CR String To Number`
- `SetNode`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `Note`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `Anything Everywhere`
- `CLIPVisionLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `ImageCASharpening+`
- `GetNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `CR String To Number`
- `InversionDemoLazyIndexSwitch`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `easy int`
- `ColorCorrectOfUtils`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `CR Text Concatenate`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `RHHiddenNodes`
- `CR Text`
- `FluxResolutionNode`
- `LoadImage`

## 知识

覆盖率 **70%**（54/77）

**有卡**：`Int`、`WanVideoClipVisionEncode`、`InversionDemoLazyIndexSwitch`、`ImageResize+`、`CR String To Number`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoTextEncode`、`easy int`、`ColorCorrectOfUtils`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoLoraSelect`、`CR Text Concatenate`、`WanVideoVAELoader`、`RHHiddenNodes`、`CR Text`、`FluxResolutionNode`、`LoadImage`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode
