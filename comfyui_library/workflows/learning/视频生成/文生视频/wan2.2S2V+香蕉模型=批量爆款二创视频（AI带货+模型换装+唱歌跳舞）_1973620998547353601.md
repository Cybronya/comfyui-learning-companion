---
key: 视频生成/文生视频/wan2.2S2V+香蕉模型=批量爆款二创视频（AI带货+模型换装+唱歌跳舞）_1973620998547353601.json
name: wan2.2S2V+香蕉模型=批量爆款二创视频（AI带货+模型换装+唱歌跳舞）_1973620998547353601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2S2V+香蕉模型=批量爆款二创视频（AI带货+模型换装+唱歌跳舞）_1973620998547353601.json
hash: 361b86717614c397
coverage: 0.5625
learned_at: 2026-10-10 23:09:40
nodes: [WanVideoDecode, Note, MarkdownNote, WanVideoSetLoRAs, WanVideoBlockSwap, Note, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, MelBandRoFormerSampler, NormalizeAudioLoudness, MarkdownNote, SetNode, SetNode, GetNode, GetNode, GetImageRangeFromBatch, INTConstant, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, Reroute, SetNode, Reroute, WanVideoTextEncodeCached, ImageResizeKJv2, PrimitiveStringMultiline, PrimitiveNode, GetNode, SetNode, RH_Nano_Banana_Image2Image, PreviewImage, WanVideoEmptyEmbeds, MelBandRoFormerModelLoader, AudioEncoderLoader, WanVideoSampler, PreviewAny, ImageResizeKJv2, DWPreprocessor, VHS_VideoCombine, WanVideoEncode, WanVideoTorchCompileSettings, Note, GetImageSizeAndCount, GetNode, ColorMatch, VHS_LoadVideo, LoadImage, ImageResizeKJv2, PreviewImage, RH_Translator, VHS_LoadVideo, VHS_LoadVideo, WanVideoEncode, WanVideoAddS2VEmbeds, AudioEncoderEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.2S2V+香蕉模型=批量爆款二创视频（AI带货+模型换装+唱歌跳舞）_1973620998547353601.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/wan2.2S2V+香蕉模型=批量爆款二创视频（AI带货+模型换装+唱歌跳舞）_1973620998547353601.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（64 个）：
- `WanVideoDecode`
- `Note`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
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
- `Reroute`
- `SetNode`
- `Reroute`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `PrimitiveStringMultiline`
- `PrimitiveNode`
- `GetNode`
- `SetNode`
- `RH_Nano_Banana_Image2Image`
- `PreviewImage`
- `WanVideoEmptyEmbeds`
- `MelBandRoFormerModelLoader`
- `AudioEncoderLoader`
- `WanVideoSampler` ★核心
- `PreviewAny`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `WanVideoEncode`
- `WanVideoTorchCompileSettings`
- `Note`
- `GetImageSizeAndCount`
- `GetNode`
- `ColorMatch`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `RH_Translator`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `WanVideoEncode`
- `WanVideoAddS2VEmbeds`
- `AudioEncoderEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **56%**（36/64）

**有卡**：`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`GetImageRangeFromBatch`、`INTConstant`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`RH_Nano_Banana_Image2Image`、`WanVideoEmptyEmbeds`、`MelBandRoFormerModelLoader`、`AudioEncoderLoader`、`WanVideoSampler`、`DWPreprocessor`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`ColorMatch`、`VHS_LoadVideo`、`LoadImage`、`RH_Translator`、`WanVideoAddS2VEmbeds`、`AudioEncoderEncode`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached
