---
key: 视频生成/图生视频/【打破次元】Wan2.2+FusionX图生视频_1955598143335403521.json
name: 【打破次元】Wan2.2+FusionX图生视频_1955598143335403521.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【打破次元】Wan2.2+FusionX图生视频_1955598143335403521.json
hash: 4ba806f1a6617f06
coverage: 0.670455
learned_at: 2026-10-15 22:31:09
nodes: [Anything Everywhere, Note, Note, Note, Int, WanVideoClipVisionEncode, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, GetNode, easy showAnything, ImageResize+, easy showAnything, ImageResize+, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, WanVideoImageToVideoEncode, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, Note, CR String To Number, InversionDemoLazyIndexSwitch, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, WanVideoSetBlockSwap, WanVideoModelLoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoBlockSwap, GetNode, VHS_VideoCombine, Note, Note, WanVideoModelLoader, Note, Note, WanVideoLoraSelect, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, Int, Int, WanVideoVAELoader, ColorCorrectOfUtils, WanVideoTextEncode, CR Text, JWInteger, LoadImage, easy textSwitch, RHHiddenNodes, Int, CR Text, Note, Note, Note, WanVideoExperimentalArgs, WanVideoSLG, CogVideoEnhanceAVideo, WanVideoTorchCompileSettings, WanVideoTorchCompileSettings, FluxResolutionNode]
patterns: []
missing: []
---

# 视频生成/图生视频/【打破次元】Wan2.2+FusionX图生视频_1955598143335403521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955598143335403521.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（88 个）：
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
- `Note`
- `CR String To Number`
- `InversionDemoLazyIndexSwitch`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `easy int`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Int`
- `Int`
- `WanVideoVAELoader`
- `ColorCorrectOfUtils`
- `WanVideoTextEncode`
- `CR Text`
- `JWInteger`
- `LoadImage`
- `easy textSwitch`
- `RHHiddenNodes`
- `Int`
- `CR Text`
- `Note`
- `Note`
- `Note`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `CogVideoEnhanceAVideo`
- `WanVideoTorchCompileSettings`
- `WanVideoTorchCompileSettings`
- `FluxResolutionNode`

## 知识

覆盖率 **67%**（59/88）

**有卡**：`Int`、`WanVideoClipVisionEncode`、`InversionDemoLazyIndexSwitch`、`ImageResize+`、`CR String To Number`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`WanVideoModelLoader`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoVAELoader`、`ColorCorrectOfUtils`、`WanVideoTextEncode`、`CR Text`、`JWInteger`、`LoadImage`、`easy textSwitch`、`RHHiddenNodes`、`WanVideoTorchCompileSettings`、`FluxResolutionNode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
