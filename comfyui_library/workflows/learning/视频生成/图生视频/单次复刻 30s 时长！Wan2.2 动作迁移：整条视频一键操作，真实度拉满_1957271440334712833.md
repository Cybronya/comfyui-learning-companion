---
key: 视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json
name: 单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/单次复刻 30s 时长！Wan2.2 动作迁移：整条视频一键操作，真实度拉满_1957271440334712833.json
hash: 7019a5b8c14d4490
coverage: 0.561983
learned_at: 2026-10-15 22:43:02
nodes: [GetNode, WanVideoTorchCompileSettings, GetNode, GetNode, GetNode, PrimitiveNode, GetNode, LoadWanVideoT5TextEncoder, SetNode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, Int, WanVideoVAELoader, Primitive float [Crystools], PrimitiveNode, WanVideoBlockSwap, LoadImage, ImageResizeKJv2, GetNode, GetImageSizeAndCount, PreviewImage, ImageResizeKJv2, GetNode, GetNode, Reroute, GetNode, GetNode, PrimitiveNode, GetNode, SetNode, GetImageRangeFromBatch, Reroute, GetNode, RepeatImageBatch, GetImageSizeAndCount, SetNode, Primitive integer [Crystools], ControlNextGetPoses, SetNode, SetNode, GetNode, WanVideoImageToVideoEncode, SimpleMath+, GetNode, Primitive integer [Crystools], VHS_VideoInfoLoaded, Primitive integer [Crystools], SetNode, SimpleMath+, SimpleMath+, SimpleMath+, ImpactSwitch, SetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ColorMatch, ImageFromBatch, RHHiddenNodes, Note, Text Multiline, SimpleMath+, RHHiddenNodes, GetNode, easy forLoopStart, RHHiddenNodes, GetNode, GetNode, GetNode, easy forLoopEnd, ImageBatchMulti, ImageConcatMulti, WanVideoSLG, ColorMatch, GetNode, Primitive float [Crystools], PrimitiveNode, RHHiddenNodes, GetNode, GetNode, WanVideoControlEmbeds, GetNode, GetNode, GetNode, Text Concatenate, RH_Captioner, GetNode, SetNode, Text Multiline, GetNode, WanVideoTextEncode, SetNode, ShowText|pysssss, ImpactSwitch, WanVideoEncode, WanVideoSampler, WanVideoSampler, ImageConcatMulti, WanVideoSLG, WanVideoEncode, WanVideoControlEmbeds, VHS_VideoCombine, WanVideoImageToVideoEncode, WanVideoSampler, ImageFromBatch, SetNode, WanVideoDecode, GetNode, WanVideoSampler, WanVideoDecode, ImageResizeKJ, Primitive integer [Crystools], VHS_LoadVideo, LoadImage, easy showAnything, LoadImage, MarkdownNote]
patterns: []
missing: []
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

覆盖率 **56%**（68/121）

**有卡**：`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoSetLoRAs`、`Int`、`WanVideoVAELoader`、`Primitive float [Crystools]`、`WanVideoBlockSwap`、`LoadImage`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`RepeatImageBatch`、`Primitive integer [Crystools]`、`ControlNextGetPoses`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ColorMatch`、`ImageFromBatch`、`RHHiddenNodes`、`Text Multiline`、`easy forLoopStart`、`easy forLoopEnd`、`ImageBatchMulti`、`ImageConcatMulti`、`WanVideoSLG`、`WanVideoControlEmbeds`、`Text Concatenate`、`RH_Captioner`、`WanVideoTextEncode`、`WanVideoEncode`、`WanVideoSampler`、`WanVideoDecode`、`ImageResizeKJ`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoEncode
