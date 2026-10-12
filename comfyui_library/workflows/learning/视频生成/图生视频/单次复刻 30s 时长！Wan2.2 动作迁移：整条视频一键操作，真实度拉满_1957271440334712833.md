---
key: 视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json
name: 单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json
hash: 7019a5b8c14d4490
coverage: 0.429752
learned_at: 2026-10-12 21:05:48
nodes: [GetNode, WanVideoTorchCompileSettings, GetNode, GetNode, GetNode, PrimitiveNode, GetNode, LoadWanVideoT5TextEncoder, SetNode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, Int, WanVideoVAELoader, Primitive float [Crystools], PrimitiveNode, WanVideoBlockSwap, LoadImage, ImageResizeKJv2, GetNode, GetImageSizeAndCount, PreviewImage, ImageResizeKJv2, GetNode, GetNode, Reroute, GetNode, GetNode, PrimitiveNode, GetNode, SetNode, GetImageRangeFromBatch, Reroute, GetNode, RepeatImageBatch, GetImageSizeAndCount, SetNode, Primitive integer [Crystools], ControlNextGetPoses, SetNode, SetNode, GetNode, WanVideoImageToVideoEncode, SimpleMath+, GetNode, Primitive integer [Crystools], VHS_VideoInfoLoaded, Primitive integer [Crystools], SetNode, SimpleMath+, SimpleMath+, SimpleMath+, ImpactSwitch, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ColorMatch, ImageFromBatch, RHHiddenNodes, Note, Text Multiline, SimpleMath+, RHHiddenNodes, GetNode, easy forLoopStart, RHHiddenNodes, GetNode, GetNode, GetNode, easy forLoopEnd, ImageBatchMulti, ImageConcatMulti, WanVideoSLG, ColorMatch, GetNode, Primitive float [Crystools], PrimitiveNode, RHHiddenNodes, GetNode, GetNode, WanVideoControlEmbeds, GetNode, GetNode, GetNode, Text Concatenate, RH_Captioner, GetNode, SetNode, Text Multiline, GetNode, WanVideoTextEncode, SetNode, ShowText|pysssss, ImpactSwitch, WanVideoEncode, WanVideoSampler, WanVideoSampler, ImageConcatMulti, WanVideoSLG, WanVideoEncode, WanVideoControlEmbeds, VHS_VideoCombine, WanVideoImageToVideoEncode, WanVideoSampler, ImageFromBatch, SetNode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoDecode, ImageResizeKJ, Primitive integer [Crystools], VHS_LoadVideo, LoadImage, easy showAnything, LoadImage, MarkdownNote]
patterns: []
missing: [Primitive float [Crystools], Primitive float [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, Text Concatenate, Text Multiline, Text Multiline, easy forLoopEnd, easy forLoopStart]
discoveries: [次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（121 个）：
- `GetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `Int`
- `Int`
- `WanVideoVAELoader`
- `Primitive float [Crystools]`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `Reroute`
- `GetNode`
- `RepeatImageBatch`
- `GetImageSizeAndCount`
- `SetNode`
- `Primitive integer [Crystools]`
- `ControlNextGetPoses`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `GetNode`
- `Primitive integer [Crystools]`
- `VHS_VideoInfoLoaded`
- `Primitive integer [Crystools]`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImpactSwitch`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ColorMatch`
- `ImageFromBatch`
- `RHHiddenNodes`
- `Note`
- `Text Multiline`
- `SimpleMath+`
- `RHHiddenNodes`
- `GetNode`
- `easy forLoopStart`
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy forLoopEnd`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `WanVideoSLG`
- `ColorMatch`
- `GetNode`
- `Primitive float [Crystools]`
- `PrimitiveNode`
- `RHHiddenNodes`
- `GetNode`
- `GetNode`
- `WanVideoControlEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `RH_Captioner`
- `GetNode`
- `SetNode`
- `Text Multiline`
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `ShowText|pysssss`
- `ImpactSwitch`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `WanVideoSLG`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `ImageFromBatch`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageResizeKJ`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `LoadImage`
- `easy showAnything`
- `LoadImage`
- `MarkdownNote`

## 知识

覆盖率 **43%**（52/121）

**有卡**：`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`Int`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadImage`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`RepeatImageBatch`、`ControlNextGetPoses`、`WanVideoImageToVideoEncode`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ColorMatch`、`ImageFromBatch`、`RHHiddenNodes`、`ImageBatchMulti`、`ImageConcatMulti`、`WanVideoSLG`、`WanVideoControlEmbeds`、`RH_Captioner`、`WanVideoTextEncode`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageResizeKJ`、`VHS_LoadVideo`

**缺卡**（16）：`Primitive float [Crystools]`、`Primitive float [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`Text Concatenate`、`Text Multiline`、`Text Multiline`、`easy forLoopEnd`、`easy forLoopStart`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncode

## 学习发现

- 次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive float [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
