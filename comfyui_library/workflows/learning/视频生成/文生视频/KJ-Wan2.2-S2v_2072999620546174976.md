---
key: 视频生成/文生视频/KJ-Wan2.2-S2v_2072999620546174976.json
name: KJ-Wan2.2-S2v_2072999620546174976
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/KJ-Wan2.2-S2v_2072999620546174976.json
hash: a4853f9669a8e4a3
coverage: 0.6
learned_at: 2026-10-11 20:38:33
nodes: [WanVideoDecode, WanVideoTorchCompileSettings, Note, Note, MarkdownNote, WanVideoSetLoRAs, Note, WanVideoSetBlockSwap, SetNode, GetNode, WanVideoEncode, Note, WanVideoEmptyEmbeds, WanVideoEncode, GetNode, VHS_LoadAudio, AudioEncoderEncode, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddS2VEmbeds, PreviewAny, ImageResizeKJv2, GetImageSizeAndCount, Reroute, WanVideoSampler, ColorMatch, GetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoBlockSwap, MergeAudioMW, Reroute, LoadAudio, PrimitiveNode, VHS_LoadVideo, VHS_LoadVideo, LoadImage, ImageResizeKJv2, GetNode, GetNode, DWPreprocessor, WanVideoTextEncodeCached, INTConstant, INTConstant, VHS_VideoCombine, MelBandRoFormerSampler, MelBandRoFormerModelLoader, NormalizeAudioLoudness, AudioEncoderLoader, GetImageRangeFromBatch, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/KJ-Wan2.2-S2v_2072999620546174976.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/KJ-Wan2.2-S2v_2072999620546174976.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（60 个）：
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoEncode`
- `Note`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `GetNode`
- `VHS_LoadAudio`
- `AudioEncoderEncode`
- `MarkdownNote`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddS2VEmbeds`
- `PreviewAny`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `Reroute`
- `WanVideoSampler` ★核心
- `ColorMatch`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `MergeAudioMW`
- `Reroute`
- `LoadAudio`
- `PrimitiveNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `DWPreprocessor`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `NormalizeAudioLoudness`
- `AudioEncoderLoader`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`

## 知识

覆盖率 **60%**（36/60）

**有卡**：`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`WanVideoEmptyEmbeds`、`VHS_LoadAudio`、`AudioEncoderEncode`、`ImageResizeKJv2`、`WanVideoAddS2VEmbeds`、`GetImageSizeAndCount`、`WanVideoSampler`、`ColorMatch`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`MergeAudioMW`、`LoadAudio`、`VHS_LoadVideo`、`LoadImage`、`DWPreprocessor`、`WanVideoTextEncodeCached`、`INTConstant`、`VHS_VideoCombine`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`NormalizeAudioLoudness`、`AudioEncoderLoader`、`GetImageRangeFromBatch`

**用到的条目**：LoadImage、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode、WanVideoTextEncodeCached
