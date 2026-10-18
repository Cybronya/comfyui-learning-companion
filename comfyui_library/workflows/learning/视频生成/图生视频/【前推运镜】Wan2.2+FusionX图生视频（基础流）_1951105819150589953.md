---
key: 视频生成/图生视频/【前推运镜】Wan2.2+FusionX图生视频（基础流）_1951105819150589953.json
name: 【前推运镜】Wan2.2+FusionX图生视频（基础流）_1951105819150589953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【前推运镜】Wan2.2+FusionX图生视频（基础流）_1951105819150589953.json
hash: 9d7939f3927bae50
coverage: 0.666667
learned_at: 2026-10-15 22:30:57
nodes: [Anything Everywhere, Note, Note, Note, Int, WanVideoClipVisionEncode, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, GetNode, easy showAnything, ImageResize+, easy showAnything, ImageResize+, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, WanVideoImageToVideoEncode, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, Note, CR String To Number, InversionDemoLazyIndexSwitch, JWInteger, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, ColorCorrectOfUtils, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoBlockSwap, GetNode, WanVideoTextEncode, VHS_VideoCombine, CR Text, Note, Note, WanVideoModelLoader, Note, CR Text Concatenate, ShowText|pysssss, Note, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, LoadImage, Note, RHHiddenNodes, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoTorchCompileSettings, FluxResolutionNode]
patterns: []
missing: []
---

# 视频生成/图生视频/【前推运镜】Wan2.2+FusionX图生视频（基础流）_1951105819150589953.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951105819150589953.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（84 个）：
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
- `GetNode`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `CR Text`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `CR Text Concatenate`
- `ShowText|pysssss`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `Note`
- `RHHiddenNodes`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoTorchCompileSettings`
- `FluxResolutionNode`

## 知识

覆盖率 **67%**（56/84）

**有卡**：`Int`、`WanVideoClipVisionEncode`、`InversionDemoLazyIndexSwitch`、`ImageResize+`、`CR String To Number`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`ColorCorrectOfUtils`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTextEncode`、`VHS_VideoCombine`、`CR Text`、`CR Text Concatenate`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`LoadImage`、`RHHiddenNodes`、`WanVideoTorchCompileSettings`、`FluxResolutionNode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
