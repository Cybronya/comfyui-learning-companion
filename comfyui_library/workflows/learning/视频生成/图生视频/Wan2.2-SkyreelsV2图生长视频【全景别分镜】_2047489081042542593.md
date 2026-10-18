---
key: 视频生成/图生视频/Wan2.2-SkyreelsV2图生长视频【全景别分镜】_2047489081042542593.json
name: Wan2.2-SkyreelsV2图生长视频【全景别分镜】_2047489081042542593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-SkyreelsV2图生长视频【全景别分镜】_2047489081042542593.json
hash: 08b671e712fc5fec
coverage: 0.662338
learned_at: 2026-10-15 22:37:05
nodes: [Anything Everywhere, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, easy showAnything, easy showAnything, easy showAnything, CR String To Number, SetNode, SetNode, Note, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, Note, CR String To Number, InversionDemoLazyIndexSwitch, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, WanVideoSetBlockSwap, GetNode, VHS_VideoCombine, Note, MathExpression|pysssss, ImageResize+, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, GetNode, GetNode, ImageResize+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoVAELoader, CR Text Concatenate, CR Text, WanVideoTextEncode, RHHiddenNodes, JWInteger, WanVideoLoraSelect, CR Text, LoadImage, Note, Note, Note, Note, Note, WanVideoBlockSwap, ColorCorrectOfUtils, CreateCFGScheduleFloatList, PrimitiveNode, Int, Int, MathExpression|pysssss, SetNode, FluxResolutionNode, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-SkyreelsV2图生长视频【全景别分镜】_2047489081042542593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047489081042542593.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（77 个）：
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
- `WanVideoSetBlockSwap`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
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
- `CR Text Concatenate`
- `CR Text`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `JWInteger`
- `WanVideoLoraSelect`
- `CR Text`
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `ColorCorrectOfUtils`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `SetNode`
- `FluxResolutionNode`
- `CR Text`

## 知识

覆盖率 **66%**（51/77）

**有卡**：`InversionDemoLazyIndexSwitch`、`CR String To Number`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`MathExpression|pysssss`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`VHS_VideoCombine`、`ImageResize+`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoVAELoader`、`CR Text Concatenate`、`CR Text`、`WanVideoTextEncode`、`RHHiddenNodes`、`JWInteger`、`LoadImage`、`ColorCorrectOfUtils`、`CreateCFGScheduleFloatList`、`Int`、`FluxResolutionNode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
