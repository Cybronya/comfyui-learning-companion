---
key: 视频生成/文生视频/【舞台镜头分镜】超长视频生成Wan2.2-SkyreelsV2图生长视频_1978980050555015169.json
name: 【舞台镜头分镜】超长视频生成Wan2.2-SkyreelsV2图生长视频_1978980050555015169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【舞台镜头分镜】超长视频生成Wan2.2-SkyreelsV2图生长视频_1978980050555015169.json
hash: fbbaa8db9010f044
coverage: 0.426966
learned_at: 2026-10-10 23:10:17
nodes: [Anything Everywhere, Note, Note, Note, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, easy showAnything, easy showAnything, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, Note, CR String To Number, InversionDemoLazyIndexSwitch, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoBlockSwap, GetNode, VHS_VideoCombine, Note, Int, ColorCorrectOfUtils, CR Text, Int, MathExpression|pysssss, ImageResize+, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, GetNode, GetNode, ImageResize+, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, CreateCFGScheduleFloatList, PrimitiveNode, Int, CR Text Concatenate, CR Text, WanVideoTextEncode, RHHiddenNodes, JWInteger, WanVideoLoraSelect, FluxResolutionNode, Note, Note, Note, Note, Note, LoadImage, CR Text]
patterns: []
missing: [CR String To Number, CR String To Number, CR Text, CR Text, CR Text, CR Text Concatenate, ImageCASharpening+, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, easy int, ImageResize+, ImageResize+]
discoveries: [次要节点 `CR String To Number` 知识库中没有该节点类型的任何知识, 次要节点 `CR String To Number` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/【舞台镜头分镜】超长视频生成Wan2.2-SkyreelsV2图生长视频_1978980050555015169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【舞台镜头分镜】超长视频生成Wan2.2-SkyreelsV2图生长视频_1978980050555015169.json`

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

覆盖率 **43%**（38/89）

**有卡**：`InversionDemoLazyIndexSwitch`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`Int`、`ColorCorrectOfUtils`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoTextEncode`、`RHHiddenNodes`、`JWInteger`、`FluxResolutionNode`、`LoadImage`

**缺卡**（22）：`CR String To Number`、`CR String To Number`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy int`、`ImageResize+`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

## 学习发现

- 次要节点 `CR String To Number` 知识库中没有该节点类型的任何知识
- 次要节点 `CR String To Number` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
