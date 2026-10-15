---
key: 视频生成/文生视频/最新wan2.2-文图首尾帧生视频多合一工作-KJ版_1995419541876432898.json
name: 最新wan2.2-文图首尾帧生视频多合一工作-KJ版_1995419541876432898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/最新wan2.2-文图首尾帧生视频多合一工作-KJ版_1995419541876432898.json
hash: 3851a47865e53f3f
coverage: 0.533981
learned_at: 2026-10-15 22:48:48
nodes: [ImageResizeKJv2, Note, SetNode, SetNode, SetNode, SetNode, Bookmark (rgthree), PrimitiveString, StringConcatenate, StringConcatenate, PrimitiveString, GetNode, SetNode, SetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), WanVideoDecode, SetNode, GetNode, easy int, Label (rgthree), Label (rgthree), Label (rgthree), WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, SetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, ImageResizeKJv2, Label (rgthree), easy int, LoadImage, easy int, easy int, GetNode, WanVideoSampler, GetNode, easy int, PrimitiveString, WanVideoBlockSwap, WanVideoTorchCompileSettings, MarkdownNote, easy int, PreviewAny, easy compare, easy ifElse, easy cleanGpuUsed, GetNode, StringLength, LoadImage, RH_Captioner, SetNode, GetNode, PreviewAny, WanVideoTextEncode, WanVideoImageToVideoEncode, PrimitiveStringMultiline, WanVideoModelLoader, VHS_VideoCombine, SetNode, SetNode, GetNode, GetNode, easy anythingIndexSwitch, Mute / Bypass Repeater (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), WanVideoModelLoader, WanVideoModelLoader, easy anythingIndexSwitch, WanVideoModelLoader, easy anythingIndexSwitch, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, SetNode, WanVideoSampler, WanVideoEmptyEmbeds, GetNode, WanVideoImageToVideoEncode, easy anythingIndexSwitch, easy int, easy seed]
patterns: []
missing: []
---

# 视频生成/文生视频/最新wan2.2-文图首尾帧生视频多合一工作-KJ版_1995419541876432898.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/最新wan2.2-文图首尾帧生视频多合一工作-KJ版_1995419541876432898.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（103 个）：
- `ImageResizeKJv2`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Bookmark (rgthree)`
- `PrimitiveString`
- `StringConcatenate`
- `StringConcatenate`
- `PrimitiveString`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoDecode`
- `SetNode`
- `GetNode`
- `easy int`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `Label (rgthree)`
- `easy int`
- `LoadImage`
- `easy int`
- `easy int`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `easy int`
- `PrimitiveString`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `easy int`
- `PreviewAny`
- `easy compare`
- `easy ifElse`
- `easy cleanGpuUsed`
- `GetNode`
- `StringLength`
- `LoadImage`
- `RH_Captioner`
- `SetNode`
- `GetNode`
- `PreviewAny`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `PrimitiveStringMultiline`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy anythingIndexSwitch`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy anythingIndexSwitch`
- `WanVideoModelLoader`
- `easy anythingIndexSwitch`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `easy anythingIndexSwitch`
- `easy int`
- `easy seed`

## 知识

覆盖率 **53%**（55/103）

**有卡**：`ImageResizeKJv2`、`Bookmark (rgthree)`、`StringConcatenate`、`Label (rgthree)`、`WanVideoDecode`、`easy int`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`easy compare`、`easy cleanGpuUsed`、`StringLength`、`RH_Captioner`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Relay (rgthree)`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
