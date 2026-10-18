---
key: 视频生成/图生视频/视频生成_无限时长_SVI_2.0_Pro_Bindweave_2000126705077452802.json
name: 视频生成_无限时长_SVI_2.0_Pro_Bindweave_2000126705077452802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频生成_无限时长_SVI_2.0_Pro_Bindweave_2000126705077452802.json
hash: 831262e1130eace6
coverage: 0.502439
learned_at: 2026-10-15 22:33:39
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, SetNode, LoadWanVideoT5TextEncoder, CLIPVisionLoader, WanVideoVAELoader, WanVideoBlockSwap, SetNode, SetNode, PreviewAny, SetNode, SetNode, FloatConstant, SetNode, SetNode, easy seed, easy seed, SetNode, SetNode, SetNode, WanVideoImageResizeToClosest, SetNode, easy boolean, PreviewImage, WanVideoImageResizeToClosest, GetNode, PreviewAny, ImpactMinMax, StringConcatenate, GetNode, StringConcatenate, PreviewAny, SaveImage, GetNode, ImageConcanate, ImageScaleBy, GetNode, ImageBatchMulti, SaveImage, Create Grid Image from Batch, INTConstant, EmptyImage, GetNode, GetNode, RepeatImageBatch, VHS_VideoCombine, GIMMVFI_interpolate, GetNode, GetNode, Reroute, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, DownloadAndLoadGIMMVFIModel, WanVideoTorchCompileSettings, SetNode, WanVideoLoraSelectMulti, SetNode, ImageScaleToMaxDimension, GetImageSizeAndCount, ImageScaleToMaxDimension, easy ifElse, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, SetNode, WanVideoEncodeLatentBatch, SetNode, VHS_VideoCombine, SomethingToString, FloatConstant, WanVideoModelLoader, SetNode, InvertMask, INTConstant, GetNode, INTConstant, StringConstantMultiline, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, WanVideoImageToVideoEncode, ImageFromBatch, GetNode, WanVideoClipVisionEncode, easy mathInt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, WanVideoEncodeLatentBatch, WanVideoAddBindweaveEmbeds, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetImageSizeAndCount, VHS_VideoCombine, ImageBatchMulti, GetNode, WanVideoSampler, Reroute, Reroute, easy compare, easy compare, INTConstant, GetNode, GetNode, GetNode, Display Int (rgthree), Display Int (rgthree), Reroute, easy mathInt, easy ifElse, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, GetNode, Reroute, Reroute, Reroute, Reroute, SetNode, SetNode, WanVideoSampler, easy promptLine, GetNode, WanVideoTextEncode, ImpactMakeAnyList, SetNode, SetNode, PreviewAny, easy lengthAnything, AILab_Preview, AILab_Preview, ImageBatchExtendWithOverlap, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoLoraSelect, GetNode, GetNode, ImpactSelectNthItemOfAnyList, WanVideoImageToVideoEncode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, GetNode, ImpactSelectNthItemOfAnyList, GetNode, Reroute, ImageBatchMulti, GetNode, WanVideoEncodeLatentBatch, WanVideoAddBindweaveEmbeds, WanVideoSampler, PreviewImage, Reroute, Reroute, Reroute, Reroute, VHS_VideoCombine, GetNode, INTConstant, INTConstant, WanVideoSVIProEmbeds, WanVideoSVIProEmbeds, Reroute, PrimitiveStringMultiline, PrimitiveStringMultiline, ImageConcanate, WanVideoLoraSelect, BiRefNetRMBG, ImageResizeKJv2, LoadImage, easy int, LoadImage, WanVideoModelLoader, AILab_Preview, Reroute, easy whileLoopStart, easy whileLoopEnd]
patterns: []
missing: []
---

# 视频生成/图生视频/视频生成_无限时长_SVI_2.0_Pro_Bindweave_2000126705077452802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000126705077452802.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（205 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `PreviewAny`
- `SetNode`
- `SetNode`
- `FloatConstant`
- `SetNode`
- `SetNode`
- `easy seed`
- `easy seed`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoImageResizeToClosest`
- `SetNode`
- `easy boolean`
- `PreviewImage`
- `WanVideoImageResizeToClosest`
- `GetNode`
- `PreviewAny`
- `ImpactMinMax`
- `StringConcatenate`
- `GetNode`
- `StringConcatenate`
- `PreviewAny`
- `SaveImage`
- `GetNode`
- `ImageConcanate`
- `ImageScaleBy`
- `GetNode`
- `ImageBatchMulti`
- `SaveImage`
- `Create Grid Image from Batch`
- `INTConstant`
- `EmptyImage`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `GetNode`
- `GetNode`
- `Reroute`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `DownloadAndLoadGIMMVFIModel`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `ImageScaleToMaxDimension`
- `GetImageSizeAndCount`
- `ImageScaleToMaxDimension`
- `easy ifElse`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `WanVideoEncodeLatentBatch`
- `SetNode`
- `VHS_VideoCombine`
- `SomethingToString`
- `FloatConstant`
- `WanVideoModelLoader`
- `SetNode`
- `InvertMask`
- `INTConstant`
- `GetNode`
- `INTConstant`
- `StringConstantMultiline`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `ImageFromBatch`
- `GetNode`
- `WanVideoClipVisionEncode`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoEncodeLatentBatch`
- `WanVideoAddBindweaveEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `ImageBatchMulti`
- `GetNode`
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `easy compare`
- `easy compare`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `Reroute`
- `easy mathInt`
- `easy ifElse`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `easy promptLine`
- `GetNode`
- `WanVideoTextEncode`
- `ImpactMakeAnyList`
- `SetNode`
- `SetNode`
- `PreviewAny`
- `easy lengthAnything`
- `AILab_Preview`
- `AILab_Preview`
- `ImageBatchExtendWithOverlap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `ImpactSelectNthItemOfAnyList`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `ImpactSelectNthItemOfAnyList`
- `GetNode`
- `Reroute`
- `ImageBatchMulti`
- `GetNode`
- `WanVideoEncodeLatentBatch`
- `WanVideoAddBindweaveEmbeds`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `WanVideoSVIProEmbeds`
- `WanVideoSVIProEmbeds`
- `Reroute`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ImageConcanate`
- `WanVideoLoraSelect`
- `BiRefNetRMBG`
- `ImageResizeKJv2`
- `LoadImage`
- `easy int`
- `LoadImage`
- `WanVideoModelLoader`
- `AILab_Preview`
- `Reroute`
- `easy whileLoopStart`
- `easy whileLoopEnd`

## 知识

覆盖率 **50%**（103/205）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`FloatConstant`、`easy seed`、`WanVideoImageResizeToClosest`、`easy boolean`、`ImpactMinMax`、`StringConcatenate`、`SaveImage`、`ImageConcanate`、`ImageScaleBy`、`ImageBatchMulti`、`Create Grid Image from Batch`、`INTConstant`、`EmptyImage`、`RepeatImageBatch`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`DownloadAndLoadGIMMVFIModel`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`ImageScaleToMaxDimension`、`GetImageSizeAndCount`、`WanVideoEncodeLatentBatch`、`SomethingToString`、`WanVideoModelLoader`、`InvertMask`、`StringConstantMultiline`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`easy mathInt`、`WanVideoSampler`、`WanVideoAddBindweaveEmbeds`、`easy compare`、`Display Int (rgthree)`、`easy promptLine`、`WanVideoTextEncode`、`ImpactMakeAnyList`、`easy lengthAnything`、`AILab_Preview`、`ImageBatchExtendWithOverlap`、`WanVideoLoraSelect`、`ImpactSelectNthItemOfAnyList`、`WanVideoSVIProEmbeds`、`BiRefNetRMBG`、`ImageResizeKJv2`、`LoadImage`、`easy int`、`easy whileLoopStart`、`easy whileLoopEnd`

**用到的条目**：LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode
