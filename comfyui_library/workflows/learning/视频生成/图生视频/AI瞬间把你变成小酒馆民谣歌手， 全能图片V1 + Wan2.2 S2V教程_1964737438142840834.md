---
key: 视频生成/图生视频/AI瞬间把你变成小酒馆民谣歌手， 全能图片V1 + Wan2.2 S2V教程_1964737438142840834.json
name: AI瞬间把你变成小酒馆民谣歌手， 全能图片V1 + Wan2.2 S2V教程_1964737438142840834.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1964737438142840834.json
hash: 6a82abb64e8666fe
coverage: 0.569231
learned_at: 2026-10-15 22:31:35
nodes: [WanVideoDecode, WanVideoTorchCompileSettings, Note, Note, MarkdownNote, WanVideoSetLoRAs, WanVideoBlockSwap, Note, WanVideoSetBlockSwap, SetNode, GetNode, WanVideoEmptyEmbeds, GetNode, MelBandRoFormerSampler, NormalizeAudioLoudness, AudioEncoderEncode, MarkdownNote, SetNode, SetNode, GetNode, GetNode, PreviewAny, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, WanVideoEncode, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, MelBandRoFormerModelLoader, AudioEncoderLoader, WanVideoSampler, VHS_LoadVideo, VHS_LoadVideo, ColorMatch, PreviewImage, SetNode, WanVideoAddS2VEmbeds, RH_Nano_Banana_Image2Image, RH_Translator, DWPreprocessor, ImageResizeKJv2, WanVideoEncode, Reroute, LoadImage, ImageResizeKJv2, LoadImage, VHS_VideoCombine, SetNode, Reroute, VHS_VideoCombine, PrimitiveNode, GetNode, PreviewImage, WanVideoTextEncodeCached, ImageResizeKJv2, PrimitiveStringMultiline, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/AI瞬间把你变成小酒馆民谣歌手， 全能图片V1 + Wan2.2 S2V教程_1964737438142840834.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964737438142840834.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（65 个）：
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
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `ColorMatch`
- `PreviewImage`
- `SetNode`
- `WanVideoAddS2VEmbeds`
- `RH_Nano_Banana_Image2Image`
- `RH_Translator`
- `DWPreprocessor`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `Reroute`
- `LoadImage`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `GetNode`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `Label (rgthree)`

## 知识

覆盖率 **57%**（37/65）

**有卡**：`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`AudioEncoderEncode`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`WanVideoEncode`、`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`MelBandRoFormerModelLoader`、`AudioEncoderLoader`、`WanVideoSampler`、`VHS_LoadVideo`、`ColorMatch`、`WanVideoAddS2VEmbeds`、`RH_Nano_Banana_Image2Image`、`RH_Translator`、`DWPreprocessor`、`ImageResizeKJv2`、`LoadImage`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached
