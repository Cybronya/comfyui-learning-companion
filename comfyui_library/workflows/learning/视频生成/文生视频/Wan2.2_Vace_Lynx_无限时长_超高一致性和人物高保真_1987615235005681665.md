---
key: 视频生成/文生视频/Wan2.2_Vace_Lynx_无限时长_超高一致性和人物高保真_1987615235005681665.json
name: Wan2.2_Vace_Lynx_无限时长_超高一致性和人物高保真_1987615235005681665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2_Vace_Lynx_无限时长_超高一致性和人物高保真_1987615235005681665.json
hash: ad5798bc123ca3b4
coverage: 0.54
learned_at: 2026-10-15 22:47:13
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, SetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, PreviewImage, SetNode, WanVideoTextEncode, SetNode, GetNode, GetNode, GetNode, FloatConstant, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Display Int (rgthree), PreviewImage, SetNode, GetNode, GetNode, GetNode, GetNode, SaveImage, PreviewAny, LynxEncodeFaceIP, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, GetNode, ImpactMakeImageList, ImageListToImageBatch, easy indexAnything, VHS_VideoCombine, GetNode, GetNode, StringConcatenate, easy forLoopEnd, PreviewImage, WanVideoBlockSwap, AutoCropFaces, AutoCropFaces, WanVideoImageResizeToClosest, PreviewImage, BiRefNetRMBG, easy mathInt, GetNode, ImpactMakeAnyList, SetNode, easy promptLine, SetNode, Display Int (rgthree), easy lengthAnything, GetNode, GetNode, MaskToImage, PreviewImage, GetNode, Display Int (rgthree), Reroute, Reroute, WanVideoTextEncode, GetNode, WanVideoDecode, GetNode, easy mathInt, ImageFromBatch, StringConstantMultiline, ImageListToImageBatch, Note, WanVideoVACEStartToEndFrame, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, SetNode, WanVideoBlockSwap, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddLynxEmbeds, WanVideoSampler, ImpactSelectNthItemOfAnyList, WanVideoSampler, WanVideoAddLynxEmbeds, GetNode, GetNode, easy mathInt, GetNode, WanVideoVACEEncode, ImpactSelectNthItemOfAnyList, WanVideoSampler, GetNode, GetNode, GetNode, ImpactMakeImageList, WanVideoVACEEncode, GetNode, SetNode, easy seed, StringConstantMultiline, SetNode, SetNode, PreviewAny, SomethingToString, INTConstant, INTConstant, INTConstant, WanVideoSetLoRAs, INTConstant, INTConstant, easy seed, Reroute, LoadLynxResampler, LoadImage, SetNode, ImageCrop, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoModelLoader, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, StringConstantMultiline, easy forLoopStart, easy mathInt, PreviewImage, easy lengthAnything, PreviewAny]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2_Vace_Lynx_无限时长_超高一致性和人物高保真_1987615235005681665.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2_Vace_Lynx_无限时长_超高一致性和人物高保真_1987615235005681665.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（150 个）：
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
- `GetNode`
- `GetNode`
- `Display Int (rgthree)`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `PreviewAny`
- `LynxEncodeFaceIP`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetNode`
- `ImpactMakeImageList`
- `ImageListToImageBatch`
- `easy indexAnything`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `StringConcatenate`
- `easy forLoopEnd`
- `PreviewImage`
- `WanVideoBlockSwap`
- `AutoCropFaces`
- `AutoCropFaces`
- `WanVideoImageResizeToClosest`
- `PreviewImage`
- `BiRefNetRMBG`
- `easy mathInt`
- `GetNode`
- `ImpactMakeAnyList`
- `SetNode`
- `easy promptLine`
- `SetNode`
- `Display Int (rgthree)`
- `easy lengthAnything`
- `GetNode`
- `GetNode`
- `MaskToImage`
- `PreviewImage`
- `GetNode`
- `Display Int (rgthree)`
- `Reroute`
- `Reroute`
- `WanVideoTextEncode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `easy mathInt`
- `ImageFromBatch`
- `StringConstantMultiline`
- `ImageListToImageBatch`
- `Note`
- `WanVideoVACEStartToEndFrame`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddLynxEmbeds`
- `WanVideoSampler` ★核心
- `ImpactSelectNthItemOfAnyList`
- `WanVideoSampler` ★核心
- `WanVideoAddLynxEmbeds`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `WanVideoVACEEncode`
- `ImpactSelectNthItemOfAnyList`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ImpactMakeImageList`
- `WanVideoVACEEncode`
- `GetNode`
- `SetNode`
- `easy seed`
- `StringConstantMultiline`
- `SetNode`
- `SetNode`
- `PreviewAny`
- `SomethingToString`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoSetLoRAs`
- `INTConstant`
- `INTConstant`
- `easy seed`
- `Reroute`
- `LoadLynxResampler` ★核心
- `LoadImage`
- `SetNode`
- `ImageCrop`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `StringConstantMultiline`
- `easy forLoopStart`
- `easy mathInt`
- `PreviewImage`
- `easy lengthAnything`
- `PreviewAny`

## 知识

覆盖率 **54%**（81/150）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageScaleToMaxDimension`、`WanVideoTextEncode`、`FloatConstant`、`Display Int (rgthree)`、`SaveImage`、`LynxEncodeFaceIP`、`VHS_VideoCombine`、`WanVideoDecode`、`ImpactMakeImageList`、`ImageListToImageBatch`、`easy indexAnything`、`StringConcatenate`、`easy forLoopEnd`、`WanVideoBlockSwap`、`AutoCropFaces`、`WanVideoImageResizeToClosest`、`BiRefNetRMBG`、`easy mathInt`、`ImpactMakeAnyList`、`easy promptLine`、`easy lengthAnything`、`MaskToImage`、`ImageFromBatch`、`StringConstantMultiline`、`WanVideoVACEStartToEndFrame`、`WanVideoSampler`、`WanVideoAddLynxEmbeds`、`ImpactSelectNthItemOfAnyList`、`WanVideoVACEEncode`、`easy seed`、`SomethingToString`、`INTConstant`、`LoadLynxResampler`、`LoadImage`、`ImageCrop`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoExtraModelSelect`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`easy forLoopStart`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
