---
key: 视频生成/图生视频/真实感-wan2.2+动作迁移_1955471370547335170.json
name: 真实感-wan2.2+动作迁移_1955471370547335170.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1955471370547335170.json
hash: 60388374f91c0815
coverage: 0.641975
learned_at: 2026-10-15 22:31:08
nodes: [GetNode, SimpleMath+, GetNode, GetNode, GetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, GetNode, WanVideoControlEmbeds, Reroute, GetNode, PreviewImage, WanVideoEncode, ImageResizeKJv2, GetImageSizeAndCount, SetNode, SetNode, SimpleMath+, PrimitiveNode, PrimitiveNode, GetNode, GetNode, Text Concatenate, WanVideoTextEncode, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, SetNode, GetNode, WanVideoImageToVideoEncode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, ImpactSwitch, ImageFromBatch, WanVideoDecode, WanVideoVAELoader, WanVideoLoraSelectMulti, Primitive float [Crystools], LoadImage, WanVideoSampler, RHHiddenNodes, ImageConcatMulti, ColorMatch, WanVideoSampler, WanVideoSLG, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Primitive integer [Crystools], Primitive integer [Crystools], VHS_LoadVideo, Primitive integer [Crystools], Int, Int, Text Multiline, ShowText|pysssss, Text Multiline, GetNode, RH_Captioner, ImageResizeKJ, ControlNextGetPoses, Note, Note, SetNode, ImageResizeKJv2, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoTorchCompileSettings, Int, VHS_VideoCombine, Primitive float [Crystools], Int]
patterns: []
missing: []
---

# 视频生成/图生视频/真实感-wan2.2+动作迁移_1955471370547335170.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1955471370547335170.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（81 个）：
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoInfoLoaded`
- `GetNode`
- `WanVideoControlEmbeds`
- `Reroute`
- `GetNode`
- `PreviewImage`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `ImpactSwitch`
- `ImageFromBatch`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `Primitive float [Crystools]`
- `LoadImage`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `ImageConcatMulti`
- `ColorMatch`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `Primitive integer [Crystools]`
- `Int`
- `Int`
- `Text Multiline`
- `ShowText|pysssss`
- `Text Multiline`
- `GetNode`
- `RH_Captioner`
- `ImageResizeKJ`
- `ControlNextGetPoses`
- `Note`
- `Note`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `Int`
- `VHS_VideoCombine`
- `Primitive float [Crystools]`
- `Int`

## 知识

覆盖率 **64%**（52/81）

**有卡**：`SimpleMath+`、`VHS_VideoInfoLoaded`、`WanVideoControlEmbeds`、`WanVideoEncode`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`Text Concatenate`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`ImageFromBatch`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`Primitive float [Crystools]`、`LoadImage`、`WanVideoSampler`、`RHHiddenNodes`、`ImageConcatMulti`、`ColorMatch`、`WanVideoSLG`、`VHS_VideoCombine`、`Primitive integer [Crystools]`、`VHS_LoadVideo`、`Int`、`Text Multiline`、`RH_Captioner`、`ImageResizeKJ`、`ControlNextGetPoses`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncode
