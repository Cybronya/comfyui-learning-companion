---
key: 平台全量/For+WAN2.2-AllInOne 控制+参考 长视频转绘_1965632961276166146.json
name: For+WAN2.2-AllInOne 控制+参考 长视频转绘_1965632961276166146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/For+WAN2.2-AllInOne 控制+参考 长视频转绘_1965632961276166146.json
hash: 89dbe5b7d10720b0
coverage: 0.615385
learned_at: 2026-11-14 00:30:43
nodes: [FaceProcessorLoader, GetNode, ApplyFaceProcessor, SetNode, easy forLoopEnd, SetNode, INTConstant, INTConstant, SetNode, SetNode, easy imageRemBg, VHS_VideoCombine, easy imageRemBg, SetNode, SetNode, GetNode, WanVideoDecode, easy batchAnything, SetNode, GetNode, GetNode, Display Int (rgthree), WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoLoraSelect, WanVideoEncode, GetNode, WanVideoSampler, WanVideoAddStandInLatent, Text Multiline, VHS_VideoCombine, GetNode, GetNode, Reroute, Display Int (rgthree), LayerUtility: If , WanVideoVACEEncode, Note, Note, Reroute, SimpleMath+, SimpleMath+, Note, ImageFromBatch, Note, GetNode, GetNode, WanVideoTextEncode, Note, Note, LoadImage, LoadImage, WanVideoVAELoader, LoadWanVideoT5TextEncoder, VHS_LoadVideo, WanVideoModelLoader, VHS_LoadVideo, WanVideoVACEStartToEndFrame, WanVideoVACEModelSelect, Image To Mask, WanVideoLoraSelect, easy forLoopStart, INTConstant, LayerUtility: BooleanOperatorV2]
patterns: []
missing: []
---

# 平台全量/For+WAN2.2-AllInOne 控制+参考 长视频转绘_1965632961276166146.json

> 来源文件 `comfyui_library/workflows/平台全量/For+WAN2.2-AllInOne 控制+参考 长视频转绘_1965632961276166146.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（65 个）：
- `FaceProcessorLoader`
- `GetNode`
- `ApplyFaceProcessor`
- `SetNode`
- `easy forLoopEnd`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `easy imageRemBg`
- `VHS_VideoCombine`
- `easy imageRemBg`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `easy batchAnything`
- `SetNode`
- `GetNode`
- `GetNode`
- `Display Int (rgthree)`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoEncode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoAddStandInLatent`
- `Text Multiline`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `Reroute`
- `Display Int (rgthree)`
- `LayerUtility: If `
- `WanVideoVACEEncode`
- `Note`
- `Note`
- `Reroute`
- `SimpleMath+`
- `SimpleMath+`
- `Note`
- `ImageFromBatch`
- `Note`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEModelSelect`
- `Image To Mask`
- `WanVideoLoraSelect`
- `easy forLoopStart`
- `INTConstant`
- `LayerUtility: BooleanOperatorV2`

## 知识

覆盖率 **62%**（40/65）

**有卡**：`FaceProcessorLoader`、`ApplyFaceProcessor`、`easy forLoopEnd`、`INTConstant`、`easy imageRemBg`、`VHS_VideoCombine`、`WanVideoDecode`、`easy batchAnything`、`Display Int (rgthree)`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoAddStandInLatent`、`Text Multiline`、`LayerUtility: If `、`WanVideoVACEEncode`、`SimpleMath+`、`ImageFromBatch`、`WanVideoTextEncode`、`LoadImage`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEModelSelect`、`Image To Mask`、`easy forLoopStart`、`LayerUtility: BooleanOperatorV2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVACEEncode
