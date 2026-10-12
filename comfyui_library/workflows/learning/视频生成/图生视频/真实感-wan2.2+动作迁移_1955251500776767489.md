---
key: 视频生成/图生视频/真实感-wan2.2+动作迁移_1955251500776767489.json
name: 真实感-wan2.2+动作迁移_1955251500776767489
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/真实感-wan2.2+动作迁移_1955251500776767489.json
hash: a6f1fe23868a2208
coverage: 0.493671
learned_at: 2026-10-12 21:05:48
nodes: [GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SimpleMath+, GetNode, GetNode, GetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, ImageResizeKJv2, ControlNextGetPoses, GetNode, WanVideoControlEmbeds, Reroute, GetNode, PreviewImage, WanVideoEncode, VHS_VideoCombine, ImageResizeKJv2, GetImageSizeAndCount, SetNode, SetNode, SimpleMath+, Text Multiline, PrimitiveNode, GetNode, WanVideoSLG, GetNode, GetNode, RH_Captioner, Text Concatenate, Text Multiline, WanVideoTextEncode, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, SetNode, Note, Note, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, Int, ImpactSwitch, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch, WanVideoDecode, RHHiddenNodes, VHS_VideoCombine, ColorMatch, ImageConcatMulti, WanVideoSetBlockSwap, WanVideoSetBlockSwap, ShowText|pysssss, WanVideoVAELoader, Primitive float [Crystools], WanVideoSampler, VHS_LoadVideo, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], RHHiddenNodes, WanVideoSampler, RHHiddenNodes, PrimitiveNode, LoadImage, ImageResizeKJ, MarkdownNote, LoadImage, LoadImage]
patterns: []
missing: [Primitive float [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], SimpleMath+, SimpleMath+, SimpleMath+, Text Concatenate, Text Multiline, Text Multiline]
discoveries: [次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/真实感-wan2.2+动作迁移_1955251500776767489.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/真实感-wan2.2+动作迁移_1955251500776767489.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（79 个）：
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
- `LoadImage`
- `ImageResizeKJ`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **49%**（39/79）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`ControlNextGetPoses`、`WanVideoControlEmbeds`、`WanVideoEncode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoSLG`、`RH_Captioner`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`Int`、`ImageFromBatch`、`WanVideoDecode`、`RHHiddenNodes`、`ColorMatch`、`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`ImageResizeKJ`

**缺卡**（10）：`Primitive float [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`Text Concatenate`、`Text Multiline`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncode

## 学习发现

- 次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
