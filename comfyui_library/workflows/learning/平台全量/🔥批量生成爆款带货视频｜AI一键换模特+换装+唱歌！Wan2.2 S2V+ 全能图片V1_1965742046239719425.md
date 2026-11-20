---
key: 平台全量/🔥批量生成爆款带货视频｜AI一键换模特+换装+唱歌！Wan2.2 S2V+ 全能图片V1_1965742046239719425.json
name: 🔥批量生成爆款带货视频｜AI一键换模特+换装+唱歌！Wan2.2 S2V+ 全能图片V1_1965742046239719425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/🔥批量生成爆款带货视频｜AI一键换模特+换装+唱歌！Wan2.2 S2V+ 全能图片V1_1965742046239719425.json
hash: 6cfc79a1d31b45dc
coverage: 0.575758
learned_at: 2026-11-14 02:55:12
nodes: [WanVideoDecode, WanVideoTorchCompileSettings, Note, Note, MarkdownNote, WanVideoSetLoRAs, WanVideoBlockSwap, Note, WanVideoSetBlockSwap, SetNode, GetNode, WanVideoEmptyEmbeds, GetNode, MelBandRoFormerSampler, NormalizeAudioLoudness, AudioEncoderEncode, MarkdownNote, SetNode, SetNode, GetNode, GetNode, PreviewAny, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, WanVideoEncode, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, MelBandRoFormerModelLoader, AudioEncoderLoader, WanVideoSampler, ColorMatch, ImageResizeKJv2, WanVideoEncode, Reroute, SetNode, Reroute, VHS_VideoCombine, WanVideoTextEncodeCached, ImageResizeKJv2, DWPreprocessor, VHS_VideoCombine, PrimitiveStringMultiline, VHS_LoadVideo, PrimitiveNode, WanVideoAddS2VEmbeds, GetNode, SetNode, PreviewImage, VHS_LoadVideo, RH_Nano_Banana_Image2Image, RH_Translator, LoadImage, ImageResizeKJv2, PreviewImage, VHS_LoadVideo, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/🔥批量生成爆款带货视频｜AI一键换模特+换装+唱歌！Wan2.2 S2V+ 全能图片V1_1965742046239719425.json

> 来源文件 `comfyui_library/workflows/平台全量/🔥批量生成爆款带货视频｜AI一键换模特+换装+唱歌！Wan2.2 S2V+ 全能图片V1_1965742046239719425.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（66 个）：
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `AudioEncoderEncode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `WanVideoEncode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `MelBandRoFormerModelLoader`
- `AudioEncoderLoader`
- `WanVideoSampler` ★核心
- `ColorMatch`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `Reroute`
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `PrimitiveNode`
- `WanVideoAddS2VEmbeds`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `VHS_LoadVideo`
- `RH_Nano_Banana_Image2Image`
- `RH_Translator`
- `LoadImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_LoadVideo`
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **58%**（38/66）

**有卡**：`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`AudioEncoderEncode`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`WanVideoEncode`、`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`MelBandRoFormerModelLoader`、`AudioEncoderLoader`、`WanVideoSampler`、`ColorMatch`、`ImageResizeKJv2`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`DWPreprocessor`、`VHS_LoadVideo`、`WanVideoAddS2VEmbeds`、`RH_Nano_Banana_Image2Image`、`RH_Translator`、`LoadImage`、`Label (rgthree)`

**用到的条目**：LoadImage、MelBandRoFormerSampler、WanVideoSampler、AudioEncoderEncode、AudioEncoderLoader、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached
