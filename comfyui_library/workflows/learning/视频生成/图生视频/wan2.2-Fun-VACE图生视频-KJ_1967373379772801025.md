---
key: 视频生成/图生视频/wan2.2-Fun-VACE图生视频-KJ_1967373379772801025.json
name: wan2.2-Fun-VACE图生视频-KJ_1967373379772801025.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967373379772801025.json
hash: b938f52d3ceaed4f
coverage: 0.727273
learned_at: 2026-10-15 22:31:41
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, WanVideoSampler, WanVideoBlockSwap, SetNode, SetNode, Reroute, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, INTConstant, INTConstant, WanVideoSampler, GetNode, GetNode, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, WanVideoVACEEncode, GetNode, INTConstant, INTConstant, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, WanVideoVACEStartToEndFrame, LoadImage, Text Multiline, ImageConcatMulti, WanVideoDecode, ColorMatch, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Fun-VACE图生视频-KJ_1967373379772801025.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967373379772801025.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `Reroute`
- `PrimitiveNode`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `WanVideoVACEStartToEndFrame`
- `LoadImage`
- `Text Multiline`
- `ImageConcatMulti`
- `WanVideoDecode`
- `ColorMatch`
- `ImageResizeKJv2`

## 知识

覆盖率 **73%**（32/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoScheduler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoLoraSelectMulti`、`WanVideoVACEStartToEndFrame`、`LoadImage`、`Text Multiline`、`ImageConcatMulti`、`WanVideoDecode`、`ColorMatch`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
