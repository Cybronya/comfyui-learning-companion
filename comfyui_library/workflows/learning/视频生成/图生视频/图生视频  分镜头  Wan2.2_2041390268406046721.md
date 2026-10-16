---
key: 视频生成/图生视频/图生视频  分镜头  Wan2.2_2041390268406046721.json
name: 图生视频  分镜头  Wan2.2_2041390268406046721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041390268406046721.json
hash: 1f6c3a1c1dea8b14
coverage: 0.666667
learned_at: 2026-10-15 22:36:19
nodes: [Anything Everywhere, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, easy showAnything, easy showAnything, easy showAnything, CR String To Number, SetNode, SetNode, Note, WanVideoBlockSwap, Anything Everywhere, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, Note, CR String To Number, InversionDemoLazyIndexSwitch, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, WanVideoSetBlockSwap, GetNode, VHS_VideoCombine, MathExpression|pysssss, ImageResize+, WanVideoModelLoader, WanVideoModelLoader, GetNode, GetNode, ImageResize+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoLoraSelect, WanVideoVAELoader, CR Text Concatenate, WanVideoTextEncode, RHHiddenNodes, WanVideoLoraSelect, Note, WanVideoBlockSwap, ColorCorrectOfUtils, CreateCFGScheduleFloatList, PrimitiveNode, MathExpression|pysssss, SetNode, CR Text, WanVideoLoraSelect, WanVideoSampler, LoadImage, Note, Note, Note, CR Text, JWInteger, Note, Int, Int, Note, CR Text, FluxResolutionNode, CLIPVisionLoader, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频  分镜头  Wan2.2_2041390268406046721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041390268406046721.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（78 个）：
- `Anything Everywhere`
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
- `Note`
- `WanVideoBlockSwap`
- `Anything Everywhere`
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
- `WanVideoSetBlockSwap`
- `GetNode`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `ImageResize+`
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
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `CR Text Concatenate`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoBlockSwap`
- `ColorCorrectOfUtils`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `MathExpression|pysssss`
- `SetNode`
- `CR Text`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `CR Text`
- `JWInteger`
- `Note`
- `Int`
- `Int`
- `Note`
- `CR Text`
- `FluxResolutionNode`
- `CLIPVisionLoader`
- `LoadImage`

## 知识

覆盖率 **67%**（52/78）

**有卡**：`InversionDemoLazyIndexSwitch`、`CR String To Number`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`MathExpression|pysssss`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`VHS_VideoCombine`、`ImageResize+`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`CR Text Concatenate`、`WanVideoTextEncode`、`RHHiddenNodes`、`ColorCorrectOfUtils`、`CreateCFGScheduleFloatList`、`CR Text`、`LoadImage`、`JWInteger`、`Int`、`FluxResolutionNode`、`CLIPVisionLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
