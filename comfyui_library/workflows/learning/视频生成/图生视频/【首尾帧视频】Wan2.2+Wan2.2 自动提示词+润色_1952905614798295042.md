---
key: 视频生成/图生视频/【首尾帧视频】Wan2.2+Wan2.2 自动提示词+润色_1952905614798295042.json
name: 【首尾帧视频】Wan2.2+Wan2.2 自动提示词+润色_1952905614798295042.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【首尾帧视频】Wan2.2+Wan2.2 自动提示词+润色_1952905614798295042.json
hash: eec616c209623c6d
coverage: 0.657534
learned_at: 2026-10-15 22:31:03
nodes: [Anything Everywhere, Note, Note, MathExpression|pysssss, WanVideoBlockSwap, Anything Everywhere, WanVideoSetBlockSwap, easy cleanGpuUsed, easy cleanGpuUsed, LayerUtility: PurgeVRAM V2, ImageCASharpening+, WanVideoDecode, WanVideoSLG, WanVideoExperimentalArgs, CogVideoEnhanceAVideo, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoVAELoader, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, SetNode, WanVideoModelLoader, ImageResize+, WanVideoModelLoader, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSampler, WanVideoSampler, CLIPVisionLoader, Anything Everywhere, CreateCFGScheduleFloatList, ColorCorrectOfUtils, WanVideoClipVisionEncode, Int, SetNode, JWInteger, GetNode, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, WanVideoApplyNAG, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, GetNode, WanVideoTextEncodeSingle, easy imageConcat, GetNode, Note, easy textSwitch, RHHiddenNodes, Int, Note, CR Text, Note, ImageResize+, SetNode, PreviewImage, PreviewImage, Note, Int, Int, Note, Note, Note, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【首尾帧视频】Wan2.2+Wan2.2 自动提示词+润色_1952905614798295042.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952905614798295042.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（73 个）：
- `Anything Everywhere`
- `Note`
- `Note`
- `MathExpression|pysssss`
- `WanVideoBlockSwap`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM V2`
- `ImageCASharpening+`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `CogVideoEnhanceAVideo`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `ImageResize+`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `Anything Everywhere`
- `CreateCFGScheduleFloatList`
- `ColorCorrectOfUtils`
- `WanVideoClipVisionEncode`
- `Int`
- `SetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoApplyNAG`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `GetNode`
- `WanVideoTextEncodeSingle`
- `easy imageConcat`
- `GetNode`
- `Note`
- `easy textSwitch`
- `RHHiddenNodes`
- `Int`
- `Note`
- `CR Text`
- `Note`
- `ImageResize+`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `Int`
- `Int`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **66%**（48/73）

**有卡**：`MathExpression|pysssss`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM V2`、`ImageCASharpening+`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`CogVideoEnhanceAVideo`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImageResize+`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoSampler`、`CLIPVisionLoader`、`CreateCFGScheduleFloatList`、`ColorCorrectOfUtils`、`WanVideoClipVisionEncode`、`Int`、`JWInteger`、`WanVideoImageToVideoEncode`、`WanVideoApplyNAG`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`easy imageConcat`、`easy textSwitch`、`RHHiddenNodes`、`CR Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
