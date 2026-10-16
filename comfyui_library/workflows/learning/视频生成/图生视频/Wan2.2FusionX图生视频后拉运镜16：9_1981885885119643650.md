---
key: 视频生成/图生视频/Wan2.2FusionX图生视频后拉运镜16：9_1981885885119643650.json
name: Wan2.2FusionX图生视频后拉运镜16：9_1981885885119643650.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981885885119643650.json
hash: 3806c8201518874c
coverage: 0.705882
learned_at: 2026-10-15 22:32:39
nodes: [Anything Everywhere, Int, WanVideoClipVisionEncode, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, GetNode, easy showAnything, ImageResize+, easy showAnything, ImageResize+, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, WanVideoImageToVideoEncode, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, GetNode, Note, Note, CR String To Number, InversionDemoLazyIndexSwitch, JWInteger, LoadWanVideoT5TextEncoder, WanVideoDecode, VHS_VideoCombine, easy int, ColorCorrectOfUtils, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoModelLoader, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoModelLoader, RHHiddenNodes, FluxResolutionNode, CR Text, WanVideoVAELoader, WanVideoLoraSelect, LoadImage, WanVideoTextEncode, CR Text Concatenate]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2FusionX图生视频后拉运镜16：9_1981885885119643650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981885885119643650.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（68 个）：
- `Anything Everywhere`
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
- `easy int`
- `ColorCorrectOfUtils`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `RHHiddenNodes`
- `FluxResolutionNode`
- `CR Text`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `LoadImage`
- `WanVideoTextEncode`
- `CR Text Concatenate`

## 知识

覆盖率 **71%**（48/68）

**有卡**：`Int`、`WanVideoClipVisionEncode`、`InversionDemoLazyIndexSwitch`、`ImageResize+`、`CR String To Number`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`、`easy int`、`ColorCorrectOfUtils`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`RHHiddenNodes`、`FluxResolutionNode`、`CR Text`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`LoadImage`、`WanVideoTextEncode`、`CR Text Concatenate`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
