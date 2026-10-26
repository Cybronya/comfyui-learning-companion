---
key: 数字人/数字人/Wan 视频编辑高级版V6.1 test_2035241818312417281.json
name: Wan 视频编辑高级版V6.1 test_2035241818312417281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan 视频编辑高级版V6.1 test_2035241818312417281.json
hash: 65e1b852c0e3d232
coverage: 0.582192
learned_at: 2026-10-26 01:57:45
nodes: [SetNode, Label (rgthree), Label (rgthree), Label (rgthree), SetNode, SetNode, PrimitiveString, GetNode, GetNode, GetNode, GetNode, GetNode, Label (rgthree), SetNode, SetNode, Label (rgthree), Label (rgthree), SetNode, SetNode, SetNode, Label (rgthree), Label (rgthree), SetNode, WanVideoDecode, GetNode, StringConcatenate, StringConcatenate, VHS_VideoInfo, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), Bookmark (rgthree), SetNode, SetNode, GetNode, Bookmark (rgthree), Label (rgthree), VHS_VideoCombine, AddLabel, GetNode, ImageConcatMulti, PlaySound|pysssss, SetNode, SetNode, WanVideoEncode, WanVideoEmptyEmbeds, SDPoseOODLoader, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, Bookmark (rgthree), GetNode, PrimitiveString, SetNode, PrimitiveString, PrimitiveStringMultiline, DWPreprocessor, Any Switch (rgthree), SimpleMath+, SimpleMath+, PoseDetectionVitPoseToDWPose, SetNode, GetImageSizeAndCount, SetNode, GetNode, GetNode, GetNode, OnnxDetectionModelLoader, SetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, GetImageSize, GetNode, easy imagePixelPerfect, SDPoseOODProcessor, LayerUtility: PurgeVRAM V2, ConvertOpenPoseKeypointsToDWPose, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTextEncode, NLFPredict, GetNode, WanVideoBlockSwap, MarkdownNote, WanVideoTorchCompileSettings, SetNode, WanVideoUni3C_embeds, GetImageSize, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, LoadNLFModel, AddLabel, ImageResizeKJ, easy seed, GetImageSizeAndCount, easy compare, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, easy ifElse, SetNode, GetImageRangeFromBatch, GetImageSizeAndCount, LoadWanVideoT5TextEncoder, WanVideoAddSCAILReferenceEmbeds, WanVideoAddSCAILPoseEmbeds, Label (rgthree), SetNode, VHS_VideoCombine, Label (rgthree), GetNode, VHS_VideoCombine, Any Switch (rgthree), Fast Groups Muter (rgthree), GetNode, GetImageSizeAndCount, ImageFromBatch, SimpleMath+, ImageBatch, PrimitiveInt, SimpleMath+, RepeatImageBatch, easy ifElse, YOLOModelLoader, RenderNLFPoses, GetNode, WanVideoSchedulerv2, WanVideoContextOptions, WanVideoSamplerv2, WanVideoSamplerExtraArgs, WanVideoLoraSelectMulti, WanVideoUni3C_ControlnetLoader, Fast Groups Muter (rgthree), easy int, Fast Groups Muter (rgthree), MarkdownNote, VHS_LoadVideo, easy int, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/Wan 视频编辑高级版V6.1 test_2035241818312417281.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan 视频编辑高级版V6.1 test_2035241818312417281.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（146 个）：
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `PrimitiveString`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `StringConcatenate`
- `StringConcatenate`
- `VHS_VideoInfo`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Bookmark (rgthree)`
- `SetNode`
- `SetNode`
- `GetNode`
- `Bookmark (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `AddLabel`
- `GetNode`
- `ImageConcatMulti`
- `PlaySound|pysssss`
- `SetNode`
- `SetNode`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `SDPoseOODLoader`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `Bookmark (rgthree)`
- `GetNode`
- `PrimitiveString`
- `SetNode`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `DWPreprocessor`
- `Any Switch (rgthree)`
- `SimpleMath+`
- `SimpleMath+`
- `PoseDetectionVitPoseToDWPose`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `GetNode`
- `easy imagePixelPerfect`
- `SDPoseOODProcessor`
- `LayerUtility: PurgeVRAM V2`
- `ConvertOpenPoseKeypointsToDWPose`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `NLFPredict`
- `GetNode`
- `WanVideoBlockSwap`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoUni3C_embeds`
- `GetImageSize`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `LoadNLFModel`
- `AddLabel`
- `ImageResizeKJ`
- `easy seed`
- `GetImageSizeAndCount`
- `easy compare`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `easy ifElse`
- `SetNode`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `LoadWanVideoT5TextEncoder`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoAddSCAILPoseEmbeds`
- `Label (rgthree)`
- `SetNode`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `GetNode`
- `VHS_VideoCombine`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `SimpleMath+`
- `ImageBatch`
- `PrimitiveInt`
- `SimpleMath+`
- `RepeatImageBatch`
- `easy ifElse`
- `YOLOModelLoader`
- `RenderNLFPoses`
- `GetNode`
- `WanVideoSchedulerv2`
- `WanVideoContextOptions`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoLoraSelectMulti`
- `WanVideoUni3C_ControlnetLoader`
- `Fast Groups Muter (rgthree)`
- `easy int`
- `Fast Groups Muter (rgthree)`
- `MarkdownNote`
- `VHS_LoadVideo`
- `easy int`
- `LoadImage`

## 知识

覆盖率 **58%**（85/146）

**有卡**：`Label (rgthree)`、`WanVideoDecode`、`StringConcatenate`、`VHS_VideoInfo`、`Bookmark (rgthree)`、`VHS_VideoCombine`、`AddLabel`、`ImageConcatMulti`、`PlaySound|pysssss`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`SDPoseOODLoader`、`GetImageSizeAndCount`、`DWPreprocessor`、`SimpleMath+`、`PoseDetectionVitPoseToDWPose`、`OnnxDetectionModelLoader`、`ImageResizeKJv2`、`GetImageSize`、`easy imagePixelPerfect`、`SDPoseOODProcessor`、`LayerUtility: PurgeVRAM V2`、`ConvertOpenPoseKeypointsToDWPose`、`WanVideoClipVisionEncode`、`WanVideoTextEncode`、`NLFPredict`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoUni3C_embeds`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`LoadNLFModel`、`ImageResizeKJ`、`easy seed`、`easy compare`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`GetImageRangeFromBatch`、`LoadWanVideoT5TextEncoder`、`WanVideoAddSCAILReferenceEmbeds`、`WanVideoAddSCAILPoseEmbeds`、`ImageFromBatch`、`ImageBatch`、`RepeatImageBatch`、`YOLOModelLoader`、`RenderNLFPoses`、`WanVideoSchedulerv2`、`WanVideoContextOptions`、`WanVideoSamplerv2`、`WanVideoSamplerExtraArgs`、`WanVideoLoraSelectMulti`、`WanVideoUni3C_ControlnetLoader`、`easy int`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、ConvertOpenPoseKeypointsToDWPose、WanVideoSamplerv2、WanVideoSamplerExtraArgs、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode
