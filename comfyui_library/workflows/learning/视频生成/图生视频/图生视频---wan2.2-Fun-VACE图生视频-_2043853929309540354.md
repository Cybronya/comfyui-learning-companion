---
key: 视频生成/图生视频/图生视频---wan2.2-Fun-VACE图生视频-_2043853929309540354.json
name: 图生视频---wan2.2-Fun-VACE图生视频-_2043853929309540354.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频---wan2.2-Fun-VACE图生视频-_2043853929309540354.json
hash: 678bf0a052303bba
coverage: 0.727273
learned_at: 2026-10-15 22:36:34
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, Note, WanVideoSampler, WanVideoBlockSwap, SetNode, SetNode, Reroute, PrimitiveNode, SetNode, WanVideoScheduler, SetNode, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVACEModelSelect, INTConstant, INTConstant, WanVideoSampler, GetNode, GetNode, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, WanVideoVACEEncode, GetNode, INTConstant, INTConstant, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, WanVideoVACEStartToEndFrame, ImageConcatMulti, WanVideoDecode, ColorMatch, ImageResizeKJv2, LoadImage, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频---wan2.2-Fun-VACE图生视频-_2043853929309540354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043853929309540354.json`

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
- `ImageConcatMulti`
- `WanVideoDecode`
- `ColorMatch`
- `ImageResizeKJv2`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **73%**（32/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoScheduler`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoLoraSelectMulti`、`WanVideoVACEStartToEndFrame`、`ImageConcatMulti`、`WanVideoDecode`、`ColorMatch`、`ImageResizeKJv2`、`LoadImage`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
