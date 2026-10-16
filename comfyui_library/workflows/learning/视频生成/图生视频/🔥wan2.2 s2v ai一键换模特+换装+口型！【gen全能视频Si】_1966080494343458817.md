---
key: 视频生成/图生视频/🔥wan2.2 s2v ai一键换模特+换装+口型！【gen全能视频Si】_1966080494343458817.json
name: 🔥wan2.2 s2v ai一键换模特+换装+口型！【gen全能视频Si】_1966080494343458817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1966080494343458817.json
hash: f9df79020dcd54f0
coverage: 0.5625
learned_at: 2026-10-15 22:31:38
nodes: [WanVideoDecode, WanVideoTorchCompileSettings, Note, Note, MarkdownNote, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, AudioEncoderEncode, MarkdownNote, SetNode, SetNode, GetImageSizeAndCount, GetImageRangeFromBatch, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, MelBandRoFormerModelLoader, AudioEncoderLoader, WanVideoSampler, WanVideoTextEncodeCached, ImageResizeKJv2, WanVideoAddS2VEmbeds, PreviewImage, RH_Nano_Banana_Image2Image, ImageResizeKJv2, PreviewImage, SetNode, ColorMatch, GetNode, MelBandRoFormerSampler, NormalizeAudioLoudness, GetNode, GetNode, SetNode, PreviewAny, PrimitiveNode, WanVideoEncode, WanVideoEmptyEmbeds, INTConstant, INTConstant, PrimitiveStringMultiline, LoadImage, VHS_LoadVideo, GetNode, GetNode, Reroute, VHS_LoadVideo, GetNode, ImageResizeKJv2, VHS_VideoCombine, WanVideoEncode, Reroute, GetNode, LoadImage, SetNode, Note, Note, DWPreprocessor, RH_Translator, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/🔥wan2.2 s2v ai一键换模特+换装+口型！【gen全能视频Si】_1966080494343458817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1966080494343458817.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（64 个）：
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `AudioEncoderEncode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `MelBandRoFormerModelLoader`
- `AudioEncoderLoader`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `WanVideoAddS2VEmbeds`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `ColorMatch`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAny`
- `PrimitiveNode`
- `WanVideoEncode`
- `WanVideoEmptyEmbeds`
- `INTConstant`
- `INTConstant`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `Reroute`
- `VHS_LoadVideo`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `Reroute`
- `GetNode`
- `LoadImage`
- `SetNode`
- `Note`
- `Note`
- `DWPreprocessor`
- `RH_Translator`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（36/64）

**有卡**：`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`AudioEncoderEncode`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`MelBandRoFormerModelLoader`、`AudioEncoderLoader`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`WanVideoAddS2VEmbeds`、`RH_Nano_Banana_Image2Image`、`ColorMatch`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`INTConstant`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`、`DWPreprocessor`、`RH_Translator`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached
