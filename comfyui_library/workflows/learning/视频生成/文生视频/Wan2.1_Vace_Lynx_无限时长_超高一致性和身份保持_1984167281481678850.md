---
key: 视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json
name: Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json
hash: 271d7e88507c183d
coverage: 0.485075
learned_at: 2026-10-15 22:47:08
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, SetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, PreviewImage, SetNode, WanVideoTextEncode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoAddLynxEmbeds, GetNode, GetNode, GetNode, FloatConstant, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEStartToEndFrame, PreviewImage, GetNode, GetNode, PreviewAny, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, easy promptLine, INTConstant, INTConstant, INTConstant, WanVideoSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoTextEncode, PreviewAny, WanVideoAddLynxEmbeds, GetNode, GetNode, WanVideoVACEEncode, LynxEncodeFaceIP, GetNode, VHS_VideoCombine, PreviewAny, easy seed, GetNode, WanVideoDecode, GetNode, VHS_VideoCombine, GetNode, GetNode, ImpactMakeImageList, ImageListToImageBatch, INTConstant, Reroute, Reroute, SetNode, easy promptLine, StringConstantMultiline, easy lengthAnything, SetNode, Display Int (rgthree), easy mathInt, easy promptLine, SetNode, SomethingToString, PreviewImage, WanVideoBlockSwap, WanVideoImageResizeToClosest, StringConstantMultiline, PreviewImage, BiRefNetRMBG, Reroute, Note, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, easy forLoopEnd, GetNode, easy indexAnything, easy forLoopStart, easy imageCount, easy mathInt, GetNode, Display Int (rgthree), easy mathInt, Display Int (rgthree), GetNode, GetNode, VHS_VideoCombine, WanVideoDecode, ImpactMakeImageList, PreviewImage, PreviewImage, MaskToImage, ImageListToImageBatch, AutoCropFaces, AutoCropFaces, LoadLynxResampler, easy seed, StringConstantMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（134 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `SetNode`
- `ImageScaleToMaxDimension`
- `ImageScaleToMaxDimension`
- `PreviewImage`
- `SetNode`
- `WanVideoTextEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddLynxEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `easy promptLine`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `PreviewAny`
- `WanVideoAddLynxEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `LynxEncodeFaceIP`
- `GetNode`
- `VHS_VideoCombine`
- `PreviewAny`
- `easy seed`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImpactMakeImageList`
- `ImageListToImageBatch`
- `INTConstant`
- `Reroute`
- `Reroute`
- `SetNode`
- `easy promptLine`
- `StringConstantMultiline`
- `easy lengthAnything`
- `SetNode`
- `Display Int (rgthree)`
- `easy mathInt`
- `easy promptLine`
- `SetNode`
- `SomethingToString`
- `PreviewImage`
- `WanVideoBlockSwap`
- `WanVideoImageResizeToClosest`
- `StringConstantMultiline`
- `PreviewImage`
- `BiRefNetRMBG`
- `Reroute`
- `Note`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `easy forLoopEnd`
- `GetNode`
- `easy indexAnything`
- `easy forLoopStart`
- `easy imageCount`
- `easy mathInt`
- `GetNode`
- `Display Int (rgthree)`
- `easy mathInt`
- `Display Int (rgthree)`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `ImpactMakeImageList`
- `PreviewImage`
- `PreviewImage`
- `MaskToImage`
- `ImageListToImageBatch`
- `AutoCropFaces`
- `AutoCropFaces`
- `LoadLynxResampler` ★核心
- `easy seed`
- `StringConstantMultiline`
- `LoadImage`

## 知识

覆盖率 **49%**（65/134）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageScaleToMaxDimension`、`WanVideoTextEncode`、`WanVideoAddLynxEmbeds`、`FloatConstant`、`WanVideoSampler`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`easy promptLine`、`INTConstant`、`LynxEncodeFaceIP`、`VHS_VideoCombine`、`easy seed`、`WanVideoDecode`、`ImpactMakeImageList`、`ImageListToImageBatch`、`StringConstantMultiline`、`easy lengthAnything`、`Display Int (rgthree)`、`easy mathInt`、`SomethingToString`、`WanVideoBlockSwap`、`WanVideoImageResizeToClosest`、`BiRefNetRMBG`、`WanVideoExtraModelSelect`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`easy forLoopEnd`、`easy indexAnything`、`easy forLoopStart`、`easy imageCount`、`MaskToImage`、`AutoCropFaces`、`LoadLynxResampler`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
