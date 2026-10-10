---
key: 视频生成/文生视频/wan2.2  图生视频动作迁移_1956657681140473857.json
name: wan2.2  图生视频动作迁移_1956657681140473857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2  图生视频动作迁移_1956657681140473857.json
hash: ee61ba55889d43d6
coverage: 0.5
learned_at: 2026-10-10 23:09:33
nodes: [GetNode, GetNode, PreviewImage, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ControlNextGetPoses, ImageResizeKJv2, ImageResizeKJ, WanVideoEncode, WanVideoControlEmbeds, SetNode, VHS_VideoInfoLoaded, PrimitiveNode, GetNode, GetNode, GetNode, GetNode, Primitive float [Crystools], WanVideoDecode, PrimitiveNode, Reroute, RHHiddenNodes, GetNode, GetNode, SetNode, VHS_VideoCombine, WanVideoImageToVideoEncode, GetImageSizeAndCount, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LoadImage, SetNode, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], SimpleMath+, SimpleMath+, SimpleMath+, ImpactSwitch, Int, Int, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, SetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, WanVideoTextEncode, WanVideoBlockSwap, WanVideoTorchCompileSettings, RH_Captioner, Text Concatenate, RHHiddenNodes, WanVideoSetBlockSwap, WanVideoSetBlockSwap, ShowText|pysssss, Note, Text Multiline, ColorMatch, ImageFromBatch, RHHiddenNodes, WanVideoSLG, ImageConcatMulti, GetNode, WanVideoSampler, WanVideoSampler, VHS_LoadVideo]
patterns: []
missing: [Primitive float [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], SimpleMath+, SimpleMath+, SimpleMath+, Text Concatenate, Text Multiline]
discoveries: [次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/wan2.2  图生视频动作迁移_1956657681140473857.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2  图生视频动作迁移_1956657681140473857.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（74 个）：
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ControlNextGetPoses`
- `ImageResizeKJv2`
- `ImageResizeKJ`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Primitive float [Crystools]`
- `WanVideoDecode`
- `PrimitiveNode`
- `Reroute`
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `SetNode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImpactSwitch`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `RH_Captioner`
- `Text Concatenate`
- `RHHiddenNodes`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `ShowText|pysssss`
- `Note`
- `Text Multiline`
- `ColorMatch`
- `ImageFromBatch`
- `RHHiddenNodes`
- `WanVideoSLG`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`

## 知识

覆盖率 **50%**（37/74）

**有卡**：`ImageResizeKJv2`、`ControlNextGetPoses`、`ImageResizeKJ`、`WanVideoEncode`、`WanVideoControlEmbeds`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`RHHiddenNodes`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`LoadImage`、`Int`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`RH_Captioner`、`WanVideoSetBlockSwap`、`ColorMatch`、`ImageFromBatch`、`WanVideoSLG`、`ImageConcatMulti`、`WanVideoSampler`、`VHS_LoadVideo`

**缺卡**（9）：`Primitive float [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`Text Concatenate`、`Text Multiline`

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
