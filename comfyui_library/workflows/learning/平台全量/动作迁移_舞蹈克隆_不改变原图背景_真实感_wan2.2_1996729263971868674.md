---
key: 平台全量/动作迁移_舞蹈克隆_不改变原图背景_真实感_wan2.2_1996729263971868674.json
name: 动作迁移_舞蹈克隆_不改变原图背景_真实感_wan2.2_1996729263971868674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作迁移_舞蹈克隆_不改变原图背景_真实感_wan2.2_1996729263971868674.json
hash: 3185896759053428
coverage: 0.618421
learned_at: 2026-11-14 01:45:34
nodes: [GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SimpleMath+, GetNode, GetNode, GetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, ImageResizeKJv2, ControlNextGetPoses, GetNode, WanVideoControlEmbeds, GetNode, PreviewImage, WanVideoEncode, VHS_VideoCombine, ImageResizeKJv2, GetImageSizeAndCount, SetNode, SetNode, SimpleMath+, Text Multiline, PrimitiveNode, GetNode, WanVideoSLG, GetNode, GetNode, RH_Captioner, Text Concatenate, Text Multiline, WanVideoTextEncode, LoadWanVideoT5TextEncoder, SetNode, SetNode, SetNode, SetNode, Note, Note, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoSetLoRAs, Int, Int, ImpactSwitch, VHS_VideoCombine, VHS_VideoCombine, ImageFromBatch, WanVideoDecode, RHHiddenNodes, VHS_VideoCombine, ColorMatch, ImageConcatMulti, WanVideoSetBlockSwap, WanVideoSetBlockSwap, ShowText|pysssss, WanVideoVAELoader, Primitive float [Crystools], WanVideoSampler, Primitive integer [Crystools], Primitive integer [Crystools], RHHiddenNodes, PrimitiveNode, LoadImage, ImageResizeKJ, Reroute, WanVideoSampler, RHHiddenNodes, VHS_LoadVideo, Primitive integer [Crystools]]
patterns: []
missing: []
---

# 平台全量/动作迁移_舞蹈克隆_不改变原图背景_真实感_wan2.2_1996729263971868674.json

> 来源文件 `comfyui_library/workflows/平台全量/动作迁移_舞蹈克隆_不改变原图背景_真实感_wan2.2_1996729263971868674.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
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
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `PrimitiveNode`
- `LoadImage`
- `ImageResizeKJ`
- `Reroute`
- `WanVideoSampler` ★核心
- `RHHiddenNodes`
- `VHS_LoadVideo`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **62%**（47/76）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`SimpleMath+`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`ControlNextGetPoses`、`WanVideoControlEmbeds`、`WanVideoEncode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`Text Multiline`、`WanVideoSLG`、`RH_Captioner`、`Text Concatenate`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`Int`、`ImageFromBatch`、`WanVideoDecode`、`RHHiddenNodes`、`ColorMatch`、`ImageConcatMulti`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`Primitive float [Crystools]`、`WanVideoSampler`、`Primitive integer [Crystools]`、`LoadImage`、`ImageResizeKJ`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoVAELoader
