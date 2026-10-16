---
key: 视频生成/图生视频/【大师运镜】Wan2.2+FusionX图生视频｜高清版_1955450074836996098.json
name: 【大师运镜】Wan2.2+FusionX图生视频｜高清版_1955450074836996098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955450074836996098.json
hash: eedecc7a6aeda682
coverage: 0.670588
learned_at: 2026-10-15 22:31:08
nodes: [Anything Everywhere, Note, Note, Note, Int, WanVideoClipVisionEncode, Anything Everywhere, InversionDemoLazyIndexSwitch, GetNode, GetNode, GetNode, easy showAnything, ImageResize+, easy showAnything, ImageResize+, easy showAnything, CR String To Number, SetNode, SetNode, MathExpression|pysssss, SetNode, Note, WanVideoImageToVideoEncode, WanVideoBlockSwap, Anything Everywhere, CLIPVisionLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, GetNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, SetNode, GetNode, Note, CR String To Number, InversionDemoLazyIndexSwitch, JWInteger, LoadWanVideoT5TextEncoder, WanVideoDecode, easy int, ColorCorrectOfUtils, WanVideoSLG, WanVideoExperimentalArgs, CogVideoEnhanceAVideo, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoBlockSwap, GetNode, WanVideoTextEncode, VHS_VideoCombine, Note, Note, WanVideoModelLoader, Note, ShowText|pysssss, Note, WanVideoLoraSelect, FluxResolutionNode, CR Text, WanVideoLoraSelect, RHHiddenNodes, WanVideoLoraSelect, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, Note, Int, Int, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【大师运镜】Wan2.2+FusionX图生视频｜高清版_1955450074836996098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955450074836996098.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（85 个）：
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
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `CogVideoEnhanceAVideo`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `ShowText|pysssss`
- `Note`
- `WanVideoLoraSelect`
- `FluxResolutionNode`
- `CR Text`
- `WanVideoLoraSelect`
- `RHHiddenNodes`
- `WanVideoLoraSelect`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Note`
- `Int`
- `Int`
- `LoadImage`

## 知识

覆盖率 **67%**（57/85）

**有卡**：`Int`、`WanVideoClipVisionEncode`、`InversionDemoLazyIndexSwitch`、`ImageResize+`、`CR String To Number`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`JWInteger`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy int`、`ColorCorrectOfUtils`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`CogVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`FluxResolutionNode`、`CR Text`、`RHHiddenNodes`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
