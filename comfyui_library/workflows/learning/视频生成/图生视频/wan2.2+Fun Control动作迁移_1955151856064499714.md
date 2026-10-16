---
key: 视频生成/图生视频/wan2.2+Fun Control动作迁移_1955151856064499714.json
name: wan2.2+Fun Control动作迁移_1955151856064499714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955151856064499714.json
hash: 0248d5a8266423d5
coverage: 0.622951
learned_at: 2026-10-15 22:31:07
nodes: [Reroute, Reroute, GetNode, ImageConcatMulti, GetNode, Reroute, PrimitiveNode, PrimitiveNode, WanVideoControlEmbeds, PrimitiveNode, GetNode, PrimitiveNode, GetImageSizeAndCount, ControlNextGetPoses, ImageResizeKJv2, SetNode, WanVideoEncode, GetNode, VHS_VideoCombine, ImageResizeKJ, GetNode, ImageResizeKJv2, PreviewImage, PreviewImage, WanVideoImageToVideoEncode, WanVideoDecode, WanVideoSampler, WanVideoSampler, LoadImage, WanVideoVAELoader, SetNode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoEmptyEmbeds, LoadWanVideoT5TextEncoder, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, Note, VHS_VideoCombine, VHS_VideoCombine, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoTextEncode, Primitive integer [Crystools], Text Multiline, Note, Note, Note, Note, SimpleMath+, SimpleMath+, VHS_VideoInfoLoaded, SetNode, easy showAnything, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2+Fun Control动作迁移_1955151856064499714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955151856064499714.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（61 个）：
- `Reroute`
- `Reroute`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `Reroute`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoControlEmbeds`
- `PrimitiveNode`
- `GetNode`
- `PrimitiveNode`
- `GetImageSizeAndCount`
- `ControlNextGetPoses`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoEncode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoEmptyEmbeds`
- `LoadWanVideoT5TextEncoder`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `Note`
- `Note`
- `Note`
- `Note`
- `SimpleMath+`
- `SimpleMath+`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `easy showAnything`
- `VHS_LoadVideo`

## 知识

覆盖率 **62%**（38/61）

**有卡**：`ImageConcatMulti`、`WanVideoControlEmbeds`、`GetImageSizeAndCount`、`ControlNextGetPoses`、`ImageResizeKJv2`、`WanVideoEncode`、`VHS_VideoCombine`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`WanVideoDecode`、`WanVideoSampler`、`LoadImage`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoEmptyEmbeds`、`LoadWanVideoT5TextEncoder`、`RHHiddenNodes`、`Primitive integer [Crystools]`、`WanVideoTextEncode`、`Text Multiline`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncode
