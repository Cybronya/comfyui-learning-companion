---
key: 视频生成/图生视频/五帧wan2.2首尾帧_2001973649991168002.json
name: 五帧wan2.2首尾帧_2001973649991168002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001973649991168002.json
hash: e6338c34bc9bcbc4
coverage: 0.763889
learned_at: 2026-10-15 22:33:47
nodes: [Anything Everywhere, Anything Everywhere, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, Anything Everywhere, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, MathExpression|pysssss, WanVideoDecode, SetNode, WanVideoApplyNAG, easy cleanGpuUsed, easy cleanGpuUsed, ImageCASharpening+, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, PreviewImage, WanVideoTextEncodeSingle, WanVideoClipVisionEncode, Int, RHHiddenNodes, RHHiddenNodes, easy batchAnything, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, RHHiddenNodes, PreviewImage, easy forLoopStart, VHS_VideoCombine, VHS_VideoCombine, easy forLoopEnd, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, easy anythingIndexSwitch, WanVideoImageToVideoEncode, Note, ImageResize+, ImageResize+, ImageResize+, PreviewImage, GetImageSize, ImageResize+, Compare, easy ifElse, ImageResize+, GetImageSize, PreviewImage, RHHiddenNodes, Note, Note, Int, Int, Note, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, WanVideoTextEncodeSingle, RHHiddenNodes, Note, Note, JWInteger, ImageResize+, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/五帧wan2.2首尾帧_2001973649991168002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001973649991168002.json`

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
- `easy batchAnything`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `PreviewImage`
- `easy forLoopStart`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
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
- `easy ifElse`
- `ImageResize+`
- `GetImageSize`
- `PreviewImage`
- `RHHiddenNodes`
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
- `WanVideoTextEncodeSingle`
- `RHHiddenNodes`
- `Note`
- `Note`
- `JWInteger`
- `ImageResize+`
- `JWInteger`

## 知识

覆盖率 **76%**（55/72）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`MathExpression|pysssss`、`WanVideoDecode`、`WanVideoApplyNAG`、`easy cleanGpuUsed`、`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncodeSingle`、`WanVideoClipVisionEncode`、`Int`、`RHHiddenNodes`、`easy batchAnything`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`easy forLoopStart`、`VHS_VideoCombine`、`easy forLoopEnd`、`easy anythingIndexSwitch`、`WanVideoImageToVideoEncode`、`ImageResize+`、`GetImageSize`、`Compare`、`LoadImage`、`JWInteger`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
