---
key: 视频生成/图生视频/（KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json
name: （KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json
hash: d1dadf487f65ed41
coverage: 0.688525
learned_at: 2026-10-15 22:31:30
nodes: [Note, Note, MarkdownNote, WanVideoSetLoRAs, Note, WanVideoSetBlockSwap, Note, WanVideoEmptyEmbeds, WanVideoEncode, MelBandRoFormerSampler, NormalizeAudioLoudness, AudioEncoderEncode, MarkdownNote, Reroute, PreviewAny, GetNode, GetNode, AudioEncoderLoader, MelBandRoFormerModelLoader, WanVideoBlockSwap, WanVideoSampler, WanVideoEncode, ImageResizeKJv2, ImageResizeKJv2, Reroute, VHS_LoadVideo, ImageResizeKJv2, WanVideoDecode, GetImageSizeAndCount, GetImageRangeFromBatch, ColorMatch, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, VHS_LoadVideo, LoadImage, JWInteger, Note, Note, Note, WanVideoTextEncodeCached, CR Prompt Text, Note, Note, JWInteger, Note, Note, Note, WanVideoLoraSelectMulti, JWInteger, WanVideoVAELoader, WanVideoAddS2VEmbeds, WanVideoContextOptions, DWPreprocessor, LoadAudio, CR Prompt Text, CR Prompt Text, AudioCrop]
patterns: []
missing: []
---

# 视频生成/图生视频/（KJ版）Wan2.2 S2V+FramePack全身姿态控制数字人V2_1962399732356222977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962399732356222977.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（61 个）：
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `MelBandRoFormerSampler` ★核心
- `NormalizeAudioLoudness`
- `AudioEncoderEncode`
- `MarkdownNote`
- `Reroute`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `AudioEncoderLoader`
- `MelBandRoFormerModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Reroute`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `ColorMatch`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy anythingIndexSwitch`
- `VHS_LoadVideo`
- `LoadImage`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `Note`
- `Note`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `JWInteger`
- `WanVideoVAELoader`
- `WanVideoAddS2VEmbeds`
- `WanVideoContextOptions`
- `DWPreprocessor`
- `LoadAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `AudioCrop`

## 知识

覆盖率 **69%**（42/61）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`AudioEncoderEncode`、`AudioEncoderLoader`、`MelBandRoFormerModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`ImageResizeKJv2`、`VHS_LoadVideo`、`WanVideoDecode`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`ColorMatch`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy anythingIndexSwitch`、`LoadImage`、`JWInteger`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoAddS2VEmbeds`、`WanVideoContextOptions`、`DWPreprocessor`、`LoadAudio`、`AudioCrop`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode
