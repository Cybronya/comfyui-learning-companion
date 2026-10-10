---
key: 视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json
name: Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.1_Vace_Lynx_无限时长_超高一致性和身份保持_1984167281481678850.json
hash: 271d7e88507c183d
coverage: 0.365672
learned_at: 2026-10-11 02:45:02
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, SetNode, ImageScaleToMaxDimension, ImageScaleToMaxDimension, PreviewImage, SetNode, WanVideoTextEncode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoAddLynxEmbeds, GetNode, GetNode, GetNode, FloatConstant, SetNode, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, WanVideoTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEStartToEndFrame, PreviewImage, GetNode, GetNode, PreviewAny, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, easy promptLine, INTConstant, INTConstant, INTConstant, WanVideoSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoTextEncode, PreviewAny, WanVideoAddLynxEmbeds, GetNode, GetNode, WanVideoVACEEncode, LynxEncodeFaceIP, GetNode, VHS_VideoCombine, PreviewAny, easy seed, GetNode, WanVideoDecode, GetNode, VHS_VideoCombine, GetNode, GetNode, ImpactMakeImageList, ImageListToImageBatch, INTConstant, Reroute, Reroute, SetNode, easy promptLine, StringConstantMultiline, easy lengthAnything, SetNode, Display Int (rgthree), easy mathInt, easy promptLine, SetNode, SomethingToString, PreviewImage, WanVideoBlockSwap, WanVideoImageResizeToClosest, StringConstantMultiline, PreviewImage, BiRefNetRMBG, Reroute, Note, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, easy forLoopEnd, GetNode, easy indexAnything, easy forLoopStart, easy imageCount, easy mathInt, GetNode, Display Int (rgthree), easy mathInt, Display Int (rgthree), GetNode, GetNode, VHS_VideoCombine, WanVideoDecode, ImpactMakeImageList, PreviewImage, PreviewImage, MaskToImage, ImageListToImageBatch, AutoCropFaces, AutoCropFaces, LoadLynxResampler, easy seed, StringConstantMultiline, LoadImage]
patterns: []
missing: [Display Int (rgthree), Display Int (rgthree), Display Int (rgthree), easy forLoopEnd, easy forLoopStart, easy imageCount, easy indexAnything, easy lengthAnything, easy mathInt, easy mathInt, easy mathInt, easy promptLine, easy promptLine, easy promptLine, easy seed, easy seed]
discoveries: [次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识, 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **37%**（49/134）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageScaleToMaxDimension`、`WanVideoTextEncode`、`WanVideoAddLynxEmbeds`、`FloatConstant`、`WanVideoSampler`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`INTConstant`、`LynxEncodeFaceIP`、`VHS_VideoCombine`、`WanVideoDecode`、`ImpactMakeImageList`、`ImageListToImageBatch`、`StringConstantMultiline`、`SomethingToString`、`WanVideoBlockSwap`、`WanVideoImageResizeToClosest`、`BiRefNetRMBG`、`WanVideoExtraModelSelect`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`MaskToImage`、`AutoCropFaces`、`LoadLynxResampler`、`LoadImage`

**缺卡**（16）：`Display Int (rgthree)`、`Display Int (rgthree)`、`Display Int (rgthree)`、`easy forLoopEnd`、`easy forLoopStart`、`easy imageCount`、`easy indexAnything`、`easy lengthAnything`、`easy mathInt`、`easy mathInt`、`easy mathInt`、`easy promptLine`、`easy promptLine`、`easy promptLine`、`easy seed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadLynxResampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode

## 学习发现

- 次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Display Int (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageCount` 知识库中没有该节点类型的任何知识
- 次要节点 `easy indexAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy lengthAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy mathInt` 知识库中没有该节点类型的任何知识
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy promptLine` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
