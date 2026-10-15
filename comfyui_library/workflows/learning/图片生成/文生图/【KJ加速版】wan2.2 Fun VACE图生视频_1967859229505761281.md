---
key: 图片生成/文生图/【KJ加速版】wan2.2 Fun VACE图生视频_1967859229505761281.json
name: 【KJ加速版】wan2.2 Fun VACE图生视频_1967859229505761281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【KJ加速版】wan2.2 Fun VACE图生视频_1967859229505761281.json
hash: 645fee60487a3a3e
coverage: 0.714286
learned_at: 2026-10-10 20:59:29
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, WanVideoSampler, WanVideoBlockSwap, SetNode, SetNode, Reroute, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, ImageConcatMulti, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, INTConstant, INTConstant, WanVideoSampler, GetNode, GetNode, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, WanVideoVACEEncode, GetNode, INTConstant, INTConstant, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, ImageResizeKJv2, WanVideoVACEStartToEndFrame, LoadImage, Text Multiline]
patterns: []
missing: [Text Multiline]
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/【KJ加速版】wan2.2 Fun VACE图生视频_1967859229505761281.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【KJ加速版】wan2.2 Fun VACE图生视频_1967859229505761281.json`

## 结构

**节点**（42 个）：
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoSampler`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `Reroute`
- `PrimitiveNode`
- `SetNode`
- `WanVideoScheduler`
- `SetNode`
- `ImageConcatMulti`
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler`
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
- `ImageResizeKJv2`
- `WanVideoVACEStartToEndFrame`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **71%**（30/42）

**有卡**：`GetNode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`Note`、`WanVideoSampler`、`WanVideoBlockSwap`、`SetNode`、`Reroute`、`PrimitiveNode`、`WanVideoScheduler`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`

**缺卡**（1）：`Text Multiline`

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
