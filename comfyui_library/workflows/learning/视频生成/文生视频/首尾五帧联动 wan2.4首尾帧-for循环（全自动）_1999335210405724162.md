---
key: 视频生成/文生视频/首尾五帧联动 wan2.4首尾帧-for循环（全自动）_1999335210405724162.json
name: 首尾五帧联动 wan2.4首尾帧-for循环（全自动）_1999335210405724162
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/首尾五帧联动 wan2.4首尾帧-for循环（全自动）_1999335210405724162.json
hash: 36ee02c7d3f270c9
coverage: 0.763889
learned_at: 2026-10-15 22:49:06
nodes: [Anything Everywhere, Anything Everywhere, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, Anything Everywhere, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, MathExpression|pysssss, WanVideoDecode, SetNode, WanVideoApplyNAG, easy cleanGpuUsed, easy cleanGpuUsed, ImageCASharpening+, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, PreviewImage, WanVideoTextEncodeSingle, WanVideoClipVisionEncode, Int, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, easy batchAnything, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, RHHiddenNodes, WanVideoTextEncodeSingle, PreviewImage, easy forLoopStart, VHS_VideoCombine, VHS_VideoCombine, Note, easy forLoopEnd, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, easy anythingIndexSwitch, WanVideoImageToVideoEncode, Note, ImageResize+, ImageResize+, ImageResize+, PreviewImage, GetImageSize, ImageResize+, Compare, ImageResize+, easy ifElse, ImageResize+, GetImageSize, PreviewImage, RHHiddenNodes, Note, JWInteger, JWInteger, Note, Note, Int, Int, Note, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/首尾五帧联动 wan2.4首尾帧-for循环（全自动）_1999335210405724162.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/首尾五帧联动 wan2.4首尾帧-for循环（全自动）_1999335210405724162.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（72 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `WanVideoDecode`
- `SetNode`
- `WanVideoApplyNAG`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageCASharpening+`
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `WanVideoTextEncodeSingle`
- `WanVideoClipVisionEncode`
- `Int`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `easy batchAnything`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `WanVideoTextEncodeSingle`
- `PreviewImage`
- `easy forLoopStart`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `easy forLoopEnd`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `easy anythingIndexSwitch`
- `WanVideoImageToVideoEncode`
- `Note`
- `ImageResize+`
- `ImageResize+`
- `ImageResize+`
- `PreviewImage`
- `GetImageSize`
- `ImageResize+`
- `Compare`
- `ImageResize+`
- `easy ifElse`
- `ImageResize+`
- `GetImageSize`
- `PreviewImage`
- `RHHiddenNodes`
- `Note`
- `JWInteger`
- `JWInteger`
- `Note`
- `Note`
- `Int`
- `Int`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **76%**（55/72）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`MathExpression|pysssss`、`WanVideoDecode`、`WanVideoApplyNAG`、`easy cleanGpuUsed`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncodeSingle`、`WanVideoClipVisionEncode`、`Int`、`RHHiddenNodes`、`easy batchAnything`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`easy forLoopStart`、`VHS_VideoCombine`、`easy forLoopEnd`、`easy anythingIndexSwitch`、`WanVideoImageToVideoEncode`、`ImageResize+`、`GetImageSize`、`Compare`、`JWInteger`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
