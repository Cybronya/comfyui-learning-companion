---
key: 视频生成/图生视频/wan2.2+动作迁移_1958329470274977793.json
name: wan2.2+动作迁移_1958329470274977793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2+动作迁移_1958329470274977793.json
hash: 7db71a9f005ae7e3
coverage: 0.674419
learned_at: 2026-10-15 22:31:21
nodes: [GetNode, SimpleMath+, GetNode, GetNode, SetNode, SetNode, SimpleMath+, VHS_VideoInfoLoaded, ImageResizeKJv2, ControlNextGetPoses, GetNode, WanVideoControlEmbeds, Reroute, GetNode, PreviewImage, WanVideoEncode, VHS_VideoCombine, ImageResizeKJv2, GetImageSizeAndCount, SetNode, SetNode, SimpleMath+, Text Multiline, PrimitiveNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, Int, Int, ImpactSwitch, ImageResizeKJ, VHS_VideoCombine, ImageFromBatch, Primitive float [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], PrimitiveNode, ImpactInt, Primitive float [Crystools], SetNode, VHS_VideoCombine, Primitive integer [Crystools], WanVideoSampler, WanVideoSampler, VHS_VideoCombine, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, GetNode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoDecode, ImageConcatMulti, GetNode, ColorMatch, WanVideoSLG, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, LayerUtility: PurgeVRAM V2, ImageUpscaleWithModel, GetImageSizeAndCount, easy showAnything, VHS_LoadVideo, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetLoRAs, Text Multiline, ShowText|pysssss, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, Text Concatenate, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2+动作迁移_1958329470274977793.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958329470274977793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（86 个）：
- `GetNode`
- `SimpleMath+`
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
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Int`
- `Int`
- `ImpactSwitch`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `Primitive float [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `PrimitiveNode`
- `ImpactInt`
- `Primitive float [Crystools]`
- `SetNode`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `ImageConcatMulti`
- `GetNode`
- `ColorMatch`
- `WanVideoSLG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UpscaleModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `ImageUpscaleWithModel`
- `GetImageSizeAndCount`
- `easy showAnything`
- `VHS_LoadVideo`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `Text Multiline`
- `ShowText|pysssss`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `Text Concatenate`
- `LoadImage`

## 知识

覆盖率 **67%**（58/86）

**有卡**：`SimpleMath+`、`VHS_VideoInfoLoaded`、`ImageResizeKJv2`、`ControlNextGetPoses`、`WanVideoControlEmbeds`、`WanVideoEncode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`Text Multiline`、`WanVideoImageToVideoEncode`、`Int`、`ImageResizeKJ`、`ImageFromBatch`、`Primitive float [Crystools]`、`Primitive integer [Crystools]`、`ImpactInt`、`WanVideoSampler`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoDecode`、`ImageConcatMulti`、`ColorMatch`、`WanVideoSLG`、`LayerUtility: ImageScaleByAspectRatio V2`、`UpscaleModelLoader`、`LayerUtility: PurgeVRAM V2`、`ImageUpscaleWithModel`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`Text Concatenate`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
