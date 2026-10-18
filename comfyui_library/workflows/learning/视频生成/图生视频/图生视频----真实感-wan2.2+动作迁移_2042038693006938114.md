---
key: 视频生成/图生视频/图生视频----真实感-wan2.2+动作迁移_2042038693006938114.json
name: 图生视频----真实感-wan2.2+动作迁移_2042038693006938114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频----真实感-wan2.2+动作迁移_2042038693006938114.json
hash: 6c75b6199cd2d8ed
coverage: 0.61039
learned_at: 2026-10-15 22:36:23
nodes: [GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SimpleMath+, GetNode, GetNode, GetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, ImageResizeKJv2, ControlNextGetPoses, GetNode, WanVideoControlEmbeds, Reroute, GetNode, PreviewImage, WanVideoEncode, VHS_VideoCombine, ImageResizeKJv2, GetImageSizeAndCount, SetNode, SetNode, SimpleMath+, Text Multiline, PrimitiveNode, GetNode, WanVideoSLG, GetNode, GetNode, RH_Captioner, Text Concatenate, Text Multiline, WanVideoTextEncode, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, SetNode, Note, Note, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, Int, ImpactSwitch, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch, WanVideoDecode, RHHiddenNodes, VHS_VideoCombine, ColorMatch, ImageConcatMulti, WanVideoSetBlockSwap, WanVideoSetBlockSwap, ShowText|pysssss, WanVideoVAELoader, Primitive float [Crystools], WanVideoSampler, VHS_LoadVideo, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], RHHiddenNodes, WanVideoSampler, RHHiddenNodes, PrimitiveNode, ImageResizeKJ, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频----真实感-wan2.2+动作迁移_2042038693006938114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042038693006938114.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoInfoLoaded`
- `ImageResizeKJv2`
- `ControlNextGetPoses`
- `GetNode`
- `WanVideoControlEmbeds`
- `Reroute`
- `GetNode`
- `PreviewImage`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `Text Multiline`
- `PrimitiveNode`
- `GetNode`
- `WanVideoSLG`
- `GetNode`
- `GetNode`
- `RH_Captioner`
- `Text Concatenate`
- `Text Multiline`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `Int`
- `Int`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `WanVideoDecode`
- `RHHiddenNodes`
- `VHS_VideoCombine`
- `ColorMatch`
- `ImageConcatMulti`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `ShowText|pysssss`
- `WanVideoVAELoader`
- `Primitive float [Crystools]`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `PrimitiveNode`
- `ImageResizeKJ`
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **61%**（47/77）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`ControlNextGetPoses`、`WanVideoControlEmbeds`、`WanVideoEncode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`Text Multiline`、`WanVideoSLG`、`RH_Captioner`、`Text Concatenate`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`Int`、`ImageFromBatch`、`WanVideoDecode`、`RHHiddenNodes`、`ColorMatch`、`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`Primitive float [Crystools]`、`WanVideoSampler`、`VHS_LoadVideo`、`Primitive integer [Crystools]`、`ImageResizeKJ`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncode
