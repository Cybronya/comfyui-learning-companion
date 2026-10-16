---
key: 视频生成/图生视频/【曲线运镜】Wan2.2+FusionX图生视频（基础流）_1951191570521464834.json
name: 【曲线运镜】Wan2.2+FusionX图生视频（基础流）_1951191570521464834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1951191570521464834.json
hash: 300753aaedb92764
coverage: 0.662791
learned_at: 2026-10-15 22:30:58
nodes: [Anything Everywhere, Note, Note, Note, Int, WanVideoClipVisionEncode, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, easy showAnything, ImageResize+, ImageResize+, easy showAnything, MathExpression|pysssss, SetNode, Note, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, Note, InversionDemoLazyIndexSwitch, JWInteger, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, ColorCorrectOfUtils, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoTextEncode, VHS_VideoCombine, Note, Note, WanVideoModelLoader, Note, ShowText|pysssss, Note, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, RHHiddenNodes, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, Note, Int, Int, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoTorchCompileSettings, MathExpression|pysssss, SetNode, GetNode, GetNode, MathExpression|pysssss, CR Text, easy showAnything, FluxResolutionNode, CR String To Number, SetNode, easy showAnything, WanVideoImageToVideoEncode, GetNode, GetNode, CR String To Number]
patterns: []
missing: []
---

# 视频生成/图生视频/【曲线运镜】Wan2.2+FusionX图生视频（基础流）_1951191570521464834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951191570521464834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（86 个）：
- `Anything Everywhere`
- `Note`
- `Note`
- `Note`
- `Int`
- `WanVideoClipVisionEncode`
- `Anything Everywhere`
- `InversionDemoLazyIndexSwitch`
- `GetNode`
- `easy showAnything`
- `ImageResize+`
- `ImageResize+`
- `easy showAnything`
- `MathExpression|pysssss`
- `SetNode`
- `Note`
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
- `easy showAnything`
- `SetNode`
- `Note`
- `InversionDemoLazyIndexSwitch`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `easy int`
- `ColorCorrectOfUtils`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `ShowText|pysssss`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `RHHiddenNodes`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Note`
- `Int`
- `Int`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoTorchCompileSettings`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `CR Text`
- `easy showAnything`
- `FluxResolutionNode`
- `CR String To Number`
- `SetNode`
- `easy showAnything`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `CR String To Number`

## 知识

覆盖率 **66%**（57/86）

**有卡**：`Int`、`WanVideoClipVisionEncode`、`InversionDemoLazyIndexSwitch`、`ImageResize+`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`ColorCorrectOfUtils`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`LoadImage`、`RHHiddenNodes`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`CR Text`、`FluxResolutionNode`、`CR String To Number`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
