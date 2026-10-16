---
key: 视频生成/图生视频/Wan2.2 Skyreels V2 图生长视频_1979077194871902210.json
name: Wan2.2 Skyreels V2 图生长视频_1979077194871902210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1979077194871902210.json
hash: 250cb8e0ebe30241
coverage: 0.674157
learned_at: 2026-10-15 22:32:21
nodes: [Anything Everywhere, Note, Note, Note, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, easy showAnything, easy showAnything, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, Note, CR String To Number, InversionDemoLazyIndexSwitch, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoBlockSwap, GetNode, VHS_VideoCombine, Note, Int, ColorCorrectOfUtils, CR Text, Int, MathExpression|pysssss, ImageResize+, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, GetNode, GetNode, ImageResize+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, CreateCFGScheduleFloatList, PrimitiveNode, Int, CR Text Concatenate, CR Text, WanVideoTextEncode, RHHiddenNodes, JWInteger, WanVideoLoraSelect, FluxResolutionNode, Note, Note, Note, Note, Note, LoadImage, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Skyreels V2 图生长视频_1979077194871902210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979077194871902210.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（89 个）：
- `Anything Everywhere`
- `Note`
- `Note`
- `Note`
- `Anything Everywhere`
- `InversionDemoLazyIndexSwitch`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `CR String To Number`
- `SetNode`
- `SetNode`
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
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `Int`
- `ColorCorrectOfUtils`
- `CR Text`
- `Int`
- `MathExpression|pysssss`
- `ImageResize+`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `ImageResize+`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `Int`
- `CR Text Concatenate`
- `CR Text`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `JWInteger`
- `WanVideoLoraSelect`
- `FluxResolutionNode`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **67%**（60/89）

**有卡**：`InversionDemoLazyIndexSwitch`、`CR String To Number`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`WanVideoTorchCompileSettings`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`Int`、`ColorCorrectOfUtils`、`CR Text`、`ImageResize+`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`CR Text Concatenate`、`WanVideoTextEncode`、`RHHiddenNodes`、`JWInteger`、`FluxResolutionNode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
