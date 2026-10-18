---
key: 视频生成/图生视频/【后拉运镜48G先行版】wan2.1图生视频（全自动）_1931043397564608513.json
name: 【后拉运镜48G先行版】wan2.1图生视频（全自动）_1931043397564608513.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【后拉运镜48G先行版】wan2.1图生视频（全自动）_1931043397564608513.json
hash: d70b134eb8cb15bf
coverage: 0.64
learned_at: 2026-10-15 22:30:08
nodes: [Anything Everywhere, Anything Everywhere, WanVideoDecode, Note, Note, Note, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoSetBlockSwap, WanVideoBlockSwap, Note, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoLoraSelect, WanVideoTeaCache, Note, WanVideoTextEncode, ShowText|pysssss, RHHiddenNodes, Int, WanVideoClipVisionEncode, CLIPVisionLoader, Anything Everywhere, WanVideoSampler, GetNode, InversionDemoLazyIndexSwitch, GetNode, WanVideoImageToVideoEncode, GetNode, GetNode, easy cleanGpuUsed, GetNode, GetNode, InversionDemoLazyIndexSwitch, MathExpression|pysssss, easy showAnything, MathExpression|pysssss, ImageResize+, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, ImageResize+, SetNode, easy showAnything, easy showAnything, CR String To Number, SetNode, CR String To Number, SetNode, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, MathExpression|pysssss, SetNode, Evaluate Integers, GetNode, easy showAnything, Int, MMAudioFeatureUtilsLoader, Anything Everywhere, SetNode, ImageCASharpening+, GetNode, Anything Everywhere, MMAudioModelLoader, easy showAnything, MMAudioSampler, VHS_VideoCombine, PreviewAudio, AudioCombine, RHHiddenNodes, RHHiddenNodes, MMAudioSampler, easy showAnything, PreviewAudio, JWInteger, LoadImage, PreviewBridge, LoadAudio, AudioCombine, AudioCrop, easy anythingIndexSwitch, AudioCleanupNode, CR Text, CR Text, Int, Note, Note, Note, VHS_LoadVideo, easy int, CR Text, FluxResolutionNode, Note, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/【后拉运镜48G先行版】wan2.1图生视频（全自动）_1931043397564608513.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1931043397564608513.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（100 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoDecode`
- `Note`
- `Note`
- `Note`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoTeaCache`
- `Note`
- `WanVideoTextEncode`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `Int`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `WanVideoSampler` ★核心
- `GetNode`
- `InversionDemoLazyIndexSwitch`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `InversionDemoLazyIndexSwitch`
- `MathExpression|pysssss`
- `easy showAnything`
- `MathExpression|pysssss`
- `ImageResize+`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageResize+`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `CR String To Number`
- `SetNode`
- `CR String To Number`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `SetNode`
- `Evaluate Integers`
- `GetNode`
- `easy showAnything`
- `Int`
- `MMAudioFeatureUtilsLoader`
- `Anything Everywhere`
- `SetNode`
- `ImageCASharpening+`
- `GetNode`
- `Anything Everywhere`
- `MMAudioModelLoader`
- `easy showAnything`
- `MMAudioSampler` ★核心
- `VHS_VideoCombine`
- `PreviewAudio`
- `AudioCombine`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `MMAudioSampler` ★核心
- `easy showAnything`
- `PreviewAudio`
- `JWInteger`
- `LoadImage`
- `PreviewBridge`
- `LoadAudio`
- `AudioCombine`
- `AudioCrop`
- `easy anythingIndexSwitch`
- `AudioCleanupNode`
- `CR Text`
- `CR Text`
- `Int`
- `Note`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `easy int`
- `CR Text`
- `FluxResolutionNode`
- `Note`
- `Note`

## 知识

覆盖率 **64%**（64/100）

**有卡**：`WanVideoDecode`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTeaCache`、`WanVideoTextEncode`、`RHHiddenNodes`、`Int`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSampler`、`InversionDemoLazyIndexSwitch`、`WanVideoImageToVideoEncode`、`easy cleanGpuUsed`、`MathExpression|pysssss`、`ImageResize+`、`CR String To Number`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`Evaluate Integers`、`MMAudioFeatureUtilsLoader`、`ImageCASharpening+`、`MMAudioModelLoader`、`MMAudioSampler`、`PreviewAudio`、`AudioCombine`、`JWInteger`、`LoadImage`、`PreviewBridge`、`LoadAudio`、`AudioCrop`、`easy anythingIndexSwitch`、`AudioCleanupNode`、`CR Text`、`VHS_LoadVideo`、`easy int`、`FluxResolutionNode`

**用到的条目**：LoadImage、WanVideoSampler、MMAudioSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
