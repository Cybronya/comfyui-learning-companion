---
key: 视频生成/图生视频/（KJ版）Wan2.2 S2V头部姿势控制数字人V2_1962391778080985089.json
name: （KJ版）Wan2.2 S2V头部姿势控制数字人V2_1962391778080985089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（KJ版）Wan2.2 S2V头部姿势控制数字人V2_1962391778080985089.json
hash: a3101bdfd7d6443e
coverage: 0.677419
learned_at: 2026-10-15 22:31:30
nodes: [Note, Note, MarkdownNote, WanVideoSetLoRAs, Note, WanVideoSetBlockSwap, Note, WanVideoEmptyEmbeds, WanVideoEncode, GetNode, MelBandRoFormerSampler, NormalizeAudioLoudness, AudioEncoderEncode, MarkdownNote, Reroute, PreviewAny, GetNode, GetNode, AudioEncoderLoader, MelBandRoFormerModelLoader, WanVideoBlockSwap, WanVideoSampler, WanVideoContextOptions, WanVideoAddS2VEmbeds, WanVideoEncode, DWPreprocessor, ImageResizeKJv2, ImageResizeKJv2, Reroute, VHS_LoadVideo, ImageResizeKJv2, WanVideoDecode, GetImageSizeAndCount, GetImageRangeFromBatch, ColorMatch, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, easy anythingIndexSwitch, VHS_LoadVideo, LoadImage, JWInteger, LoadAudio, Note, Note, Note, WanVideoTextEncodeCached, CR Prompt Text, Note, Note, JWInteger, Note, Note, Note, WanVideoLoraSelectMulti, JWInteger, CR Prompt Text, CR Prompt Text, AudioCrop]
patterns: []
missing: []
---

# 视频生成/图生视频/（KJ版）Wan2.2 S2V头部姿势控制数字人V2_1962391778080985089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962391778080985089.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（62 个）：
- `Note`
- `Note`
- `MarkdownNote`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `GetNode`
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
- `WanVideoContextOptions`
- `WanVideoAddS2VEmbeds`
- `WanVideoEncode`
- `DWPreprocessor`
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
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `VHS_LoadVideo`
- `LoadImage`
- `JWInteger`
- `LoadAudio`
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
- `CR Prompt Text`
- `CR Prompt Text`
- `AudioCrop`

## 知识

覆盖率 **68%**（42/62）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoEmptyEmbeds`、`WanVideoEncode`、`MelBandRoFormerSampler`、`NormalizeAudioLoudness`、`AudioEncoderEncode`、`AudioEncoderLoader`、`MelBandRoFormerModelLoader`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoAddS2VEmbeds`、`DWPreprocessor`、`ImageResizeKJv2`、`VHS_LoadVideo`、`WanVideoDecode`、`GetImageSizeAndCount`、`GetImageRangeFromBatch`、`ColorMatch`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`easy anythingIndexSwitch`、`LoadImage`、`JWInteger`、`LoadAudio`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`WanVideoLoraSelectMulti`、`AudioCrop`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、MelBandRoFormerSampler、AudioEncoderLoader、WanVideoDecode、WanVideoVAELoader、AudioEncoderEncode
